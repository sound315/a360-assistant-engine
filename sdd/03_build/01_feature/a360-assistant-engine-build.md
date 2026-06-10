# Build Summary: A360 Assistant Engine

## Phase 1 — 초기 구현

### backend/schemas.py
- `ChatRequest`: 사용자 메시지 + 히스토리
- `ChatResponse`: steps(A360Action 리스트) + message(요약 텍스트)
- `A360Action`: package, action, data_item_name

### backend/main.py
- FastAPI 앱, CORS 전체 허용
- `GET /health`: 상태 확인
- `GET /tasks`: 전체 액션 목록 반환
- `POST /chat`: LLM 호출 → `_ITEM_NAME_MAP`으로 data_item_name 보강 → ChatResponse 반환

### frontend/app.py
- Streamlit 2컬럼 레이아웃 (챗봇 + JSON 미리보기)
- 대화 히스토리 유지 (session_state)
- 응답 후 `window.parent.postMessage({type:'A360_STEPS', payload:steps}, '*')` 발송
- JSON 다운로드 버튼

### extension/
- `manifest.json`: MV3, `http://www.a360-kds.com/*`
- `content.js`: 해시 URL 패턴 감지, 드래그 가능 iframe 주입, expandAllGroups(), addActionToEditor()
  - 액션 셀렉터: `[data-path="EditorPalette.item"][data-item-name="{data_item_name}"]`
  - SPA 해시 변경 MutationObserver 감지
- `background.js`, `popup.html/js`: 팝업 상태 표시

---

## Phase 2 — A360 액션 데이터 추출 및 강화

### a360-kds-analysis/scripts/ (toolchain)
| 스크립트 | 역할 | 결과 |
|---------|------|------|
| `05_extract_tooltips.js` | headless:false hover → 액션 설명 대량 추출 | 1115/1127개 |
| `07_reextract_missing.js` | 누락 12개 재추출 (`[class*="help"]` + popover 파싱) | 12/12개 |
| `08d_extract_package_desc_v2.js` | 패키지 그룹 hover → `use-popover-poppy` 신규 감지 | 105/135개 |
| `09_generate_package_descriptions.py` | 공식설명 + 액션요약 합산 → 패키지 설명 완성 | 135개 |

### backend/a360_tasks.py
- 135개 패키지 메타데이터 (name, id, action_count, file, **description**)
- `load_all_tasks()` 위임 → `a360_packages/__init__.py`
- `A360_TASKS`: 1127개 전체 액션
- `PACKAGES`: 135개 패키지 메타데이터 (description 포함)
- `ALLOWED_PAIRS`: LLM 필터용 허용 조합

### backend/a360_packages/__init__.py
- `importlib`로 `*.py` 동적 로드
- 각 모듈에서 `PACKAGE_NAME`, `ACTIONS` 읽어 통합

### backend/a360_packages/*.py (135개 파일)
- 각 파일: `PACKAGE_NAME`, `PACKAGE_ID`, `PACKAGE_DESCRIPTION`, `ACTIONS`
- 각 액션: `action`, `data_item_name`, `description`
- 1127개 액션 설명 100% 채움

---

## Phase 3 — LLM 프롬프트 최적화

### backend/llm_client.py
- `PACKAGES` import 추가
- `_build_system_prompt()`: 패키지 설명 헤더 포함
  ```
  [브라우저] — 브라우저 작업을 수행하기 위한 동작을 제공합니다. 주요 액션: ...
    - 열기 (URL을 지정된 브라우저에서 열기)
    - 닫기 (현재 브라우저 탭 닫기)
  ```
- Azure OpenAI / OpenAI 자동 전환 (환경변수)
- `response_format: json_object` 강제 JSON 반환
- ALLOWED_PAIRS 필터링

---

## Phase 4 — Extension 실환경 연동

### frontend/.streamlit/config.toml (신규)
- `enableCORS=false`, `enableXsrfProtection=false`, `headless=true`
- Streamlit 기본 X-Frame-Options 제거 → iframe 임베딩 허용

