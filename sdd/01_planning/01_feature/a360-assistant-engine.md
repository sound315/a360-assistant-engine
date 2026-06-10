# Feature Planning: A360 Assistant Engine

## 개요

자연어 입력을 기반으로 A360 자동화 단계를 생성하는 AI 엔진.

## 핵심 기능

### F-01: LLM 기반 챗봇
- 사용자의 자연어 입력을 받아 A360 작업 단계를 추천
- 사전 정의된 A360 태스크 목록에서만 추천
- 응답은 지정한 JSON 형식으로 반환

### F-02: A360 태스크 정의
- 브라우저 자동화: 열기, 이동, 클릭, 더블클릭, 텍스트 입력/읽기, 스크린샷, 대기
- 엑셀: 파일 열기, 셀 읽기/쓰기, 저장
- 파일: 읽기, 쓰기, 복사, 이동, 삭제
- 이메일: 전송, 읽기
- 데이터베이스: 조회, 삽입, 업데이트
- 제어 흐름: 조건 분기, 반복 루프, 대기
- 변수, 로그, API 호출

### F-03: Streamlit 챗봇 UI
- 대화형 인터페이스
- 생성된 JSON 미리보기 표시
- 채팅 히스토리 유지

### F-04: Chrome Extension 임베딩
- 대상 URL: `http://www.a360-kds.com/#/bots/repository/private/files/task/*/edit`
- Iframe으로 Streamlit 챗봇 임베딩
- 확장프로그램 ↔ Iframe 메시지 통신
- JSON 수신 후 JS 호출로 A360 소스에 작업 더블클릭 추가

## JSON 응답 포맷

A360 구조(패키지 > 액션)를 그대로 반영. 필수 키: `package`, `action`.

```json
[
  { "package": "브라우저", "action": "열기" },
  { "package": "브라우저", "action": "클릭" }
]
```

## 수용 기준

- LLM이 사전 정의된 태스크 목록 외의 태스크를 반환하지 않아야 함
- JSON 형식이 항상 스키마를 준수해야 함
- Chrome Extension이 대상 URL에서 챗봇을 정상 임베딩해야 함
- 확장프로그램이 JSON 결과를 받아 A360 UI에 작업을 추가해야 함
