# -*- coding: utf-8 -*-
PACKAGE_NAME        = "기록"
PACKAGE_ID          = "기록"
PACKAGE_DESCRIPTION = "주요 액션: 기록 생성(지정된 테이블에 하나의 기록 삽입)、기록 삭제(지정된 테이블에서 기록 삭제)、기록 가져오기(지정된 테이블에서 지정된 sys_id로 식별된 기록 검색하기)、여러 기록 가져오기(지정된 테이블에서 여러 기록 검색하기)、기록 업데이트(요청 본문에 포함된 이름-값 쌍으로 지정된 기록 업데이트) (총 5개)."

ACTIONS = [
    {"action": "기록 생성", "data_item_name": "servicenow#create_record", "description": "지정된 테이블에 하나의 기록 삽입"},
    {"action": "기록 삭제", "data_item_name": "servicenow#delete_record", "description": "지정된 테이블에서 기록 삭제"},
    {"action": "기록 가져오기", "data_item_name": "servicenow#get_record", "description": "지정된 테이블에서 지정된 sys_id로 식별된 기록 검색하기"},
    {"action": "여러 기록 가져오기", "data_item_name": "servicenow#list_record", "description": "지정된 테이블에서 여러 기록 검색하기"},
    {"action": "기록 업데이트", "data_item_name": "servicenow#update_record", "description": "요청 본문에 포함된 이름-값 쌍으로 지정된 기록 업데이트"},
]