const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe'
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
    waitUntil: 'domcontentloaded', timeout: 30000
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  console.log('[3/4] Expanding recorder group...');
  await page.evaluate(async () => {
    const buttons = Array.from(document.querySelectorAll(
      '.editor-palette__accordion.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"]'
    ));
    const recorderBtn = buttons.find(b => b.getAttribute('data-group-name') === 'command-group:recorder');
    if (recorderBtn && recorderBtn.getAttribute('aria-expanded') === 'false') {
      recorderBtn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      await new Promise(r => setTimeout(r, 800));
    }
  });

  // 에디터 스텝 수 확인 (더블클릭 전) - 올바른 셀렉터 찾기
  const beforeInfo = await page.evaluate(() => {
    // 에디터 우측 영역 클래스 탐색
    const editorArea = document.querySelector('[data-path="EditorFlow"], .editor-flow, [class*="editor-flow"]');
    const allDataPaths = [...new Set(
      Array.from(document.querySelectorAll('[data-path]'))
        .map(e => e.getAttribute('data-path'))
        .filter(p => p.includes('flow') || p.includes('step') || p.includes('node') || p.includes('action'))
    )];
    return {
      editorAreaFound: !!editorArea,
      editorAreaClass: editorArea ? editorArea.className.substring(0, 80) : null,
      relevantDataPaths: allDataPaths
    };
  });
  console.log('Editor area info:', JSON.stringify(beforeInfo, null, 2));

  console.log('[4/4] Double-clicking 캡처 with force...');
  const item = await page.$('[data-item-name="recorder#capture"]');

  // 더블클릭 전 스크린샷
  await page.screenshot({ path: path.join(__dirname, '..', 'screenshots', 'before_dblclick.png') });

  // force:true 로 포인터 차단 무시하고 더블클릭
  await item.dblclick({ force: true });
  await page.waitForTimeout(2000);

  // 더블클릭 후 스크린샷
  await page.screenshot({ path: path.join(__dirname, '..', 'screenshots', 'after_dblclick.png') });
  console.log('Screenshots saved. Checking result...');

  // 변화 감지
  const afterInfo = await page.evaluate(() => {
    const allDataPaths = [...new Set(
      Array.from(document.querySelectorAll('[data-path]'))
        .map(e => e.getAttribute('data-path'))
        .filter(p => p.includes('flow') || p.includes('step') || p.includes('node') || p.includes('action'))
    )];
    return { relevantDataPaths: allDataPaths };
  });
  console.log('After dblclick paths:', JSON.stringify(afterInfo, null, 2));

  await browser.close();
})();
