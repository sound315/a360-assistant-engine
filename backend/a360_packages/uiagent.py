# -*- coding: utf-8 -*-
PACKAGE_NAME        = "UI 에이전트 - 웹"
PACKAGE_ID          = "command-group:uiagent"
PACKAGE_DESCRIPTION = "웹 운영에 대해 프롬프트로 정의된 목표를 분석하고 자동화하며, 생성형 AI 기능을 활용하여 자동으로 조치 항목을 타겟팅하고 참여를 유도합니다. 주요 액션: 세션 종료(UI 에이전트 세션 종료)、실행(에이전트의 목표에 맞춰 클릭, 입력 및 웹 페이지로부터의 데이터 추출과...)、세션 시작(UI 에이전트 세션 생성) (총 3개)."

ACTIONS = [
    {"action": "세션 종료", "data_item_name": "uiagent#uiwebagentend", "description": "UI 에이전트 세션 종료"},
    {"action": "실행", "data_item_name": "uiagent#uiwebagentrun", "description": "에이전트의 목표에 맞춰 클릭, 입력 및 웹 페이지로부터의 데이터 추출과 같은 브라우저 기반 작업을 실행합니다."},
    {"action": "세션 시작", "data_item_name": "uiagent#uiwebagentstart", "description": "UI 에이전트 세션 생성"},
]