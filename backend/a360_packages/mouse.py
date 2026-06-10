# -*- coding: utf-8 -*-
PACKAGE_NAME        = "마우스"
PACKAGE_ID          = "command-group:mouse"
PACKAGE_DESCRIPTION = "마우스 동작을 시뮬레이션합니다. 주요 액션: 클릭(마우스 클릭을 시뮬레이션하고 화면이나 창과 같은 UI 요소를 캡처합니다.)、이동(한 위치에서 다른 위치로 마우스 포인터 이동을 시뮬레이션합니다.)、스크롤(마우스 휠을 위 또는 아래로 스크롤하는 것을 시뮬레이션합니다.) (총 3개)."

ACTIONS = [
    {"action": "클릭", "data_item_name": "mouse#mouseclick", "description": "마우스 클릭을 시뮬레이션하고 화면이나 창과 같은 UI 요소를 캡처합니다."},
    {"action": "이동", "data_item_name": "mouse#mousemove", "description": "한 위치에서 다른 위치로 마우스 포인터 이동을 시뮬레이션합니다."},
    {"action": "스크롤", "data_item_name": "mouse#mousescroll", "description": "마우스 휠을 위 또는 아래로 스크롤하는 것을 시뮬레이션합니다."},
]