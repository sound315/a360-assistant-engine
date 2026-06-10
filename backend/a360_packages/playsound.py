# -*- coding: utf-8 -*-
PACKAGE_NAME        = "사운드 재생"
PACKAGE_ID          = "command-group:playsound"
PACKAGE_DESCRIPTION = "사운드 파일을 재생하는 명령을 제공합니다. 주요 액션: 경보음 재생(경보음 사운드를 재생합니다.)、미디어 파일 재생(미디어 파일을 재생합니다.) (총 2개)."

ACTIONS = [
    {"action": "경보음 재생", "data_item_name": "playsound#playbeep", "description": "경보음 사운드를 재생합니다."},
    {"action": "미디어 파일 재생", "data_item_name": "playsound#playmediafile", "description": "미디어 파일을 재생합니다."},
]