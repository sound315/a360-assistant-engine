# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Workday"
PACKAGE_ID          = "command-group:workday"
PACKAGE_DESCRIPTION = "Workday Rest API에 대한 작업을 제공합니다. 주요 액션: 통합 이벤트 가져오기(통합 이벤트 가져오기로 개발자는 EIB 통합 또는 다른 통합의 진행 상황...)、보고서 가져오기(사용자 지정 보고서 세부 정보 검색)、EIB 시작(EIB는 개발자가 시스템에 데이터를 가져오거나 시스템에서 외부 소스로 데...)、인증(Workday API를 통해 인증하여 액세스 토큰 생성) (총 4개)."

ACTIONS = [
    {"action": "통합 이벤트 가져오기", "data_item_name": "workday#getintegrationevent", "description": "통합 이벤트 가져오기로 개발자는 EIB 통합 또는 다른 통합의 진행 상황을 모니터링할 수 있습니다"},
    {"action": "보고서 가져오기", "data_item_name": "workday#getreport", "description": "사용자 지정 보고서 세부 정보 검색"},
    {"action": "EIB 시작", "data_item_name": "workday#launcheib", "description": "EIB는 개발자가 시스템에 데이터를 가져오거나 시스템에서 외부 소스로 데이터를 내보낼 수 있는 중요한 기능입니다"},
    {"action": "인증", "data_item_name": "workday#soapauthentication", "description": "Workday API를 통해 인증하여 액세스 토큰 생성"},
]