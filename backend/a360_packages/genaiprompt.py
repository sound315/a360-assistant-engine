# -*- coding: utf-8 -*-
PACKAGE_NAME        = "AI 스킬"
PACKAGE_ID          = "command-group:genaiprompt"
PACKAGE_DESCRIPTION = "이 패키지는 Microsoft Azure OpenAI, Google Vertex AI, Amazon Bedrock, OpenAI 등과 같은 다양한 공급업체에서 지원하는 모델에 대해 사전 구성된 AI 스킬을 실행합니다. 주요 액션: 실행(AI 스킬을 실행합니다.) (총 1개)."

ACTIONS = [
    {"action": "실행", "data_item_name": "genaiprompt#genaipromptcommand", "description": "AI 스킬을 실행합니다."},
]