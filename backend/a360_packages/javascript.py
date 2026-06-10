# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Javascript"
PACKAGE_ID          = "command-group:javascript"
PACKAGE_DESCRIPTION = "Bot에서 JavaScript를 열고 실행합니다. 주요 액션: 닫기(JavaScript를 닫습니다.)、JavaScript 실행(JavaScript 파일 내에서 함수를 실행합니다.)、열기(JavaScript를 엽니다) (총 3개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "javascript#javascript.commands.closescript", "description": "JavaScript를 닫습니다."},
    {"action": "JavaScript 실행", "data_item_name": "javascript#javascript.commands.executefunction", "description": "JavaScript 파일 내에서 함수를 실행합니다."},
    {"action": "열기", "data_item_name": "javascript#javascript.commands.openscript", "description": "JavaScript를 엽니다"},
]