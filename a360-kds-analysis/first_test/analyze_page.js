const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe'
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page = await context.newPage();

  // 로그인
  console.log('Logging in...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);

  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');

  console.log('Waiting for login...');
  await page.waitForTimeout(5000);
  console.log('After login URL:', page.url());

  // 타겟 페이지로 이동
  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded',
    timeout: 30000
  });
  await page.waitForTimeout(5000);
  console.log('Target URL:', page.url());

  // editor-palette__accordion 요소 분석
  const accordions = await page.evaluate(() => {
    const els = document.querySelectorAll('.editor-palette__accordion');
    return els.length;
  });
  console.log('Total accordions:', accordions);

  const activeAccordions = await page.evaluate(() => {
    const els = document.querySelectorAll('.editor-palette__accordion.editor-palette__accordion--is_active');
    return els.length;
  });
  console.log('Active accordions:', activeAccordions);

  // aria-expanded 요소 분석
  const ariaExpandedInfo = await page.evaluate(() => {
    const container = document.querySelectorAll('.editor-palette__accordion.editor-palette__accordion--is_active');
    const result = [];
    container.forEach((accordion, i) => {
      const expandedEls = accordion.querySelectorAll('[aria-expanded]');
      expandedEls.forEach(el => {
        result.push({
          accordionIndex: i,
          tagName: el.tagName,
          className: el.className.substring(0, 100),
          ariaExpanded: el.getAttribute('aria-expanded'),
          ariaLabel: el.getAttribute('aria-label'),
          dataPath: el.getAttribute('data-path'),
          text: el.textContent.trim().substring(0, 50)
        });
      });
    });
    return result;
  });
  console.log('aria-expanded elements:', JSON.stringify(ariaExpandedInfo, null, 2));

  await page.screenshot({ path: '/c/DEV/screenshot_target.png', fullPage: false });
  console.log('Screenshot saved');

  await browser.close();
})();
