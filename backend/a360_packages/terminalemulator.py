# -*- coding: utf-8 -*-
PACKAGE_NAME        = "터미널 에뮬레이터"
PACKAGE_ID          = "command-group:terminalemulator"
PACKAGE_DESCRIPTION = "다른 시스템에 연결하고 태스크를 자동화합니다. 예를 들어 다른 운영 체제에서 애플리케이션을 실행하고 파일에 액세스합니다. 주요 액션: 터미널 지우기(터미널 화면을 지웁니다.)、연결(작업을 자동화하려는 호스트 머신과의 연결을 설정합니다.)、연결 끊기(터미널과의 연결 작업을 사용하여 설정한 연결을 종료합니다.)、모든 필드 가져오기(터미널 콘솔에서 모든 필드 값을 검색하여 테이블 변수에 할당합니다.)、필드 가져오기(인덱스 또는 이름에 따라 필드 값을 검색하여 문자열 변수에 할당합니다.) 외 10개."

ACTIONS = [
    {"action": "터미널 지우기", "data_item_name": "terminalemulator#clearterminal", "description": "터미널 화면을 지웁니다."},
    {"action": "연결", "data_item_name": "terminalemulator#connectv2", "description": "작업을 자동화하려는 호스트 머신과의 연결을 설정합니다."},
    {"action": "연결 끊기", "data_item_name": "terminalemulator#disconnect", "description": "터미널과의 연결 작업을 사용하여 설정한 연결을 종료합니다."},
    {"action": "모든 필드 가져오기", "data_item_name": "terminalemulator#getallfields", "description": "터미널 콘솔에서 모든 필드 값을 검색하여 테이블 변수에 할당합니다."},
    {"action": "필드 가져오기", "data_item_name": "terminalemulator#getfield", "description": "인덱스 또는 이름에 따라 필드 값을 검색하여 문자열 변수에 할당합니다."},
    {"action": "텍스트 가져오기", "data_item_name": "terminalemulator#gettext", "description": "터미널에서 텍스트를 검색하여 변수에 저장합니다."},
    {"action": "터미널 숨기기", "data_item_name": "terminalemulator#hideterminal", "description": "연결 작업의 터미널 창 표시 옵션을 선택한 경우 터미널 창을 숨깁니다. Bot이 특정 작업을 수행하는 동안 터미널 화면을 표시하지 않으려면 이 작업을 사용합니다."},
    {"action": "검색 필드", "data_item_name": "terminalemulator#searchfield", "description": "포함하는 텍스트에 따라 필드를 검색합니다. 인덱스를 검색할지 필드 이름을 검색할지 지정할 수 있습니다."},
    {"action": "키 전송", "data_item_name": "terminalemulator#sendkey", "description": "터미널에 키를 전송합니다."},
    {"action": "텍스트 전송", "data_item_name": "terminalemulator#sendtext", "description": "터미널에 텍스트를 전송합니다."},
    {"action": "커서 위치 설정", "data_item_name": "terminalemulator#setcursorposition", "description": "지정된 행 번호와 열 번호에 따라 터미널의 화면에서 커서의 위치를 설정합니다."},
    {"action": "필드 설정", "data_item_name": "terminalemulator#setfield", "description": "터미널의 특정 필드에 값을 설정합니다."},
    {"action": "키 매핑 설정", "data_item_name": "terminalemulator#setkeymaps", "description": "키를 설정하고 사용자 지정 문자열 또는 매크로에 매핑하여 특정 터미널 세션에서 사용할 수 있습니다."},
    {"action": "터미널 보기", "data_item_name": "terminalemulator#showterminal", "description": "연결 작업의 터미널 창 표시 옵션이 선택 취소된 경우 터미널 창을 표시합니다. Bot이 특정 작업을 수행하는 동안 터미널 화면을 표시하려면 이 작업을 사용합니다."},
    {"action": "대기", "data_item_name": "terminalemulator#wait", "description": "터미널에서 특정 조건이 충족될 때까지 대기합니다."},
]