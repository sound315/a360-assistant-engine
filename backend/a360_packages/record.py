# -*- coding: utf-8 -*-
PACKAGE_NAME        = "기록"
PACKAGE_ID          = "command-group:record"
PACKAGE_DESCRIPTION = "레코드 유형 변수에 대해 다양한 작업을 수행합니다. 주요 액션: 열 추가(레코드 변수에 새 열을 추가합니다.)、지정(소스 기록 변수의 값을 대상 기록 변수에 지정)、열 삭제(레코드 변수에서 열을 삭제합니다.)、열 업데이트(레코드 변수의 열 값을 업데이트합니다.) (총 4개)."

ACTIONS = [
    {"action": "열 추가", "data_item_name": "record#addcolumn", "description": "레코드 변수에 새 열을 추가합니다."},
    {"action": "지정", "data_item_name": "record#assign", "description": "소스 기록 변수의 값을 대상 기록 변수에 지정"},
    {"action": "열 삭제", "data_item_name": "record#deletecolumn", "description": "레코드 변수에서 열을 삭제합니다."},
    {"action": "열 업데이트", "data_item_name": "record#updatecolumn", "description": "레코드 변수의 열 값을 업데이트합니다."},
]