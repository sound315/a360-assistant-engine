# -*- coding: utf-8 -*-
PACKAGE_NAME        = "목록"
PACKAGE_ID          = "command-group:list"
PACKAGE_DESCRIPTION = "목록 데이터 유형의 변수에 대해 다양한 작업을 수행합니다. 주요 액션: 항목 추가(목록 변수에 항목을 삽입합니다.)、지정(소스 목록의 값을 대상 목록 변수에 할당합니다.)、지우기(선택한 목록 변수에서 모든 항목을 지웁니다.)、항목 가져오기(목록의 지정된 위치에서 값을 검색하고 출력을 변수에 저장합니다.)、항목 결합(사용 가능한 모든 값을 목록 변수에 결합하고 출력을 문자열 변수에 저장합...) 외 4개."

ACTIONS = [
    {"action": "항목 추가", "data_item_name": "list#additem", "description": "목록 변수에 항목을 삽입합니다."},
    {"action": "지정", "data_item_name": "list#assign", "description": "소스 목록의 값을 대상 목록 변수에 할당합니다."},
    {"action": "지우기", "data_item_name": "list#clear", "description": "선택한 목록 변수에서 모든 항목을 지웁니다."},
    {"action": "항목 가져오기", "data_item_name": "list#get", "description": "목록의 지정된 위치에서 값을 검색하고 출력을 변수에 저장합니다."},
    {"action": "항목 결합", "data_item_name": "list#joinlist", "description": "사용 가능한 모든 값을 목록 변수에 결합하고 출력을 문자열 변수에 저장합니다."},
    {"action": "추가", "data_item_name": "list#assigntodatatable", "description": "데이터 테이블의 열 인덱스에 목록 변수를 추가합니다."},
    {"action": "항목 제거", "data_item_name": "list#listremove", "description": "목록에서 항목을 제거하고 출력을 변수에 할당합니다."},
    {"action": "항목 설정", "data_item_name": "list#listset", "description": "목록의 특정 위치에 항목을 설정하고 출력을 변수에 저장합니다."},
    {"action": "크기", "data_item_name": "list#listsize", "description": "목록의 항목 수를 검색하고 출력을 숫자 변수에 할당합니다."},
]