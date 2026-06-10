# -*- coding: utf-8 -*-
PACKAGE_NAME        = "목록 및 목록 항목"
PACKAGE_ID          = "목록 및 목록 항목"
PACKAGE_DESCRIPTION = "주요 액션: 목록 생성(선택한 템플릿으로 목록을 만듭니다.)、목록 삭제(SharePoint 사이트에서 목록을 삭제합니다.)、목록 가져오기(필터를 사용하여 목록 가져오기)、목록 업데이트(목록을 업데이트합니다.)、목록 항목 생성(목록에 목록 항목을 추가합니다.) 외 7개."

ACTIONS = [
    {"action": "목록 생성", "data_item_name": "sharepoint#createlist", "description": "선택한 템플릿으로 목록을 만듭니다."},
    {"action": "목록 삭제", "data_item_name": "sharepoint#deletelist", "description": "SharePoint 사이트에서 목록을 삭제합니다."},
    {"action": "목록 가져오기", "data_item_name": "sharepoint#getlist", "description": "필터를 사용하여 목록 가져오기"},
    {"action": "목록 업데이트", "data_item_name": "sharepoint#updatelist", "description": "목록을 업데이트합니다."},
    {"action": "목록 항목 생성", "data_item_name": "sharepoint#createlistitem", "description": "목록에 목록 항목을 추가합니다."},
    {"action": "목록 항목 삭제", "data_item_name": "sharepoint#deletelistitem", "description": "목록에서 목록 항목을 삭제합니다."},
    {"action": "목록 항목 가져오기", "data_item_name": "sharepoint#getlistitem", "description": "필터를 사용하여 목록 항목 가져오기"},
    {"action": "목록 항목 업데이트", "data_item_name": "sharepoint#updatelistitem", "description": "목록의 목록 항목 업데이트"},
    {"action": "목록 이미지 업로드", "data_item_name": "sharepoint#uploadlistimage", "description": "목록 항목에 이미지 파일을 업로드합니다. 그래프 API에서는 목록 항목 이미지 기능이 지원되지 않습니다. 대신 REST API 옵션을 사용하세요."},
    {"action": "목록 첨부 파일 삭제", "data_item_name": "sharepoint#deletelistitemattachment", "description": "올바른 정보가 입력되면 SharePoint의 목록 항목에서 첨부파일을 삭제합니다. 그래프 API에서는 '첨부파일 목록' 기능이 지원되지 않습니다. 대신 REST API 옵션을 사용하세요."},
    {"action": "목록 첨부 파일 다운로드", "data_item_name": "sharepoint#downloadlistattachment", "description": "SharePoint에서 목록 항목의 목록 첨부파일을 다운로드합니다. 그래프 API에서는 '첨부파일 목록' 기능이 지원되지 않습니다. 대신 REST API 옵션을 사용하세요."},
    {"action": "첨부 파일 업로드 목록", "data_item_name": "sharepoint#uplistattachment", "description": "목록 항목에 목록 첨부파일을 업로드합니다. 그래프 API에서는 '첨부파일 목록' 기능이 지원되지 않습니다. 대신 REST API 옵션을 사용하세요."},
]