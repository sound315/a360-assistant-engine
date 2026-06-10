# -*- coding: utf-8 -*-
PACKAGE_NAME        = "외부 조직"
PACKAGE_ID          = "외부 조직"
PACKAGE_DESCRIPTION = "주요 액션: 조직 만들기(외부 조직 만들기)、조직 삭제(외부 조직 삭제)、조직 가져오기(외부 조직에 대한 세부 정보 가져오기)、조직 목록/검색(쿼리가 있는 외부 조직 목록/검색)、조직 업데이트(새 정보로 외부 조직을 업데이트합니다. 업데이트가 필요 없는 경우 필드를...) (총 5개)."

ACTIONS = [
    {"action": "조직 만들기", "data_item_name": "genesys#organization_create", "description": "외부 조직 만들기"},
    {"action": "조직 삭제", "data_item_name": "genesys#organization_delete", "description": "외부 조직 삭제"},
    {"action": "조직 가져오기", "data_item_name": "genesys#organization_get", "description": "외부 조직에 대한 세부 정보 가져오기"},
    {"action": "조직 목록/검색", "data_item_name": "genesys#organization_search", "description": "쿼리가 있는 외부 조직 목록/검색"},
    {"action": "조직 업데이트", "data_item_name": "genesys#organization_update", "description": "새 정보로 외부 조직을 업데이트합니다. 업데이트가 필요 없는 경우 필드를 비워 두십시오."},
]