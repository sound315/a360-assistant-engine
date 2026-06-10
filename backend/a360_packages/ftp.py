# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Ftp/Sftp"
PACKAGE_ID          = "command-group:ftp"
PACKAGE_DESCRIPTION = "FTP/SFTP 작업을 자동화합니다. 주요 액션: 폴더 변경(FTP/SFTP 서버의 상위 폴더 또는 특정 폴더로 이동합니다.)、연결(태스크 자동화에 사용할 FTP/SFTP 서버와의 연결을 설정합니다. 이...)、폴더 생성(FTP/SFTP 서버에 폴더를 생성합니다.)、폴더 삭제(FTP/SFTP 서버에서 폴더(그 안의 모든 하위 폴더 및 파일 포함)를...)、파일 삭제(FTP/SFTP 서버에서 파일을 제거합니다.) 외 6개."

ACTIONS = [
    {"action": "폴더 변경", "data_item_name": "ftp#changefolder", "description": "FTP/SFTP 서버의 상위 폴더 또는 특정 폴더로 이동합니다."},
    {"action": "연결", "data_item_name": "ftp#connectv2", "description": "태스크 자동화에 사용할 FTP/SFTP 서버와의 연결을 설정합니다. 이 작업은 FTP/SFTP 관련 태스크를 자동화하기 위해 사용하는 첫 번째 작업이어야 합니다."},
    {"action": "폴더 생성", "data_item_name": "ftp#createfolder", "description": "FTP/SFTP 서버에 폴더를 생성합니다."},
    {"action": "폴더 삭제", "data_item_name": "ftp#deletefolder", "description": "FTP/SFTP 서버에서 폴더(그 안의 모든 하위 폴더 및 파일 포함)를 제거합니다."},
    {"action": "파일 삭제", "data_item_name": "ftp#deletefiles", "description": "FTP/SFTP 서버에서 파일을 제거합니다."},
    {"action": "연결 끊기", "data_item_name": "ftp#disconnect", "description": "FTP/SFTP 서버에 대한 활성 연결을 종료합니다."},
    {"action": "폴더 가져오기", "data_item_name": "ftp#getfolder", "description": "FTP/SFTP 서버의 폴더를 클라이언트 시스템으로 다운로드합니다."},
    {"action": "파일 가져오기", "data_item_name": "ftp#getfiles", "description": "원격 FTP/SFTP 폴더에서 클라이언트 시스템의 특정 위치로 파일을 다운로드합니다."},
    {"action": "폴더 업로드", "data_item_name": "ftp#putfolder", "description": "클라이언트 시스템에서 FTP/SFTP 서버로 폴더를 업로드합니다."},
    {"action": "파일 업로드", "data_item_name": "ftp#putfiles", "description": "클라이언트 시스템에서 FTP/SFTP 서버로 하나 이상의 파일을 업로드합니다."},
    {"action": "파일 이름 바꾸기", "data_item_name": "ftp#renamefile", "description": "FTP/SFTP 서버의 파일 이름을 편집하거나 변경합니다."},
]