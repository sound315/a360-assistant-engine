# -*- coding: utf-8 -*-
PACKAGE_NAME        = "ServiceNow"
PACKAGE_ID          = "command-group:servicenow"
PACKAGE_DESCRIPTION = "기록 변경 또는 웹훅 이벤트를 모니터링하는 트리거를 통해 자동화를 시작합니다. 주요 액션: 첨부 파일 추가(지정된 기록에 첨부 파일 추가)、파일 할당(ServiceNow 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니...)、첨부 파일 삭제(지정된 기록의 첨부 파일 삭제)、첨부 파일 가져오기(파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다.)、인증(ServiceNow API를 통해 인증하여 액세스 토큰 생성) 외 6개."

ACTIONS = [
    {"action": "첨부 파일 추가", "data_item_name": "servicenow#add_attachment", "description": "지정된 기록에 첨부 파일 추가"},
    {"action": "파일 할당", "data_item_name": "servicenow#assignfiletovariable", "description": "ServiceNow 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "첨부 파일 삭제", "data_item_name": "servicenow#delete_attachment", "description": "지정된 기록의 첨부 파일 삭제"},
    {"action": "첨부 파일 가져오기", "data_item_name": "servicenow#get_attachment", "description": "파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다."},
    {"action": "인증", "data_item_name": "servicenow#authentication", "description": "ServiceNow API를 통해 인증하여 액세스 토큰 생성"},
    {"action": "인증 취소", "data_item_name": "servicenow#revoke_authentication", "description": "세션에서 인증 컨텍스트 취소"},
    {"action": "기록 생성", "data_item_name": "servicenow#create_record", "description": "지정된 테이블에 하나의 기록 삽입"},
    {"action": "기록 삭제", "data_item_name": "servicenow#delete_record", "description": "지정된 테이블에서 기록 삭제"},
    {"action": "기록 가져오기", "data_item_name": "servicenow#get_record", "description": "지정된 테이블에서 지정된 sys_id로 식별된 기록 검색하기"},
    {"action": "여러 기록 가져오기", "data_item_name": "servicenow#list_record", "description": "지정된 테이블에서 여러 기록 검색하기"},
    {"action": "기록 업데이트", "data_item_name": "servicenow#update_record", "description": "요청 본문에 포함된 이름-값 쌍으로 지정된 기록 업데이트"},
]