# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Google Application Integration"
PACKAGE_ID          = "command-group:apigeex"
PACKAGE_DESCRIPTION = "Google Application Integration API에 대한 작업을 제공합니다. 주요 액션: 연결(Google Application Integration에 연결)、연결 끊기(사용자 연결을 끊고 세션을 지웁니다)、통합 실행(Google Application Integration 실행)、통합 재개(일시 중단된 Google Application Integration 재개) (총 4개)."

ACTIONS = [
    {"action": "연결", "data_item_name": "apigeex#connect", "description": "Google Application Integration에 연결"},
    {"action": "연결 끊기", "data_item_name": "apigeex#disconnect", "description": "사용자 연결을 끊고 세션을 지웁니다"},
    {"action": "통합 실행", "data_item_name": "apigeex#executeintegration", "description": "Google Application Integration 실행"},
    {"action": "통합 재개", "data_item_name": "apigeex#resumeintegration", "description": "일시 중단된 Google Application Integration 재개"},
]