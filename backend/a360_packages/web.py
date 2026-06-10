# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Web"
PACKAGE_ID          = "Web"
PACKAGE_DESCRIPTION = "주요 액션: 페이지 닫기(Internet Explorer 페이지를 닫습니다.)、창 제목 업데이트(사용자 지정 값을 창 제목으로 창 변수에 지정)、자바 스크립트 함수 실행(Internet Explorer 페이지에서 JavaScript 함수를 실...)、데이터 추출(Internet Explorer 페이지에서 데이터를 추출합니다. 신규 B...)、패턴 데이터 추출(Internet Explorer 페이지에서 패턴 기반 데이터를 추출합니다...) 외 8개."

ACTIONS = [
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
]