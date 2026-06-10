# -*- coding: utf-8 -*-
PACKAGE_NAME        = "프린터"
PACKAGE_ID          = "command-group:printer"
PACKAGE_DESCRIPTION = "기본 프린터 검색 및 설정과 사용 가능한 프린터 목록에서 프린터 제거를 자동화합니다. 주요 액션: 기본값 가져오기(기본 프린터를 검색하고 문자열 변수에 값을 할당합니다.)、제거(프린터를 제거합니다.)、기본값 설정(프린터를 기본값으로 설정합니다.) (총 3개)."

ACTIONS = [
    {"action": "기본값 가져오기", "data_item_name": "printer#getdefaultprinter", "description": "기본 프린터를 검색하고 문자열 변수에 값을 할당합니다."},
    {"action": "제거", "data_item_name": "printer#removeprinter", "description": "프린터를 제거합니다."},
    {"action": "기본값 설정", "data_item_name": "printer#setdefaultprinter", "description": "프린터를 기본값으로 설정합니다."},
]