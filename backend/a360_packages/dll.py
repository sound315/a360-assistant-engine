# -*- coding: utf-8 -*-
PACKAGE_NAME        = "DLL"
PACKAGE_ID          = "command-group:dll"
PACKAGE_DESCRIPTION = ".dll 파일을 참조로 사용하고 Bot에서 함수를 호출합니다. 주요 액션: 닫기(DLL 참조를 닫습니다.)、열기(참조 파일을 엽니다.)、함수 실행(매개변수를 활용해 특정 DLL 함수를 실행합니다.) (총 3개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "dll#close", "description": "DLL 참조를 닫습니다."},
    {"action": "열기", "data_item_name": "dll#open", "description": "참조 파일을 엽니다."},
    {"action": "함수 실행", "data_item_name": "dll#runcsharpdll_v1", "description": "매개변수를 활용해 특정 DLL 함수를 실행합니다."},
]