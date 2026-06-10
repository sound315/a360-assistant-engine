# 🚀 A360 Assistant Engine

LLM 기반 A360 자동화 플래너 & 챗봇 엔진

---

## 📌 프로젝트 소개

자연어 입력을 기반으로 A360 자동화 단계를 생성하는 AI 엔진입니다.

```text
사용자 입력 → FastAPI or Streamlit → LLM → 자동화 단계(JSON)
```

---

## 🧱 아키텍처

```
[Streamlit / Chrome Extension]
                ↓
           FastAPI Backend
                ↓
        Azure OpenAI (LLM)

```
## 🎯 핵심 기능

* 자연어 → 자동화 단계 변환
* LLM 기반 플래닝
* Streamlit 챗봇 UI
* Chrome Extension 연동
* 서버리스 배포 지원

## 세부 조건
- 가장 기본적인 기능은 LLM 을 활용한 챗봇이 메인 기능이어야 한다.
- LLM은 답변을 지정한 포맷의 JSON으로 반환한다.
- JSON은 사전에 정의된 목록에서만 반환 된다.
- LLM은 사용자 의도를 파악하여 A360 작업을 추천한다.
- 추천받은 작업은 반드시 A360에 존재하는 기능이어야 하며, 사전에 정의 되어야 한다. (추후 RAG 고려)
- 지정한 JSON 형식으로 반환한다.
- 해당 챗봇은 브라우저 확장프로그램으로 지정한 URL에 챗봇 임베딩이 되어야 한다.
  지정한 URL : http://www.a360-kds.com/#/bots/repository/private/files/task/*/edit 
- 임베딩 하기 위해선 Iframe 를 사용해야 할 수 있다.
- 임베딩 된 챗봇을 통해 결과를 전달받은 JSON으로 확장프로그램은 js를 호출하여 원하는 액션을 더블클릭이 되어 소스에 추가된다.
