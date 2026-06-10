# -*- coding: utf-8 -*-
PACKAGE_NAME        = "PGP"
PACKAGE_ID          = "command-group:pgp"
PACKAGE_DESCRIPTION = "보안을 위해 파일을 자동으로 암호화 및 해독합니다. 주요 액션: 키 생성(공개 및 비공개 암호화 키 쌍을 생성합니다.)、파일 암호 해독(암호화된 파일 및 폴더의 내용을 검색합니다.)、파일 암호화(안전하게 공유할 파일 및 폴더를 준비합니다.) (총 3개)."

ACTIONS = [
    {"action": "키 생성", "data_item_name": "pgp#createkey", "description": "공개 및 비공개 암호화 키 쌍을 생성합니다."},
    {"action": "파일 암호 해독", "data_item_name": "pgp#decrypt", "description": "암호화된 파일 및 폴더의 내용을 검색합니다."},
    {"action": "파일 암호화", "data_item_name": "pgp#encrypt", "description": "안전하게 공유할 파일 및 폴더를 준비합니다."},
]