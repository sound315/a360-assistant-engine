# Verify Summary: A360 Assistant Engine

## 데이터 검증 (완료)

### actions.json 완전성
```
총 135개 패키지, 1127개 액션
설명 없는 액션: 0/1127개
패키지 공식 설명: 103개 (A360 UI popover 추출)
패키지 액션 요약: 32개 (공식 설명 없는 패키지)
```

### 패키지 파일 로드 검증
```bash
cd backend
python -c "
from a360_tasks import A360_TASKS, PACKAGES, ALLOWED_PAIRS
print(len(A360_TASKS))   # 1127
print(len(PACKAGES))     # 135
print(len(ALLOWED_PAIRS))# 1121
"
```
결과: 정상 확인 (2026-06-09)

### 시스템 프롬프트 검증
```bash
cd backend
python -c "
from llm_client import _build_system_prompt
p = _build_system_prompt()
lines = p.split('\n')
headers = [l for l in lines if l.startswith('[')]
print(len(headers))   # 133 패키지 헤더
print(len(p))         # ~88,944자
"
```
결과:
- 전체 라인: 1,280개
- 패키지 헤더 133개 중 132개에 `— 설명` 포함
- 총 문자수: 88,944자

---

## 백엔드 실행 검증 절차

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 환경변수 설정
copy .env.example .env
# .env 파일에 AZURE_OPENAI_API_KEY 등 입력

# 3. 백엔드 실행
cd backend
uvicorn main:app --reload --port 8000

# 4. 헬스 체크
curl http://localhost:8000/health
# → {"status":"ok"}