### extension/rules.json (신규) + manifest.json
- `declarativeNetRequest` 규칙: localhost:8501 응답에 `Access-Control-Allow-Private-Network: true` 주입, `X-Frame-Options`/`CSP` 제거
- Chrome Private Network Access(공인 HTTP → localhost) 차단 해제
- manifest: `declarativeNetRequest` 권한 + 룰셋 등록

### frontend/app.py
- postMessage 발송 경로: `window.parent` → **`window.top`** (+ parent 폴백)
- 3단계 중첩 iframe(A360 > Streamlit > components) 관통하여 최상위 content.js 리스너에 도달

### extension/content.js
- iframe `sandbox` 속성 제거 (Streamlit WebSocket 차단 해소)
- `applyStepsToA360()`: async, **선택적 펼치기 → 폴백 → step별 순차 추가**
  1. `findPaletteItem()`으로 이미 보이는 항목 확인 → 안 보이는 패키지만 추림
  2. `expandGroups(needed)`로 필요한 그룹만 펼침 (이미 펼쳐진 건 건너뜀)
  3. 그래도 못 찾으면 `expandAllGroups()` 전체 펼치기 폴백
  4. step별 `addActionToEditor()` 순차 더블클릭
- **`findPaletteItem(step)`**: data_item_name 우선, action 텍스트 폴백. 접힌 그룹 아이템은 null
- **`expandGroups(packageNames)`**: 그룹 버튼 텍스트(한글 패키지명) ↔ step.package 매칭,
  `aria-expanded="false"`인 것만 클릭. 그룹 버튼엔 data 속성이 없어 텍스트가 유일한 키
- **`fireMouseSequence(el, types)`**: leaf로 내려가 지정 이벤트 시퀀스 발사 (공통 헬퍼)
- **`fireDoubleClick()`: 컨테이너가 아닌 가장 안쪽 자식(leaf)에 dispatch**
  - `[data-path="EditorPalette.item"]` 직접 dispatch는 A360 핸들러가 무시
  - leaf로 내려가 `mousedown→mouseup→click ×2 → dblclick` 발사해야 노드 추가
  - CDP/chrome.debugger 불필요 — 합성 이벤트로 동작

### 챗봇 헤더 — 캔버스 전체 펼치기/접기 버튼
- 헤더 좌측에 SVG 아이콘 버튼 2개 (이중 chevron: 아래=펼치기, 위=접기) + 한글 tooltip
- **`setAllCanvasNodes(collapse)`**: 캔버스 컨테이너 노드(loop·if·try) 일괄 토글
  - 토글 요소: `.taskbot-canvas-list-node__collapser`
  - 상태: 자식 아이콘 `fa-caret-down`=펼침 / `fa-caret-right`=접힘
  - 중첩 대응: 최대 12패스 반복 (접으면 자식 collapser가 DOM 제거, 펼치면 새로 나타남)
  - 버튼 mousedown에 `stopPropagation` → 헤더 드래그 간섭 방지
- content.js가 A360 페이지에 직접 주입한 헤더라 postMessage 없이 캔버스 DOM 직접 조작

### a360-kds-analysis/ (검증 스크립트, 보존)
| 스크립트 | 검증 내용 | 결과 |
|---------|----------|------|
| `test_add.js` | dispatch 방식별 노드 추가 | leaf 시퀀스 +1, 컨테이너 dispatch 변화없음 |
| `test_selective.js` | 선택적 그룹 펼치기 | 3패키지만 펼침(3/106), 노드 +3 |
| `test_collapse_all.js` | 캔버스 전체 접기/펼치기 | 중첩 4→접기2, 펼치기 4 복원 |

## 구현 제약사항
- 시스템 프롬프트: ~88,000자 / ~16,000 tokens (패키지 설명 포함)
- Azure OpenAI `response_format: json_object`는 메시지에 "JSON" 언급 필요
- 더블클릭 대상은 반드시 leaf 요소 (컨테이너 dispatch 무효)
- 접힌 그룹은 아이템이 DOM에서 제거 → 그룹은 패키지명(버튼 텍스트)으로만 식별
- 일부 패키지명 불일치(예: "Web"↔"UI 에이전트 - 웹") → 전체 펼치기 폴백으로 보완
- 파라미터 자동 입력·삽입 위치 제어는 미구현 (다음 단계)
