# -*- coding: utf-8 -*-
PACKAGE_NAME        = "분석"
PACKAGE_ID          = "command-group:analyze"
PACKAGE_DESCRIPTION = "본 패키지는 분석용으로 사용할 수 있습니다. 주요 액션: 닫기(트랜잭션 닫기)、열기(트랜잭션 열기) (총 2개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "analyze#closetransaction", "description": "트랜잭션 닫기"},
    {"action": "열기", "data_item_name": "analyze#opentransaction", "description": "트랜잭션 열기"},
]