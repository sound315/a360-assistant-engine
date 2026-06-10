# -*- coding: utf-8 -*-
PACKAGE_NAME        = "대기열"
PACKAGE_ID          = "대기열"
PACKAGE_DESCRIPTION = "주요 액션: 대기열에 추가(대기열에 사용자 추가)、구성원 목록(대기열의 모든 구성원 나열)、대기열 목록/검색(조직에 대해 정의된 모든 대기열 목록 검색)、대기열에서 제거(대기열에서 사용자 제거) (총 4개)."

ACTIONS = [
    {"action": "대기열에 추가", "data_item_name": "genesys#queue_add", "description": "대기열에 사용자 추가"},
    {"action": "구성원 목록", "data_item_name": "genesys#queue_list", "description": "대기열의 모든 구성원 나열"},
    {"action": "대기열 목록/검색", "data_item_name": "genesys#queue_listqueues", "description": "조직에 대해 정의된 모든 대기열 목록 검색"},
    {"action": "대기열에서 제거", "data_item_name": "genesys#queue_remove", "description": "대기열에서 사용자 제거"},
]