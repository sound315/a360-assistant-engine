# Task Plan: A360 Assistant Engine

---

## Phase 1 — 초기 구현 (완료)

### 범위
FastAPI 백엔드, Streamlit UI, Chrome Extension 초기 골격 구현

### 수용 기준
- [x] FastAPI /health, /tasks, /chat 엔드포인트
- [x] LLM이 허용 목록 내 A360 액션만 포함한 JSON 반환
- [x] Streamlit 2컬럼 챗봇 UI + postMessage 발송
- [x] Chrome Extension iframe 주입 + A360 더블클릭

### 체크리스트
- [x] 01_planning 아티팩트 (feature, architecture, api, integration)
- [x] backend/schemas.py, llm_client.py, main.py
- [x] frontend/app.py
- [x] extension/manifest.json, content.js, background.js, popup.html/js
- [x] .env.example, requirements.txt

---

## Phase 2 — A360 액션 데이터 추출 및 강화 (완료)

### 범위
실제 A360 UI에서 1127개 액션 + 설명 추출, 135개 패키지 설명 생성

### 수용 기준
- [x] actions.json: 135패키지 1127액션, 설명 100% 채움
- [x] a360_packages/*.py: 135개 개별 파일 (PACKAGE_NAME, PACKAGE_ID, PACKAGE_DESCRIPTION, ACTIONS)
- [x] a360_tasks.py: PACKAGES 메타데이터에 description 포함
- [x] 패키지 설명: 103개 A360 UI 공식 설명 + 32개 액션 기반 요약

### 체크리스트
- [x] 05_extract_tooltips.js: headless:false hover → 1115개 설명
- [x] 07_reextract_missing.js: 12개 누락 재추출
- [x] 08d_extract_package_desc_v2.js: 패키지 popover 감지 → 105개 공식 설명
- [x] 09_generate_package_descriptions.py: 공식설명 + 액션요약 합산 생성
- [x] 99_toolchain/a360-kds-analysis.md 문서화

---

## Phase 3 — LLM 프롬프트 최적화 (완료)

### 범위
패키지 설명을 시스템 프롬프트에 통합, 정확도 향상

### 가정
- Azure OpenAI API Key 필요 (.env 설정 후 실행 가능)
- 패키지 설명이 LLM의 패키지 선택 정확도를 높임

### 수용 기준
- [x] llm_client.py: 시스템 프롬프트에 패키지 설명 헤더 포함
- [x] 시스템 프롬프트 형식: `[패키지명] — 패키지설명\n  - 액션명 (액션설명)`
- [x] /chat 엔드포인트 실 테스트 — 정상 응답 확인 (2026-06-09)

### 체크리스트
- [x] llm_client.py _build_system_prompt() 에 PACKAGES description 통합
- [x] 03_build 갱신
- [x] 04_verify 갱신

### 현재 노트
- 시스템 프롬프트 예상 토큰: ~16,000 (패키지 설명 포함 시 ~1,000 추가)
- 패키지 설명으로 동음이의 액션 구분 가능 (예: "지정" → 기록/날짜시간/변수 등)

---

## Phase 5 — Cloud Run 배포 (완료, 2026-06-12)

### 범위
FastAPI 백엔드 + Streamlit 프론트엔드를 Google Cloud Run 서버리스로 배포

### 수용 기준
- [x] 백엔드 Cloud Run 배포 및 /health 응답 확인
- [x] 프론트엔드 Cloud Run 배포 및 HTTP 200 확인
- [x] Azure OpenAI 환경변수 Cloud Run 설정 완료
- [x] 확장프로그램 URL → Cloud Run URL로 교체
- [x] GitHub Cloud Build 트리거 연동 (main 브랜치 push → 자동 빌드)

### 체크리스트
- [x] backend/Dockerfile, requirements.txt, .dockerignore 추가
- [x] frontend/Dockerfile, requirements.txt, .dockerignore 추가
- [x] frontend/app.py BACKEND_URL → Cloud Run 백엔드 URL
- [x] extension/content.js iframe.src → Cloud Run 프론트엔드 URL
- [x] extension/popup.html 챗봇 링크 → Cloud Run 프론트엔드 URL
- [x] extension/manifest.json host_permissions → Cloud Run URL + http://a360-kds.com/* (www 제거)
- [x] Cloud Build 트리거 Dockerfile 빌드 설정 (backend/, frontend/ 각각)
- [x] 종단 테스트 확인 (확장프로그램 → Streamlit → FastAPI → Azure OpenAI)

### 배포 정보
| 서비스 | URL |
|--------|-----|
| 백엔드 | https://a360-assistant-backend-10058727458.asia-northeast3.run.app |
| 프론트엔드 | https://a360-assistant-frontend-10058727458.asia-northeast3.run.app |

---

## Phase 4 — Extension 실환경 연동 (완료)

### 범위
챗봇 결과(steps)를 Chrome Extension으로 전달하여 A360 편집기에 자동 추가하는 종단 연동

### 가정
- A360 편집기는 팔레트 아이템 더블클릭으로 캔버스 추가 지원 (분석 단계 검증 완료)
- DOM 셀렉터(`EditorPalette.group.button`, `EditorPalette.item`) 실환경 유효 (분석 단계 검증 완료)

### 수용 기준
- [x] Streamlit iframe 임베딩 차단 해제 (config.toml: enableCORS/XSRF off)
- [x] Extension Private Network Access 헤더 주입 (declarativeNetRequest rules.json)
- [x] postMessage 전달 경로 수정: `window.parent` → `window.top` (3단계 중첩 iframe 관통)
- [x] **더블클릭 대상 수정**: 컨테이너가 아닌 leaf 자식에 dispatch (Playwright 실측 검증)
- [x] 실환경 Extension 종단 동작 확인 (사용자 브라우저 — 노드 추가 성공)
- [x] **선택적 그룹 펼치기**: 필요한 패키지 그룹만 펼침 + 이미 펼쳐진 그룹 건너뜀
- [x] **캔버스 전체 펼치기/접기 버튼**: 챗봇 헤더 좌측 아이콘 2개 (loop·if·try 블록 일괄 토글)
- [ ] 파라미터 자동 입력 (URL·파일경로 등) — 미구현
- [ ] 삽입 위치/순서 제어 — 미구현 (현재 캔버스 끝 순차 추가)

### 체크리스트
- [x] frontend/.streamlit/config.toml 생성
- [x] extension/rules.json 생성 + manifest.json declarativeNetRequest 등록
- [x] extension/content.js: iframe sandbox 제거, 메시지 수신 로그 추가
- [x] frontend/app.py: window.top postMessage + parent 폴백
- [x] content.js fireDoubleClick: leaf 자식 타겟으로 수정
- [x] test_add.js Playwright 실측 검증 (노드 6→7 추가 확인)
- [x] content.js: findPaletteItem / expandGroups 선택적 펼치기 + 전체펼치기 폴백
- [x] test_selective.js Playwright 검증 (3패키지만 펼침, 3/106 그룹, 노드 +3)
- [x] content.js: 헤더 좌측 SVG 버튼 2개 + setAllCanvasNodes(collapse) 반복 토글
- [x] test_collapse_all.js Playwright 검증 (중첩 4개 접기→2개, 펼치기→4개 복원)

### 현재 노트
- **자동 추가 미동작 원인 2가지 모두 해소:**
  1. postMessage가 `window.parent`로만 발송 → 최상위 A360 페이지에 미도달. `window.top`으로 수정.
  2. 더블클릭을 `[data-path="EditorPalette.item"]` 컨테이너에 dispatch → A360 핸들러 무시. **가장 안쪽 자식(leaf)에 dispatch해야 노드 추가됨** (React가 event.target을 leaf 기준 판정).
- 검증 방법: test_add.js — leaf 시퀀스(A4)는 노드 +1, 컨테이너 dispatch(A1~A3)는 변화없음, 신뢰된 더블클릭(B)도 +1. 즉 **CDP/debugger 불필요, 합성 이벤트로 충분.**
- **선택적 펼치기 설계 (test_selective.js 검증):**
  - 접힌 그룹은 아이템이 DOM에서 **제거**됨 → 미리 못 찾으므로 패키지명으로 그룹 식별
  - 그룹 버튼은 한글 패키지명 **텍스트로만** 식별 가능 (data 속성 없음). 버튼 헤더는 접혀도 DOM 잔존
  - step.package ↔ 그룹 버튼 텍스트 매칭 → 접힌(`aria-expanded=false`) 것만 클릭 (펼쳐진 건 건너뜀)
  - 패키지명 불일치(예: "Web"↔"UI 에이전트 - 웹") 대비 **전체 펼치기 폴백** 유지
  - 결과: 3패키지 입력 시 3/106 그룹만 펼침 (기존 전체 펼치기 대비 최소화)
- 중첩 구조: A360 페이지 > Streamlit iframe > components.v1.html iframe
- 다음 고도화: 파라미터 입력, 삽입 위치 — 종단 검증 후 착수
