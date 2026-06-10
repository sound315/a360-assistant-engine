const { chromium } = require('playwright');
const fs = require('fs');
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

  console.log('[3/4] Expanding all groups...');
  let pass = 0;
  while (pass++ < 10) {
    const clicked = await page.evaluate(async () => {
      const buttons = Array.from(document.querySelectorAll(
        '.editor-palette__accordion.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]'
      ));
      for (const btn of buttons) {
        btn.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
        await new Promise(r => setTimeout(r, 150));
      }
      await new Promise(r => setTimeout(r, 800));
      return buttons.length;
    });
    if (clicked === 0) break;
    console.log(`  Pass ${pass}: ${clicked}개 펼침`);
  }

  console.log('[4/4] Extracting package & action data...');
  const data = await page.evaluate(() => {
    const active = document.querySelector('.editor-palette__accordion--is_active');
    if (!active) return [];

    const packages = [];

    // 각 그룹 컨테이너 순회
    const containers = active.querySelectorAll('.editor-palette-group-container');
    containers.forEach(container => {
      const btn = container.querySelector('[data-path="EditorPalette.group.button"]');
      if (!btn) return;

      const packageId = btn.getAttribute('data-group-name') || '';
      const packageName = btn.textContent.trim();
      const isOpen = btn.getAttribute('aria-expanded') === 'true';

      // children 영역에서 아이템 추출
      const childrenEl = container.querySelector('.editor-palette-group__children');
      const actions = [];

      if (childrenEl) {
        const items = childrenEl.querySelectorAll('[data-path="EditorPalette.item"]');
        items.forEach(item => {
          // 아이템 텍스트 (라벨)
          const labelEl = item.querySelector('[class*="label"], [class*="title"], [class*="name"]');
          const name = labelEl ? labelEl.textContent.trim() : item.textContent.trim().split('\n')[0].trim();

          // data 속성 전체 수집
          const attrs = {};
          Array.from(item.attributes).forEach(a => {
            attrs[a.name] = a.value;
          });

          actions.push({ name, attrs });
        });
      }

      packages.push({ packageId, packageName, isOpen, actionCount: actions.length, actions });
    });

    return packages;
  });

  const totalActions = data.reduce((sum, pkg) => sum + pkg.actionCount, 0);
  console.log(`\n총 ${data.length}개 패키지, ${totalActions}개 액션 추출`);
  data.forEach(pkg => {
    console.log(`  [${pkg.packageName}] (${pkg.packageId}) - ${pkg.actionCount}개`);
    pkg.actions.slice(0, 3).forEach(a => console.log(`    - ${a.name}`));
    if (pkg.actionCount > 3) console.log(`    ... 외 ${pkg.actionCount - 3}개`);
  });

  const outputPath = path.join(__dirname, '..', 'output', 'actions.json');
  fs.writeFileSync(outputPath, JSON.stringify(data, null, 2), 'utf8');
  console.log(`\nJSON 저장 완료: ${outputPath}`);

  await browser.close();
})();