# 5. 채팅 테스트
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"웹사이트를 열고 버튼을 클릭해줘"}'
# → {"steps":[{"package":"브라우저","action":"열기","data_item_name":"browser#open"},...],"message":"..."}
```

**상태:** 전체 엔드포인트 검증 완료 (2026-06-09)

| 엔드포인트 | 결과 |
|-----------|------|
| `GET /health` | `{"status":"ok"}` ✅ |
| `GET /tasks` | 1127개 액션 목록 반환 ✅ |
| `POST /chat` "웹사이트를 열고 로그인 버튼을 클릭해줘" | `브라우저 > 열기 [browser#openbrowser]`, `마우스 > 클릭 [mouse#mouseclick]` ✅ |
| `POST /chat` "PDF 파일에서 텍스트를 추출해줘" | `PDF > 텍스트 추출 [pdf#extracttext]` ✅ |
| `POST /chat` "이메일을 보내줘" | `이메일 > 연결 [email#emailconnect]`, `이메일 > 보내기 [email#sendmailv2]` ✅ |

---

## 프론트엔드 검증

```bash
cd frontend
streamlit run app.py --server.port 8501
# → http://localhost:8501
```

---

## Chrome Extension 검증
1. Chrome → `chrome://extensions/` → 개발자 모드 ON
2. "압축해제된 확장 프로그램 로드" → `extension/` 폴더 선택
3. `http://www.a360-kds.com/#/bots/repository/private/files/task/13/edit` 접속
4. 우하단 챗봇 iframe 확인
5. 챗봇 대화 → A360 편집기 더블클릭 확인
   - 셀렉터: `[data-path="EditorPalette.item"][data-item-name="{data_item_name}"]`
   - ⚠️ dispatch 대상은 컨테이너가 아닌 **leaf 자식 요소**

---

## 더블클릭 노드 추가 메커니즘 검증 (Playwright 실측, 2026-06-09)

`a360-kds-analysis/test_add.js` 로 dispatch 방식별 캔버스 노드 증감 실측.
대상: `record#assign` (기록>지정), 캔버스 노드 셀렉터 `[data-path="TaskbotCanvasListNode"]`

| 방식 | dispatch 대상 | 결과 |
|------|--------------|------|
| A1 `dblclick`만 | 컨테이너 | ❌ 변화없음 (6→6) |
| A2 `click`×2 | 컨테이너 | ❌ 변화없음 (6→6) |
| A3 전체 시퀀스 | 컨테이너 | ❌ 변화없음 (6→6) |
| **A4 전체 시퀀스** | **leaf 자식** | ✅ **+1 (6→7)** |
| B 신뢰된 dblclick(force) | leaf | ✅ +1 (7→8) |
| B2 신뢰된 dblclick | leaf | ✅ +1 (8→9) |

**결론:**
- 합성 이벤트(`dispatchEvent`)로 노드 추가 가능 — CDP/chrome.debugger 불필요
- 단, **반드시 가장 안쪽 자식(leaf)에 dispatch** (React가 event.target을 leaf 기준 판정)
- 시각 확인: 스크린샷 `dbg_add_final.png` — 7·8·9번 "기록: 지정" 노드 추가됨
- 명령: `cd a360-kds-analysis && node test_add.js`

### iframe 임베딩 / 통신 검증
- Streamlit config.toml 적용 후 응답 헤더에서 X-Frame-Options 제거 확인 (`curl -I localhost:8501`)
- 콘솔 로그 `[A360 Assistant] 메시지 수신` 확인 → postMessage(window.top) 도달 검증 완료
- 실환경 Extension 종단(챗봇→캔버스 추가) 사용자 브라우저 확인 완료 ✅

---

## 선택적 그룹 펼치기 검증 (Playwright 실측, 2026-06-09)

`a360-kds-analysis/test_selective.js` — 필요한 그룹만 펼치는 로직 실측.
입력 steps: 기록>지정, Excel 기본>열기, 마우스>클릭 (3개 패키지)

| 항목 | 결과 |
|------|------|
| 초기 표시 | 3개 모두 미표시 (그룹 접힘 상태) |
| 펼칠 패키지 식별 | 기록, Excel 기본, 마우스 (텍스트 매칭) |
| 클릭한 그룹 수 | **3개만** |
| 펼친 후 아이템 발견 | 3개 모두 ✅ |
| 펼쳐진 그룹 / 전체 | **3 / 106** (전체 펼치기 대비 대폭 최소화) |
| 노드 추가 | 6 → 9 (+3, 기대치 일치) ✅ |

**핵심 동작:**
- 접힌 그룹은 아이템이 DOM에서 제거 → step.package(한글)를 그룹 버튼 텍스트와 매칭해 식별
- `aria-expanded="false"`인 그룹만 클릭 → **이미 펼쳐진 그룹은 건너뜀**
- 패키지명 불일치 시 `expandAllGroups()` 전체 펼치기 폴백 (안전망)
- 명령: `cd a360-kds-analysis && node test_selective.js`

---

## 캔버스 전체 펼치기/접기 검증 (Playwright 실측, 2026-06-09)

`a360-kds-analysis/test_collapse_all.js` — 챗봇 헤더 버튼이 호출하는 `setAllCanvasNodes()` 로직 실측.
대상: task/13 캔버스의 중첩 루프 4개. 토글 요소 `.taskbot-canvas-list-node__collapser`.

| 단계 | collapser 상태 | 비고 |
|------|---------------|------|
| 초기 | total=4, 펼침=4 | 중첩 루프 모두 펼침 |
| **전체 접기** | total=2, 접힘=2 | 바깥 접으니 안쪽 2개 DOM 제거 → 컴팩트 ✅ |
| **전체 펼치기** | total=4, 펼침=4 | 반복 처리로 중첩까지 복원 ✅ |

**핵심 동작:**
- 상태 판정: 자식 아이콘 `fa-caret-down`=펼침 / `fa-caret-right`=접힘
- 합성 이벤트(`mousedown→mouseup→click`)로 토글 (CDP 불필요)
- 중첩: 접으면 자식 collapser DOM 제거, 펼치면 새로 나타남 → 최대 12패스 반복으로 수렴
- 시각 확인: `dbg_collapsed_all.png`(2개 접힘), `dbg_expanded_all.png`(4개 펼침)
- 명령: `cd a360-kds-analysis && node test_collapse_all.js`

---

---

## Cloud Run 배포 검증 (2026-06-12)

| 항목 | 결과 |
|------|------|
| 백엔드 `GET /health` | `{"status":"ok"}` ✅ |
| 백엔드 `POST /chat` | 정상 응답 (Azure OpenAI gpt-5.4-mini) ✅ |
| 프론트엔드 HTTP 200 | ✅ |
| 확장프로그램 iframe 표시 | ✅ |

---

## 잔여 위험

| 항목 | 위험 | 비고 |
|------|------|------|
| Azure OpenAI API Key | /chat 검증 완료 | ✅ |
| iframe CSP | a360-kds.com CSP 정책에 따라 차단 가능 | 실 환경 확인 필요 |
| LLM 토큰 비용 | 시스템 프롬프트 ~88,000자 (매 요청) | 필요 시 패키지 필터링으로 축소 |

## 해소된 위험

| 항목 | 해소 방법 |
|------|----------|
| A360 UI 셀렉터 | DOM 분석으로 `data-item-name` 패턴 확인, content.js 적용 완료 |
| 액션 설명 미비 | headless:false hover + 12개 재추출 → 1127개 100% |
| 패키지 설명 미비 | use-popover-poppy 신규 감지 → 103개 공식 + 32개 요약 |
| 동음이의 액션 구분 | 패키지 설명 + 액션 설명으로 LLM 컨텍스트 강화 |
| 잘못된 태스크 목록 | 수동 30개 → actions.json 기반 실제 1127개로 교체 |

## 회귀 범위
- 직접 대상: FastAPI /chat, /health, /tasks, Streamlit UI, Extension content.js
- 영향 없음: 외부 A360 서버 (읽기/클릭만 수행)
- 회귀 자동화: 미구성 (수동 검증)
