# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Excel 기본"
PACKAGE_ID          = "command-group:excel"
PACKAGE_DESCRIPTION = "장치에서 Microsoft Excel을 사용할 수 없는 경우 xlsx 통합 문서에서 스프레드시트 작업을 자동화합니다. 주요 액션: 닫기(Excel 스프레드시트를 닫고 파일을 닫을 때 변경 사항을 저장합니다.)、셀 삭제(현재 워크시트에서 활성 셀 또는 특정 셀을 삭제합니다.)、찾기(Microsoft Excel 스프레드시트에서 값을 찾습니다.)、여러 셀 가져오기(Microsoft Excel 스프레드시트의 셀에서 값을 검색하여 테이블...)、단일 셀 가져오기(Microsoft Excel 스프레드시트의 단일 셀에서 값을 검색하여 문...) 외 9개."

ACTIONS = [
    {"action": "닫기", "data_item_name": "excel#closespreadsheet", "description": "Excel 스프레드시트를 닫고 파일을 닫을 때 변경 사항을 저장합니다."},
    {"action": "셀 삭제", "data_item_name": "excel#deletecells", "description": "현재 워크시트에서 활성 셀 또는 특정 셀을 삭제합니다."},
    {"action": "찾기", "data_item_name": "excel#find", "description": "Microsoft Excel 스프레드시트에서 값을 찾습니다."},
    {"action": "여러 셀 가져오기", "data_item_name": "excel#getmultiplecells", "description": "Microsoft Excel 스프레드시트의 셀에서 값을 검색하여 테이블 변수에 저장합니다."},
    {"action": "단일 셀 가져오기", "data_item_name": "excel#getsinglecell", "description": "Microsoft Excel 스프레드시트의 단일 셀에서 값을 검색하여 문자열 변수에 저장합니다."},
    {"action": "셀 주소 가져오기", "data_item_name": "excel#getsinglecelladdress", "description": "활성 셀 위치를 검색하여 문자열 변수에 저장합니다."},
    {"action": "열 이름 가져오기", "data_item_name": "excel#getsinglecolumnname", "description": "활성 또는 지정 셀의 열 문자 값을 검색하여 문자열 변수에 저장합니다."},
    {"action": "행 번호 가져오기", "data_item_name": "excel#getsinglerownumber", "description": "활성 또는 지정 셀의 행 번호를 검색하여 문자열 변수에 저장합니다."},
    {"action": "셀로 이동", "data_item_name": "excel#gotocell", "description": "Microsoft Excel 스프레드시트에서 특정 셀을 선택합니다."},
    {"action": "열기", "data_item_name": "excel#openspreadsheet", "description": "확장자가 .xlsx인 Microsoft Excel 스프레드시트를 엽니다. 비밀번호 등을 사용해 읽기 전용 또는 쓰기 전용 모드로 스프레드시트를 열 수 있습니다."},
    {"action": "바꾸기", "data_item_name": "excel#replace", "description": "특정 문자열을 포함하는 셀을 찾아 다른 문자열로 바꿉니다."},
    {"action": "통합 문서 저장", "data_item_name": "excel#savespreadsheet", "description": "Microsoft Excel 스프레드시트를 지정된 위치에 저장합니다."},
    {"action": "셀 설정", "data_item_name": "excel#setcell", "description": "지정한 값을 Microsoft Excel 스프레드시트의 셀에 설정합니다."},
    {"action": "시트로 전환", "data_item_name": "excel#activatesheet", "description": "특정 워크시트를 활성화합니다."},
]