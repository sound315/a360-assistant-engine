/**
 * 06_inspect_item_dom.js
 * 액션 아이템의 DOM 구조(속성, 자식 요소, 텍스트 전체)를 덤프해서
 * description 이 숨어있는 위치를 찾는 진단 스크립트.
 *
 * 실행: node scripts/06_inspect_item_dom.js
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe',
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page = await context.newPage();

  console.log('[1/3] Logging in...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  console.log('[2/3] Navigating to editor...');
  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000,
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  // 첫 번째 그룹 하나만 펼치기
  await page.evaluate(async () => {
    const btn = document.querySelector(
      '.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
    );
    if (btn) {
      btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      await new Promise(r => setTimeout(r, 800));
    }
  });

  console.log('[3/3] Dumping DOM structure of first 5 action items...');
  const result = await page.evaluate(() => {
    function dumpElement(el, depth = 0) {
      const indent = '  '.repeat(depth);
      const attrs = Array.from(el.attributes).map(a => `${a.name}="${a.value}"`).join(' ');
      const ownText = Array.from(el.childNodes)
        .filter(n => n.nodeType === Node.TEXT_NODE)
        .map(n => n.textContent.trim())
        .filter(Boolean)
        .join(' ');

      const info = {
        tag: el.tagName.toLowerCase(),
        attrs: Object.fromEntries(Array.from(el.attributes).map(a => [a.name, a.value])),
        ownText,
        children: [],
      };

      for (const child of el.children) {
        info.children.push(dumpElement(child, depth + 1));
      }
      return info;
    }

    const items = Array.from(
      document.querySelectorAll('[data-path="EditorPalette.item"]')
    ).slice(0, 5);

    return items.map(item => dumpElement(item));
  });

  const outPath = path.join(__dirname, '..', 'output', 'item_dom_dump.json');
  fs.writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf8');
  console.log(`DOM 덤프 저장: ${outPath}`);
  console.log('\n--- 첫 번째 아이템 요약 ---');
  console.log(JSON.stringify(result[0], null, 2));

  await browser.close();
})();
