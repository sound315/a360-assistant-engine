# -*- coding: utf-8 -*-
PACKAGE_NAME        = "워크로드"
PACKAGE_ID          = "command-group:wlm"
PACKAGE_DESCRIPTION = "워크로드 작업을 수행하기 위한 명령을 제공합니다. 주요 액션: 작업 항목 삽입(대기열에 작업 항목 삽입)、작업 항목 업데이트(대기열의 작업 항목 업데이트) (총 2개)."

ACTIONS = [
    {"action": "작업 항목 삽입", "data_item_name": "wlm#insertworkitem", "description": "대기열에 작업 항목 삽입"},
    {"action": "작업 항목 업데이트", "data_item_name": "wlm#updateworkitem", "description": "대기열의 작업 항목 업데이트"},
]