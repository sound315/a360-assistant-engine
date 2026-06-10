# -*- coding: utf-8 -*-
PACKAGE_NAME        = "날짜 시간"
PACKAGE_ID          = "command-group:datetime"
PACKAGE_DESCRIPTION = "날짜/시간 변수의 값 업데이트 및 비교와 같은 날짜/시간 값에 대해 다양한 작업을 수행할 수 있습니다. 주요 액션: 추가(날짜/시간 변수의 값을 지정된 시간 값 및 단위만큼 증가시킵니다. 예를...)、지정(선택한 날짜/시간 형식으로 문자열 변수를 할당하거나 날짜/시간 값을 수동...)、날짜 간 차이(두 날짜 간의 차이를 계산합니다.)、가져오기(선택한 날짜 및 시간 매개변수의 값을 표시합니다.)、이후임(두 날짜/시간 변수를 비교하고 원본 변수의 값이 비교 변수의 값 이후인지...) 외 5개."

ACTIONS = [
    {"action": "추가", "data_item_name": "datetime#add", "description": "날짜/시간 변수의 값을 지정된 시간 값 및 단위만큼 증가시킵니다. 예를 들어 날짜/시간 변수 값을 3시간 또는 3일 늘립니다."},
    {"action": "지정", "data_item_name": "datetime#assign", "description": "선택한 날짜/시간 형식으로 문자열 변수를 할당하거나 날짜/시간 값을 수동으로 할당하거나 기존 날짜/시간 변수를 날짜/시간 변수에 할당합니다."},
    {"action": "날짜 간 차이", "data_item_name": "datetime#differencebetweendates", "description": "두 날짜 간의 차이를 계산합니다."},
    {"action": "가져오기", "data_item_name": "datetime#get", "description": "선택한 날짜 및 시간 매개변수의 값을 표시합니다."},
    {"action": "이후임", "data_item_name": "datetime#isafter", "description": "두 날짜/시간 변수를 비교하고 원본 변수의 값이 비교 변수의 값 이후인지 확인하고 출력을 부울 변수에 저장합니다."},
    {"action": "이전임", "data_item_name": "datetime#isbefore", "description": "두 날짜/시간 변수를 비교하고 원본 변수의 값이 비교 변수의 값 이전인지 확인하고 출력을 부울 변수에 저장합니다."},
    {"action": "동등함", "data_item_name": "datetime#isequal", "description": "두 날짜/시간 변수를 비교하고 원본 변수의 값이 비교 변수의 값과 같은지 확인하고 출력을 부울 변수에 저장합니다."},
    {"action": "윤년입니다.", "data_item_name": "datetime#isleapyear", "description": "해당 연도가 윤년인지 확인합니다."},
    {"action": "빼기", "data_item_name": "datetime#subtract", "description": "날짜/시간 변수의 값을 지정된 시간 값 및 단위만큼 감소시킵니다. 예를 들어 날짜/시간 변수 값을 3시간 또는 3일 줄입니다."},
    {"action": "To 문자열", "data_item_name": "datetime#tostring", "description": "날짜/시간 값을 문자열 값으로 변환하고 미리 정의된 형식을 선택하거나 출력 값에 대한 사용자 지정 형식을 지정할 수 있습니다."},
]