/**
 * 08b_diagnose_package_tooltip.js
 * "기록" 패키지 헤더 hover 후 DOM에 어떤 요소가 나타나는지 전부 덤프
 * → 정확한 셀렉터 파악용
 */

const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    ignoreHTTPSErrors: true,
    executablePath: 'C:\\DEV\\ms-playwright\\chromium-1223\\chrome-win64\\chrome.exe',
  });
  const context = await browser.newContext({ ignoreHTTPSErrors: true });
  const page    = await context.newPage();

  console.log('로그인...');
  await page.goto('http://www.a360-kds.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(3000);
  await page.fill('input[name="username"]', 'ds.kim');
  await page.fill('input[name="password"]', 'qwert11!!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(8000);

  console.log('에디터 이동...');
  await page.goto('http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit', {
    waitUntil: 'domcontentloaded', timeout: 30000,
  });
  await page.waitForSelector('.editor-palette__accordion--is_active', { timeout: 15000 });
  await page.waitForTimeout(3000);

  // hover 전 DOM 스냅샷
  const before = await page.evaluate(() =>
    Array.from(document.querySelectorAll('body *')).map(el => el.className).filter(c => c && typeof c === 'string')
  );
  const beforeSet = new Set(before);

  // "기록" 그룹 버튼 찾아서 hover
  const btn = await page.evaluateHandle(() => {
    const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    return btns.find(b => b.textContent.trim() === '기록') || null;
  });

  const isNull = await page.evaluate(el => el === null, btn);
  if (isNull) { console.log('기록 버튼 없음'); await browser.close(); return; }

  await page.evaluate(el => el.scrollIntoView({ block: 'center' }), btn);
  await page.waitForTimeout(300);

  console.log('hover 시작...');
  await btn.hover({ force: true });

  // 최대 3초 기다리며 새로 생긴 요소 감지
  for (let i = 1; i <= 6; i++) {
    await page.waitForTimeout(500);

    const snapshot = await page.evaluate((beforeClasses) => {
      const beforeSet = new Set(beforeClasses);
      const results = [];

      // 새로 추가된 visible 요소
      for (const el of document.querySelectorAll('body *')) {
        const cls = typeof el.className === 'string' ? el.className : '';
        const text = el.textContent.trim();
        const rect = el.getBoundingClientRect();
        const visible = rect.width > 0 && rect.height > 0;

        if (!visible || !text || text.length < 5) continue;

        // "레코드" 또는 "변수" 포함하는 요소 우선 체크
        if (text.includes('레코드') || text.includes('변수') || text.includes('수행')) {
          results.push({
            tag: el.tagName,
            class: cls.slice(0, 100),
            text: text.slice(0, 150),
            isNew: !beforeSet.has(cls),
          });
        }
      }
      return results;
    }, [...beforeSet]);

    if (snapshot.length > 0) {
      console.log(`\n[${i*0.5}s] 관련 요소 ${snapshot.length}개 발견:`);
      for (const el of snapshot) {
        console.log(`  TAG: ${el.tag}`);
        console.log(`  CLS: ${el.class}`);
        console.log(`  TXT: ${el.text}`);
        console.log(`  NEW: ${el.isNew}`);
        console.log('  ---');
      }
      break;
    } else {
      console.log(`  ${i*0.5}s: 관련 요소 없음`);
    }
  }

  // 추가로 전체 visible 텍스트 중 짧지 않은 것 덤프
  console.log('\n=== hover 후 전체 tooltip/popover/overlay 요소 ===');
  const all = await page.evaluate(() => {
    const keywords = ['tooltip', 'popover', 'overlay', 'dropdown', 'menu', 'panel', 'help', 'hint', 'desc'];
    const results = [];
    for (const el of document.querySelectorAll('body *')) {
      const cls = typeof el.className === 'string' ? el.className.toLowerCase() : '';
      if (!keywords.some(k => cls.includes(k))) continue;
      const text = el.textContent.trim();
      const rect = el.getBoundingClientRect();
      if (rect.width === 0 || rect.height === 0 || !text || text.length < 5) continue;
      results.push({ tag: el.tagName, class: el.className.slice(0, 120), text: text.slice(0, 200) });
    }
    return results;
  });

  if (all.length === 0) {
    console.log('  없음');
  } else {
    for (const el of all) {
      console.log(`  [${el.tag}] .${el.class}`);
      console.log(`    → "${el.text}"`);
    }
  }

  console.log('\n10초 대기 (브라우저에서 직접 확인 가능)...');
  await page.waitForTimeout(10000);

  await browser.close();
})();
