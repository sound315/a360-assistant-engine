# -*- coding: utf-8 -*-
PACKAGE_NAME        = "문서 추출"
PACKAGE_ID          = "command-group:document-extraction"
PACKAGE_DESCRIPTION = "문서에서 데이터를 추출하고 해당 데이터를 다운로드합니다. 이 패키지는 Document Automation에서 문서를 처리하는 데 사용됩니다. 주요 액션: 문서 데이터 가져오기(사전이나 JSON과 같은 사용자 친화적인 형식으로 문서 데이터 검색)、문서 데이터 업데이트(이 작업은 사전/JSON에 대한 사용자 수정 사항을 기반으로 문서 데이터...)、데이터 다운로드(성공적으로 처리된 문서에서 추출된 데이터 다운로드)、데이터 추출(업로드된 문서를 처리하여 데이터 추출) (총 4개)."

ACTIONS = [
    {"action": "문서 데이터 가져오기", "data_item_name": "document-extraction#getdocumentdata", "description": "사전이나 JSON과 같은 사용자 친화적인 형식으로 문서 데이터 검색"},
    {"action": "문서 데이터 업데이트", "data_item_name": "document-extraction#updatedocumentdata", "description": "이 작업은 사전/JSON에 대한 사용자 수정 사항을 기반으로 문서 데이터를 업데이트합니다."},
    {"action": "데이터 다운로드", "data_item_name": "document-extraction#downloadcommand", "description": "성공적으로 처리된 문서에서 추출된 데이터 다운로드"},
    {"action": "데이터 추출", "data_item_name": "document-extraction#extractioncommand", "description": "업로드된 문서를 처리하여 데이터 추출"},
]