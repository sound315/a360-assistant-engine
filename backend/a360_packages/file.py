# -*- coding: utf-8 -*-
PACKAGE_NAME        = "파일"
PACKAGE_ID          = "command-group:file"
PACKAGE_DESCRIPTION = "다양한 파일 관련 작업을 자동화합니다. 주요 액션: 지정(파일 변수를 사용자 지정 파일 변수에 할당합니다.)、복사(데스크톱에서 다른 위치로 파일을 복사합니다.)、생성(새 파일을 생성합니다.)、삭제(파일을 삭제합니다.)、컨트롤룸 파일 다운로드(Control Room 파일을 특정 위치에 복사합니다.) 외 8개."

ACTIONS = [
    {"action": "지정", "data_item_name": "file#assign", "description": "파일 변수를 사용자 지정 파일 변수에 할당합니다."},
    {"action": "복사", "data_item_name": "file#copyfiles", "description": "데스크톱에서 다른 위치로 파일을 복사합니다."},
    {"action": "생성", "data_item_name": "file#createfile", "description": "새 파일을 생성합니다."},
    {"action": "삭제", "data_item_name": "file#deletefiles", "description": "파일을 삭제합니다."},
    {"action": "컨트롤룸 파일 다운로드", "data_item_name": "file#downloadto", "description": "Control Room 파일을 특정 위치에 복사합니다."},
    {"action": "이름 가져오기", "data_item_name": "file#getname", "description": "파일의 이름을 검색합니다."},
    {"action": "경로 가져오기", "data_item_name": "file#getpath", "description": "파일의 경로를 검색합니다."},
    {"action": "열기", "data_item_name": "file#openfile", "description": "기존 파일을 엽니다."},
    {"action": "인쇄", "data_item_name": "file#printfile", "description": "지정된 파일을 인쇄합니다."},
    {"action": "여러 파일 인쇄", "data_item_name": "file#printmultiplefiles", "description": "여러 파일을 인쇄합니다."},
    {"action": "이름 바꾸기", "data_item_name": "file#renamefiles", "description": "파일 이름을 바꿉니다."},
    {"action": "바로가기 생성", "data_item_name": "file#createshortcut", "description": "대상 파일에 대한 바로 가기를 만듭니다."},
    {"action": "기호 링크 생성", "data_item_name": "file#createfileshortcut", "description": "대상 파일에 대한 기호 링크를 생성합니다."},
]