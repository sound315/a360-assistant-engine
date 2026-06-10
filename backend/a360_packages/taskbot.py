# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Task Bot"
PACKAGE_ID          = "command-group:taskbot"
PACKAGE_DESCRIPTION = "TaskBot을 실행합니다. 주요 액션: 일시 중지(현재 처리 중인 태스크를 일시 중지합니다.)、실행(선택한 TaskBot을 실행합니다.)、중지(현재 처리 중인 태스크를 중지합니다.) (총 3개)."

ACTIONS = [
    {"action": "일시 중지", "data_item_name": "taskbot#pausetask", "description": "현재 처리 중인 태스크를 일시 중지합니다."},
    {"action": "실행", "data_item_name": "taskbot#runtask", "description": "선택한 TaskBot을 실행합니다."},
    {"action": "중지", "data_item_name": "taskbot#stoptask", "description": "현재 처리 중인 태스크를 중지합니다."},
]