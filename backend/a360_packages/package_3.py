# -*- coding: utf-8 -*-
PACKAGE_NAME        = "부서"
PACKAGE_ID          = "부서"
PACKAGE_DESCRIPTION = "주요 액션: 부서에 역할 추가(부서에서 역할 부여 하기)、부서에 역할 일괄 추가(부서에서 사용자 역할 일괄 추가)、부서에서 역할 일괄 제거(부서에서 사용자 역할 일괄 추가)、부서에서 역할 일괄 바꾸기(부서에서 사용자 역할 일괄 바꾸기)、홈 부서 가져오기(조직의 홈 부서를 검색합니다. 개체 수는 포함되지 않습니다.) 외 2개."

ACTIONS = [
    {"action": "부서에 역할 추가", "data_item_name": "genesys#division_adduserroleindivision", "description": "부서에서 역할 부여 하기"},
    {"action": "부서에 역할 일괄 추가", "data_item_name": "genesys#division_bulkadduserroleindivision", "description": "부서에서 사용자 역할 일괄 추가"},
    {"action": "부서에서 역할 일괄 제거", "data_item_name": "genesys#division_bulkremoveuserroleindivision", "description": "부서에서 사용자 역할 일괄 추가"},
    {"action": "부서에서 역할 일괄 바꾸기", "data_item_name": "genesys#division_bulkreplaceuserroleindivision", "description": "부서에서 사용자 역할 일괄 바꾸기"},
    {"action": "홈 부서 가져오기", "data_item_name": "genesys#division_getdivisionhome", "description": "조직의 홈 부서를 검색합니다. 개체 수는 포함되지 않습니다."},
    {"action": "부서 목록/검색", "data_item_name": "genesys#division_listdivisions", "description": "조직에 대해 정의된 모든 부서 목록 검색"},
    {"action": "부서에서 역할 제거", "data_item_name": "genesys#division_removeuserroleindivision", "description": "부서에서 역할 부여 삭제"},
]