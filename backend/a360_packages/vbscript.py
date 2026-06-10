# -*- coding: utf-8 -*-
PACKAGE_NAME        = "VBScript"
PACKAGE_ID          = "command-group:vbscript"
PACKAGE_DESCRIPTION = "태스크에서 VBScript 함수를 활성화합니다. 주요 액션: 닫기(VBScript에서 세션을 닫습니다.)、함수 실행(VBScript 내에서 함수를 실행합니다.)、열기(VBScript 파일을 엽니다.) (총 3개)."

ACTIONS = [
    {"action": "닫기", "data_item_name": "vbscript#vbscript.commands.closescript", "description": "VBScript에서 세션을 닫습니다."},
    {"action": "함수 실행", "data_item_name": "vbscript#vbscript.commands.executefunction", "description": "VBScript 내에서 함수를 실행합니다."},
    {"action": "열기", "data_item_name": "vbscript#vbscript.commands.openscript", "description": "VBScript 파일을 엽니다."},
]