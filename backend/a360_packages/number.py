# -*- coding: utf-8 -*-
PACKAGE_NAME        = "숫자"
PACKAGE_ID          = "command-group:number"
PACKAGE_DESCRIPTION = "숫자 변수에 대해 다양한 작업을 수행합니다. 숫자 변수는 정수 및 소수를 포함한 숫자 값을 보유합니다. 주요 액션: 지정(지정된 숫자 또는 식의 결과를 사용자 정의 숫자 변수에 할당할 수 있습니...)、감소(사용자가 지정한 값만큼 숫자를 감소시킵니다(설정 간격만큼 감소).)、증가(사용자가 지정한 값만큼 숫자를 증가시킵니다(설정 간격만큼 증가).)、무작위(사용자 지정 범위에서 임의의 정수를 생성하여 숫자 변수에 할당합니다.)、문자열로(사용자 지정 숫자를 문자열로 변환합니다.) (총 5개)."

ACTIONS = [
    {"action": "지정", "data_item_name": "number#assigntonumber", "description": "지정된 숫자 또는 식의 결과를 사용자 정의 숫자 변수에 할당할 수 있습니다."},
    {"action": "감소", "data_item_name": "number#decrement", "description": "사용자가 지정한 값만큼 숫자를 감소시킵니다(설정 간격만큼 감소)."},
    {"action": "증가", "data_item_name": "number#increment", "description": "사용자가 지정한 값만큼 숫자를 증가시킵니다(설정 간격만큼 증가)."},
    {"action": "무작위", "data_item_name": "number#randomnumber", "description": "사용자 지정 범위에서 임의의 정수를 생성하여 숫자 변수에 할당합니다."},
    {"action": "문자열로", "data_item_name": "number#tostring", "description": "사용자 지정 숫자를 문자열로 변환합니다."},
]