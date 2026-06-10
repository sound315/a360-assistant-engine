# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Microsoft 365 Outlook"
PACKAGE_ID          = "command-group:microsoft 365 outlook"
PACKAGE_DESCRIPTION = "Exchange Server에 연결하여 이메일 작업을 수행하는 데 사용할 수 있는 작업을 제공합니다. 주요 액션: 첨부 파일 지정(이메일의 첨부 파일을 파일 변수에 할당합니다)、상태 변경(이메일의 상태를 읽음 또는 읽지 않음으로 변경합니다. 루프 작업 내에서...)、폴더가 존재하는지 확인(지정한 이름의 폴더가 Microsoft 365 Outlook 서버에 있는...)、연결(이메일 작업을 수행하기 위해 OAuth2 인증으로 Microsoft 36...)、삭제(Microsoft 365 Outlook 서버의 받은 편지함에서 지정된 이...) 외 11개."

ACTIONS = [
    {"action": "첨부 파일 지정", "data_item_name": "microsoft 365 outlook#assignattachments", "description": "이메일의 첨부 파일을 파일 변수에 할당합니다"},
    {"action": "상태 변경", "data_item_name": "microsoft 365 outlook#changestatus", "description": "이메일의 상태를 읽음 또는 읽지 않음으로 변경합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "폴더가 존재하는지 확인", "data_item_name": "microsoft 365 outlook#checkiffolderexists", "description": "지정한 이름의 폴더가 Microsoft 365 Outlook 서버에 있는지 확인합니다."},
    {"action": "연결", "data_item_name": "microsoft 365 outlook#connect", "description": "이메일 작업을 수행하기 위해 OAuth2 인증으로 Microsoft 365 Outlook 서버에 연결합니다."},
    {"action": "삭제", "data_item_name": "microsoft 365 outlook#delete", "description": "Microsoft 365 Outlook 서버의 받은 편지함에서 지정된 이메일을 삭제합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "모두 삭제", "data_item_name": "microsoft 365 outlook#deleteall", "description": "Microsoft 365 Outlook 서버의 필터에서 읽은 이메일, 읽지 않은 이메일 또는 지정된 이메일을 삭제합니다."},
    {"action": "연결 끊기", "data_item_name": "microsoft 365 outlook#disconnect", "description": "Microsoft 365 Outlook 서버와의 연결을 종료합니다."},
    {"action": "전달", "data_item_name": "microsoft 365 outlook#forward", "description": "이메일 및 첨부 파일을 한 명 이상의 수신자에게 전달합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "이동", "data_item_name": "microsoft 365 outlook#move", "description": "Microsoft 365 Outlook 서버의 한 폴더에서 다른 폴더로 이메일을 이동합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "모두 이동", "data_item_name": "microsoft 365 outlook#moveall", "description": "Microsoft 365 Outlook 서버의 한 폴더에서 다른 폴더로 모든 이메일을 이동합니다."},
    {"action": "회신", "data_item_name": "microsoft 365 outlook#reply", "description": "같은 제목으로 이메일에 답장을 보냅니다. 루프 작업 내에서 이 작업을 사용합니다. 원본 이메일에 첨부된 파일은 포함되지 않습니다."},
    {"action": "전체 회신", "data_item_name": "microsoft 365 outlook#replyall", "description": "이메일의 발신자와 모든 수신자에게 답장을 보냅니다. 루프 작업 내에서 이 작업을 사용합니다. 원본 이메일에 첨부된 파일은 포함되지 않습니다."},
    {"action": "모든 첨부파일 저장", "data_item_name": "microsoft 365 outlook#saveallattachments", "description": "지정된 모든 이메일의 첨부 파일을 지정된 폴더에 저장합니다."},
    {"action": "첨부파일 저장", "data_item_name": "microsoft 365 outlook#saveattachments", "description": "한 이메일의 첨부 파일을 지정된 폴더에 저장합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "이메일 저장", "data_item_name": "microsoft 365 outlook#saveemail", "description": "이메일 메시지를 폴더에 저장합니다. 루프 작업 내에서 이 작업을 사용합니다."},
    {"action": "보내기", "data_item_name": "microsoft 365 outlook#send", "description": "한 명 이상의 수신자에게 이메일을 보냅니다."},
]