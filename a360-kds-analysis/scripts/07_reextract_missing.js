/**
 * 07_reextract_missing.js
 * description 이 비어있는 액션만 골라 재추출.
 * hover 대기 시간을 늘리고, 팝오버 셀렉터를 더 넓게 탐색.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ACTIONS_PATH = path.join(__dirname, '..', 'output', 'actions.json');

// data-item-name → 액션 표시명 (popover 파싱용)
const MISSING_META = {
  'record#addcolumn':                    '열 추가',
  'datetime#assign':                     '지정',
  'datatable#getnumberofrows':           '행 개수 가져오기',
  'datatable#searchforavalue':           '값 검색',
  'datatable#setcellvalue':              '단일 셀의 값 설정',
  'recorder#capture':                    '캡처',
  'recorder#structureddataextraction':   '구조화된 데이터 추출',
  'excel_ms#getcellcolor':               '셀 색상 가져오기',
  'servicenow#get_record':               '기록 가져오기',
  'servicenow#list_record':              '여러 기록 가져오기',
  'servicenow#authentication':           '인증',
  'uiagent#uiwebagentrun':              '실행',
};

const MISSING = [
  'record#addcolumn',
  'datetime#assign',
  'datatable#getnumberofrows',
  'datatable#searchforavalue',
  'datatable#setcellvalue',
  'recorder#capture',
  'recorder#structureddataextraction',
  'excel_ms#getcellcolor',
  'servicenow#get_record',
  'servicenow#list_record',
  'servicenow#authentication',
  'uiagent#uiwebagentrun',
];

async function getDesc(page, actionName) {
  return await page.evaluate((actionName) => {
    // 1순위: [class*="help"] — 순수 설명 텍스트
    for (const el of document.querySelectorAll('[class*="help"]')) {
      const t = el.textContent.trim();
      if (t && t.length > 5) return t;
    }

    // 2순위: [class*="popover"] — "패키지: 액션명설명필요한 Bot Agent 버전: ..." 에서 설명만 파싱
    for (const el of document.querySelectorAll('[class*="popover"]')) {
      const t = el.textContent.trim();
      if (!t || t.length < 5) continue;
      // "패키지: 액션명설명필요한 Bot Agent 버전: X" 패턴에서 설명 추출
      const versionSplit = t.split('필요한 Bot Agent 버전:');
      const beforeVersion = versionSplit[0];
      // "패키지명: 액션명" 이후 부분 추출
      const colonIdx = beforeVersion.indexOf(': ');
      if (colonIdx !== -1) {
        const afterColon = beforeVersion.slice(colonIdx + 2); // "액션명설명"
        // 액션명 이후 설명 추출
        const descStart = afterColon.indexOf(actionName);
        if (descStart !== -1) {
          const desc = afterColon.slice(descStart + actionName.length).trim();
          if (desc.length > 3) return desc;
        }
        // 액션명 매칭 실패 시 전체 beforeVersion 에서 패키지:액션명 제거 후 반환
        const parts = afterColon.trim();
        if (parts.length > 5) return parts;
      }
      if (t.length > 10) return t;
    }
    return '';
  }, actionName);
}

(async () => {
  const data = JSON.parse(fs.readFileSync(ACTIONS_PATH, 'utf8'));

  const browser = await chromium.launch({
    headless: false,
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

  console.log('[4/4] Re-extracting missing descriptions...');
  const results = {};

  for (const itemName of MISSING) {
    console.log(`\n  처리: ${itemName}`);
    const el = await page.$(`[data-item-name="${itemName}"]`);
    if (!el) {
      console.log(`    → 요소 없음 (팔레트에 미표시)`);
      results[itemName] = '';
      continue;
    }

    // 스크롤해서 보이게 한 뒤 hover
    await el.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await el.hover({ force: true });

    // 최대 3초 대기하며 설명 탐색 (액션명 전달해서 정확히 파싱)
    const actionName = MISSING_META[itemName] || '';
    let desc = '';
    for (let i = 0; i < 6; i++) {
      await page.waitForTimeout(500);
      desc = await getDesc(page, actionName);
      if (desc) break;
    }

    console.log(`    → "${desc || '없음'}"`);
    results[itemName] = desc;
  }

  // actions.json 에 결과 병합
  let updated = 0;
  for (const pkg of data) {
    for (const act of pkg.actions) {
      const itemName = act.attrs['data-item-name'];
      if (itemName in results && results[itemName]) {
        act.description = results[itemName];
        updated++;
      }
    }
  }

  fs.writeFileSync(ACTIONS_PATH, JSON.stringify(data, null, 2), 'utf8');
  console.log(`\n완료: ${updated}개 업데이트, 저장: ${ACTIONS_PATH}`);

  await browser.close();
})();
