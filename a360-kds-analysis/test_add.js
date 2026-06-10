const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true, ignoreHTTPSErrors: true,
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

  for (let pass = 0; pass < 10; pass++) {
    const r = await page.evaluate(async () => {
      const btns = Array.from(document.querySelectorAll(
        '.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
      ));
      for (const b of btns) { b.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true })); await new Promise(r => setTimeout(r, 120)); }
      await new Promise(r => setTimeout(r, 800));
      return btns.length;
    });
    if (r === 0) break;
  }

  const TARGET = 'record#assign'; // 기록 > 지정
  const sel = `[data-path="EditorPalette.item"][data-item-name="${TARGET}"]`;

  const count = () => page.evaluate(() => document.querySelectorAll('[data-path="TaskbotCanvasListNode"]').length);

  let prev = await count();
  console.log(`초기 노드 수: ${prev}  (대상: ${TARGET})`);

  async function trial(label, fn) {
    await fn();
    await page.waitForTimeout(1500);
    const now = await count();
    const delta = now - prev;
    console.log(`[${label}] 노드 ${prev} → ${now}  ${delta > 0 ? '✅ +' + delta : '변화없음'}`);
    prev = now;
  }

  // A1: dblclick 이벤트 하나만
  await trial('A1 dblclick만', () => page.evaluate((sel) => {
    const el = document.querySelector(sel); el.scrollIntoView({ block: 'center' });
    el.dispatchEvent(new MouseEvent('dblclick', { bubbles: true, cancelable: true, view: window }));
  }, sel));

  // A2: click 2번
  await trial('A2 click×2', () => page.evaluate((sel) => {
    const el = document.querySelector(sel);
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
    el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
  }, sel));

  // A3: 전체 시퀀스 (down/up/click ×2 + dblclick)
  await trial('A3 전체시퀀스', () => page.evaluate((sel) => {
    const el = document.querySelector(sel);
    ['mousedown','mouseup','click','mousedown','mouseup','click','dblclick']
      .forEach(t => el.dispatchEvent(new MouseEvent(t, { bubbles: true, cancelable: true, view: window })));
  }, sel));

  // A4: 가장 안쪽 자식에 전체 시퀀스
  await trial('A4 자식타겟 시퀀스', () => page.evaluate((sel) => {
    let el = document.querySelector(sel);
    // 가장 깊은 첫 자식
    while (el.firstElementChild) el = el.firstElementChild;
    ['mousedown','mouseup','click','mousedown','mouseup','click','dblclick']
      .forEach(t => el.dispatchEvent(new MouseEvent(t, { bubbles: true, cancelable: true, view: window })));
  }, sel));

  // B: 신뢰된 더블클릭 (force - overlay 무시)
  await trial('B 신뢰된 dblclick(force)', async () => {
    try { await page.dblclick(sel, { force: true, timeout: 5000 }); }
    catch (e) { console.log('   page.dblclick err:', e.message.split('\n')[0]); }
  });

  // B2: 신뢰된 더블클릭 (정상 - 액션어빌리티 체크)
  await trial('B2 신뢰된 dblclick(정상)', async () => {
    try { await page.dblclick(sel, { timeout: 5000 }); }
    catch (e) { console.log('   page.dblclick err:', e.message.split('\n')[0]); }
  });

  await page.screenshot({ path: 'C:\\DEV\\a360-assistant-engine_sdd\\a360-kds-analysis\\dbg_add_final.png' });
  await browser.close();
  console.log('\nDone.');
})();
