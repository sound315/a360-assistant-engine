# -*- coding: utf-8 -*-
PACKAGE_NAME        = "IQ Bot Pre-processor"
PACKAGE_ID          = "command-group:iq bot pre-processor"
PACKAGE_DESCRIPTION = "문서 또는 프로세스 이미지 파일에서 콘텐츠를 추출하여 IQ Bot으로 전송합니다 주요 액션: 이미지 연결(두 개의 이미지 파일을 연결합니다.)、이미지를 PDF로 변환(선택한 이미지 파일을 텍스트 지원 PDF 문서로 변환합니다. 변환된 PD...)、이미지 편집(이미지 파일을 자르거나 크기를 조정합니다.)、바코드 가져오기(문서에서 사용 가능한 모든 바코드를 감지하고 추출합니다.)、문서 정보 얻기(페이지 수 및 확장자 유형과 같은 문서 정보를 추출합니다.) 외 3개."

ACTIONS = [
    {"action": "이미지 연결", "data_item_name": "iq bot pre-processor#concatenateimages", "description": "두 개의 이미지 파일을 연결합니다."},
    {"action": "이미지를 PDF로 변환", "data_item_name": "iq bot pre-processor#convertimagetopdf", "description": "선택한 이미지 파일을 텍스트 지원 PDF 문서로 변환합니다. 변환된 PDF 파일은 기본으로 입력 이미지 파일의 이름을 유지합니다."},
    {"action": "이미지 편집", "data_item_name": "iq bot pre-processor#editimage", "description": "이미지 파일을 자르거나 크기를 조정합니다."},
    {"action": "바코드 가져오기", "data_item_name": "iq bot pre-processor#getbarcodes", "description": "문서에서 사용 가능한 모든 바코드를 감지하고 추출합니다."},
    {"action": "문서 정보 얻기", "data_item_name": "iq bot pre-processor#getdocumentinfo", "description": "페이지 수 및 확장자 유형과 같은 문서 정보를 추출합니다."},
    {"action": "페이지 콘텐츠 가져오기", "data_item_name": "iq bot pre-processor#getpagecontent", "description": "문서(PDF, 이미지 파일)의 특정 페이지에서 텍스트를 문자열 목록으로 추출합니다."},
    {"action": "이미지 향상", "data_item_name": "iq bot pre-processor#imageenhancement", "description": "선택한 이미지 파일을 향상시킵니다."},
    {"action": "이미지 방향", "data_item_name": "iq bot pre-processor#orientimage", "description": "선택한 이미지 파일의 방향을 변경합니다."},
]