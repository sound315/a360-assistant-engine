# -*- coding: utf-8 -*-
PACKAGE_NAME        = "브라우저"
PACKAGE_ID          = "command-group:browser"
PACKAGE_DESCRIPTION = "브라우저 작업을 수행하기 위한 동작을 제공합니다. 주요 액션: 닫기(브라우저 창 또는 탭을 닫습니다(지원되는 브라우저만 해당).)、파일 다운로드(NTLM 인증이 필요할 수 있는 지정된 URL에서 파일을 다운로드하고 저...)、소스 코드 받기(전체 웹 페이지 또는 웹 페이지 iFrame의 소스 코드를 검색하여 출력...)、JavaScript 실행(웹 페이지 또는 웹 페이지의 iFrame에서 기존 JavaScript 함...)、JavaScript 함수 호출(웹 페이지 또는 웹 페이지의 iFrame에서 기존 JavaScript 함...) 외 3개."

ACTIONS = [
    {"action": "닫기", "data_item_name": "browser#close", "description": "브라우저 창 또는 탭을 닫습니다(지원되는 브라우저만 해당)."},
    {"action": "파일 다운로드", "data_item_name": "browser#downloadfile", "description": "NTLM 인증이 필요할 수 있는 지정된 URL에서 파일을 다운로드하고 저장합니다."},
    {"action": "소스 코드 받기", "data_item_name": "browser#extractsource", "description": "전체 웹 페이지 또는 웹 페이지 iFrame의 소스 코드를 검색하여 출력을 문자열 변수에 저장합니다. \n\niFrame에서 소스 코드를 캡처하려면 레코더 패키지 2.5.0 이상을 사용하십시오(Chrome 및 Edge만 해당)."},
    {"action": "JavaScript 실행", "data_item_name": "browser#runjavascript", "description": "웹 페이지 또는 웹 페이지의 iFrame에서 기존 JavaScript 함수를 실행합니다(지원되는 브라우저만 해당).\n\niFrame에서 JavaScript를 호출하려면 레코더 패키지 2.5.0 이상을 사용하십시오(Chrome 및 Edge 만 해당)."},
    {"action": "JavaScript 함수 호출", "data_item_name": "browser#calljavascript", "description": "웹 페이지 또는 웹 페이지의 iFrame에서 기존 JavaScript 함수 호출합니다(지원되는 브라우저만 해당).\n\niFrame에서 JavaScript를 호출하려면 레코더 패키지 2.5.0 이상을 사용하십시오(Chrome 및 Edge 만 해당)."},
    {"action": "깨진 링크 찾기", "data_item_name": "browser#findbrokenlinks", "description": "특정 페이지나 웹사이트에서 끊어진 링크를 찾아서 출력을 CSV 파일에 저장합니다."},
    {"action": "뒤로 이동", "data_item_name": "browser#goback", "description": "지정된 브라우저 탭에서 이전에 방문한 웹 페이지로 돌아갑니다. 이 동작은 브라우저의 뒤로 옵션을 클릭할 때와 동일하게 작동합니다(지원되는 브라우저에만 해당)."},
    {"action": "열기", "data_item_name": "browser#openbrowser", "description": "지정된 웹 페이지를 브라우저에서 엽니다."},
]