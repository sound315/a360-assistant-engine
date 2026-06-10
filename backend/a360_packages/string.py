# -*- coding: utf-8 -*-
PACKAGE_NAME        = "문자열"
PACKAGE_ID          = "command-group:string"
PACKAGE_DESCRIPTION = "주요 액션: 지정(문자열을 할당하거나 연결합니다.)、텍스트 추출(소스 문자열로부터 논리 연산자를 사용하여 텍스트의 범위를 추출합니다.)、비교(두 개의 문자열을 비교합니다.)、변수 평가(Bot의 사용자 지정 문자열 변수와 문자열 변수를 비교하고 일치하는 변수...)、찾기(지정된 문자열 내에서 하위 문자열을 찾습니다.) 외 12개."

ACTIONS = [
    {"action": "지정", "data_item_name": "string#assign", "description": "문자열을 할당하거나 연결합니다."},
    {"action": "텍스트 추출", "data_item_name": "string#beforeafter", "description": "소스 문자열로부터 논리 연산자를 사용하여 텍스트의 범위를 추출합니다."},
    {"action": "비교", "data_item_name": "string#compare", "description": "두 개의 문자열을 비교합니다."},
    {"action": "변수 평가", "data_item_name": "string#evaluate", "description": "Bot의 사용자 지정 문자열 변수와 문자열 변수를 비교하고 일치하는 변수의 값이 발견되면 반환합니다."},
    {"action": "찾기", "data_item_name": "string#find", "description": "지정된 문자열 내에서 하위 문자열을 찾습니다."},
    {"action": "길이", "data_item_name": "string#length", "description": "문자열의 길이를 검색합니다."},
    {"action": "소문자", "data_item_name": "string#lowercase", "description": "소스 문자열을 소문자로 변환합니다."},
    {"action": "랜덤 문자열 생성", "data_item_name": "string#randomstring", "description": "대문자 및 소문자 영숫자 문자열을 생성해 문자열 변수에 할당합니다."},
    {"action": "바꾸기", "data_item_name": "string#replace", "description": "소스 문자열 텍스트 한 부분을 찾아 다른 텍스트로 바꿉니다."},
    {"action": "반대로 뒤집기", "data_item_name": "string#reverse", "description": "소스 문자열을 반대로 뒤집습니다."},
    {"action": "분할", "data_item_name": "string#split", "description": "지정된 문자열을 여러 문자열로 분할하여 목록 변수에 출력을 저장합니다."},
    {"action": "하위 문자열", "data_item_name": "string#substring", "description": "문자열로부터 하위 문자열을 추출합니다."},
    {"action": "부울로", "data_item_name": "string#toboolean", "description": "문자열 값을 부울로 변환합니다."},
    {"action": "로케일 번호로", "data_item_name": "string#tolocalenumber", "description": "문자열을 로케일 형식의 숫자로 변환합니다."},
    {"action": "숫자로", "data_item_name": "string#tonumber", "description": "문자열을 숫자로 변환합니다."},
    {"action": "공백 제거", "data_item_name": "string#trim", "description": "문자열에서 공백, 탭, 줄바꿈을 제거합니다."},
    {"action": "대문자", "data_item_name": "string#uppercase", "description": "소스 문자열을 대문자로 변환합니다."},
]