# -*- coding: utf-8 -*-
PACKAGE_NAME        = "AWS SageMaker"
PACKAGE_ID          = "AWS SageMaker"
PACKAGE_DESCRIPTION = "주요 액션: 인증(작업이 AWS SageMaker에 연결됩니다.)、SageMaker 엔드포인트 호출(이 작업을 통해 추론 모델의 엔드포인트까지 쉽게 실행할 수 있습니다.) (총 2개)."

ACTIONS = [
    {"action": "인증", "data_item_name": "ai#authenticationcommand", "description": "작업이 AWS SageMaker에 연결됩니다."},
    {"action": "SageMaker 엔드포인트 호출", "data_item_name": "ai#invokeendpointcommand", "description": "이 작업을 통해 추론 모델의 엔드포인트까지 쉽게 실행할 수 있습니다."},
]