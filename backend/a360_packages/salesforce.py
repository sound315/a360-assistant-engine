# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Salesforce"
PACKAGE_ID          = "command-group:salesforce"
PACKAGE_DESCRIPTION = "Salesforce는 소프트웨어 및 서비스를 제공하여 관련 고객 경험을 생성하는 클라우드 기반 플랫폼입니다. 주요 액션: 파일 할당(Salesforce 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니...)、인증(Salesforce 인증은 Salesforce를 사용하여 인증을 받기 위...)、레코드 삭제(Salesforce 레코드 삭제 작업을 사용하여 Salesforce에서...)、첨부 파일 가져오기(파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다.)、SOQL 실행(Salesforce 데이터에서 특정 정보를 검색하려면 Salesforce...) 외 6개."

ACTIONS = [
    {"action": "파일 할당", "data_item_name": "salesforce#assignfiletovariable", "description": "Salesforce 파일에 대한 파일 스트림을 열고 파일 변수에 할당합니다."},
    {"action": "인증", "data_item_name": "salesforce#authentication", "description": "Salesforce 인증은 Salesforce를 사용하여 인증을 받기 위해 호출해야 하는 첫 번째 명령 작업입니다."},
    {"action": "레코드 삭제", "data_item_name": "salesforce#delete_record", "description": "Salesforce 레코드 삭제 작업을 사용하여 Salesforce에서 레코드를 삭제합니다."},
    {"action": "첨부 파일 가져오기", "data_item_name": "salesforce#download_file_attachment", "description": "파일과 함께 첨부파일 메타데이터를 대상 폴더에 다운로드합니다."},
    {"action": "SOQL 실행", "data_item_name": "salesforce#execute_soql", "description": "Salesforce 데이터에서 특정 정보를 검색하려면 Salesforce SOQL 실행 작업을 사용하여 Automation 360에서 Salesforce SOQL(객체 쿼리 언어) 명령을 실행합니다."},
    {"action": "레코드 가져오기", "data_item_name": "salesforce#get_record", "description": "Salesforce 레코드 가져오기 작업은 Salesforce 객체의 필드를 읽는 데 사용됩니다."},
    {"action": "레코드 삽입", "data_item_name": "salesforce#insert_record", "description": "Salesforce 레코드 삽입 작업을 사용하여 객체의 필드에 매핑되어야 하는 필드 값과 함께 Salesforce 객체에 새 레코드를 삽입합니다."},
    {"action": "인증 취소", "data_item_name": "salesforce#revokeauthentication", "description": "세션에서 인증 컨텍스트 취소"},
    {"action": "레코드 업데이트", "data_item_name": "salesforce#update_record", "description": "Salesforce 레코드 업데이트 작업을 사용하여 Salesforce 객체의 필드를 업데이트합니다."},
    {"action": "첨부 파일 업로드", "data_item_name": "salesforce#upload_file_attachment", "description": "Salesforce 첨부 파일 업로드 작업을 사용하여 Salesforce의 레코드에 파일을 업로드할 수 있습니다."},
    {"action": "Upsert 레코드(외부 ID 사용)", "data_item_name": "salesforce#upsert_record_using_external_id", "description": "Salesforce 레코드 upsert 작업을 사용하여 레코드를 삽입하거나 업데이트합니다. Upsert 작업은 사용자 지정 외부 ID를 키로 사용하여 레코드를 식별합니다."},
]