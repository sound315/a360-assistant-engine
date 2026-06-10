# -*- coding: utf-8 -*-
PACKAGE_NAME        = "If"
PACKAGE_ID          = "command-group:if"
PACKAGE_DESCRIPTION = "If 및 else 작업입니다. 주요 액션: If(조건을 지정하고 조건이 참인 경우 실행할 작업 시퀀스를 보유합니다.)、Else If(If 작업에 지정된 조건이 거짓인지 테스트할 대체 조건을 지정합니다.)、Else(If 조치 및 Else if 작업(사용된 경우)에 지정된 조건이 거짓인...) (총 3개)."

ACTIONS = [
    {"action": "If", "data_item_name": "if#if", "description": "조건을 지정하고 조건이 참인 경우 실행할 작업 시퀀스를 보유합니다."},
    {"action": "Else If", "data_item_name": "if#elseif", "description": "If 작업에 지정된 조건이 거짓인지 테스트할 대체 조건을 지정합니다."},
    {"action": "Else", "data_item_name": "if#else", "description": "If 조치 및 Else if 작업(사용된 경우)에 지정된 조건이 거짓인 경우 작업의 대체 순서를 지정합니다."},
]