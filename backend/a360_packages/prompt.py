# -*- coding: utf-8 -*-
PACKAGE_NAME        = "프롬프트"
PACKAGE_ID          = "command-group:prompt"
PACKAGE_DESCRIPTION = "값 입력, 예 또는 아니오 응답 요청, 파일 또는 폴더 선택과 같은 프롬프트 작업을 수행합니다. 주요 액션: 파일용(Bot 실행 시 하나 이상의 파일을 선택하라는 메시지가 표시됩니다.)、폴더용(폴더를 선택하라는 메시지가 표시됩니다.)、값용(값을 입력하라는 메시지가 표시됩니다.)、예/아니요용(예 또는 아니오 응답을 선택하라는 메시지가 표시됩니다.) (총 4개)."

ACTIONS = [
    {"action": "파일용", "data_item_name": "prompt#forfile", "description": "Bot 실행 시 하나 이상의 파일을 선택하라는 메시지가 표시됩니다."},
    {"action": "폴더용", "data_item_name": "prompt#forfolder", "description": "폴더를 선택하라는 메시지가 표시됩니다."},
    {"action": "값용", "data_item_name": "prompt#forvalue", "description": "값을 입력하라는 메시지가 표시됩니다."},
    {"action": "예/아니요용", "data_item_name": "prompt#foryesno", "description": "예 또는 아니오 응답을 선택하라는 메시지가 표시됩니다."},
]