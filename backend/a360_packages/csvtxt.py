# -*- coding: utf-8 -*-
PACKAGE_NAME        = "CSV/TXT"
PACKAGE_ID          = "command-group:csvtxt"
PACKAGE_DESCRIPTION = "CSV 또는 텍스트 파일을 열고 파일에서 데이터를 읽고 테이블 변수에 데이터를 할당합니다. 주요 액션: 닫기(CSV 또는 텍스트 파일을 닫습니다.)、열기(파일에 사용되는 구분 기호, 공백 제거 여부 및 파일에 적용되는 인코딩을...)、읽기(CSV 또는 TXT 파일에서 값을 검색하고 데이터 값이 있는 작업을 위해...) (총 3개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "csvtxt#closecsvtxt", "description": "CSV 또는 텍스트 파일을 닫습니다."},
    {"action": "열기", "data_item_name": "csvtxt#opencsvtxt", "description": "파일에 사용되는 구분 기호, 공백 제거 여부 및 파일에 적용되는 인코딩을 지정합니다."},
    {"action": "읽기", "data_item_name": "csvtxt#readfromcsvtxt", "description": "CSV 또는 TXT 파일에서 값을 검색하고 데이터 값이 있는 작업을 위해 테이블 변수에 삽입합니다."},
]