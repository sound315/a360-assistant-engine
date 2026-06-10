# -*- coding: utf-8 -*-
PACKAGE_NAME        = "기술"
PACKAGE_ID          = "기술"
PACKAGE_DESCRIPTION = "주요 액션: 사용자 라우팅 기술 추가(사용자 라우팅 기술 추가)、라우팅 기술 일괄 추가(사용자에게 라우팅 기술 일괄 추가)、라우팅 기술 일괄 바꾸기(사용자에게 라우팅 기술을 대량으로 대체)、라우팅 기술 목록/검색(라우팅 기술 목록 가져오기)、사용자의 라우팅 기술 목록(사용자의 라우팅 기술 목록 가져오기) 외 1개."

ACTIONS = [
    {"action": "사용자 라우팅 기술 추가", "data_item_name": "genesys#skill_adduserroutingskill", "description": "사용자 라우팅 기술 추가"},
    {"action": "라우팅 기술 일괄 추가", "data_item_name": "genesys#skill_bulkaddroutingskill", "description": "사용자에게 라우팅 기술 일괄 추가"},
    {"action": "라우팅 기술 일괄 바꾸기", "data_item_name": "genesys#skill_bulkreplaceroutingskill", "description": "사용자에게 라우팅 기술을 대량으로 대체"},
    {"action": "라우팅 기술 목록/검색", "data_item_name": "genesys#skill_listroutingskills", "description": "라우팅 기술 목록 가져오기"},
    {"action": "사용자의 라우팅 기술 목록", "data_item_name": "genesys#skill_listuserroutingskills", "description": "사용자의 라우팅 기술 목록 가져오기"},
    {"action": "사용자 라우팅 기술 제거", "data_item_name": "genesys#skill_removeuserroutingskill", "description": "사용자 라우팅 기술 제거"},
]