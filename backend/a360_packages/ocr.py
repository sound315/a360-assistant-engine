# -*- coding: utf-8 -*-
PACKAGE_NAME        = "OCR"
PACKAGE_ID          = "command-group:ocr"
PACKAGE_DESCRIPTION = "이미지 또는 애플리케이션에서 텍스트를 추출합니다. 주요 액션: 경로별 이미지 캡처(Control Room의 기기 또는 폴더에 있는 이미지에서 텍스트를 추출...)、URL별 이미지 캡처(온라인 이미지에서 텍스트를 추출합니다. 추출된 텍스트를 필터링하고 문자열...)、창 캡처(애플리케이션 창에서 텍스트를 추출합니다. 추출된 텍스트를 필터링하고 문자...)、캡처 영역(애플리케이션 창의 지정된 영역에서 텍스트를 추출합니다. 추출된 텍스트를...) (총 4개)."

ACTIONS = [
    {"action": "경로별 이미지 캡처", "data_item_name": "ocr#captureimagebypath", "description": "Control Room의 기기 또는 폴더에 있는 이미지에서 텍스트를 추출합니다. 추출된 텍스트는 변수로 할당할 수 있습니다."},
    {"action": "URL별 이미지 캡처", "data_item_name": "ocr#captureimagebyurl", "description": "온라인 이미지에서 텍스트를 추출합니다. 추출된 텍스트를 필터링하고 문자열 변수에 할당할 수 있습니다."},
    {"action": "창 캡처", "data_item_name": "ocr#capturewindow", "description": "애플리케이션 창에서 텍스트를 추출합니다. 추출된 텍스트를 필터링하고 문자열 변수에 할당할 수 있습니다."},
    {"action": "캡처 영역", "data_item_name": "ocr#capturewindowarea", "description": "애플리케이션 창의 지정된 영역에서 텍스트를 추출합니다. 추출된 텍스트를 필터링하고 변수로 할당할 수 있습니다."},
]