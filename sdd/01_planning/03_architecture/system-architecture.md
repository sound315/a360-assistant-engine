# Architecture Planning: A360 Assistant Engine

## 시스템 구성

```
[Chrome Extension]
        ↓ (iframe embed)
[Streamlit UI :8501]
        ↓ (HTTP POST /chat)
[FastAPI Backend :8000]
        ↓ (Azure OpenAI API)
[LLM (GPT-4o)]
```

## 컴포넌트

| 컴포넌트 | 기술 | 역할 |
|----------|------|------|
| FastAPI Backend | Python, FastAPI, Uvicorn | REST API, LLM 호출, JSON 생성 |
| Streamlit UI | Python, Streamlit | 챗봇 인터페이스 |
| LLM Client | OpenAI SDK | Azure OpenAI 연동 |
| A360 Task Registry | Python dict/JSON | 허용 태스크 정의 |
| Chrome Extension | MV3, JS | URL 매칭, Iframe 주입, 메시지 전달 |

## 디렉터리 구조

```
a360-assistant-engine_sdd/
├── backend/
│   ├── main.py          # FastAPI 앱
│   ├── llm_client.py    # Azure OpenAI 클라이언트
│   ├── a360_tasks.py    # 허용 A360 태스크 정의
│   └── schemas.py       # Pydantic 스키마
├── frontend/
│   └── app.py           # Streamlit 앱
├── extension/
│   ├── manifest.json    # Chrome Extension MV3
│   ├── content.js       # 페이지 주입 스크립트
│   ├── background.js    # 서비스 워커
│   └── popup.html       # 팝업 UI
├── .env.example
└── requirements.txt
```

## 보안 고려사항

- Azure OpenAI API Key는 환경변수로 관리 (`.env`)
- Chrome Extension의 content_security_policy 설정
- CORS: Streamlit ↔ FastAPI 허용
- iframe allow-scripts, allow-same-origin 설정
