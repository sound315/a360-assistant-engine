# -*- coding: utf-8 -*-
PACKAGE_NAME        = "부울"
PACKAGE_ID          = "command-group:boolean"
PACKAGE_DESCRIPTION = "부울 값에 대해 다양한 작업을 수행합니다. 주요 액션: 지정(부울 값에 상수 값(True 또는 False) 또는 사용자 정의 값을 할...)、비교(두 부울 값을 비교하고 출력을 숫자 변수에 할당합니다.)、동일(두 부울 값이 같은지 확인하고 출력을 부울 변수에 할당합니다.)、반전(부울 값을 반대 값으로 변환하고(True를 False로, False를 T...)、숫자로(부울 값을 숫자 값으로 변환합니다. 이 작업은 True를 1로, Fals...) 외 1개."

ACTIONS = [
    {"action": "지정", "data_item_name": "boolean#assign", "description": "부울 값에 상수 값(True 또는 False) 또는 사용자 정의 값을 할당합니다."},
    {"action": "비교", "data_item_name": "boolean#compareto", "description": "두 부울 값을 비교하고 출력을 숫자 변수에 할당합니다."},
    {"action": "동일", "data_item_name": "boolean#equalto", "description": "두 부울 값이 같은지 확인하고 출력을 부울 변수에 할당합니다."},
    {"action": "반전", "data_item_name": "boolean#invert", "description": "부울 값을 반대 값으로 변환하고(True를 False로, False를 True로) 출력을 변수에 할당합니다."},
    {"action": "숫자로", "data_item_name": "boolean#tonumber", "description": "부울 값을 숫자 값으로 변환합니다. 이 작업은 True를 1로, False를 0으로 변환합니다."},
    {"action": "문자열로", "data_item_name": "boolean#tostring", "description": "부울 값을 문자열 값으로 변환합니다."},
]