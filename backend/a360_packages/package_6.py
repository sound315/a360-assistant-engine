# -*- coding: utf-8 -*-
PACKAGE_NAME        = "언어"
PACKAGE_ID          = "언어"
PACKAGE_DESCRIPTION = "주요 액션: 라우팅 언어 추가(사용자에게 라우팅 언어 추가)、사용자에게 라우팅 언어 일괄 추가(사용자에게 라우팅 언어 일괄 추가)、사용자의 라우팅 언어 목록(사용자의 라우팅 언어 목록)、모든 라우팅 언어 목록(지원되는 언어 목록 가져오기)、사용자의 라우팅 언어 제거(사용자의 라우팅 언어 제거) (총 5개)."

ACTIONS = [
    {"action": "라우팅 언어 추가", "data_item_name": "genesys#language_add", "description": "사용자에게 라우팅 언어 추가"},
    {"action": "사용자에게 라우팅 언어 일괄 추가", "data_item_name": "genesys#language_bulkaddroutinglanguage", "description": "사용자에게 라우팅 언어 일괄 추가"},
    {"action": "사용자의 라우팅 언어 목록", "data_item_name": "genesys#language_list", "description": "사용자의 라우팅 언어 목록"},
    {"action": "모든 라우팅 언어 목록", "data_item_name": "genesys#language_listsupportedroutinglanguages", "description": "지원되는 언어 목록 가져오기"},
    {"action": "사용자의 라우팅 언어 제거", "data_item_name": "genesys#language_removeuserroutinglanguage", "description": "사용자의 라우팅 언어 제거"},
]