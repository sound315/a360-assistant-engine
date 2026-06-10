# -*- coding: utf-8 -*-
PACKAGE_NAME        = "첨부"
PACKAGE_ID          = "첨부"
PACKAGE_DESCRIPTION = "주요 액션: 첨부 파일 추가(지정된 기록에 첨부 파일 추가)、파일 할당(ServiceNow 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니...)、첨부 파일 삭제(지정된 기록의 첨부 파일 삭제)、첨부 파일 가져오기(파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다.) (총 4개)."

ACTIONS = [
    {"action": "첨부 파일 추가", "data_item_name": "servicenow#add_attachment", "description": "지정된 기록에 첨부 파일 추가"},
    {"action": "파일 할당", "data_item_name": "servicenow#assignfiletovariable", "description": "ServiceNow 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "첨부 파일 삭제", "data_item_name": "servicenow#delete_attachment", "description": "지정된 기록의 첨부 파일 삭제"},
    {"action": "첨부 파일 가져오기", "data_item_name": "servicenow#get_attachment", "description": "파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다."},
]