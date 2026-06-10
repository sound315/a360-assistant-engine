# -*- coding: utf-8 -*-
PACKAGE_NAME        = "AI"
PACKAGE_ID          = "command-group:ai"
PACKAGE_DESCRIPTION = "이 패키지에는 모든 AI 관련 명령 작업이 포함되어 있습니다. 공급자로는 AWS SageMaker가 포함됩니다. 주요 액션: 인증(작업이 AWS SageMaker에 연결됩니다.)、SageMaker 엔드포인트 호출(이 작업을 통해 추론 모델의 엔드포인트까지 쉽게 실행할 수 있습니다.)、인증(이 작업은 Hugging Face에 연결됩니다)、서버리스 추론(이 작업은 Hugging Face의 모델에 대한 서버리스 추론 호출을 실...) (총 4개)."

ACTIONS = [
    {"action": "인증", "data_item_name": "ai#authenticationcommand", "description": "작업이 AWS SageMaker에 연결됩니다."},
    {"action": "SageMaker 엔드포인트 호출", "data_item_name": "ai#invokeendpointcommand", "description": "이 작업을 통해 추론 모델의 엔드포인트까지 쉽게 실행할 수 있습니다."},
    {"action": "인증", "data_item_name": "ai#huggingfaceauthenticationcommand", "description": "이 작업은 Hugging Face에 연결됩니다"},
    {"action": "서버리스 추론", "data_item_name": "ai#huggingfaceserverlessinferencecommand", "description": "이 작업은 Hugging Face의 모델에 대한 서버리스 추론 호출을 실행합니다."},
]