# -*- coding: utf-8 -*-
PACKAGE_NAME        = "이메일"
PACKAGE_ID          = "command-group:email"
PACKAGE_DESCRIPTION = "EWS, Microsoft Outlook 및 기타 이메일 서버를 통해 이메일 관련 태스크를 자동화합니다. 주요 액션: 상태 변경(이메일 상태를 읽음/읽지 않음으로 변경 루프 안에서 이 동작 사용)、폴더가 존재하는지 확인(주어진 이름의 폴더가 존재하는지 확인하고 결과(참/거짓)를 부울 변수로...)、모두 삭제(메일 서버에서 읽은 이메일, 읽지 않은 이메일 또는 모든 이메일을 삭제합...)、삭제(단일 이메일을 삭제합니다. 루프 안에서 이 작업을 사용합니다.)、연결 끊기(이메일 서버와의 연결 닫기) 외 10개."

ACTIONS = [
    {"action": "상태 변경", "data_item_name": "email#changestatus", "description": "이메일 상태를 읽음/읽지 않음으로 변경 루프 안에서 이 동작 사용"},
    {"action": "폴더가 존재하는지 확인", "data_item_name": "email#checkfolder", "description": "주어진 이름의 폴더가 존재하는지 확인하고 결과(참/거짓)를 부울 변수로 반환"},
    {"action": "모두 삭제", "data_item_name": "email#deleteall", "description": "메일 서버에서 읽은 이메일, 읽지 않은 이메일 또는 모든 이메일을 삭제합니다."},
    {"action": "삭제", "data_item_name": "email#deletemessage", "description": "단일 이메일을 삭제합니다. 루프 안에서 이 작업을 사용합니다."},
    {"action": "연결 끊기", "data_item_name": "email#closeemail", "description": "이메일 서버와의 연결 닫기"},
    {"action": "연결", "data_item_name": "email#emailconnect", "description": "연결 작업을 사용하여 이메일 서버와 연결을 설정합니다. 이메일 관련 작업을 자동화려면 이 작업을 가장 먼저 사용해야 합니다."},
    {"action": "전달", "data_item_name": "email#forwardemailv2", "description": "동일한 제목의 이메일을 전달합니다. 루프 안에서 이 작업을 사용합니다."},
    {"action": "모두 이동", "data_item_name": "email#moveemail", "description": "모든 이메일 메시지를 지정된 폴더로 이동합니다"},
    {"action": "이동", "data_item_name": "email#move", "description": "단일 이메일을 이동합니다. 루프 내에서 이 작업을 사용합니다."},
    {"action": "전체 회신", "data_item_name": "email#replyallemail", "description": "제목이 같거나 수정된 이메일의 발신자와 모든 수신자에게 답장을 보냅니다."},
    {"action": "회신", "data_item_name": "email#replyemailv2", "description": "동일한 제목으로 이메일 발신자에게 회신합니다. 루프 안에서 이 작업을 사용합니다."},
    {"action": "모든 첨부파일 저장", "data_item_name": "email#saveallatatchments", "description": "특정 서버로부터 여러 이메일의 모든 첨부파일 저장"},
    {"action": "첨부파일 저장", "data_item_name": "email#saveattachment", "description": "한 이메일의 첨부 파일을 지정된 폴더에 저장합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "이메일 저장", "data_item_name": "email#saveemailv2", "description": "단일 이메일을 저장합니다. 루프 안에서 이 동작 사용"},
    {"action": "보내기", "data_item_name": "email#sendmailv2", "description": "이메일 전송"},
]