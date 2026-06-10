# -*- coding: utf-8 -*-
PACKAGE_NAME        = "동적 영역"
PACKAGE_ID          = "동적 영역"
PACKAGE_DESCRIPTION = "주요 액션: 동적 영역에 행 추가(실행 시간 동안 동적 영역의 한 행에 양식 필드를 렌더링합니다)、지우기(양식 동적 영역에서 모든 요소 지우기) (총 2개)."

ACTIONS = [
    {"action": "동적 영역에 행 추가", "data_item_name": "forms#uiformaddelement", "description": "실행 시간 동안 동적 영역의 한 행에 양식 필드를 렌더링합니다"},
    {"action": "지우기", "data_item_name": "forms#uiformclearelement", "description": "양식 동적 영역에서 모든 요소 지우기"},
]