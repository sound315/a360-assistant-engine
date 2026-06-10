/**
 * 08_extract_package_desc.js
 * 패키지 그룹 헤더 hover → 공식 설명 추출 시도
 * 결과: output/package_hover_desc.json  { packageId: "설명 or ''" }
 */

const { chromium } = require('playwright');
const fs   = require('fs');
const path = require('path');

const ACTIONS_PATH = path.join(__dirname, '..', 'output', 'actions.json');
const OUTPUT_PATH  = path.join(__dirname, '..', 'output', 'package_hover_desc.json');

async function getDesc(page) {
  return await page.evaluate(() => {
    const selectors = ['[class*="help"]', '[class*="tooltip"]', '[class*="popover"]'];
    for (const sel of selectors) {
      for (const el of document.querySelectorAll(sel)) {
        const t = el.textContent.trim();
        if (t && t.length > 5) return t;
      }
    }
    return '';
  });
}

(async () => {
  const data = JSON.parse(fs.readFileSync(ACTIONS_PATH, 'utf8'));

  const browser = await chromium.launch({
    headless: false,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe',
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page    = await context.newPage();

  console.log('[1/4] 로그인...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  console.log('[2/4] 에디터 이동...');
  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000,
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  console.log('[3/4] 팔레트 패키지 헤더 목록 수집...');
  // 실제 DOM에 있는 그룹 버튼 텍스트와 요소 수 확인
  const groupInfo = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    return btns.map(b => b.textContent.trim());
  });
  console.log(`  팔레트 그룹 버튼 수: ${groupInfo.length}개`);
  console.log(`  샘플: ${groupInfo.slice(0, 5).join(', ')}`);

  console.log('[4/4] 패키지별 hover 추출...');
  const results = {};
  let found = 0;

  for (const pkg of data) {
    const pkgName = pkg.packageName;

    // 텍스트 매칭으로 버튼 찾기
    const btn = await page.evaluateHandle((name) => {
      const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
      return btns.find(b => b.textContent.trim() === name) || null;
    }, pkgName);

    const isNull = await page.evaluate(el => el === null, btn);
    if (isNull) {
      process.stdout.write(`  [ ] ${pkgName}\n`);
      results[pkg.packageId] = '';
      continue;
    }

    await page.evaluate(el => el.scrollIntoView({ block: 'center' }), btn);
    await page.waitForTimeout(150);
    await btn.hover({ force: true });

    let desc = '';
    for (let i = 0; i < 5; i++) {
      await page.waitForTimeout(400);
      desc = await getDesc(page);
      if (desc) break;
    }

    // hover 후 다른 영역 이동 (tooltip 사라지게)
    await page.mouse.move(0, 0);

    results[pkg.packageId] = desc;
    if (desc) {
      found++;
      process.stdout.write(`  [O] ${pkgName}: "${desc.slice(0, 50)}"\n`);
    } else {
      process.stdout.write(`  [ ] ${pkgName}\n`);
    }
  }

  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2), 'utf8');
  console.log(`\n완료: ${found}/${data.length}개 공식 설명 추출`);
  console.log(`저장: ${OUTPUT_PATH}`);

  await browser.close();
})();
