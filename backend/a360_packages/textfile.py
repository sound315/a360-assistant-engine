# -*- coding: utf-8 -*-
PACKAGE_NAME        = "텍스트 파일"
PACKAGE_ID          = "command-group:textfile"
PACKAGE_DESCRIPTION = "텍스트 파일을 열고 파일에서 데이터를 읽고 문자열 변수에 저장합니다. 주요 액션: 텍스트 가져오기(텍스트 파일에서 내용을 추출하고 문자열 변수에 내용을 저장합니다.)、변수 읽기(텍스트 파일에서 변수 값을 읽습니다.) (총 2개)."

ACTIONS = [
    {"action": "텍스트 가져오기", "data_item_name": "textfile#readfile", "description": "텍스트 파일에서 내용을 추출하고 문자열 변수에 내용을 저장합니다."},
    {"action": "변수 읽기", "data_item_name": "textfile#readvariables", "description": "텍스트 파일에서 변수 값을 읽습니다."},
]