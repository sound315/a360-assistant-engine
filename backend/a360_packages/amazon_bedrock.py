# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Amazon Bedrock"
PACKAGE_ID          = "Amazon Bedrock"
PACKAGE_DESCRIPTION = "주요 액션: AI21 Labs: 채팅 AI(이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21...)、AI21 Labs: 프롬프트 AI(이 작업은 뛰어난 품질을 제공하는 AI21의 가장 강력한 모델인 AI21...)、인증(이 작업은 AWS Bedrock에 연결됩니다.)、Anthropic: 채팅 AI(이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthro...)、Anthropic: 멀티모달 AI(이 작업은 유용하고 정직하며 무해한 AI 시스템 학습에 대한 Anthro...) 외 4개."

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
]