# -*- coding: utf-8 -*-
PACKAGE_NAME        = "프로세스 검색"
PACKAGE_ID          = "command-group:processdiscovery"
PACKAGE_DESCRIPTION = "이 패키지는 객체 작업을 수행하는 데 사용할 수 있습니다. 주요 액션: Process Recorder Start Command(Starts Process Recorder)、프로세스 캡처(이 명령은 객체의 클릭 이벤트를 시뮬레이션하는 데 사용할 수 있습니다.) (총 2개)."

ACTIONS = [
    {"action": "Process Recorder Start Command", "data_item_name": "processdiscovery#processrecorderstartcommand", "description": "Starts Process Recorder"},
    {"action": "프로세스 캡처", "data_item_name": "processdiscovery#capture", "description": "이 명령은 객체의 클릭 이벤트를 시뮬레이션하는 데 사용할 수 있습니다."},
]