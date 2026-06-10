# -*- coding: utf-8 -*-
PACKAGE_NAME        = "로깅"
PACKAGE_ID          = "command-group:logtofile"
PACKAGE_DESCRIPTION = "데이터가 있는 로그 파일을 생성합니다. 주요 액션: 파일에 텍스트 기록(TaskBot이 실행될 때 발생하는 이벤트에 대한 데이터로 로그 파일을...)、서버에 로그온(자동화 로그 설정의 사양에 따라 SIEM/Syslog 또는 Control...)、파일에 변수 기록(사용자 정의 변수로 로그 파일 생성) (총 3개)."

ACTIONS = [
    {"action": "파일에 텍스트 기록", "data_item_name": "logtofile#logtofile", "description": "TaskBot이 실행될 때 발생하는 이벤트에 대한 데이터로 로그 파일을 생성합니다."},
    {"action": "서버에 로그온", "data_item_name": "logtofile#logtoserver", "description": "자동화 로그 설정의 사양에 따라 SIEM/Syslog 또는 Control Room에 데이터를 기록합니다."},
    {"action": "파일에 변수 기록", "data_item_name": "logtofile#logvariablestofile", "description": "사용자 정의 변수로 로그 파일 생성"},
]