# -*- coding: utf-8 -*-
PACKAGE_NAME        = "역할"
PACKAGE_ID          = "역할"
PACKAGE_DESCRIPTION = "주요 액션: 역할에 사용자 추가(역할에 사용자 목록 추가)、역할 목록/검색(조직에 대해 정의된 모든 역할의 목록 검색)、사용자의 역할 목록(사용자의 역할과 권한 목록을 반환합니다.)、역할의 사용자 목록(지정된 역할의 사용자 목록을 가져옵니다. 지정된 역할에 있는 사용자의 u...)、역할에서 사용자 제거(역할에서 사용자 목록 제거) 외 1개."

ACTIONS = [
    {"action": "역할에 사용자 추가", "data_item_name": "genesys#role_adduserstorole", "description": "역할에 사용자 목록 추가"},
    {"action": "역할 목록/검색", "data_item_name": "genesys#role_listroles", "description": "조직에 대해 정의된 모든 역할의 목록 검색"},
    {"action": "사용자의 역할 목록", "data_item_name": "genesys#role_listuserroles", "description": "사용자의 역할과 권한 목록을 반환합니다."},
    {"action": "역할의 사용자 목록", "data_item_name": "genesys#role_listusersinrole", "description": "지정된 역할의 사용자 목록을 가져옵니다. 지정된 역할에 있는 사용자의 uuid 배열을 가져옵니다."},
    {"action": "역할에서 사용자 제거", "data_item_name": "genesys#role_removeuserstorole", "description": "역할에서 사용자 목록 제거"},
    {"action": "사용자의 역할 설정", "data_item_name": "genesys#role_setuserroles", "description": "사용자의 역할 설정"},
]