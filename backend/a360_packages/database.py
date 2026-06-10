# -*- coding: utf-8 -*-
PACKAGE_NAME        = "데이터베이스"
PACKAGE_ID          = "command-group:database"
PACKAGE_DESCRIPTION = "데이터베이스에 연결하여 트랜잭션을 시작하고 저장된 데이터를 관리합니다. 주요 액션: 대량 삽입(소스 파일에서 데이터를 읽고 대상 데이터베이스 테이블에 삽입합니다.)、데이터베이스 트랜잭션 시작(데이터베이스 트랜잭션 종료까지 모든 데이터베이스 동작을 커밋할 데이터베이...)、데이터베이스 트랜잭션 종료(Bot이 해당 작업을 성공적으로 실행한 조건에서 데이터베이스 트랜잭션 시...)、연결(데이터베이스 관련 작업을 자동화하는 데 사용할 데이터베이스 서버와의 연결...)、연결 끊기(데이터베이스에서 연결을 끊습니다. 세션 이름에는 연결 작업에서 사용한 세...) 외 6개."

ACTIONS = [
    {"action": "대량 삽입", "data_item_name": "database#batchinsert", "description": "소스 파일에서 데이터를 읽고 대상 데이터베이스 테이블에 삽입합니다."},
    {"action": "데이터베이스 트랜잭션 시작", "data_item_name": "database#begin", "description": "데이터베이스 트랜잭션 종료까지 모든 데이터베이스 동작을 커밋할 데이터베이스 트랜잭션을 시작합니다. 트랜잭션 시작과 종료 사이의 작업에 삽입된 작업은 단일 단위로 처리됩니다."},
    {"action": "데이터베이스 트랜잭션 종료", "data_item_name": "database#commit", "description": "Bot이 해당 작업을 성공적으로 실행한 조건에서 데이터베이스 트랜잭션 시작 작업 후의 작업으로 수행된 모든 데이터베이스 작업을 커밋합니다."},
    {"action": "연결", "data_item_name": "database#connect", "description": "데이터베이스 관련 작업을 자동화하는 데 사용할 데이터베이스 서버와의 연결을 설정합니다."},
    {"action": "연결 끊기", "data_item_name": "database#disconnect", "description": "데이터베이스에서 연결을 끊습니다. 세션 이름에는 연결 작업에서 사용한 세션 이름을 입력합니다."},
    {"action": "읽기 원본", "data_item_name": "database#sqlquery", "description": "데이터베이스에서 기록을 검색하여 CSV 파일에 검색된 데이터를 저장합니다."},
    {"action": "저장된 절차 실행", "data_item_name": "database#store", "description": "데이터베이스로부터 저장된 절차를 실행합니다. 저장된 절차는 데이터베이스에서 생성되어 저장된 일련의 SQL 명령문입니다."},
    {"action": "데이터 테이블로 내보내기", "data_item_name": "database#exporttodatatable", "description": "데이터베이스에서 기록을 검색해 테이블 변수에 검색된 데이터를 저장합니다."},
    {"action": "파일 스트림으로 내보내기", "data_item_name": "database#exporttofilestream", "description": "데이터베이스에서 데이터를 읽고 결과를 파일 스트림 변수로 내보냅니다."},
    {"action": "저장된 절차 관리", "data_item_name": "database#createupdatedelete", "description": "지정된 데이터베이스 내에서 저장된 절차를 생성하고, 업데이트하고, 삭제합니다."},
    {"action": "삽입/업데이트/삭제", "data_item_name": "database#insertupdatedelete", "description": "데이터베이스에서 'INSERT', 'UPDATE' 또는 'DELETE' 명령문을 실행합니다."},
]