const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true, ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe'
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
    waitUntil: 'domcontentloaded', timeout: 30000
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  // 상태 카운트: caret-down(펼침) / caret-right(접힘)
  const state = () => page.evaluate(() => {
    const cs = Array.from(document.querySelectorAll('.taskbot-canvas-list-node__collapser'));
    let open = 0, closed = 0;
    cs.forEach(c => {
      if (c.querySelector('.fa-caret-down')) open++;
      else if (c.querySelector('.fa-caret-right')) closed++;
    });
    return { total: cs.length, open, closed };
  });

  // 전체 토글: collapse=true → 접기, false → 펼치기 (반복 처리)
  const setAll = (collapse) => page.evaluate(async (collapse) => {
    const sleep = (ms) => new Promise(r => setTimeout(r, ms));
    const targetIcon = collapse ? 'fa-caret-down' : 'fa-caret-right';
    let totalClicked = 0;
    for (let pass = 0; pass < 12; pass++) {
      const targets = Array.from(document.querySelectorAll('.taskbot-canvas-list-node__collapser'))
        .filter(c => c.querySelector('.' + targetIcon));
      if (!targets.length) break;
      targets.forEach(c => {
        let leaf = c; while (leaf.firstElementChild) leaf = leaf.firstElementChild;
        ['mousedown', 'mouseup', 'click'].forEach(t =>
          leaf.dispatchEvent(new MouseEvent(t, { bubbles: true, cancelable: true, view: window })));
      });
      totalClicked += targets.length;
      await sleep(400);
    }
    return totalClicked;
  }, collapse);

  console.log('초기:', JSON.stringify(await state()));

  let clicked = await setAll(true);
  console.log(`\n전체 접기 (클릭 ${clicked}회):`, JSON.stringify(await state()), '← closed=total 기대');
  await page.screenshot({ path: 'C:\\DEV\\a360-assistant-engine_sdd\\a360-kds-analysis\\dbg_collapsed_all.png' });

  clicked = await setAll(false);
  console.log(`\n전체 펼치기 (클릭 ${clicked}회):`, JSON.stringify(await state()), '← open=total 기대');
  await page.screenshot({ path: 'C:\\DEV\\a360-assistant-engine_sdd\\a360-kds-analysis\\dbg_expanded_all.png' });

  await browser.close();
  console.log('\nDone.');
})();
