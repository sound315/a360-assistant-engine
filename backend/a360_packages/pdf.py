# -*- coding: utf-8 -*-
PACKAGE_NAME        = "PDF"
PACKAGE_ID          = "command-group:pdf"
PACKAGE_DESCRIPTION = "PDF 파일에 대한 다양한 작업을 자동화합니다. 주요 액션: 문서 비밀번호 해독(문서 암호화 작업을 사용하여 이전에 암호화된 PDF 파일의 암호를 해독합...)、문서 비밀번호화(PDF 파일을 암호화합니다.)、필드 추출(PDF에서 필드를 추출하여 변수에 할당합니다.)、이미지 추출(PDF 파일을 이미지로 저장합니다.)、텍스트 추출(PDF 파일에서 텍스트를 추출하여 텍스트 파일로 저장합니다.) 외 3개."

ACTIONS = [
    {"action": "문서 비밀번호 해독", "data_item_name": "pdf#decryptdocument", "description": "문서 암호화 작업을 사용하여 이전에 암호화된 PDF 파일의 암호를 해독합니다."},
    {"action": "문서 비밀번호화", "data_item_name": "pdf#encryptdocument", "description": "PDF 파일을 암호화합니다."},
    {"action": "필드 추출", "data_item_name": "pdf#extractfield", "description": "PDF에서 필드를 추출하여 변수에 할당합니다."},
    {"action": "이미지 추출", "data_item_name": "pdf#extractimage", "description": "PDF 파일을 이미지로 저장합니다."},
    {"action": "텍스트 추출", "data_item_name": "pdf#extracttext", "description": "PDF 파일에서 텍스트를 추출하여 텍스트 파일로 저장합니다."},
    {"action": "속성 가져오기", "data_item_name": "pdf#getproperty", "description": "PDF 문서의 속성을 검색합니다."},
    {"action": "문서 병합", "data_item_name": "pdf#mergedocument", "description": "여러 PDF 파일을 하나의 PDF 파일로 병합합니다."},
    {"action": "문서 분할", "data_item_name": "pdf#splitdocument", "description": "PDF 파일을 여러 파일로 분할합니다."},
]