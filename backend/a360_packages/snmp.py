# -*- coding: utf-8 -*-
PACKAGE_NAME        = "SNMP"
PACKAGE_ID          = "command-group:snmp"
PACKAGE_DESCRIPTION = "데이터 검색 및 수정, 알림 메시지 전송과 같은 네트워크 관리 태스크를 자동화합니다. 주요 액션: 가져오기(SNMP 에이전트가 관리하는 객체의 데이터를 검색합니다.)、다음 가져오기(SNMP 에이전트가 관리하는 다음 객체의 데이터를 검색합니다.)、트랩 전송(SNMP 에이전트에서 SNMP 관리자에게 메시지를 보냅니다. 이러한 메시...)、설정(SNMP 에이전트가 관리하는 객체에 대한 값을 설정합니다.)、워크(연결된 모든 노드 또는 하위 트리에서 사용 가능한 모든 기기에 대한 정보...) (총 5개)."

ACTIONS = [
    {"action": "가져오기", "data_item_name": "snmp#get", "description": "SNMP 에이전트가 관리하는 객체의 데이터를 검색합니다."},
    {"action": "다음 가져오기", "data_item_name": "snmp#getnext", "description": "SNMP 에이전트가 관리하는 다음 객체의 데이터를 검색합니다."},
    {"action": "트랩 전송", "data_item_name": "snmp#sendtrap", "description": "SNMP 에이전트에서 SNMP 관리자에게 메시지를 보냅니다. 이러한 메시지는 시스템 재시작과 같은 특정 이벤트가 발생할 때 에이전트에서 전송됩니다."},
    {"action": "설정", "data_item_name": "snmp#set", "description": "SNMP 에이전트가 관리하는 객체에 대한 값을 설정합니다."},
    {"action": "워크", "data_item_name": "snmp#walk", "description": "연결된 모든 노드 또는 하위 트리에서 사용 가능한 모든 기기에 대한 정보 수집을 설정합니다."},
]