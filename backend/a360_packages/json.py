# -*- coding: utf-8 -*-
PACKAGE_NAME        = "JSON"
PACKAGE_ID          = "command-group:json"
PACKAGE_DESCRIPTION = "JSON 텍스트 또는 파일에서 필요한 정보를 추출하고 추출된 값을 Bot에서 사용합니다. 주요 액션: 노드 값 추가(기존 JSON에 새 값 추가)、사전을 JSON으로 변환(사전을 JSON 문자열로 변환)、세션 종료(JSON 세션을 닫습니다.)、노드 목록 가져오기(노드 경로에 대한 노드 목록을 검색합니다.)、Get nodes(Gets multiple nodes value from specified...) 외 6개."

ACTIONS = [
    {"action": "노드 값 추가", "data_item_name": "json#addnodevalue", "description": "기존 JSON에 새 값 추가"},
    {"action": "사전을 JSON으로 변환", "data_item_name": "json#dictionarytojson", "description": "사전을 JSON 문자열로 변환"},
    {"action": "세션 종료", "data_item_name": "json#endsession", "description": "JSON 세션을 닫습니다."},
    {"action": "노드 목록 가져오기", "data_item_name": "json#getnodelist", "description": "노드 경로에 대한 노드 목록을 검색합니다."},
    {"action": "Get nodes", "data_item_name": "json#getnodes", "description": "Gets multiple nodes value from specified keys or paths"},
    {"action": "노드 값 가져오기", "data_item_name": "json#getnodevalue", "description": "JSON에서 노드 값을 검색합니다."},
    {"action": "JSON을 사전으로 변환", "data_item_name": "json#jsontodictionary", "description": "JSON 문자열을 사전으로 변환"},
    {"action": "Convert JSON to Table", "data_item_name": "json#convertjsontotable", "description": "Converts a JSON string into a table variable."},
    {"action": "세션 시작", "data_item_name": "json#startsession", "description": "JSON 파일 또는 지정된 텍스트를 기준으로 새 JSON 세션을 생성합니다."},
    {"action": "노드 값 업데이트", "data_item_name": "json#updatenodevalue", "description": "기존 JSON에 새 값 업데이트"},
    {"action": "Validate", "data_item_name": "json#validatejson", "description": "Validates JSON by checking the full content format, specified key or path exist, or a JSON schema."},
]