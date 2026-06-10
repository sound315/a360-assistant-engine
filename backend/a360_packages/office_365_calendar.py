# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Microsoft 365 캘린더"
PACKAGE_ID          = "command-group:office 365 calendar"
PACKAGE_DESCRIPTION = "Office 365 캘린더에서 회의 관련 태스크를 자동화합니다. 주요 액션: 첨부 파일 추가(회의에 하나 이상의 첨부 파일을 추가합니다.)、참석자 추가(한 명 이상의 참석자를 회의에 추가하고 참석이 필수인지 선택 사항인지 지...)、회의 취소(회의를 취소합니다.)、연결(OAuth2 인증으로 Microsoft 365 Calendar에 연결하여...)、회의 생성(회의 안건, 첨부 파일, 참석자, 기간, 장소, 반복 및 회의 제목을 지...) 외 6개."

ACTIONS = [
    {"action": "첨부 파일 추가", "data_item_name": "office 365 calendar#addattachment", "description": "회의에 하나 이상의 첨부 파일을 추가합니다."},
    {"action": "참석자 추가", "data_item_name": "office 365 calendar#addattendee", "description": "한 명 이상의 참석자를 회의에 추가하고 참석이 필수인지 선택 사항인지 지정합니다."},
    {"action": "회의 취소", "data_item_name": "office 365 calendar#cancelmeeting", "description": "회의를 취소합니다."},
    {"action": "연결", "data_item_name": "office 365 calendar#connect", "description": "OAuth2 인증으로 Microsoft 365 Calendar에 연결하여 캘린더 작업을 수행합니다."},
    {"action": "회의 생성", "data_item_name": "office 365 calendar#createmeeting", "description": "회의 안건, 첨부 파일, 참석자, 기간, 장소, 반복 및 회의 제목을 지정합니다. 런타임 동안 회의 참석자에게 초대 이메일이 전송됩니다."},
    {"action": "참석자 삭제", "data_item_name": "office 365 calendar#deleteattendee", "description": "회의에서 참석자를 제거합니다."},
    {"action": "회의 정보 삭제", "data_item_name": "office 365 calendar#deletemeetinginformation", "description": "제목, 장소 등 회의와 관련된 정보를 삭제합니다."},
    {"action": "연결 끊기", "data_item_name": "office 365 calendar#disconnect", "description": "Office 365 애플리케이션에서 연결을 종료합니다."},
    {"action": "사용 가능한 회의 슬롯 확보", "data_item_name": "office 365 calendar#getavailablemeetingslots", "description": "지정된 날짜 및 시간 범위에서 참석자가 참석할 수 있는 시간 슬롯을 검색합니다. 시간대 간 예약이 지원됩니다."},
    {"action": "회의 수정", "data_item_name": "office 365 calendar#modifymeeting", "description": "회의 정보를 수정합니다."},
    {"action": "회의에 응답", "data_item_name": "office 365 calendar#respondtomeeting", "description": "수락, 거부 또는 미정으로 회의에 응답합니다."},
]