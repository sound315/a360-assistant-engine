# -*- coding: utf-8 -*-
PACKAGE_NAME        = "전화"
PACKAGE_ID          = "전화"
PACKAGE_DESCRIPTION = "주요 액션: 전화 할당(사용자에게 전화 라인 할당)、전화 만들기(전화 만들기)、전화 기본 설정 목록(전화 기본 설정 목록)、전화 목록/검색(전화 목록/검색)、사이트 목록/검색(사이트 목록/검색) 외 1개."

ACTIONS = [
    {"action": "전화 할당", "data_item_name": "genesys#edgephone_assignphone", "description": "사용자에게 전화 라인 할당"},
    {"action": "전화 만들기", "data_item_name": "genesys#edgephone_createphone", "description": "전화 만들기"},
    {"action": "전화 기본 설정 목록", "data_item_name": "genesys#edgephonebasesetting_listphonebasesettings", "description": "전화 기본 설정 목록"},
    {"action": "전화 목록/검색", "data_item_name": "genesys#edgephone_listphones", "description": "전화 목록/검색"},
    {"action": "사이트 목록/검색", "data_item_name": "genesys#edgesite_listsites", "description": "사이트 목록/검색"},
    {"action": "전화 제거", "data_item_name": "genesys#edgephone_removephone", "description": "Genesys: 전화 제거전화 제거필요한 Bot Agent 버전: 21.210 이상"},
]