# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Hugging Face"
PACKAGE_ID          = "Hugging Face"
PACKAGE_DESCRIPTION = "주요 액션: 인증(이 작업은 Hugging Face에 연결됩니다)、서버리스 추론(이 작업은 Hugging Face의 모델에 대한 서버리스 추론 호출을 실...) (총 2개)."

ACTIONS = [
    {"action": "인증", "data_item_name": "ai#huggingfaceauthenticationcommand", "description": "이 작업은 Hugging Face에 연결됩니다"},
    {"action": "서버리스 추론", "data_item_name": "ai#huggingfaceserverlessinferencecommand", "description": "이 작업은 Hugging Face의 모델에 대한 서버리스 추론 호출을 실행합니다."},
]