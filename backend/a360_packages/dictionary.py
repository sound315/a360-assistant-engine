# -*- coding: utf-8 -*-
PACKAGE_NAME        = "사전"
PACKAGE_ID          = "command-group:dictionary"
PACKAGE_DESCRIPTION = "사전 형식의 값에 대해 다양한 작업을 수행합니다. 주요 액션: 지정(원본 사전의 값을 대상 사전 변수에 할당합니다.)、가져오기(사전 변수에 키가 존재하는지 확인하고 해당 값을 반환합니다.)、업로드(사전의 키에 값을 할당합니다. 키가 이미 값과 연결되어 있으면 값을 업데...)、삭제(지정된 키에서 값을 제거합니다. 제거된 값은 '제거된 항목을 변수에 할당...)、크기(사전의 항목 수를 검색합니다.) (총 5개)."

ACTIONS = [
    {"action": "지정", "data_item_name": "dictionary#assign", "description": "원본 사전의 값을 대상 사전 변수에 할당합니다."},
    {"action": "가져오기", "data_item_name": "dictionary#get", "description": "사전 변수에 키가 존재하는지 확인하고 해당 값을 반환합니다."},
    {"action": "업로드", "data_item_name": "dictionary#put", "description": "사전의 키에 값을 할당합니다. 키가 이미 값과 연결되어 있으면 값을 업데이트할 수 있습니다."},
    {"action": "삭제", "data_item_name": "dictionary#remove", "description": "지정된 키에서 값을 제거합니다. 제거된 값은 '제거된 항목을 변수에 할당' 목록에서 선택한 변수에 할당됩니다."},
    {"action": "크기", "data_item_name": "dictionary#size", "description": "사전의 항목 수를 검색합니다."},
]