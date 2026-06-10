# -*- coding: utf-8 -*-
PACKAGE_NAME        = "창"
PACKAGE_ID          = "command-group:window"
PACKAGE_DESCRIPTION = "창과 관련된 작업을 자동화합니다. 주요 액션: 활성화...(창을 활성화합니다)、활성 창 제목 변경 가져오기(활성 창의 제목 검색)、지정(지정된 창에 소스 창 변수의 값을 할당합니다.)、닫기(애플리케이션 창을 닫습니다.)、모두 닫기(모든 창을 닫습니다.) 외 5개."

ACTIONS = [
    {"action": "활성화...", "data_item_name": "window#activatewindow", "description": "창을 활성화합니다"},
    {"action": "활성 창 제목 변경 가져오기", "data_item_name": "window#activewindowtitle", "description": "활성 창의 제목 검색"},
    {"action": "지정", "data_item_name": "window#assign", "description": "지정된 창에 소스 창 변수의 값을 할당합니다."},
    {"action": "닫기", "data_item_name": "window#closewindow", "description": "애플리케이션 창을 닫습니다."},
    {"action": "모두 닫기", "data_item_name": "window#closeallwindows", "description": "모든 창을 닫습니다."},
    {"action": "최대화", "data_item_name": "window#maximizewindow", "description": "창: 최대화창 최대화필요한 Bot Agent 버전: 20.11 이상"},
    {"action": "최소화", "data_item_name": "window#minimizewindow", "description": "창: 최소화창 최소화필요한 Bot Agent 버전: 20.11 이상"},
    {"action": "크기 조정", "data_item_name": "window#resizewindow", "description": "창 크기 조정"},
    {"action": "복원", "data_item_name": "window#restorewindow", "description": "창: 복원창 복원필요한 Bot Agent 버전: 20.11 이상"},
    {"action": "제목 설정", "data_item_name": "window#settitle", "description": "창 변수에 새 창 제목을 지정합니다."},
]