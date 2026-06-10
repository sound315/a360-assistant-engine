# -*- coding: utf-8 -*-
PACKAGE_NAME        = "대기"
PACKAGE_ID          = "command-group:wait"
PACKAGE_DESCRIPTION = "애플리케이션 화면이 변경될 때까지 대기하거나 다음 작업을 진행하기 전에 별도의 창을 열거나 닫는 조건을 추가합니다. 주요 액션: 조건 대기(다음 작업을 실행하기 전 특정 조건이 참이 될 때까지 Bot이 대기하게...)、화면 바뀜 대기(다음 작업을 실행하기 전 특정 창 또는 화면에서 콘텐츠가 변경될 때까지...)、창 대기(다음 작업을 실행하기 전 특정 창이 닫히거나 열릴 때까지 Bot이 대기하...) (총 3개)."

ACTIONS = [
    {"action": "조건 대기", "data_item_name": "wait#waitforcondition", "description": "다음 작업을 실행하기 전 특정 조건이 참이 될 때까지 Bot이 대기하게 합니다."},
    {"action": "화면 바뀜 대기", "data_item_name": "wait#waitforscreenchange_v1", "description": "다음 작업을 실행하기 전 특정 창 또는 화면에서 콘텐츠가 변경될 때까지 Bot이 대기하게 합니다."},
    {"action": "창 대기", "data_item_name": "wait#waitforwindow", "description": "다음 작업을 실행하기 전 특정 창이 닫히거나 열릴 때까지 Bot이 대기하게 합니다."},
]