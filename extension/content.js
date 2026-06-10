// A360 작업 편집기 URL 패턴 확인
const TARGET_HASH_PATTERN = /\/#\/bots\/repository\/private\/files\/task\/[^/]+\/edit/;

function isTargetPage() {
  return TARGET_HASH_PATTERN.test(window.location.href);
}

// Iframe 주입
function injectChatbot() {
  if (document.getElementById("a360-assistant-iframe")) return;

  const wrapper = document.createElement("div");
  wrapper.id = "a360-assistant-wrapper";
  wrapper.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 420px;
    height: 600px;
    z-index: 99999;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    display: flex;
    flex-direction: column;
  `;

  const header = document.createElement("div");
  header.style.cssText = `
    background: #1a73e8;
    color: white;
    padding: 8px 12px;
    font-family: sans-serif;
    font-size: 14px;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: move;
    user-select: none;
  `;
  const iconBtnStyle =
    "background:rgba(255,255,255,0.18);border:none;color:white;cursor:pointer;" +
    "border-radius:5px;padding:3px 5px;display:flex;align-items:center;justify-content:center;";
  header.innerHTML = `
    <div style="display:flex;align-items:center;gap:5px;">
      <button id="a360-expand-all" title="전체 펼치기 (loop·if·try 등 모든 블록 펼침)" style="${iconBtnStyle}">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor"
             stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 4l4 4 4-4"/><path d="M4 9l4 4 4-4"/>
        </svg>
      </button>
      <button id="a360-collapse-all" title="전체 접기 (loop·if·try 등 모든 블록 접음)" style="${iconBtnStyle}">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor"
             stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 7l4-4 4 4"/><path d="M4 12l4-4 4 4"/>
        </svg>
      </button>
    </div>
    <span style="flex:1;text-align:center;">🤖 A360 Assistant</span>
    <button id="a360-toggle-btn" style="background:none;border:none;color:white;font-size:18px;cursor:pointer;">−</button>
  `;

  const iframe = document.createElement("iframe");
  iframe.id = "a360-assistant-iframe";
  iframe.src = "http://localhost:8501";
  iframe.style.cssText = "flex:1;border:none;background:#fff;";

  wrapper.appendChild(header);
  wrapper.appendChild(iframe);
  document.body.appendChild(wrapper);

  // 토글 (최소화/복원)
  let collapsed = false;
  document.getElementById("a360-toggle-btn").addEventListener("click", () => {
    collapsed = !collapsed;
    iframe.style.display = collapsed ? "none" : "flex";
    wrapper.style.height = collapsed ? "40px" : "600px";
    document.getElementById("a360-toggle-btn").textContent = collapsed ? "+" : "−";
  });

  // 캔버스 전체 펼치기 / 접기 버튼 (loop·if·try 등 블록 노드)
  const expandBtn = document.getElementById("a360-expand-all");
  const collapseBtn = document.getElementById("a360-collapse-all");
  // 버튼 클릭이 헤더 드래그로 번지지 않도록
  [expandBtn, collapseBtn].forEach((b) =>
    b.addEventListener("mousedown", (e) => e.stopPropagation())
  );
  expandBtn.addEventListener("click", () => setAllCanvasNodes(false));
  collapseBtn.addEventListener("click", () => setAllCanvasNodes(true));

  // 드래그
  makeDraggable(wrapper, header);

  // iframe 메시지 수신 → A360 UI에 액션 적용
  window.addEventListener("message", (event) => {
    if (event.data?.type === "A360_STEPS") {
      console.log("[A360 Assistant] 메시지 수신:", event.data.payload);
      applyStepsToA360(event.data.payload);
    }
  });
}

// 드래그 기능
function makeDraggable(el, handle) {
  let startX, startY, startLeft, startTop;
  handle.addEventListener("mousedown", (e) => {
    startX = e.clientX;
    startY = e.clientY;
    const rect = el.getBoundingClientRect();
    startLeft = rect.left;
    startTop = rect.top;

    function onMove(ev) {
      el.style.left = startLeft + (ev.clientX - startX) + "px";
      el.style.top = startTop + (ev.clientY - startY) + "px";
      el.style.right = "auto";
      el.style.bottom = "auto";
    }
    function onUp() {
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseup", onUp);
    }
    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseup", onUp);
    e.preventDefault();
  });
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const normalizeName = (s) => (s || "").replace(/\s+/g, " ").trim();

// A360 액션 목록을 편집기에 순차 적용
// payload: [{ package, action, data_item_name? }, ...]
async function applyStepsToA360(payload) {
  const steps = Array.isArray(payload) ? payload : [];
  if (!steps.length) return;

  // 1. 이미 펼쳐져 보이는 항목은 제외하고, 펼쳐야 할 패키지만 추림
  //    (접힌 그룹은 아이템이 DOM에서 제거되므로 미리 못 찾음 → 패키지명으로 식별)
  const neededPackages = new Set();
  for (const step of steps) {
    if (!findPaletteItem(step)) neededPackages.add(step.package);
  }

  // 2. 필요한 그룹만 선택적으로 펼침 (이미 펼쳐진 그룹은 건너뜀)
  if (neededPackages.size) {
    const clicked = await expandGroups(neededPackages);
    console.log(`[A360 Assistant] 선택적 펼치기: ${clicked}개 그룹 (대상: ${[...neededPackages].join(", ")})`);
  }

  // 3. 안전망 — 그래도 못 찾은 항목이 있으면(패키지명 불일치 등) 전체 펼치기 폴백
  const stillMissing = steps.some((s) => !findPaletteItem(s));
  if (stillMissing) {
    console.log("[A360 Assistant] 일부 항목 미발견 → 전체 펼치기 폴백");
    await expandAllGroups();
  }

  // 4. 순차 더블클릭으로 추가
  for (const step of steps) {
    await addActionToEditor(step);
    await sleep(400);
  }
}

// 팔레트에서 액션 아이템 요소를 찾음 (data_item_name 우선, 텍스트 폴백)
// 접힌 그룹의 아이템은 DOM에 없으므로 null 반환
function findPaletteItem(step) {
  if (step.data_item_name) {
    const el = document.querySelector(
      `[data-path="EditorPalette.item"][data-item-name="${step.data_item_name}"]`
    );
    if (el) return el;
  }
  if (step.action) {
    for (const el of document.querySelectorAll('[data-path="EditorPalette.item"]')) {
      if (el.textContent.trim() === step.action) return el;
    }
  }
  return null;
}

// 지정된 패키지명에 해당하는 그룹만 펼침
// 그룹 버튼은 한글 패키지명 텍스트로만 식별 가능 (data 속성 없음)
// 이미 펼쳐진(aria-expanded=true) 그룹은 건너뜀
async function expandGroups(packageNames) {
  const palette = document.querySelector(".editor-palette__accordion--is_active");
  if (!palette) return 0;

  const wanted = new Set([...packageNames].map(normalizeName));
  const buttons = Array.from(
    palette.querySelectorAll('[data-path="EditorPalette.group.button"]')
  );

  let clicked = 0;
  for (const btn of buttons) {
    if (wanted.has(normalizeName(btn.textContent)) && btn.getAttribute("aria-expanded") === "false") {
      btn.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
      clicked++;
    }
  }
  if (clicked) await sleep(700);
  return clicked;
}

// 팔레트의 닫힌 그룹 아코디언을 모두 펼침 (선택적 펼치기 실패 시 폴백)
// DOM: [data-path="EditorPalette.group.button"][aria-expanded="false"]
async function expandAllGroups() {
  const palette = document.querySelector(".editor-palette__accordion--is_active");
  if (!palette) return;

  for (let pass = 0; pass < 5; pass++) {
    const closedBtns = Array.from(
      palette.querySelectorAll('[data-path="EditorPalette.group.button"][aria-expanded="false"]')
    );
    if (!closedBtns.length) break;
    closedBtns.forEach((btn) =>
      btn.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }))
    );
    await new Promise((r) => setTimeout(r, 600));
  }
}

// 액션 아이템을 팔레트에서 찾아 더블클릭(합성 이벤트)으로 캔버스에 삽입
// DOM: [data-path="EditorPalette.item"][data-item-name="{packageId}#{actionId}"]
// ref: a360-kds-analysis/output/actions.json, a360-kds-analysis/test_add.js (검증)
async function addActionToEditor(step) {
  const { package: pkg, action, data_item_name } = step;

  const target = findPaletteItem(step);

  if (!target) {
    console.warn(`[A360 Assistant] 요소 없음: ${pkg} > ${action} — actions.json 매핑 확인 필요`);
    return;
  }

  // 보이도록 스크롤 (가상 스크롤 팔레트 대비)
  try { target.scrollIntoView({ block: "center", inline: "center" }); } catch (e) {}
  await sleep(150);

  fireDoubleClick(target);
  console.log(`[A360 Assistant] 추가됨: ${pkg} > ${action} (${data_item_name ?? "텍스트 매칭"})`);
}

// 가장 안쪽 자식(leaf)에 마우스 이벤트 시퀀스를 발사
// ※ Playwright 실측 검증(test_add.js): 컨테이너에 직접 dispatch하면 A360 핸들러가 무시.
//   leaf에 dispatch해야 동작 (React가 event.target 을 leaf 기준으로 판정)
function fireMouseSequence(el, types) {
  let leaf = el;
  while (leaf.firstElementChild) leaf = leaf.firstElementChild;
  types.forEach((type) =>
    leaf.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true, view: window }))
  );
}

// 팔레트 아이템을 더블클릭으로 캔버스에 추가
function fireDoubleClick(el) {
  fireMouseSequence(el, ["mousedown", "mouseup", "click", "mousedown", "mouseup", "click", "dblclick"]);
}

// 캔버스의 컨테이너 노드(loop·if·try 등) 전체 펼치기/접기
// 토글 요소: .taskbot-canvas-list-node__collapser
// 상태: 자식 아이콘 fa-caret-down=펼침, fa-caret-right=접힘
// ※ Playwright 검증(test_collapse_all.js): 중첩 노드는 반복 처리 필요
//   (접으면 자식 collapser가 DOM에서 제거, 펼치면 자식이 새로 나타남)
async function setAllCanvasNodes(collapse) {
  const targetIcon = collapse ? "fa-caret-down" : "fa-caret-right";
  let clicked = 0;

  for (let pass = 0; pass < 12; pass++) {
    const targets = Array.from(
      document.querySelectorAll(".taskbot-canvas-list-node__collapser")
    ).filter((c) => c.querySelector("." + targetIcon));
    if (!targets.length) break;
    targets.forEach((c) => fireMouseSequence(c, ["mousedown", "mouseup", "click"]));
    clicked += targets.length;
    await sleep(400);
  }

  console.log(`[A360 Assistant] 캔버스 ${collapse ? "전체 접기" : "전체 펼치기"}: ${clicked}회 토글`);
}

// URL 변경 감지 (SPA 해시 라우팅)
let lastHref = window.location.href;
const observer = new MutationObserver(() => {
  if (window.location.href !== lastHref) {
    lastHref = window.location.href;
    if (isTargetPage()) {
      setTimeout(injectChatbot, 500);
    }
  }
});
observer.observe(document.body, { childList: true, subtree: true });

// 초기 실행
if (isTargetPage()) {
  setTimeout(injectChatbot, 500);
}
