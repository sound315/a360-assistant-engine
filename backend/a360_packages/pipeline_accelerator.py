# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Pipeline Accelerator"
PACKAGE_ID          = "command-group:pipeline accelerator"
PACKAGE_DESCRIPTION = "Shibumi 포털에 연결하여 Pipeline Accelerator 관련 작업을 자동화합니다 주요 액션: 세션 종료(Pipeline Accelerator 세션을 닫습니다.)、메트릭 데이터 가져오기(지정된 메트릭에 대한 메트릭 데이터를 검색합니다.)、기회 가져오기(CoE Manager에서 지정된 워크스트림에 대한 모든 기회를 나열하고...)、기회 세부 정보 보기(CoE Manager에서 지정된 기회에 대한 모든 세부 정보를 검색하고...)、질문 레이블 가져오기(CoE Manager에서 엔터프라이즈에 대한 모든 객관적인 질문을 검색하...) 외 9개."

ACTIONS = [
    {"action": "세션 종료", "data_item_name": "pipeline accelerator#endpipelineacceleratorsession", "description": "Pipeline Accelerator 세션을 닫습니다."},
    {"action": "메트릭 데이터 가져오기", "data_item_name": "pipeline accelerator#metricsdata", "description": "지정된 메트릭에 대한 메트릭 데이터를 검색합니다."},
    {"action": "기회 가져오기", "data_item_name": "pipeline accelerator#getopportunities", "description": "CoE Manager에서 지정된 워크스트림에 대한 모든 기회를 나열하고 출력을 변수에 저장합니다."},
    {"action": "기회 세부 정보 보기", "data_item_name": "pipeline accelerator#opportunitydetails", "description": "CoE Manager에서 지정된 기회에 대한 모든 세부 정보를 검색하고 출력을 변수에 저장합니다."},
    {"action": "질문 레이블 가져오기", "data_item_name": "pipeline accelerator#getquestionlabels", "description": "CoE Manager에서 엔터프라이즈에 대한 모든 객관적인 질문을 검색하고 그 결과를 변수에 저장합니다."},
    {"action": "워크스트림 가져오기", "data_item_name": "pipeline accelerator#getworkstreams", "description": "CoE Manager에서 지정된 엔터프라이즈에 대한 워크스트림 목록을 검색하고 출력을 변수에 저장합니다."},
    {"action": "새로운 기회", "data_item_name": "pipeline accelerator#newopportunity", "description": "CoE Manager에서 지정된 엔터프라이즈 및 워크스트림에 기회를 만듭니다."},
    {"action": "새로운 워크스트림", "data_item_name": "pipeline accelerator#newworkstream", "description": "CoE Manager에서 새 워크스트림을 만듭니다."},
    {"action": "Pipeline Accelerator 세션 시작", "data_item_name": "pipeline accelerator#startpipelineaccelerator", "description": "Shibumi와 연결하고 상호작용할 수 있는 세션을 생성합니다."},
    {"action": "인스턴스 속성 업데이트", "data_item_name": "pipeline accelerator#updateinstanceattribute", "description": "CoE Manager에서 인스턴스 세부 정보를 업데이트합니다."},
    {"action": "Update metrics", "data_item_name": "pipeline accelerator#updatemetrics", "description": "Updates existing CoE Manager metrics with provided value(s)"},
    {"action": "기회 업데이트", "data_item_name": "pipeline accelerator#updateopportunity", "description": "CoE Manager의 기회 ID를 기준으로 기회 세부 정보를 업데이트합니다."},
    {"action": "프로세스 메트릭 업데이트", "data_item_name": "pipeline accelerator#updateprocessmetrics", "description": "제어실 메트릭을 기반으로 CoE Manager의 기존 프로세스 메트릭을 업데이트합니다."},
    {"action": "첨부 파일 업로드", "data_item_name": "pipeline accelerator#uploadattachment", "description": "기회 ID를 기준으로 기회에 대한 첨부 파일을 CoE Manager에 업로드합니다."},
]