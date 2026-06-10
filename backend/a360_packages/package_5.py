# -*- coding: utf-8 -*-
PACKAGE_NAME        = "그룹"
PACKAGE_ID          = "그룹"
PACKAGE_DESCRIPTION = "주요 액션: 그룹에 구성원 일괄 추가(그룹에 구성원 일괄 추가)、구성원 삭제(그룹 구성원 삭제)、그룹 목록(모든 그룹 목록)、구성원 목록(그룹의 모든 구성원 목록) (총 4개)."

ACTIONS = [
    {"action": "그룹에 구성원 일괄 추가", "data_item_name": "genesys#group_addmembers", "description": "그룹에 구성원 일괄 추가"},
    {"action": "구성원 삭제", "data_item_name": "genesys#group_deletememebers", "description": "그룹 구성원 삭제"},
    {"action": "그룹 목록", "data_item_name": "genesys#group_list", "description": "모든 그룹 목록"},
    {"action": "구성원 목록", "data_item_name": "genesys#group_listmembers", "description": "그룹의 모든 구성원 목록"},
]