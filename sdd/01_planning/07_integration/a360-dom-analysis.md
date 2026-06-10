# Integration Planning: A360 KDS 편집기 DOM 분석

## 분석 도구

`a360-kds-analysis/` — Playwright 기반 A360 편집기 페이지 분석 프로젝트.

| 스크립트 | 역할 |
|----------|------|
| `scripts/01_analyze_page.js` | 페이지 초기 구조 분석, 아코디언 요소 카운트 |
| `scripts/02_expand_all.js` | 아코디언 그룹 전체 펼치기 |
| `scripts/03_extract_actions.js` | 패키지/액션 JSON 추출 (메인) |

## 확인된 DOM 구조

### 팔레트 컨테이너
```css
.editor-palette__accordion.editor-palette__accordion--is_active
```

### 그룹(패키지) 펼치기 버튼
```css
[data-path="EditorPalette.group.button"][aria-expanded="false"]
```
- `click` 이벤트로 펼치기/접기 토글

### 액션 아이템
```css
[data-path="EditorPalette.item"]
.editor-palette-item
```
- `data-item-name` 속성: `{packageId}#{actionId}` 형식 (예: `record#addcolumn`)
- **더블클릭으로 편집기 캔버스에 액션 삽입**

## 추출 결과

- `output/actions.json` — **135 패키지, 1127 액션** (실제 추출 완료)
- `backend/a360_tasks.py` — actions.json 기반으로 자동 생성됨 (1271줄)
- 구조:
  ```json
  [
    {
      "packageId": "command-group:record",
      "packageName": "기록",
      "isOpen": true,
      "actionCount": 4,
      "actions": [
        {
          "name": "열 추가",
          "attrs": {
            "data-path": "EditorPalette.item",
            "data-item-name": "record#addcolumn",
            "class": "editor-palette-item"
          }
        }
      ]
    }
  ]
  ```

## 더블클릭 삽입 구현 패턴

```javascript
// 그룹이 닫혀 있으면 먼저 펼치기
const groupBtn = document.querySelector(
  `.editor-palette__accordion--is_active [data-path="EditorPalette.group.button"][aria-expanded="false"]`
);
if (groupBtn) groupBtn.dispatchEvent(new MouseEvent('click', { bubbles: true }));

// 액션 더블클릭
const item = document.querySelector(
  `[data-path="EditorPalette.item"][data-item-name="${packageId}#${actionId}"]`
);
item.dispatchEvent(new MouseEvent('dblclick', { bubbles: true, cancelable: true, view: window }));
```

## 연결 작업

- `a360_tasks.py`의 각 태스크에 `data_item_name` 매핑 필요 → `output/actions.json` 참조
- `extension/content.js`의 `addActionToEditor`에 위 셀렉터 패턴 반영
- 스크린샷: `screenshots/before.png`, `after.png`, `palette.png`
