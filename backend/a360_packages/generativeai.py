# -*- coding: utf-8 -*-
PACKAGE_NAME        = "생성형 AI"
PACKAGE_ID          = "command-group:generativeai"
PACKAGE_DESCRIPTION = "이 패키지에는 모든 생성형 AI 관련 명령 작업이 포함되어 있습니다. 공급자로는 Microsoft Azure, OpenAI, Google Vertex AI 및 Amazon AWS Bedrock AI가 포함됩니다. 주요 액션: AI21 Labs: 채팅 AI(이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21...)、AI21 Labs: 프롬프트 AI(이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21...)、인증(이 작업은 AWS Bedrock에 연결됩니다.)、Anthropic: 채팅 AI(이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthro...)、Anthropic: 멀티모달 AI(이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthro...) 외 19개."

ACTIONS = [
    {"action": "AI21 Labs: 채팅 AI", "data_item_name": "generativeai#ai21labschatcommand", "description": "이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21 Lab Jurassic-2/Jamba 시리즈 AI를 실행합니다"},
    {"action": "AI21 Labs: 프롬프트 AI", "data_item_name": "generativeai#ai21labspromptcommand", "description": "이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21 Lab Jurassic-2/Jamba 시리즈 AI를 실행합니다"},
    {"action": "인증", "data_item_name": "generativeai#authenticationcommand", "description": "이 작업은 AWS Bedrock에 연결됩니다."},
    {"action": "Anthropic: 채팅 AI", "data_item_name": "generativeai#anthropicchatcommand", "description": "이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthropic의 연구를 기반으로 하는 차세대 AI 비서인 Anthropic Claude AI를 실행합니다."},
    {"action": "Anthropic: 멀티모달 AI", "data_item_name": "generativeai#anthropicmultimodalcommand", "description": "이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthropic의 연구를 기반으로 하는 차세대 AI 비서인 Anthropic Claude AI를 실행합니다."},
    {"action": "Anthropic: 프롬프트 AI", "data_item_name": "generativeai#anthropicpromptcommand", "description": "이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthropic의 연구를 기반으로 하는 차세대 AI 비서인 Anthropic Claude AI를 실행합니다."},
    {"action": "Stability AI: 텍스트-이미지 AI", "data_item_name": "generativeai#stabilityaitexttoimagecommand", "description": "이 작업은 텍스트 설명, 인페인팅, 아웃페인팅 및 이미지-이미지 번역을 생성하는 데 사용되는 딥 러닝, 텍스트-이미지 모델인 Stability AI 모델을 실행하여 세부 이미지를 생성합니다."},
    {"action": "Amazon Titan: 채팅 AI", "data_item_name": "generativeai#titanaichatcommand", "description": "이 작업은 대규모 데이터 세트에 대해 사전 학습된 Amazon Titan Foundation Model을 실행하여 강력한 범용 모델로 만듭니다."},
    {"action": "Amazon Titan: 프롬프트 AI", "data_item_name": "generativeai#titanaipromptcommand", "description": "이 작업은 대규모 데이터 세트에 대해 사전 학습된 Amazon Titan Foundation Model을 실행하여 강력한 범용 모델로 만듭니다."},
    {"action": "연결 끊기", "data_item_name": "generativeai#disconnect", "description": "사용자 연결을 끊고 세션을 지웁니다"},
    {"action": "연결", "data_item_name": "generativeai#connect", "description": "Vertex AI에 연결"},
    {"action": "Vertex AI: 채팅 AI", "data_item_name": "generativeai#vertexaichat", "description": "자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다."},
    {"action": "Vertex AI: 멀티모달 프롬프트 AI", "data_item_name": "generativeai#vertexaimultimodalprompt", "description": "멀티모달 모델은 이미지, 비디오, 텍스트 등 다양한 양식의 정보를 처리할 수 있는 모델입니다."},
    {"action": "Vertex AI: 프롬프트 AI", "data_item_name": "generativeai#vertexaiprompt", "description": "자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다."},
    {"action": "인증", "data_item_name": "generativeai#azureopenaiauth", "description": "Azure용 엔드포인트, API 키 및 API 버전 설정"},
    {"action": "Azure OpenAI: 채팅 AI", "data_item_name": "generativeai#azureopenaichat", "description": "ChatGPT(미리 보기) 및 GPT-4(미리 보기) 모델을 사용하여 채팅 메시지에 대한 완성본을 만듭니다."},
    {"action": "Azure OpenAI:  멀티모달 채팅 AI", "data_item_name": "generativeai#azuremultimodalchat", "description": "생성형 AI: Azure OpenAI:  멀티모달 채팅 AI필요한 Bot Agent 버전: 22.200.16 이상"},
    {"action": "Azure OpenAI: 프롬프트 AI", "data_item_name": "generativeai#azureopenaicompletion", "description": "제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다."},
    {"action": "인증", "data_item_name": "generativeai#openaiauth", "description": "OpenAI용 API 키 설정"},
    {"action": "OpenAI: 채팅 AI", "data_item_name": "generativeai#openaichat", "description": "주어진 채팅 대화에 대한 모델 응답을 만듭니다."},
    {"action": "OpenAI: 멀티모달 채팅 AI", "data_item_name": "generativeai#openaimultimodalchat", "description": "주어진 채팅 대화에 대한 비전 모델 응답을 만듭니다."},
    {"action": "OpenAI: 프롬프트 AI", "data_item_name": "generativeai#openaicompletion", "description": "제공된 프롬프트 및 매개변수에 대한 완성본을 만듭니다."},
    {"action": "OpenAI: 어시스턴트 실행", "data_item_name": "generativeai#openairunassistant", "description": "스레드에서 어시스턴트를 실행하여 응답을 트리거합니다. 그러면 관련 도구가 자동으로 호출됩니다."},
    {"action": "OpenAI: 어시스턴트 실행 함수", "data_item_name": "generativeai#openairunassistantfunction", "description": "각각의 스레드 ID, 실행 ID, 도구 호출 ID를 사용하여 어시스턴트 함수를 실행하십시오."},
]