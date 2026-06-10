# -*- coding: utf-8 -*-
PACKAGE_NAME        = "트리거 루프"
PACKAGE_ID          = "command-group:triggerloop"
PACKAGE_DESCRIPTION = "중지될 때까지 트리거된 이벤트를 처리하는 루프를 실행합니다. 주요 액션: 트리거 루프(트리거가 발생할 때까지 루프를 돈 다음 일부 작업을 실행합니다.)、핸들(트리거 발생 시 몇 가지 작업을 실행합니다.)、중단(현재 트리거 루프를 종료하고 루프 이후의 다음 작업으로 이동합니다.) (총 3개)."

ACTIONS = [
    {"action": "트리거 루프", "data_item_name": "triggerloop#triggerloop.commands.loop", "description": "트리거가 발생할 때까지 루프를 돈 다음 일부 작업을 실행합니다."},
    {"action": "핸들", "data_item_name": "triggerloop#triggerloop.commands.handle", "description": "트리거 발생 시 몇 가지 작업을 실행합니다."},
    {"action": "중단", "data_item_name": "triggerloop#triggerloop.commands.break", "description": "현재 트리거 루프를 종료하고 루프 이후의 다음 작업으로 이동합니다."},
]