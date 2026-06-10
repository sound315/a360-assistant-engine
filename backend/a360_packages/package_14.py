# -*- coding: utf-8 -*-
PACKAGE_NAME        = "인증"
PACKAGE_ID          = "인증"
PACKAGE_DESCRIPTION = "주요 액션: 인증(ServiceNow API를 통해 인증하여 액세스 토큰 생성)、인증 취소(세션에서 인증 컨텍스트 취소) (총 2개)."

ACTIONS = [
    {"action": "인증", "data_item_name": "servicenow#authentication", "description": "ServiceNow API를 통해 인증하여 액세스 토큰 생성"},
    {"action": "인증 취소", "data_item_name": "servicenow#revoke_authentication", "description": "세션에서 인증 컨텍스트 취소"},
]