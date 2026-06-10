# -*- coding: utf-8 -*-
PACKAGE_NAME        = "클립보드"
PACKAGE_ID          = "command-group:clipboard"
PACKAGE_DESCRIPTION = "주요 액션: 복사 원본(클립보드에 저장된 값을 검색하고 변수에 지정)、복사 대상(변수를 검색하여 클립보드에 할당합니다.)、지우기(클립보드에서 내용을 지웁니다.) (총 3개)."

ACTIONS = [
    {"action": "복사 원본", "data_item_name": "clipboard#assignfromclipboard", "description": "클립보드에 저장된 값을 검색하고 변수에 지정"},
    {"action": "복사 대상", "data_item_name": "clipboard#assigntoclipboard", "description": "변수를 검색하여 클립보드에 할당합니다."},
    {"action": "지우기", "data_item_name": "clipboard#clearclipboard", "description": "클립보드에서 내용을 지웁니다."},
]