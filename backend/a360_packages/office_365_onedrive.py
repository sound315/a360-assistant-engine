# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Microsoft 365 OneDrive"
PACKAGE_ID          = "command-group:office 365 onedrive"
PACKAGE_DESCRIPTION = "OneDrive 애플리케이션에서 반복 태스크를 자동화합니다. 주요 액션: 파일 할당(OneDrive 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다.)、권한 확인(OneDrive에서 지정 파일 또는 폴더에 대한 읽기 또는 쓰기 권한을...)、연결(OAuth2 인증으로 Microsoft 365 OneDrive에 연결하여...)、파일 또는 폴더 복사(OneDrive의 한 폴더에서 다른 폴더로 파일 또는 폴더를 복사합니다.)、폴더 생성(OneDrive의 특정 디렉터리에 폴더를 생성합니다.) 외 10개."

ACTIONS = [
    {"action": "파일 할당", "data_item_name": "office 365 onedrive#assignfiletovariable", "description": "OneDrive 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "권한 확인", "data_item_name": "office 365 onedrive#checkdriveitempermissions", "description": "OneDrive에서 지정 파일 또는 폴더에 대한 읽기 또는 쓰기 권한을 확인합니다."},
    {"action": "연결", "data_item_name": "office 365 onedrive#connect", "description": "OAuth2 인증으로 Microsoft 365 OneDrive에 연결하여 파일 및 폴더 작업을 수행합니다."},
    {"action": "파일 또는 폴더 복사", "data_item_name": "office 365 onedrive#copydriveitem", "description": "OneDrive의 한 폴더에서 다른 폴더로 파일 또는 폴더를 복사합니다."},
    {"action": "폴더 생성", "data_item_name": "office 365 onedrive#createdriveitem", "description": "OneDrive의 특정 디렉터리에 폴더를 생성합니다."},
    {"action": "파일 또는 폴더 삭제", "data_item_name": "office 365 onedrive#deletedriveitem", "description": "OneDrive의 특정 디렉터리에 있는 파일 또는 폴더를 삭제합니다."},
    {"action": "연결 끊기", "data_item_name": "office 365 onedrive#disconnect", "description": "OneDrive 애플리케이션에서 연결을 종료합니다."},
    {"action": "파일 다운로드", "data_item_name": "office 365 onedrive#downloaddriveitem", "description": "OneDrive의 특정 디렉터리에 있는 파일을 다운로드합니다."},
    {"action": "PDF로 내보내기", "data_item_name": "office 365 onedrive#exportaspdf", "description": "OneDrive의 기존 파일을 기기의 PDF로 내보냅니다."},
    {"action": "파일 및 폴더 찾기", "data_item_name": "office 365 onedrive#finddriveitem", "description": "OneDrive의 특정 디렉터리에 있는 파일 및 폴더를 찾습니다."},
    {"action": "파일 또는 폴더 정보 얻기", "data_item_name": "office 365 onedrive#getdriveitemdetails", "description": "OneDrive의 특정 파일 또는 폴더에 대한 정보를 검색합니다."},
    {"action": "파일 또는 폴더 이동", "data_item_name": "office 365 onedrive#movedriveitem", "description": "OneDrive의 한 폴더에서 다른 폴더로 파일을 이동합니다."},
    {"action": "파일 또는 폴더 이름 바꾸기", "data_item_name": "office 365 onedrive#renamedriveitem", "description": "OneDrive의 특정 디렉터리에 있는 파일 또는 폴더의 이름을 바꿉니다."},
    {"action": "마지막 버전 복원", "data_item_name": "office 365 onedrive#restoredriveitem", "description": "파일을 마지막 버전으로 복원합니다. 파일을 그 이전 버전으로 복원하면 현재 버전은 손실됩니다."},
    {"action": "파일 업로드", "data_item_name": "office 365 onedrive#uploadfileondrive", "description": "OneDrive의 특정 디렉터리에 있는 파일을 업로드합니다."},
]