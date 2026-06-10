/**
 * 05_extract_tooltips.js
 * 각 액션 아이템에 hover 해서 popover/help 텍스트를 추출하고
 * output/actions.json 의 각 action 에 "description" 필드로 병합.
 *
 * 확인된 셀렉터:
 *   [class*="help"]    → 순수 설명 텍스트 (우선)
 *   [class*="popover"] → "패키지명: 액션명설명필요한 Bot Agent 버전: ..." (폴백)
 *
 * 실행: node scripts/05_extract_tooltips.js
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ACTIONS_PATH = path.join(__dirname, '..', 'output', 'actions.json');
const OUTPUT_PATH  = path.join(__dirname, '..', 'output', 'actions.json'); // 덮어쓰기

(async () => {
  const data = JSON.parse(fs.readFileSync(ACTIONS_PATH, 'utf8'));
  const totalActions = data.reduce((s, p) => s + p.actionCount, 0);
  console.log(`총 ${data.length}개 패키지, ${totalActions}개 액션`);

  const browser = await chromium.launch({
    headless: false, // headless 모드에서는 popover가 렌더링되지 않음
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe',
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page = await context.newPage();

  console.log('[1/4] Logging in...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  console.log('[2/4] Navigating to editor...');
  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000,
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  console.log('[3/4] Expanding all groups...');
  for (let pass = 0; pass < 10; pass++) {
    const clicked = await page.evaluate(async () => {
      const btns = Array.from(document.querySelectorAll(
        '.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
      ));
      for (const btn of btns) {
        btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        await new Promise(r => setTimeout(r, 150));
      }
      await new Promise(r => setTimeout(r, 800));
      return btns.length;
    });
    if (clicked === 0) break;
    console.log(`  Pass ${pass + 1}: ${clicked}개 펼침`);
  }

  console.log('[4/4] Hovering each action and collecting descriptions...');
  let processed = 0;
  let found = 0;

  for (const pkg of data) {
    for (const act of pkg.actions) {
      const itemName = act.attrs['data-item-name'];
      if (!itemName) { act.description = ''; continue; }

      try {
        const el = await page.$(`[data-item-name="${itemName}"]`);
        if (!el) { act.description = ''; processed++; continue; }

        await el.hover({ force: true });

        // popover 또는 help 텍스트가 나타날 때까지 최대 1.5초 대기
        let desc = '';
        const deadline = Date.now() + 1500;
        while (Date.now() < deadline) {
          desc = await page.evaluate(() => {
            // 1순위: [class*="help"] — 순수 설명 텍스트
            for (const el of document.querySelectorAll('[class*="help"]')) {
              const t = el.textContent.trim();
              if (t && t.length > 5) return t;
            }
            // 2순위: [class*="popover"]
            for (const el of document.querySelectorAll('[class*="popover"]')) {
              const t = el.textContent.trim();
              if (t && t.length > 5) return t;
            }
            return '';
          });
          if (desc) break;
          await page.waitForTimeout(200);
        }

        act.description = desc;
        if (desc) found++;
      } catch (_) {
        act.description = '';
      }

      processed++;
      if (processed % 50 === 0) {
        console.log(`  ${processed}/${totalActions} 처리 중... (설명 확보: ${found}개)`);
      }
    }
  }

  console.log(`\n완료: ${processed}개 처리, ${found}개 설명 확보 (${Math.round(found/processed*100)}%)`);

  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(data, null, 2), 'utf8');
  console.log(`저장: ${OUTPUT_PATH}`);

  await browser.close();
})();
