# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Microsoft Azure OpenAI"
PACKAGE_ID          = "Microsoft Azure OpenAI"
PACKAGE_DESCRIPTION = "주요 액션: 인증(Azure용 엔드포인트, API 키 및 API 버전 설정)、Azure OpenAI: 채팅 AI(ChatGPT(미리 보기) 및 GPT-4(미리 보기) 모델을 사용하여 채...)、Azure OpenAI:  멀티모달 채팅 AI(생성형 AI: Azure OpenAI:  멀티모달 채팅 AI필요한 Bot...)、Azure OpenAI: 프롬프트 AI(제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다.) (총 4개)."

ACTIONS = [
    {"action": "인증", "data_item_name": "generativeai#azureopenaiauth", "description": "Azure용 엔드포인트, API 키 및 API 버전 설정"},
    {"action": "Azure OpenAI: 채팅 AI", "data_item_name": "generativeai#azureopenaichat", "description": "ChatGPT(미리 보기) 및 GPT-4(미리 보기) 모델을 사용하여 채팅 메시지에 대한 완성본을 만듭니다."},
    {"action": "Azure OpenAI:  멀티모달 채팅 AI", "data_item_name": "generativeai#azuremultimodalchat", "description": "생성형 AI: Azure OpenAI:  멀티모달 채팅 AI필요한 Bot Agent 버전: 22.200.16 이상"},
    {"action": "Azure OpenAI: 프롬프트 AI", "data_item_name": "generativeai#azureopenaicompletion", "description": "제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다."},
]