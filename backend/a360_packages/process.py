# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Process Composer"
PACKAGE_ID          = "command-group:process"
PACKAGE_DESCRIPTION = "Automation 360 Process Composer용 작업 제공 주요 액션: 휴먼 태스크 할당(휴먼 태스크를 사용자에게 할당합니다)、휴먼 태스크 취소(휴먼 태스크 취소)、요청 생성(초기 입력이 있는 프로세스에서 요청을 생성합니다)、스토리지 파일 가져오기(스토리지 파일을 Bot 기기로 다운로드합니다)、Get Storage file V2(Open a file stream for a Storage file an...) 외 5개."

ACTIONS = [
    {"action": "휴먼 태스크 할당", "data_item_name": "process#assigntask", "description": "휴먼 태스크를 사용자에게 할당합니다"},
    {"action": "휴먼 태스크 취소", "data_item_name": "process#canceltask", "description": "휴먼 태스크 취소"},
    {"action": "요청 생성", "data_item_name": "process#createrequestv2", "description": "초기 입력이 있는 프로세스에서 요청을 생성합니다"},
    {"action": "스토리지 파일 가져오기", "data_item_name": "process#getstoragefile", "description": "스토리지 파일을 Bot 기기로 다운로드합니다"},
    {"action": "Get Storage file V2", "data_item_name": "process#getstoragefilev2", "description": "Open a file stream for a Storage file and assign it to a file variable."},
    {"action": "요청 쿼리", "data_item_name": "process#queryrequest", "description": "필터를 사용한 쿼리 요청"},
    {"action": "휴먼 태스크 쿼리", "data_item_name": "process#queryhumantask", "description": "필터로 원하는 휴먼 태스크를 가져옵니다"},
    {"action": "팀원", "data_item_name": "process#teammembers", "description": "팀원을 받습니다"},
    {"action": "스토리지 파일 업로드", "data_item_name": "process#uploadstoragefile", "description": "스토리지 파일을 Bot 기기에 업로드"},
    {"action": "Upload Storage file V2", "data_item_name": "process#uploadstoragefilev2", "description": "Upload file Stream to Storage"},
]