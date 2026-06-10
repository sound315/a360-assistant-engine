# -*- coding: utf-8 -*-
PACKAGE_NAME        = "시스템"
PACKAGE_ID          = "command-group:system"
PACKAGE_DESCRIPTION = "주요 액션: 컴퓨터 잠금(Bot이 실행되는 로컬 시스템을 잠급니다.)、로그오프(Bot이 실행되는 로컬 시스템의 현재 사용자 세션에서 로그오프합니다.)、재시작(Bot이 실행되는 로컬 시스템을 다시 시작합니다.)、종료(Bot이 실행되는 로컬 시스템을 끕니다.)、환경 변수 받기(지정된 로컬 시스템에서 모든 환경 변수를 검색하여 변수에 할당합니다.) (총 5개)."

ACTIONS = [
    {"action": "컴퓨터 잠금", "data_item_name": "system#lock", "description": "Bot이 실행되는 로컬 시스템을 잠급니다."},
    {"action": "로그오프", "data_item_name": "system#logoff", "description": "Bot이 실행되는 로컬 시스템의 현재 사용자 세션에서 로그오프합니다."},
    {"action": "재시작", "data_item_name": "system#restart", "description": "Bot이 실행되는 로컬 시스템을 다시 시작합니다."},
    {"action": "종료", "data_item_name": "system#shutdown", "description": "Bot이 실행되는 로컬 시스템을 끕니다."},
    {"action": "환경 변수 받기", "data_item_name": "system#systeminformation", "description": "지정된 로컬 시스템에서 모든 환경 변수를 검색하여 변수에 할당합니다."},
]