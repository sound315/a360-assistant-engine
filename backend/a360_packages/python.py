# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Python 스크립트"
PACKAGE_ID          = "command-group:python"
PACKAGE_DESCRIPTION = "태스크에서 Python 스크립트 함수를 활성화합니다. 주요 액션: 닫기(Python 세션을 닫습니다.)、함수 실행(Python 스크립트 패키지 내에서 함수를 실행합니다.)、스크립트 실행(Python 스크립트 패키지 내에서 스크립트를 실행합니다.)、열기(Python 세션을 엽니다.) (총 4개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "python#python.commands.closescript", "description": "Python 세션을 닫습니다."},
    {"action": "함수 실행", "data_item_name": "python#python.commands.executefunction", "description": "Python 스크립트 패키지 내에서 함수를 실행합니다."},
    {"action": "스크립트 실행", "data_item_name": "python#python.commands.executescript", "description": "Python 스크립트 패키지 내에서 스크립트를 실행합니다."},
    {"action": "열기", "data_item_name": "python#python.commands.openscript", "description": "Python 세션을 엽니다."},
]