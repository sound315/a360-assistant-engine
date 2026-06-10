# -*- coding: utf-8 -*-
PACKAGE_NAME        = "SAP BAPI"
PACKAGE_ID          = "command-group:sapbapi"
PACKAGE_DESCRIPTION = "이 패키지는 SAP-BAPI 작업을 수행하는 데 사용할 수 있습니다. 주요 액션: 함수 생성(선택한 BAPI 함수에 대한 사용자 정의 함수를 만듭니다.)、필드 값 가져오기(함수를 호출하여 함수, 테이블 또는 구조에서 필드 데이터를 가져옵니다)、구조 가져오기(구조에서 테이블 데이터를 얻기 위해 함수를 호출합니다)、테이블 가져오기(사용자 정의 함수를 호출하여 테이블 형식 데이터 가져오기)、사용자 지정 워크플로 실행(SAP BAPI에서 사용자 지정 워크플로를 실행합니다.) 외 5개."

ACTIONS = [
    {"action": "함수 생성", "data_item_name": "sapbapi#sapbapicreatefunction", "description": "선택한 BAPI 함수에 대한 사용자 정의 함수를 만듭니다."},
    {"action": "필드 값 가져오기", "data_item_name": "sapbapi#sapbapigetfield", "description": "함수를 호출하여 함수, 테이블 또는 구조에서 필드 데이터를 가져옵니다"},
    {"action": "구조 가져오기", "data_item_name": "sapbapi#sapbapigetstructure", "description": "구조에서 테이블 데이터를 얻기 위해 함수를 호출합니다"},
    {"action": "테이블 가져오기", "data_item_name": "sapbapi#sapbapigettable", "description": "사용자 정의 함수를 호출하여 테이블 형식 데이터 가져오기"},
    {"action": "사용자 지정 워크플로 실행", "data_item_name": "sapbapi#runcustomworkflow", "description": "SAP BAPI에서 사용자 지정 워크플로를 실행합니다."},
    {"action": "사용자 지정 워크플로 고급 실행", "data_item_name": "sapbapi#runcustomworkflowadvanced", "description": "SAP 시스템에 연결하여 사용자 지정 워크플로 검색 및 실행"},
    {"action": "함수 실행", "data_item_name": "sapbapi#sapbapiinvokefunction", "description": "함수 가져오기에서 별칭이 지정된 BAPI 함수를 실행합니다"},
    {"action": "표준 워크플로 실행", "data_item_name": "sapbapi#runstandardworkflow", "description": "SAP BAPI에서 표준 워크플로를 실행합니다."},
    {"action": "연결", "data_item_name": "sapbapi#sapbapiconnect", "description": "BAPI를 사용하여 SAP에 대한 연결을 만듭니다."},
    {"action": "필드 값 설정", "data_item_name": "sapbapi#sapbapisetfield", "description": "함수를 호출하여 필드 데이터를 함수나 테이블 또는 구조에 집어 넣습니다"},
]