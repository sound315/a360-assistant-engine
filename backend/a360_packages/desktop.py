# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Desktop"
PACKAGE_ID          = "Desktop"
PACKAGE_DESCRIPTION = "주요 액션: SAP 세션 추가(SAP 세션 데이터를 스크립트에 추가합니다. 이것은 11.x 마이그레이션...)、윈도우 컨트롤 관리(Windows 애플리케이션을 자동화합니다. 신규 Bot에서는 이 작업을...)、스크립트 실행(VBscript 및 Javascript를 실행합니다. 이것은 11.x 마...) (총 3개)."

ACTIONS = [
    {"action": "SAP 세션 추가", "data_item_name": "legacyautomation#appendsapsession", "description": "SAP 세션 데이터를 스크립트에 추가합니다. 이것은 11.x 마이그레이션된 Bot을 지원하기 위한 레거시 작업입니다."},
    {"action": "윈도우 컨트롤 관리", "data_item_name": "legacyautomation#managewindowscontrols", "description": "Windows 애플리케이션을 자동화합니다. 신규 Bot에서는 이 작업을 사용할 수 없습니다."},
    {"action": "스크립트 실행", "data_item_name": "legacyautomation#runscript", "description": "VBscript 및 Javascript를 실행합니다. 이것은 11.x 마이그레이션된 Bot을 지원하기 위한 레거시 작업입니다."},
]