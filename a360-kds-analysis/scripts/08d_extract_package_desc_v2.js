/**
 * 08d_extract_package_desc_v2.js
 * editor-palette-group--has_description 클래스를 가진 그룹만 대상
 * hover 후 use-popover-poppy(action과 동일 구조) 요소가 새로 나타날 때만 추출
 * 결과: output/package_hover_desc.json
 */

const { chromium } = require('playwright');
const fs   = require('fs');
const path = require('path');

const ACTIONS_PATH = path.join(__dirname, '..', 'output', 'actions.json');
const OUTPUT_PATH  = path.join(__dirname, '..', 'output', 'package_hover_desc.json');

// hover 후 새로 생긴 use-popover-poppy 텍스트 반환
async function getNewPopoverText(page, beforeTexts) {
  return await page.evaluate((beforeSet) => {
    for (const el of document.querySelectorAll('.use-popover-poppy__content, [class*="use-popover-poppy__content"]')) {
      const t = el.textContent.trim();
      const r = el.getBoundingClientRect();
      if (!t || r.width === 0 || r.height === 0) continue;
      if (!beforeSet.includes(t)) return t;  // 새로 나타난 것만
    }
    return '';
  }, beforeTexts);
}

// 패키지 popover 텍스트에서 설명 파싱
// 형식: "기록레코드 유형 변수에 대해 다양한 작업을 수행합니다.필요한 Bot Agent 버전: X"
// 또는: "기록: {설명}필요한..." 등 변형 가능
function parsePackageDesc(text, packageName) {
  if (!text) return '';

  // "필요한 Bot Agent 버전:" 이전 부분만 취
  const beforeVersion = text.split('필요한 Bot Agent 버전:')[0].trim();

  // 패키지명으로 시작하면 제거
  let desc = beforeVersion;
  if (desc.startsWith(packageName)) {
    desc = desc.slice(packageName.length).trim();
    // ": " 로 시작하면 제거
    if (desc.startsWith(':')) desc = desc.slice(1).trim();
  }

  return desc.trim();
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

  // has_description 클래스 패키지 목록 수집
  const hasDescGroups = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll(
      '[data-path="EditorPalette.group.button"].editor-palette-group--has_description'
    ));
    return btns.map(b => ({
      name:    b.textContent.trim(),
      groupId: b.getAttribute('data-group-name'),
    }));
  });
  console.log(`[3/4] has_description 패키지: ${hasDescGroups.length}개`);

  const results = {};

  // 먼저 기존 popover 텍스트 목록 수집
  const beforePopovers = await page.evaluate(() =>
    Array.from(document.querySelectorAll('.use-popover-poppy__content'))
      .map(el => el.textContent.trim())
      .filter(Boolean)
  );

  let found = 0;
  let i = 0;
  for (const grp of hasDescGroups) {
    i++;
    process.stdout.write(`  [${i}/${hasDescGroups.length}] ${grp.name} ... `);

    const btn = await page.evaluateHandle((name) => {
      const btns = Array.from(document.querySelectorAll(
        '[data-path="EditorPalette.group.button"].editor-palette-group--has_description'
      ));
      return btns.find(b => b.textContent.trim() === name) || null;
    }, grp.name);

    const isNull = await page.evaluate(el => el === null, btn);
    if (isNull) {
      process.stdout.write('요소 없음\n');
      results[grp.groupId] = '';
      continue;
    }

    await page.evaluate(el => el.scrollIntoView({ block: 'center' }), btn);
    await page.waitForTimeout(200);

    // 마우스를 중립 위치로 이동 후 hover
    await page.mouse.move(0, 0);
    await page.waitForTimeout(100);
    await btn.hover({ force: true });

    // use-popover-poppy 가 새로 나타날 때까지 최대 2초 대기
    let rawText = '';
    for (let t = 0; t < 5; t++) {
      await page.waitForTimeout(400);
      rawText = await getNewPopoverText(page, beforePopovers);
      if (rawText) break;
    }

    // 마우스 이동해서 popover 닫기
    await page.mouse.move(0, 0);
    await page.waitForTimeout(300);

    const desc = parsePackageDesc(rawText, grp.name);
    results[grp.groupId] = desc;

    if (desc) {
      found++;
      process.stdout.write(`"${desc.slice(0, 60)}"\n`);
    } else {
      process.stdout.write(`없음 (raw: "${rawText.slice(0, 40)}")\n`);
    }
  }

  // has_description 없는 패키지는 빈 문자열
  for (const pkg of data) {
    if (!(pkg.packageId in results)) {
      results[pkg.packageId] = '';
    }
  }

  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2), 'utf8');
  console.log(`\n완료: has_description ${hasDescGroups.length}개 중 ${found}개 설명 추출`);
  console.log(`저장: ${OUTPUT_PATH}`);

  await browser.close();
})();
