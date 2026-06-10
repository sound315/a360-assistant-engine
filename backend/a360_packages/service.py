# -*- coding: utf-8 -*-
PACKAGE_NAME        = "서비스"
PACKAGE_ID          = "command-group:service"
PACKAGE_DESCRIPTION = "서비스 상태의 시작, 중지, 일시 중지, 다시 시작 또는 검색을 포함하여 Windows 및 애플리케이션 서비스의 작업을 자동화합니다. 주요 액션: 서비스 일시 중지됨(현재 실행 중인 선택한 Windows 또는 애플리케이션 서비스를 일시 중...)、서비스 다시 시작(이전에 일시 중지된 선택한 Windows 또는 애플리케이션 서비스를 다시...)、서비스 시작(실행되고 있지 않은 선택한 Windows 또는 애플리케이션 서비스를 시작...)、서비스 상태 받기(선택한 Windows 또는 애플리케이션 서비스의 현재 상태를 검색합니다.)、서비스 중지(현재 실행 중인 선택한 Windows 또는 애플리케이션 서비스를 중지합니...) (총 5개)."

ACTIONS = [
    {"action": "서비스 일시 중지됨", "data_item_name": "service#pauseservice", "description": "현재 실행 중인 선택한 Windows 또는 애플리케이션 서비스를 일시 중지합니다."},
    {"action": "서비스 다시 시작", "data_item_name": "service#resumeservice", "description": "이전에 일시 중지된 선택한 Windows 또는 애플리케이션 서비스를 다시 시작합니다."},
    {"action": "서비스 시작", "data_item_name": "service#startservice", "description": "실행되고 있지 않은 선택한 Windows 또는 애플리케이션 서비스를 시작합니다."},
    {"action": "서비스 상태 받기", "data_item_name": "service#getservicestatus", "description": "선택한 Windows 또는 애플리케이션 서비스의 현재 상태를 검색합니다."},
    {"action": "서비스 중지", "data_item_name": "service#stopservice", "description": "현재 실행 중인 선택한 Windows 또는 애플리케이션 서비스를 중지합니다."},
]