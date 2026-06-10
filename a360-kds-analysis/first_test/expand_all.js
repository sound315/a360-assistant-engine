const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe'
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page = await context.newPage();

  console.log('Logging in...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  // 펼치기 전 스크린샷
  await page.screenshot({ path: 'C:\\DEV\\before.png' });
  console.log('Before screenshot saved');

  // 모두 열릴 때까지 반복
  let pass = 0;
  while (true) {
    pass++;
    const result = await page.evaluate(async () => {
      const buttons = Array.from(document.querySelectorAll(
        '.editor-palette__accordion.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
      ));
      for (const btn of buttons) {
        btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        await new Promise(r => setTimeout(r, 150));
      }
      await new Promise(r => setTimeout(r, 1000));
      return {
        clicked: buttons.length,
        stillClosed: document.querySelectorAll(
          '.editor-palette__accordion.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
        ).length,
        nowOpen: document.querySelectorAll(
          '.editor-palette__accordion.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="true"]'
        ).length
      };
    });

    console.log(`Pass ${pass}: clicked=${result.clicked}, open=${result.nowOpen}, still closed=${result.stillClosed}`);
    if (result.clicked === 0 || result.stillClosed === 0) break;
    if (pass > 10) break;
  }

  // 펼친 후 스크린샷
  await page.screenshot({ path: 'C:\\DEV\\after.png', fullPage: false });
  console.log('After screenshot saved');

  // 좌측 팔레트 영역만 캡처
  const palette = await page.$('.editor-palette__accordion--is_active');
  if (palette) {
    await palette.screenshot({ path: 'C:\\DEV\\palette.png' });
    console.log('Palette screenshot saved');
  }

  await browser.close();
})();
