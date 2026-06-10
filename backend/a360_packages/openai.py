# -*- coding: utf-8 -*-
PACKAGE_NAME        = "OpenAI"
PACKAGE_ID          = "OpenAI"
PACKAGE_DESCRIPTION = "주요 액션: 인증(OpenAI용 API 키 설정)、OpenAI: 채팅 AI(주어진 채팅 대화에 대한 모델 응답을 만듭니다.)、OpenAI: 멀티모달 채팅 AI(주어진 채팅 대화에 대한 비전 모델 응답을 만듭니다.)、OpenAI: 프롬프트 AI(제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다.)、OpenAI: 어시스턴트 실행(스레드에서 어시스턴트를 실행하여 응답을 트리거합니다. 그러면 관련 도구가...) 외 1개."

ACTIONS = [
    {"action": "인증", "data_item_name": "generativeai#openaiauth", "description": "OpenAI용 API 키 설정"},
    {"action": "OpenAI: 채팅 AI", "data_item_name": "generativeai#openaichat", "description": "주어진 채팅 대화에 대한 모델 응답을 만듭니다."},
    {"action": "OpenAI: 멀티모달 채팅 AI", "data_item_name": "generativeai#openaimultimodalchat", "description": "주어진 채팅 대화에 대한 비전 모델 응답을 만듭니다."},
    {"action": "OpenAI: 프롬프트 AI", "data_item_name": "generativeai#openaicompletion", "description": "제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다."},
    {"action": "OpenAI: 어시스턴트 실행", "data_item_name": "generativeai#openairunassistant", "description": "스레드에서 어시스턴트를 실행하여 응답을 트리거합니다. 그러면 관련 도구가 자동으로 호출됩니다."},
    {"action": "OpenAI: 어시스턴트 실행 함수", "data_item_name": "generativeai#openairunassistantfunction", "description": "각각의 스레드 ID, 실행 ID, 도구 호출 ID를 사용하여 어시스턴트 함수를 실행하십시오."},
]