# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Google Drive"
PACKAGE_ID          = "command-group:google drive"
PACKAGE_DESCRIPTION = "Google Drive의 파일 및 폴더에 대한 태스크를 자동화합니다. 주요 액션: 파일 할당(Google 드라이브 파일에 대한 파일 스트림을 열고 파일 변수에 할당합...)、권한 확인(Google Drive의 파일 또는 폴더에 대한 권한을 확인하고 목록 변...)、연결(Google 서버와의 연결을 설정합니다.)、파일 복사(Google Drive의 한 폴더에서 다른 폴더로 파일을 복사합니다.)、폴더 복사(Google Drive의 한 위치에서 다른 위치로 폴더를 복사합니다.) 외 15개."

ACTIONS = [
    {"action": "파일 할당", "data_item_name": "google drive#assignfile", "description": "Google 드라이브 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "권한 확인", "data_item_name": "google drive#checkpermissions", "description": "Google Drive의 파일 또는 폴더에 대한 권한을 확인하고 목록 변수에 대한 읽기, 쓰기 또는 삭제 권한을 반환합니다."},
    {"action": "연결", "data_item_name": "google drive#connect", "description": "Google 서버와의 연결을 설정합니다."},
    {"action": "파일 복사", "data_item_name": "google drive#copyfile", "description": "Google Drive의 한 폴더에서 다른 폴더로 파일을 복사합니다."},
    {"action": "폴더 복사", "data_item_name": "google drive#copyfolder", "description": "Google Drive의 한 위치에서 다른 위치로 폴더를 복사합니다."},
    {"action": "파일 권한 생성", "data_item_name": "google drive#createfilepermission", "description": "파일에 대한 새 권한을 만듭니다."},
    {"action": "폴더 생성...", "data_item_name": "google drive#createfolder", "description": "Google Drive에 폴더 생성"},
    {"action": "파일 삭제", "data_item_name": "google drive#deletefile", "description": "Google Drive에서 파일 삭제"},
    {"action": "파일 권한 삭제", "data_item_name": "google drive#deletefilepermission", "description": "파일에 대한 파일 권한을 삭제합니다."},
    {"action": "폴더 삭제", "data_item_name": "google drive#deletefolder", "description": "Google Drive에서 폴더를 삭제합니다."},
    {"action": "연결 끊기", "data_item_name": "google drive#disconnect", "description": "Google 서버와의 연결을 종료합니다."},
    {"action": "파일 다운로드", "data_item_name": "google drive#downloadfile", "description": "Google Drive에서 바탕 화면의 특정 위치로 파일을 다운로드합니다."},
    {"action": "파일/폴더 찾기", "data_item_name": "google drive#findfilesandfolders", "description": "Google Drive의 특정 디렉터리에서 파일 또는 폴더를 찾습니다."},
    {"action": "파일 정보 가져오기", "data_item_name": "google drive#getfileinformation", "description": "Google Drive에서 파일의 파일 정보를 검색합니다."},
    {"action": "파일 권한 가져오기", "data_item_name": "google drive#getfilepermission", "description": "Google Drive에서 파일 또는 폴더의 파일 권한을 검색합니다."},
    {"action": "파일 이동", "data_item_name": "google drive#movefile", "description": "Google Drive의 한 폴더에서 다른 폴더로 파일을 이동합니다."},
    {"action": "폴더 이동", "data_item_name": "google drive#movefolder", "description": "Google Drive의 한 위치에서 다른 위치로 폴더를 이동합니다."},
    {"action": "파일 이름 변경", "data_item_name": "google drive#renamefile", "description": "Google Drive에서 파일 이름 바꾸기"},
    {"action": "폴더 이름 변경", "data_item_name": "google drive#renamefolder", "description": "Google Drive의 특정 디렉터리에 있는 폴더 이름을 바꿉니다."},
    {"action": "파일 업로드", "data_item_name": "google drive#uploadfile", "description": "기기에서 Google Drive로 파일을 업로드합니다."},
]