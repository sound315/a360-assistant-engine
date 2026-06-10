# -*- coding: utf-8 -*-
PACKAGE_NAME        = "GitHub"
PACKAGE_ID          = "command-group:github"
PACKAGE_DESCRIPTION = "GitHub에 연결하여 리포지토리, 이슈, 풀 리퀘스트 및 브랜치를 관리하세요. 주요 액션: 코멘트 추가(지정된 이슈 또는 풀 리퀘스트에 댓글을 추가하거나 GitHub 리포지토리...)、연결(Github에서 보안 세션을 설정합니다.)、이슈 만들기(리포지토리에서 새 이슈 만들기)、풀 리퀘스트 생성(리포지토리에서 새 풀 리퀘스트 만들기)、연결 끊기(Github 세션을 종료합니다.) 외 9개."

ACTIONS = [
    {"action": "코멘트 추가", "data_item_name": "github#addcomment", "description": "지정된 이슈 또는 풀 리퀘스트에 댓글을 추가하거나 GitHub 리포지토리에 풀 리퀘스트를 추가하세요."},
    {"action": "연결", "data_item_name": "github#connect", "description": "Github에서 보안 세션을 설정합니다."},
    {"action": "이슈 만들기", "data_item_name": "github#createissue", "description": "리포지토리에서 새 이슈 만들기"},
    {"action": "풀 리퀘스트 생성", "data_item_name": "github#createpullrequest", "description": "리포지토리에서 새 풀 리퀘스트 만들기"},
    {"action": "연결 끊기", "data_item_name": "github#disconnect", "description": "Github 세션을 종료합니다."},
    {"action": "이슈 받기", "data_item_name": "github#getissue", "description": "GitHub 리포지토리에서 특정 이슈에 대한 자세한 정보를 검색합니다."},
    {"action": "풀 리퀘스트 받기", "data_item_name": "github#getpullrequest", "description": "풀 리퀘스트에 대한 자세한 정보를 검색합니다."},
    {"action": "리포지토리 가져오기", "data_item_name": "github#getrepository", "description": "GitHub 리포지토리에 대한 자세한 정보를 검색합니다."},
    {"action": "지점 목록", "data_item_name": "github#listbranches", "description": "GitHub 리포지토리에 있는 모든 브랜치를 나열합니다."},
    {"action": "문제 목록", "data_item_name": "github#listissues", "description": "GitHub 리포지토리의 모든 이슈를 나열합니다."},
    {"action": "풀 리퀘스트 목록", "data_item_name": "github#listpullrequests", "description": "GitHub 리포지토리에서 풀 리퀘스트를 나열합니다."},
    {"action": "리포지토리 목록", "data_item_name": "github#listrepositories", "description": "지정된 GitHub 소유자에 대한 리포지토리를 나열합니다."},
    {"action": "풀 리퀘스트 병합", "data_item_name": "github#mergepullrequest", "description": "리포지토리에서 풀 리퀘스트를 병합합니다."},
    {"action": "업데이트 문제", "data_item_name": "github#updateissue", "description": "새로운 세부 정보로 GitHub 이슈를 업데이트하세요."},
]