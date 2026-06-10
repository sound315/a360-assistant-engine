/**
 * 08c_inspect_group_inner.js
 * "기록" 패키지 그룹 내부 전체 구조 덤프
 * + 각 액션 hover 시 popover에 패키지 설명이 포함되는지 확인
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

  // ── 1. 기록 패키지 그룹 컨테이너 내부 HTML 전체 덤프 ─────────────────────
  console.log('\n=== [1] 기록 그룹 컨테이너 내부 구조 ===');
  const groupHTML = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    const btn  = btns.find(b => b.textContent.trim() === '기록');
    if (!btn) return '기록 버튼 없음';
    // 버튼의 상위 컨테이너 (editor-palette-group-container 또는 비슷한 것)
    const container = btn.closest('[class*="group"]') || btn.parentElement;
    return container ? container.outerHTML.slice(0, 3000) : '컨테이너 없음';
  });
  console.log(groupHTML);

  // ── 2. 기록 그룹 버튼 내부 자식 요소 목록 ────────────────────────────────
  console.log('\n=== [2] 기록 버튼 자식 요소 ===');
  const children = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    const btn  = btns.find(b => b.textContent.trim() === '기록');
    if (!btn) return [];
    return Array.from(btn.querySelectorAll('*')).map(el => ({
      tag: el.tagName,
      cls: el.className?.slice?.(0, 80) || '',
      txt: el.textContent.trim().slice(0, 50),
    }));
  });
  for (const c of children) console.log(`  [${c.tag}] .${c.cls} → "${c.txt}"`);

  // ── 3. 기록 그룹 전체 컨테이너 (버튼 포함 상위) 자식 요소 ──────────────
  console.log('\n=== [3] 기록 그룹 컨테이너 전체 자식 ===');
  const allInGroup = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
    const btn  = btns.find(b => b.textContent.trim() === '기록');
    if (!btn) return [];
    // 2단계 상위까지 탐색
    const root = btn.parentElement?.parentElement || btn.parentElement;
    if (!root) return [];
    return Array.from(root.querySelectorAll('*')).map(el => ({
      tag: el.tagName,
      cls: el.className?.slice?.(0, 80) || '',
      txt: el.textContent.trim().slice(0, 80),
    }));
  });
  for (const c of allInGroup) {
    if (c.txt && c.txt.length > 3 && c.txt.length < 200)
      console.log(`  [${c.tag}] .${c.cls} → "${c.txt}"`);
  }

  // ── 4. 기록 첫 번째 액션(열 추가) hover → popover 전체 텍스트 확인 ────────
  console.log('\n=== [4] 기록>열 추가 hover → popover 전체 텍스트 ===');
  const item = await page.$('[data-item-name="record#addcolumn"]');
  if (item) {
    await item.scrollIntoViewIfNeeded();
    await item.hover({ force: true });
    await page.waitForTimeout(1500);

    const popoverText = await page.evaluate(() => {
      const results = [];
      for (const el of document.querySelectorAll('[class*="popover"], [class*="help"], [class*="tooltip"]')) {
        const t = el.textContent.trim();
        const r = el.getBoundingClientRect();
        if (t && r.width > 0 && r.height > 0)
          results.push({ cls: el.className?.slice?.(0, 80) || '', txt: t.slice(0, 300) });
      }
      return results;
    });

    for (const p of popoverText) {
      console.log(`  .${p.cls}`);
      console.log(`    → "${p.txt}"`);
    }
  } else {
    console.log('  record#addcolumn 요소 없음 (그룹 펼쳐야 함)');

    // 그룹 펼치기 시도
    const groupBtn = await page.evaluateHandle(() => {
      const btns = Array.from(document.querySelectorAll('[data-path="EditorPalette.group.button"]'));
      return btns.find(b => b.textContent.trim() === '기록') || null;
    });
    await groupBtn.click();
    await page.waitForTimeout(1000);

    const item2 = await page.$('[data-item-name="record#addcolumn"]');
    if (item2) {
      await item2.scrollIntoViewIfNeeded();
      await item2.hover({ force: true });
      await page.waitForTimeout(1500);

      const popoverText2 = await page.evaluate(() => {
        const results = [];
        for (const el of document.querySelectorAll('[class*="popover"], [class*="help"], [class*="tooltip"]')) {
          const t = el.textContent.trim();
          const r = el.getBoundingClientRect();
          if (t && r.width > 0 && r.height > 0)
            results.push({ cls: el.className?.slice?.(0, 80) || '', txt: t.slice(0, 300) });
        }
        return results;
      });
      for (const p of popoverText2) {
        console.log(`  .${p.cls}`);
        console.log(`    → "${p.txt}"`);
      }
    }
  }

  console.log('\n15초 대기...');
  await page.waitForTimeout(15000);
  await browser.close();
})();
