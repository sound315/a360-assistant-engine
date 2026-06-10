# -*- coding: utf-8 -*-
PACKAGE_NAME        = "사용자"
PACKAGE_ID          = "사용자"
PACKAGE_DESCRIPTION = "주요 액션: 사용자 생성(새 사용자 만들기)、사용자 삭제(기존 사용자 삭제)、사용자 가져오기(기존 사용자에 대한 세부 정보 가져오기)、사용자 목록/검색(사용자 목록/검색)、사용자 업데이트(기존 사용자를 업데이트합니다. 업데이트가 필요 없는 경우 필드를 비워 두...) (총 5개)."

ACTIONS = [
    {"action": "사용자 생성", "data_item_name": "genesys#user_create", "description": "새 사용자 만들기"},
    {"action": "사용자 삭제", "data_item_name": "genesys#user_delete", "description": "기존 사용자 삭제"},
    {"action": "사용자 가져오기", "data_item_name": "genesys#user_getdetail", "description": "기존 사용자에 대한 세부 정보 가져오기"},
    {"action": "사용자 목록/검색", "data_item_name": "genesys#list_users", "description": "사용자 목록/검색"},
    {"action": "사용자 업데이트", "data_item_name": "genesys#user_update", "description": "기존 사용자를 업데이트합니다. 업데이트가 필요 없는 경우 필드를 비워 두십시오."},
]