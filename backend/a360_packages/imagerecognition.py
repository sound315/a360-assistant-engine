# -*- coding: utf-8 -*-
PACKAGE_NAME        = "이미지 인식"
PACKAGE_ID          = "command-group:imagerecognition"
PACKAGE_DESCRIPTION = "이미지를 기반으로 애플리케이션에서 사용자 인터페이스 요소를 검색하여 해당 애플리케이션의 작업을 자동화합니다. 주요 액션: 이미지를 창에서 찾기(대상 이미지(바늘)를 사용하여 애플리케이션 창(건초 더미)에서 UI 요소...)、창을 창에서 찾기(애플리케이션에서 UI 요소의 이미지를 캡처하고 캡처된 이미지를 사용하여...) (총 2개)."

ACTIONS = [
    {"action": "이미지를 창에서 찾기", "data_item_name": "imagerecognition#findfileimageinwindowimage", "description": "대상 이미지(바늘)를 사용하여 애플리케이션 창(건초 더미)에서 UI 요소를 검색합니다. 대상 이미지는 UI 요소를 검색하는 데 사용할 수 있는 기존 이미지입니다."},
    {"action": "창을 창에서 찾기", "data_item_name": "imagerecognition#findwindowimageinwindowimage", "description": "애플리케이션에서 UI 요소의 이미지를 캡처하고 캡처된 이미지를 사용하여 다른 창에서 해당 UI 요소를 검색합니다."},
]