# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Google Document AI"
PACKAGE_ID          = "command-group:googledocai"
PACKAGE_DESCRIPTION = "Google Document AI로 문서 추출을 수행합니다. 주요 액션: 연결(Google Cloud 서비스 계정에 연결합니다.)、연결 끊기(Google Cloud 서비스 연결을 끊습니다.)、추출(Google Document AI로 문서에서 정보를 추출합니다. 최대 2...) (총 3개)."

ACTIONS = [
    {"action": "연결", "data_item_name": "googledocai#connect", "description": "Google Cloud 서비스 계정에 연결합니다."},
    {"action": "연결 끊기", "data_item_name": "googledocai#disconnect", "description": "Google Cloud 서비스 연결을 끊습니다."},
    {"action": "추출", "data_item_name": "googledocai#extract", "description": "Google Document AI로 문서에서 정보를 추출합니다. 최대 20MB 크기의 파일을 지원합니다."},
]