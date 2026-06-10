# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Google Calendar"
PACKAGE_ID          = "command-group:google calendar"
PACKAGE_DESCRIPTION = "Google Calendar의 캘린더 이벤트를 기반으로 워크플로를 자동화하는 작업 및 트리거. 주요 액션: 연결(Google 서버와의 연결을 설정합니다.)、이벤트 생성(새 이벤트 생성)、이벤트 삭제(기존 이벤트 삭제)、연결 끊기(사용자 연결을 끊고 세션을 지웁니다) (총 4개)."

ACTIONS = [
    {"action": "연결", "data_item_name": "google calendar#connect", "description": "Google 서버와의 연결을 설정합니다."},
    {"action": "이벤트 생성", "data_item_name": "google calendar#create", "description": "새 이벤트 생성"},
    {"action": "이벤트 삭제", "data_item_name": "google calendar#delete", "description": "기존 이벤트 삭제"},
    {"action": "연결 끊기", "data_item_name": "google calendar#disconnect", "description": "사용자 연결을 끊고 세션을 지웁니다"},
]