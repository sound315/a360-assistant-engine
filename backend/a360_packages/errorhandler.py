# -*- coding: utf-8 -*-
PACKAGE_NAME        = "오류 처리기"
PACKAGE_ID          = "command-group:errorhandler"
PACKAGE_DESCRIPTION = "Bot에서 오류를 처리하는 명령을 제공합니다. 주요 액션: Try(예외로 실패할 수 있는 일련의 명령을 시도합니다.)、Catch(Try의 명령이 예외로 실패할 경우 일련의 명령을 실행합니다.)、Finally(Try 또는 Catch가 완료된 후 일련의 명령을 실행합니다.)、Throw(오류를 나타내기 위해 예외를 표시합니다.) (총 4개)."

ACTIONS = [
    {"action": "Try", "data_item_name": "errorhandler#try", "description": "예외로 실패할 수 있는 일련의 명령을 시도합니다."},
    {"action": "Catch", "data_item_name": "errorhandler#catch", "description": "Try의 명령이 예외로 실패할 경우 일련의 명령을 실행합니다."},
    {"action": "Finally", "data_item_name": "errorhandler#finally", "description": "Try 또는 Catch가 완료된 후 일련의 명령을 실행합니다."},
    {"action": "Throw", "data_item_name": "errorhandler#throw", "description": "오류를 나타내기 위해 예외를 표시합니다."},
]