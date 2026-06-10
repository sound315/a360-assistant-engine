# -*- coding: utf-8 -*-
PACKAGE_NAME        = "XML"
PACKAGE_ID          = "command-group:xml"
PACKAGE_DESCRIPTION = "웹 서비스 및 클라우드 컴퓨팅 애플리케이션에서 생성된 XML 데이터 처리를 자동화합니다. 주요 액션: 노드 삭제(XML 파일에서 특정 노드를 삭제합니다.)、세션 종료(XML 세션을 닫습니다.)、XPath 기능 실행(XPath 함수를 실행하고 결과를 변수에 저장합니다.)、여러 노드 가져오기(여러 노드의 값을 검색합니다.)、단일 노드 가져오기(단일 노드의 값을 검색합니다.) 외 5개."

ACTIONS = [
    {"action": "노드 삭제", "data_item_name": "xml#deletenode", "description": "XML 파일에서 특정 노드를 삭제합니다."},
    {"action": "세션 종료", "data_item_name": "xml#endsession", "description": "XML 세션을 닫습니다."},
    {"action": "XPath 기능 실행", "data_item_name": "xml#executexpath", "description": "XPath 함수를 실행하고 결과를 변수에 저장합니다."},
    {"action": "여러 노드 가져오기", "data_item_name": "xml#getmultiplenodev2", "description": "여러 노드의 값을 검색합니다."},
    {"action": "단일 노드 가져오기", "data_item_name": "xml#getsinglenodev2", "description": "단일 노드의 값을 검색합니다."},
    {"action": "노드 삽입", "data_item_name": "xml#insertnode", "description": "기존 XML 파일에 노드를 삽입하고 값에 할당합니다. 필요에 따라 네임스페이스와 속성을 노드에 할당합니다."},
    {"action": "세션 데이터 저장", "data_item_name": "xml#savexml", "description": "XML 세션 데이터를 문자열 유형의 파일이나 변수에 저장합니다."},
    {"action": "세션 시작", "data_item_name": "xml#startsession", "description": "XML 파일이나 지정된 텍스트를 기준으로 새 XML 세션을 생성합니다."},
    {"action": "노드 업데이트", "data_item_name": "xml#updatenode", "description": "노드의 값을 업데이트합니다."},
    {"action": "XML 문서 유효성 검사", "data_item_name": "xml#validatexml", "description": "XML 문서의 유효성을 검사합니다. 태그와 문서 구조는 문서가 생성될 때 정의됩니다."},
]