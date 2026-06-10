# -*- coding: utf-8 -*-
PACKAGE_NAME        = "폴더"
PACKAGE_ID          = "command-group:folder"
PACKAGE_DESCRIPTION = "폴더 관련 작업을 자동화합니다. 주요 액션: 압축(파일 및 폴더를 .zip 형식으로 압축합니다.)、복사(기존 폴더를 지정된 위치에 복사합니다.)、생성(지정된 위치에 폴더를 생성합니다.)、압축 해제(압축된 콘텐츠(파일 및 폴더)를 .zip 파일에서 지정된 위치로 추출합니...)、삭제(지정된 위치에서 폴더를 제거합니다.) 외 4개."

ACTIONS = [
    {"action": "압축", "data_item_name": "folder#zipfiles", "description": "파일 및 폴더를 .zip 형식으로 압축합니다."},
    {"action": "복사", "data_item_name": "folder#copyfolder", "description": "기존 폴더를 지정된 위치에 복사합니다."},
    {"action": "생성", "data_item_name": "folder#createfolder", "description": "지정된 위치에 폴더를 생성합니다."},
    {"action": "압축 해제", "data_item_name": "folder#unzipfiles", "description": "압축된 콘텐츠(파일 및 폴더)를 .zip 파일에서 지정된 위치로 추출합니다."},
    {"action": "삭제", "data_item_name": "folder#deletefolder", "description": "지정된 위치에서 폴더를 제거합니다."},
    {"action": "바로가기 생성", "data_item_name": "folder#createshortcut", "description": "지정된 위치에 폴더의 바로 가기를 만듭니다. 폴더 바로 가기는 원본 폴더를 기준으로 하므로 원본 폴더에 대한 변경 사항이 바로 가기에도 적용됩니다."},
    {"action": "열기", "data_item_name": "folder#openfolder", "description": "지정된 위치에서 폴더를 엽니다."},
    {"action": "이름 바꾸기", "data_item_name": "folder#renamefolder", "description": "기존 폴더의 이름을 바꿉니다."},
    {"action": "심볼릭 링크 생성", "data_item_name": "folder#createfoldershortcut", "description": "지정된 위치의 폴더에 대한 기호 링크를 만듭니다. 이 링크는 원본 폴더를 기준으로 하므로 원본 폴더에 대한 변경 사항이 링크에도 적용됩니다."},
]