# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Microsoft Teams"
PACKAGE_ID          = "command-group:msteam"
PACKAGE_DESCRIPTION = "Microsoft Teams의 채팅 또는 채널 이벤트를 기반으로 워크플로를 자동화하는 작업 및 트리거 주요 액션: 연결(OAuth2 인증을 사용하여 Teams 연결을 설정합니다.)、연결 끊기(설정된 연결을 종료합니다.)、이름으로 채널 가져오기(채널의 아이디를 검색합니다.)、채널 세부 정보 보기(채널의 세부 정보를 검색합니다.)、이름으로 팀 찾기(팀의 ID를 검색합니다.) 외 4개."

ACTIONS = [
    {"action": "연결", "data_item_name": "msteam#connect", "description": "OAuth2 인증을 사용하여 Teams 연결을 설정합니다."},
    {"action": "연결 끊기", "data_item_name": "msteam#disconnect", "description": "설정된 연결을 종료합니다."},
    {"action": "이름으로 채널 가져오기", "data_item_name": "msteam#getchannelbyname", "description": "채널의 아이디를 검색합니다."},
    {"action": "채널 세부 정보 보기", "data_item_name": "msteam#getchanneldetails", "description": "채널의 세부 정보를 검색합니다."},
    {"action": "이름으로 팀 찾기", "data_item_name": "msteam#getteambyname", "description": "팀의 ID를 검색합니다."},
    {"action": "팀 세부 정보 보기", "data_item_name": "msteam#getteamdetails", "description": "팀에 대한 세부 정보를 검색합니다."},
    {"action": "사용자 세부 정보 가져오기", "data_item_name": "msteam#getuserdetails", "description": "사용자에 대한 세부 정보를 검색합니다."},
    {"action": "채널 메시지 보내기", "data_item_name": "msteam#sendchannelmessage", "description": "채널에 메시지를 보냅니다."},
    {"action": "채팅 메시지 보내기", "data_item_name": "msteam#sendchatmessage", "description": "사용자에게 메시지를 보냅니다."},
]