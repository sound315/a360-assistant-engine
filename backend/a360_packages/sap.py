# -*- coding: utf-8 -*-
PACKAGE_NAME        = "SAP"
PACKAGE_ID          = "command-group:sap"
PACKAGE_DESCRIPTION = "SAP 애플리케이션에서 태스크 및 프로세스를 자동화합니다. 주요 액션: 확인란 선택/선택 취소(SAP 창의 확인란을 선택하거나 선택 취소합니다.)、클릭(클릭 작업을 수행합니다.)、클릭 메뉴(SAP 창에서 텍스트 또는 인덱스별로 메뉴 항목을 클릭합니다.)、연결(SAP 애플리케이션과의 연결을 설정합니다.)、연결 끊기(SAP 애플리케이션에 대한 연결을 종료합니다.) 외 21개."

ACTIONS = [
    {"action": "확인란 선택/선택 취소", "data_item_name": "sap#checkboxactions", "description": "SAP 창의 확인란을 선택하거나 선택 취소합니다."},
    {"action": "클릭", "data_item_name": "sap#click", "description": "클릭 작업을 수행합니다."},
    {"action": "클릭 메뉴", "data_item_name": "sap#clickmenu", "description": "SAP 창에서 텍스트 또는 인덱스별로 메뉴 항목을 클릭합니다."},
    {"action": "연결", "data_item_name": "sap#connect", "description": "SAP 애플리케이션과의 연결을 설정합니다."},
    {"action": "연결 끊기", "data_item_name": "sap#disconnect", "description": "SAP 애플리케이션에 대한 연결을 종료합니다."},
    {"action": "더블클릭", "data_item_name": "sap#doubleclick", "description": "SAP 창에서 더블 클릭 작업을 수행합니다."},
    {"action": "확장", "data_item_name": "sap#expand", "description": "SAP 창에서 텍스트 또는 인덱스별로 항목을 확장합니다."},
    {"action": "내보내기 테이블", "data_item_name": "sap#exporttable", "description": "테이블 컨트롤을 데이터 테이블 또는 CSV 파일로 내보냅니다."},
    {"action": "셀 수 가져오기", "data_item_name": "sap#getcell", "description": "테이블 또는 그리드의 셀 수를 검색합니다."},
    {"action": "하위 이름 가져오기", "data_item_name": "sap#getchildrennames", "description": "하위 컨트롤 이름을 검색합니다."},
    {"action": "하위 텍스트 가져오기", "data_item_name": "sap#getchildrentext", "description": "하위 컨트롤과 관련된 텍스트를 검색합니다."},
    {"action": "열 수 가져오기", "data_item_name": "sap#getcolumn", "description": "테이블 또는 그리드의 열 수를 검색합니다."},
    {"action": "행 수 가져오기", "data_item_name": "sap#getrow", "description": "테이블 또는 그리드의 행 수를 검색합니다."},
    {"action": "선택한 항목 가져오기", "data_item_name": "sap#getselecteditemaction", "description": "콤보 박스, 페이지 탭 또는 트리 뷰 컨트롤로부터 선택한 항목 인덱스를 검색합니다."},
    {"action": "상태 가져오기", "data_item_name": "sap#getstatusaction", "description": "라디오 버튼 또는 확인란의 상태를 검색합니다."},
    {"action": "테이블 셀 인덱스 가져오기", "data_item_name": "sap#gettablecellindexbytextaction", "description": "텍스트에 대한 테이블 셀 인덱스를 검색합니다."},
    {"action": "테이블 셀 텍스트 가져오기", "data_item_name": "sap#gettablecelltextbyindexaction", "description": "인덱스별 테이블 셀 텍스트를 검색합니다."},
    {"action": "텍스트 가져오기", "data_item_name": "sap#gettext", "description": "텍스트 상자, 라벨 또는 상태 표시줄로부터 텍스트를 검색합니다."},
    {"action": "항목 개수 가져오기", "data_item_name": "sap#getitemcountaction", "description": "콤보 박스, 페이지 탭 또는 트리 뷰 컨트롤에서 항목 개수를 검색합니다."},
    {"action": "왼쪽 클릭", "data_item_name": "sap#leftclick", "description": "왼쪽을 클릭하는 작업을 수행합니다."},
    {"action": "오른쪽 클릭", "data_item_name": "sap#rightclick", "description": "오른쪽을 클릭하는 작업을 수행합니다."},
    {"action": "항목 선택", "data_item_name": "sap#selectitem", "description": "텍스트 또는 인덱스별로 항목을 선택합니다."},
    {"action": "라디오 옵션 선택", "data_item_name": "sap#selectradiooption", "description": "라디오 버튼을 선택합니다."},
    {"action": "가상 키 전송", "data_item_name": "sap#sendvirtualkey", "description": "가상 키를 SAP 창으로 전송합니다."},
    {"action": "테이블 셀 텍스트 설정", "data_item_name": "sap#settablecelltext", "description": "텍스트 또는 인덱스별로 테이블의 값을 설정합니다."},
    {"action": "텍스트 설정", "data_item_name": "sap#settext", "description": "편집 가능 필드에 텍스트를 설정합니다."},
]