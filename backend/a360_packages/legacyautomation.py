# -*- coding: utf-8 -*-
PACKAGE_NAME        = "레거시 자동화"
PACKAGE_ID          = "command-group:legacyautomation"
PACKAGE_DESCRIPTION = "레거시 자동화 작업을 수행하기 위한 액션을 제공합니다. 주요 액션: SAP 세션 추가(SAP 세션 데이터를 스크립트에 추가합니다. 이것은 11.x 마이그레이션...)、윈도우 컨트롤 관리(Windows 애플리케이션을 자동화합니다. 신규 Bot에서는 이 작업을...)、스크립트 실행(VBscript 및 Javascript를 실행합니다. 이것은 11.x 마...)、페이지 닫기(Internet Explorer 페이지를 닫습니다.)、창 제목 업데이트(사용자 지정 값을 창 제목으로 창 변수에 지정) 외 13개."

ACTIONS = [
    {"action": "SAP 세션 추가", "data_item_name": "legacyautomation#appendsapsession", "description": "SAP 세션 데이터를 스크립트에 추가합니다. 이것은 11.x 마이그레이션된 Bot을 지원하기 위한 레거시 작업입니다."},
    {"action": "윈도우 컨트롤 관리", "data_item_name": "legacyautomation#managewindowscontrols", "description": "Windows 애플리케이션을 자동화합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "스크립트 실행", "data_item_name": "legacyautomation#runscript", "description": "VBscript 및 Javascript를 실행합니다. 이것은 11.x 마이그레이션된 Bot을 지원하기 위한 레거시 작업입니다."},
    {"action": "페이지 닫기", "data_item_name": "legacyautomation#close", "description": "Internet Explorer 페이지를 닫습니다."},
    {"action": "창 제목 업데이트", "data_item_name": "legacyautomation#converttowindowtitle", "description": "사용자 지정 값을 창 제목으로 창 변수에 지정"},
    {"action": "자바 스크립트 함수 실행", "data_item_name": "legacyautomation#executejavascriptfunction", "description": "Internet Explorer 페이지에서 JavaScript 함수를 실행합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "데이터 추출", "data_item_name": "legacyautomation#extractdata", "description": "Internet Explorer 페이지에서 데이터를 추출합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "패턴 데이터 추출", "data_item_name": "legacyautomation#extractpatterndata", "description": "Internet Explorer 페이지에서 패턴 기반 데이터를 추출합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "소스코드 추출", "data_item_name": "legacyautomation#extractsource", "description": "Internet Explorer 페이지에서 소스 코드를 가져옵니다. 신규 Bot에서는 지원하지 않는 작업입니다."},
    {"action": "테이블 추출", "data_item_name": "legacyautomation#extracttable", "description": "Internet Explorer 페이지에서 테이블 데이터를 읽습니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "뒤로 이동", "data_item_name": "legacyautomation#goback", "description": "마지막으로 열었던 Internet Explorer 페이지로 돌아갑니다."},
    {"action": "웹 컨트롤 관리", "data_item_name": "legacyautomation#managewebcontrols", "description": "웹 애플리케이션을 자동화합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "페이지로 이동", "data_item_name": "legacyautomation#navigate", "description": "기존 Internet Explorer 창에서 웹 페이지를 엽니다."},
    {"action": "페이지 열기", "data_item_name": "legacyautomation#open", "description": "Internet Explorer 창에서 웹 페이지를 엽니다."},
    {"action": "캡션으로 검색", "data_item_name": "legacyautomation#searchbycaption", "description": "Internet Explorer 페이지에서 지정된 텍스트를 찾아 클릭합니다."},
    {"action": "설정 구성", "data_item_name": "legacyautomation#configuration", "description": "레거시 패키지에서 웹 실행을 위한 구성 옵션을 설정합니다."},
    {"action": "키 입력 지연 가져오기", "data_item_name": "legacyautomation#getkeystrokesdelay", "description": "키 입력과 키 입력 사이의 지연 시간을 반환합니다. 이는 마이그레이션한 11.x Bot을 지원하기 위한 기존 조치입니다."},
    {"action": "텍스트 파일에서 목록 가져오기", "data_item_name": "legacyautomation#importlistfromtextfile", "description": "텍스트 파일에서 하위 유형 문자열 목록으로 텍스트를 가져옵니다. 텍스트 파일에서 쉼표로 구분된 값을 기준으로 목록 항목을 가져옵니다"},
]