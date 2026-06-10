# A360 KDS Action Palette Analyzer

Automation Anywhere A360 에디터 팔레트에서 패키지/액션 목록을 추출하고 활용하는 프로젝트.

## 폴더 구조

```
a360-kds-analysis/
├── scripts/
│   ├── 01_analyze_page.js     # 페이지 구조 초기 분석
│   ├── 02_expand_all.js       # 아코디언 그룹 전체 펼치기
│   └── 03_extract_actions.js  # 패키지/액션 JSON 추출 (메인)
├── output/
│   └── actions.json           # 추출 결과 (135 패키지, 1127 액션)
├── screenshots/
│   ├── before.png             # 펼치기 전
│   ├── after.png              # 펼친 후
│   └── palette.png            # 팔레트 클로즈업
└── README.md
```

## 추출 결과 (actions.json 구조)

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

## 다음 작업 (TODO)

- [ ] actions.json을 원래 프로젝트에서 활용
- [ ] 더블클릭 시 해당 액션 삽입 기능 구현
