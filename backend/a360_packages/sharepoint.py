# -*- coding: utf-8 -*-
PACKAGE_NAME        = "SharePoint"
PACKAGE_ID          = "command-group:sharepoint"
PACKAGE_DESCRIPTION = "SharePoint 사이트의 파일, 폴더 또는 목록 이벤트를 기반으로 워크플로를 자동화하는 작업 및 트리거. 주요 액션: 인증(SharePoint API를 통해 인증하여 액세스 토큰 생성)、인증 취소(세션에서 인증 컨텍스트 취소)、폴더 생성(올바른 정보를 입력하면 제공된 경로에 폴더를 생성합니다.)、폴더 삭제(올바른 정보를 입력하면 SharePoint에서 폴더를 삭제합니다.)、폴더 가져오기(올바른 입력값을 입력했다면 작업이 SharePoint에서 폴더 목록을 반...) 외 18개."

ACTIONS = [
    {"action": "인증", "data_item_name": "sharepoint#authentication", "description": "SharePoint API를 통해 인증하여 액세스 토큰 생성"},
    {"action": "인증 취소", "data_item_name": "sharepoint#revokeauthentication", "description": "세션에서 인증 컨텍스트 취소"},
    {"action": "폴더 생성", "data_item_name": "sharepoint#createfolder", "description": "올바른 정보를 입력하면 제공된 경로에 폴더를 생성합니다."},
    {"action": "폴더 삭제", "data_item_name": "sharepoint#deletefolder", "description": "올바른 정보를 입력하면 SharePoint에서 폴더를 삭제합니다."},
    {"action": "폴더 가져오기", "data_item_name": "sharepoint#listfolders", "description": "올바른 입력값을 입력했다면 작업이 SharePoint에서 폴더 목록을 반환해야 합니다."},
    {"action": "폴더 이름 변경", "data_item_name": "sharepoint#renamefolder", "description": "폴더 경로에 전달된 기존 폴더 이름을 새 폴더 이름으로 변경"},
    {"action": "파일 할당", "data_item_name": "sharepoint#assignfiletovariable", "description": "SharePoint 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "파일 삭제", "data_item_name": "sharepoint#deletefile", "description": "올바른 정보를 입력하면 SharePoint에서 파일을 삭제합니다."},
    {"action": "파일 다운로드", "data_item_name": "sharepoint#downloadfile", "description": "올바른 정보를 입력하면 제공된 대상 폴더에 파일을 다운로드합니다."},
    {"action": "파일 가져오기", "data_item_name": "sharepoint#listfiles", "description": "올바른 입력값을 입력했다면 SharePoint에서 파일 목록을 가져옵니다."},
    {"action": "파일 업로드", "data_item_name": "sharepoint#uploadfile", "description": "올바른 정보를 입력하면 제공된 경로에 파일을 생성합니다."},
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