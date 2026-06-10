# -*- coding: utf-8 -*-
PACKAGE_NAME        = "REST Web Services"
PACKAGE_ID          = "command-group:rest"
PACKAGE_DESCRIPTION = "DELETE, GET, PATCH, POST 또는 PUT과 같은 메서드를 사용하여 API에 요청을 보내고 API에서 응답을 받습니다. 주요 액션: 삭제 방법(URI에 의해 식별된 리소스를 삭제합니다.)、가져오기 방법(URI에 포함되어 있는 매개변수가 식별한 정보를 검색합니다. 모든 매개변...)、파일 스트림 가져오기(URI 매개변수를 사용하여 파일 스트림 리소스를 검색하고 파일 변수를 할...)、Patch 메소드(URI에 의해 식별되는 리소스를 수정합니다.)、Post 메소드(URI에 새 리소스를 생성합니다. 매개변수는 요청 본문에 전달되며 요청...) 외 1개."

ACTIONS = [
    {"action": "삭제 방법", "data_item_name": "rest#restdelete", "description": "URI에 의해 식별된 리소스를 삭제합니다."},
    {"action": "가져오기 방법", "data_item_name": "rest#restget", "description": "URI에 포함되어 있는 매개변수가 식별한 정보를 검색합니다. 모든 매개변수는 URI의 일부로 전달되므로 이 메서드에는 콘텐츠 유형이 없습니다."},
    {"action": "파일 스트림 가져오기", "data_item_name": "rest#restgetfilestream", "description": "URI 매개변수를 사용하여 파일 스트림 리소스를 검색하고 파일 변수를 할당합니다."},
    {"action": "Patch 메소드", "data_item_name": "rest#restpatch", "description": "URI에 의해 식별되는 리소스를 수정합니다."},
    {"action": "Post 메소드", "data_item_name": "rest#restpost", "description": "URI에 새 리소스를 생성합니다. 매개변수는 요청 본문에 전달되며 요청 본문의 길이에는 제한이 없습니다."},
    {"action": "Put 메소드", "data_item_name": "rest#restput", "description": "URI 또는 본문에 전달된 매개변수에 따라 리소스를 업데이트하거나 바꿉니다."},
]