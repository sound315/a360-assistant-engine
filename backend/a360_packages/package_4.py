# -*- coding: utf-8 -*-
PACKAGE_NAME        = "외부 연락처"
PACKAGE_ID          = "외부 연락처"
PACKAGE_DESCRIPTION = "주요 액션: 연락처 만들기(외부 연락처 만들기)、연락처 삭제(외부 연락처 삭제)、연락처 목록/검색(연락처 ID 또는 검색 쿼리로 외부 연락처 목록을 가져옵니다. ID 또는...)、연락처 업데이트(외부 연락처 업데이트) (총 4개)."

ACTIONS = [
    {"action": "연락처 만들기", "data_item_name": "genesys#externalcontact_create", "description": "외부 연락처 만들기"},
    {"action": "연락처 삭제", "data_item_name": "genesys#externalcontact_deletecontact", "description": "외부 연락처 삭제"},
    {"action": "연락처 목록/검색", "data_item_name": "genesys#externalcontact_listcontacts", "description": "연락처 ID 또는 검색 쿼리로 외부 연락처 목록을 가져옵니다. ID 또는 검색 쿼리가 필요합니다."},
    {"action": "연락처 업데이트", "data_item_name": "genesys#externalcontact_update", "description": "외부 연락처 업데이트"},
]