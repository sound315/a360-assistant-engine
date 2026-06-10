/**
 * 05a_test_tooltip.js — 툴팁 존재 여부 빠른 검증 (첫 10개 액션만)
 */
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false, // 화면 보면서 확인
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe',
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page = await context.newPage();

  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000,
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  // 첫 번째 그룹 펼치기
  await page.evaluate(async () => {
    const btn = document.querySelector(
      '.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
    );
    if (btn) {
      btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      await new Promise(r => setTimeout(r, 1000));
    }
  });

  // 처음 10개 액션에 hover 후 전체 DOM에서 툴팁 탐색
  const items = await page.$$('[data-path="EditorPalette.item"]');
  const testItems = items.slice(0, 10);

  console.log(`테스트 대상: ${testItems.length}개`);

  for (const item of testItems) {
    const itemName = await item.getAttribute('data-item-name');
    await item.hover({ force: true });
    await page.waitForTimeout(700);

    // 모든 새로 생성된 tooltip 후보 탐색
    const tooltipInfo = await page.evaluate(() => {
      const candidates = [
        '[role="tooltip"]',
        '[class*="tooltip"]',
        '[class*="popover"]',
        '[class*="hint"]',
        '[class*="description"]',
        '[class*="help"]',
        '[data-path*="tooltip"]',
        '[data-path*="Tooltip"]',
      ];
      const results = [];
      for (const sel of candidates) {
        const els = document.querySelectorAll(sel);
        els.forEach(el => {
          const text = el.textContent.trim();
          if (text && text.length > 3) {
            results.push({ selector: sel, text: text.substring(0, 100) });
          }
        });
      }
      return results;
    });

    console.log(`\n[${itemName}]`);
    if (tooltipInfo.length) {
      tooltipInfo.forEach(t => console.log(`  ${t.selector}: "${t.text}"`));
    } else {
      console.log('  → 툴팁 없음');
    }
  }

  await browser.close();
})();
