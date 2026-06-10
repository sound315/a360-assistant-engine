# -*- coding: utf-8 -*-
PACKAGE_NAME        = "루프"
PACKAGE_ID          = "command-group:loop"
PACKAGE_DESCRIPTION = "일련의 작업을 반복합니다. 주요 액션: 루프(특정 횟수만큼 또는 조건이 충족될 때까지 일련의 작업을 실행합니다.)、계속(현재 반복을 종료하고 루프의 다음 반복을 계속 진행합니다.)、중단(현재 또는 지정된 루프를 종료하고 루프 이후 다음 작업으로 이동합니다.) (총 3개)."

ACTIONS = [
    {"action": "루프", "data_item_name": "loop#loop.commands.start", "description": "특정 횟수만큼 또는 조건이 충족될 때까지 일련의 작업을 실행합니다."},
    {"action": "계속", "data_item_name": "loop#loop.commands.continue", "description": "현재 반복을 종료하고 루프의 다음 반복을 계속 진행합니다."},
    {"action": "중단", "data_item_name": "loop#loop.commands.break", "description": "현재 또는 지정된 루프를 종료하고 루프 이후 다음 작업으로 이동합니다."},
]