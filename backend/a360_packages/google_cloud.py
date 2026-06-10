# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Google Cloud"
PACKAGE_ID          = "Google Cloud"
PACKAGE_DESCRIPTION = "주요 액션: 연결 끊기(사용자 연결을 끊고 세션을 지웁니다)、연결(Vertex AI에 연결)、Vertex AI: 채팅 AI(자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다.)、Vertex AI: 멀티모달 프롬프트 AI(멀티모달 모델은 이미지, 비디오, 텍스트 등 다양한 양식의 정보를 처리할...)、Vertex AI: 프롬프트 AI(자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다.) (총 5개)."

ACTIONS = [
    {"action": "연결 끊기", "data_item_name": "generativeai#disconnect", "description": "사용자 연결을 끊고 세션을 지웁니다"},
    {"action": "연결", "data_item_name": "generativeai#connect", "description": "Vertex AI에 연결"},
    {"action": "Vertex AI: 채팅 AI", "data_item_name": "generativeai#vertexaichat", "description": "자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다."},
    {"action": "Vertex AI: 멀티모달 프롬프트 AI", "data_item_name": "generativeai#vertexaimultimodalprompt", "description": "멀티모달 모델은 이미지, 비디오, 텍스트 등 다양한 양식의 정보를 처리할 수 있는 모델입니다."},
    {"action": "Vertex AI: 프롬프트 AI", "data_item_name": "generativeai#vertexaiprompt", "description": "자연어, 텍스트 입력으로 Google Vertex 신경망을 호출합니다."},
]