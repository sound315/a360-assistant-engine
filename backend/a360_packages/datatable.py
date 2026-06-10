# -*- coding: utf-8 -*-
PACKAGE_NAME        = "데이터 테이블"
PACKAGE_ID          = "command-group:datatable"
PACKAGE_DESCRIPTION = "테이블 변수의 값에 대해 다양한 작업을 수행합니다. 주요 액션: 지정(값을 테이블 변수에 할당합니다.)、열 유형 변경(열의 데이터 유형을 변경합니다.)、내용 지우기(지정된 테이블 변수의 내용을 지웁니다.)、열 개수 가져오기(테이블에서 열 수를 검색합니다.)、열 삭제(특정 열을 삭제합니다.) 외 13개."

ACTIONS = [
    {"action": "지정", "data_item_name": "datatable#assign", "description": "값을 테이블 변수에 할당합니다."},
    {"action": "열 유형 변경", "data_item_name": "datatable#changecolumntype", "description": "열의 데이터 유형을 변경합니다."},
    {"action": "내용 지우기", "data_item_name": "datatable#clearcontent", "description": "지정된 테이블 변수의 내용을 지웁니다."},
    {"action": "열 개수 가져오기", "data_item_name": "datatable#getnumberofcolumns", "description": "테이블에서 열 수를 검색합니다."},
    {"action": "열 삭제", "data_item_name": "datatable#deletecolumn", "description": "특정 열을 삭제합니다."},
    {"action": "행 삭제", "data_item_name": "datatable#deleterow", "description": "특정 행을 삭제합니다."},
    {"action": "Get column name", "data_item_name": "datatable#getcolumnname", "description": "Gets the name of a column in a data table by its index."},
    {"action": "열 삽입", "data_item_name": "datatable#insertcolumn", "description": "한 테이블의 열을 다른 테이블에 삽입합니다."},
    {"action": "행 삽입", "data_item_name": "datatable#insertrow", "description": "테이블에 행을 삽입합니다."},
    {"action": "조인", "data_item_name": "datatable#join", "description": "두 테이블 변수의 내용을 결합합니다."},
    {"action": "병합", "data_item_name": "datatable#merge", "description": "두 테이블이 동일한 열 머리글을 포함하는 경우 두 테이블의 내용을 결합합니다."},
    {"action": "중복 행 제거", "data_item_name": "datatable#removeduplicaterows", "description": "테이블에서 중복된 행을 삭제합니다."},
    {"action": "행 개수 가져오기", "data_item_name": "datatable#getnumberofrows", "description": "테이블의 행 수를 검색합니다."},
    {"action": "값 검색", "data_item_name": "datatable#searchforavalue", "description": "테이블에서 특정 값을 검색하여 해당 값이 존재하는 행과 열 번호을 반환합니다."},
    {"action": "단일 셀의 값 설정", "data_item_name": "datatable#setcellvalue", "description": "사용자 지정 행과 열에 따라 테이블 셀에 특정 값을 할당합니다."},
    {"action": "분류", "data_item_name": "datatable#sort", "description": "오름차순 또는 내림차순으로 열을 기준으로 테이블 데이터를 정렬합니다."},
    {"action": "파일에 쓰기", "data_item_name": "datatable#writetofile", "description": "테이블 유형 변수의 데이터를 CSV 또는 TXT 파일에 씁니다."},
    {"action": "파일 스트림에 쓰기", "data_item_name": "datatable#writetofilestream", "description": "테이블 유형 변수의 데이터를 파일 스트림에 씁니다."},
]