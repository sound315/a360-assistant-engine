# -*- coding: utf-8 -*-
PACKAGE_NAME        = "레코더"
PACKAGE_ID          = "command-group:recorder"
PACKAGE_DESCRIPTION = "클릭, 읽기 및 쓰기와 같은 UI 요소와의 상호 작용을 기록합니다. 주요 액션: 캡처(클릭, 읽기 및 쓰기와 같은 UI 요소와의 상호 작용을 기록합니다.)、구조화된 데이터 추출(웹 애플리케이션에서 구조화된 데이터 블록을 추출합니다) (총 2개)."

ACTIONS = [
    {"action": "캡처", "data_item_name": "recorder#capture", "description": "클릭, 읽기 및 쓰기와 같은 UI 요소와의 상호 작용을 기록합니다."},
    {"action": "구조화된 데이터 추출", "data_item_name": "recorder#structureddataextraction", "description": "웹 애플리케이션에서 구조화된 데이터 블록을 추출합니다"},
]