# -*- coding: utf-8 -*-
PACKAGE_NAME        = "대화형 양식"
PACKAGE_ID          = "command-group:forms"
PACKAGE_DESCRIPTION = "양식에서의 상호 작용 및 작업 주요 액션: 표시(지정된 양식 로드 및 표시)、닫기(대화형 양식: 닫기양식 닫기필요한 Bot Agent 버전: 21.88 이...)、보기(숨겨진 양식 보기)、숨기기(표시된 양식 숨기기)、재설정(양식에서 모든 값을 지웁니다) 외 13개."

ACTIONS = [
    {"action": "표시", "data_item_name": "forms#uiformdisplay", "description": "지정된 양식 로드 및 표시"},
    {"action": "닫기", "data_item_name": "forms#uiformclose", "description": "대화형 양식: 닫기양식 닫기필요한 Bot Agent 버전: 21.88 이상"},
    {"action": "보기", "data_item_name": "forms#uiformshow", "description": "숨겨진 양식 보기"},
    {"action": "숨기기", "data_item_name": "forms#uiformhide", "description": "표시된 양식 숨기기"},
    {"action": "재설정", "data_item_name": "forms#uiformclear", "description": "양식에서 모든 값을 지웁니다"},
    {"action": "양식 검증", "data_item_name": "forms#uiformvalidateform", "description": "대화형 양식: 양식 검증양식 검증필요한 Bot Agent 버전: 21.88 이상"},
    {"action": "양식 제목 변경", "data_item_name": "forms#uiformchangetitle", "description": "양식 제목 변경"},
    {"action": "지정", "data_item_name": "forms#uiformassign", "description": "옵션을 양식 드롭다운에 할당"},
    {"action": "활성화", "data_item_name": "forms#uiformenable", "description": "양식 요소 활성화"},
    {"action": "비활성화", "data_item_name": "forms#uiformdisable", "description": "양식 요소 비활성화"},
    {"action": "가져오기", "data_item_name": "forms#uiformgetvalue", "description": "지정된 양식 요소에서 값을 가져옵니다"},
    {"action": "설정", "data_item_name": "forms#formsetvalue", "description": "변수 값을 양식 요소로 설정합니다"},
    {"action": "포커스 설정", "data_item_name": "forms#uiformsetfocus", "description": "포커스를 양식 요소로 설정"},
    {"action": "강조 표시", "data_item_name": "forms#uiformhighlight", "description": "양식 요소 강조 표시"},
    {"action": "강조 표시 해제", "data_item_name": "forms#uiformunhighlight", "description": "양식 요소 강조 표시 해제"},
    {"action": "라벨 변경", "data_item_name": "forms#uiformchangelabel", "description": "양식 요소의 라벨 변경"},
    {"action": "동적 영역에 행 추가", "data_item_name": "forms#uiformaddelement", "description": "실행 시간 동안 동적 영역의 한 행에 양식 필드를 렌더링합니다"},
    {"action": "지우기", "data_item_name": "forms#uiformclearelement", "description": "양식 동적 영역에서 모든 요소 지우기"},
]