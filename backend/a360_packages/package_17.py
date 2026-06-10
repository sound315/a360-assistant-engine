# -*- coding: utf-8 -*-
PACKAGE_NAME        = "폴더 및 파일"
PACKAGE_ID          = "폴더 및 파일"
PACKAGE_DESCRIPTION = "주요 액션: 폴더 생성(올바른 정보를 입력하면 제공된 경로에 폴더를 생성합니다.)、폴더 삭제(올바른 정보를 입력하면 SharePoint에서 폴더를 삭제합니다.)、폴더 가져오기(올바른 입력값을 입력했다면 작업이 SharePoint에서 폴더 목록을 반...)、폴더 이름 변경(폴더 경로에 전달된 기존 폴더 이름을 새 폴더 이름으로 변경)、파일 할당(SharePoint 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니...) 외 4개."

ACTIONS = [
    {"action": "폴더 생성", "data_item_name": "sharepoint#createfolder", "description": "올바른 정보를 입력하면 제공된 경로에 폴더를 생성합니다."},
    {"action": "폴더 삭제", "data_item_name": "sharepoint#deletefolder", "description": "올바른 정보를 입력하면 SharePoint에서 폴더를 삭제합니다."},
    {"action": "폴더 가져오기", "data_item_name": "sharepoint#listfolders", "description": "올바른 입력값을 입력했다면 작업이 SharePoint에서 폴더 목록을 반환해야 합니다."},
    {"action": "폴더 이름 변경", "data_item_name": "sharepoint#renamefolder", "description": "폴더 경로에 전달된 기존 폴더 이름을 새 폴더 이름으로 변경"},
    {"action": "파일 할당", "data_item_name": "sharepoint#assignfiletovariable", "description": "SharePoint 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "파일 삭제", "data_item_name": "sharepoint#deletefile", "description": "올바른 정보를 입력하면 SharePoint에서 파일을 삭제합니다."},
    {"action": "파일 다운로드", "data_item_name": "sharepoint#downloadfile", "description": "올바른 정보를 입력하면 제공된 대상 폴더에 파일을 다운로드합니다."},
    {"action": "파일 가져오기", "data_item_name": "sharepoint#listfiles", "description": "올바른 입력값을 입력했다면 SharePoint에서 파일 목록을 가져옵니다."},
    {"action": "파일 업로드", "data_item_name": "sharepoint#uploadfile", "description": "올바른 정보를 입력하면 제공된 경로에 파일을 생성합니다."},
]