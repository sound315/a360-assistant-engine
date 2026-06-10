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

  // 테스트 대상: 기록>지정, Excel 기본>열기, 마우스>클릭
  const steps = [
    { package: '기록', action: '지정', data_item_name: 'record#assign' },
    { package: 'Excel 기본', action: '열기', data_item_name: 'excel#openspreadsheet' },
    { package: '마우스', action: '클릭', data_item_name: 'mouse#mouseclick' },
  ];

  const result = await page.evaluate(async (steps) => {
    const sleep = (ms) => new Promise(r => setTimeout(r, ms));
    const norm = (s) => (s || '').replace(/\s+/g, ' ').trim();

    function findItem(step) {
      if (step.data_item_name) {
        const el = document.querySelector(`[data-path="EditorPalette.item"][data-item-name="${step.data_item_name}"]`);
        if (el) return el;
      }
      return null;
    }

    async function expandGroups(pkgNames) {
      const palette = document.querySelector('.editor-palette__accordion--is_active');
      if (!palette) return 0;
      const wanted = new Set([...pkgNames].map(norm));
      const buttons = Array.from(palette.querySelectorAll('[data-path="EditorPalette.group.button"]'));
      let clicked = 0;
      for (const btn of buttons) {
        if (wanted.has(norm(btn.textContent)) && btn.getAttribute('aria-expanded') === 'false') {
          btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
          clicked++;
        }
      }
      if (clicked) await sleep(800);
      return clicked;
    }

    // 1. 초기 상태: 어떤 게 이미 보이는지
    const initiallyVisible = steps.map(s => ({ name: s.data_item_name, visible: !!findItem(s) }));

    // 2. 필요한 패키지만 추림
    const needed = new Set();
    for (const s of steps) if (!findItem(s)) needed.add(s.package);

    // 3. 선택적 펼치기
    const clicked = await expandGroups(needed);

    // 4. 펼친 후 각 아이템 존재 여부
    const afterExpand = steps.map(s => ({ name: s.data_item_name, found: !!findItem(s) }));

    // 5. 펼쳐진 그룹 수 (전체 대비)
    const palette = document.querySelector('.editor-palette__accordion--is_active');
    const allBtns = Array.from(palette.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    const expandedCount = allBtns.filter(b => b.getAttribute('aria-expanded') === 'true').length;

    return {
      initiallyVisible,
      neededPackages: [...needed],
      clicked,
      afterExpand,
      expandedGroups: expandedCount,
      totalGroups: allBtns.length,
    };
  }, steps);

  console.log('=== 선택적 펼치기 검증 ===');
  console.log('초기 표시:', JSON.stringify(result.initiallyVisible));
  console.log('펼칠 패키지:', JSON.stringify(result.neededPackages));
  console.log('클릭한 그룹 수:', result.clicked);
  console.log('펼친 후 발견:', JSON.stringify(result.afterExpand));
  console.log(`펼쳐진 그룹: ${result.expandedGroups}/${result.totalGroups} (전체 펼치기 대비 최소화 확인)`);

  // 6. 실제 노드 추가까지 (leaf 더블클릭)
  const count = () => page.evaluate(() => document.querySelectorAll('[data-path="TaskbotCanvasListNode"]').length);
  let prev = await count();
  console.log('\n노드 추가 전:', prev);
  for (const s of steps) {
    await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      if (!el) return;
      el.scrollIntoView({ block: 'center' });
      let leaf = el; while (leaf.firstElementChild) leaf = leaf.firstElementChild;
      ['mousedown','mouseup','click','mousedown','mouseup','click','dblclick']
        .forEach(t => leaf.dispatchEvent(new MouseEvent(t, { bubbles: true, cancelable: true, view: window })));
    }, `[data-path="EditorPalette.item"][data-item-name="${s.data_item_name}"]`);
    await page.waitForTimeout(800);
  }
  const now = await count();
  console.log('노드 추가 후:', now, `(델타 +${now - prev}, 기대 +${steps.length})`);

  await browser.close();
  console.log('\nDone.');
})();
