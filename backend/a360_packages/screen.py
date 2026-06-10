# -*- coding: utf-8 -*-
PACKAGE_NAME        = "화면"
PACKAGE_ID          = "command-group:screen"
PACKAGE_DESCRIPTION = "애플리케이션 창, 전체 화면 또는 열려 있는 활성 창의 영역을 캡처하는 프로세스를 자동화하고 지정된 위치에 이미지 형식으로 저장합니다. 주요 액션: 캡처 영역(애플리케이션 창 영역의 스크린샷을 캡처합니다.)、바탕화면 캡처(전체 바탕 화면의 이미지를 캡처합니다.)、창 캡처(열려 있는 애플리케이션 창을 캡처합니다.) (총 3개)."

ACTIONS = [
    {"action": "캡처 영역", "data_item_name": "screen#capturearea", "description": "애플리케이션 창 영역의 스크린샷을 캡처합니다."},
    {"action": "바탕화면 캡처", "data_item_name": "screen#capturedesktop", "description": "전체 바탕 화면의 이미지를 캡처합니다."},
    {"action": "창 캡처", "data_item_name": "screen#capturewindow", "description": "열려 있는 애플리케이션 창을 캡처합니다."},
]