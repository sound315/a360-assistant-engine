# Toolchain: A360 KDS Action Palette Analyzer

**위치:** `a360-kds-analysis/`  
**목적:** A360 편집기 팔레트의 실제 패키지/액션 목록 추출 및 더블클릭 동작 검증

## 실행 방법

```bash
cd a360-kds-analysis
npm install

# 1단계: 페이지 구조 분석
node scripts/01_analyze_page.js

# 2단계: 아코디언 전체 펼치기 확인
node scripts/02_expand_all.js

# 3단계: 패키지/액션 전체 추출 → output/actions.json
node scripts/03_extract_actions.js
```

## 의존성

- `playwright` ^1.60.0
- Chromium 실행 경로: `C:\DEV\ms-playwright\chromium-1223\chrome-win64\chrome.exe`

## 출력물

| 파일 | 설명 |
|------|------|
| `output/actions.json` | 135 패키지, 1127 액션 전체 목록 |
| `screenshots/before.png` | 팔레트 펼치기 전 |
| `screenshots/after.png` | 팔레트 펼친 후 |
| `screenshots/palette.png` | 팔레트 클로즈업 |

## actions.json 활용

`output/actions.json`의 `data-item-name` 값을 `backend/a360_tasks.py`의 각 태스크에 `data_item_name` 필드로 매핑하면 `extension/content.js`에서 정확한 셀렉터로 더블클릭 삽입이 가능해진다.

→ 상세 DOM 패턴은 `sdd/01_planning/07_integration/a360-dom-analysis.md` 참조
