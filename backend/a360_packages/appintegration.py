# -*- coding: utf-8 -*-
PACKAGE_NAME        = "앱 통합"
PACKAGE_ID          = "command-group:appintegration"
PACKAGE_DESCRIPTION = "사용자가 지정한 창이나 영역을 캡처하여 텍스트를 추출합니다. 주요 액션: 캡처 영역(창의 캡처된 영역 내에서 텍스트를 추출하여 문자열 변수에 저장합니다.)、스크롤 가능한 텍스트 캡처(지정된 창에서 스크롤 가능한 모든 텍스트를 캡처합니다.)、창 텍스트 캡처(창에서 모든 텍스트를 추출하여 문자열 변수에 저장합니다.) (총 3개)."

ACTIONS = [
    {"action": "캡처 영역", "data_item_name": "appintegration#capturearea", "description": "창의 캡처된 영역 내에서 텍스트를 추출하여 문자열 변수에 저장합니다."},
    {"action": "스크롤 가능한 텍스트 캡처", "data_item_name": "appintegration#capturescrollabletext", "description": "지정된 창에서 스크롤 가능한 모든 텍스트를 캡처합니다."},
    {"action": "창 텍스트 캡처", "data_item_name": "appintegration#capturewindow", "description": "창에서 모든 텍스트를 추출하여 문자열 변수에 저장합니다."},
]