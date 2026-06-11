import json
import requests
import streamlit as st

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="A360 Assistant", page_icon="🤖", layout="wide")
st.title("🤖 A360 Assistant Engine")
st.caption("자연어로 입력하면 A360 패키지 > 액션을 추천해드립니다.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_steps" not in st.session_state:
    st.session_state.last_steps = []
if "last_usage" not in st.session_state:
    st.session_state.last_usage = None

col_chat, col_result = st.columns([3, 2])

with col_chat:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("예: 웹사이트를 열고 로그인 버튼을 클릭해줘"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("분석 중..."):
                try:
                    history = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages[:-1]
                    ]
                    resp = requests.post(
                        f"{BACKEND_URL}/chat",
                        json={"message": prompt, "history": history},
                        timeout=30,
                    )
                    resp.raise_for_status()
                    data = resp.json()

                    steps = data.get("steps", [])
                    reply = data.get("message", "") or "추천 액션이 없습니다."
                    st.session_state.last_steps = steps
                    st.session_state.last_usage = data.get("usage")

                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})

                    # iframe → Chrome Extension 메시지 전송
                    # 중첩 구조: A360페이지 > Streamlit iframe > components iframe
                    # window.top 으로 최상위 A360 페이지(content.js 리스너)까지 직접 전달
                    st.components.v1.html(
                        f"""<script>
                        (function() {{
                            var payload = {{
                                type: 'A360_STEPS',
                                payload: {json.dumps(steps)}
                            }};
                            // 최상위(A360 페이지)로 직접 전송
                            try {{ window.top.postMessage(payload, '*'); }} catch (e) {{}}
                            // 폴백: 한 단계 위(Streamlit 앱)에도 전송 → 릴레이 가능하도록
                            try {{ window.parent.postMessage(payload, '*'); }} catch (e) {{}}
                        }})();
                        </script>""",
                        height=0,
                    )

                except requests.exceptions.ConnectionError:
                    msg = "⚠️ 백엔드 서버 연결 실패. `uvicorn main:app` 을 먼저 실행하세요."
                    st.error(msg)
                    st.session_state.messages.append({"role": "assistant", "content": msg})
                except Exception as e:
                    msg = f"⚠️ 오류: {e}"
                    st.error(msg)
                    st.session_state.messages.append({"role": "assistant", "content": msg})

with col_result:
    st.subheader("📋 추천 A360 액션")
    if st.session_state.last_steps:
        steps = st.session_state.last_steps

        for i, s in enumerate(steps):
            st.markdown(f"`{i+1}` &nbsp; **{s['package']}** › {s['action']}")

        st.divider()
        st.caption("JSON")
        st.code(json.dumps(steps, ensure_ascii=False, indent=2), language="json")

        st.download_button(
            "⬇️ JSON 다운로드",
            data=json.dumps(steps, ensure_ascii=False, indent=2),
            file_name="a360_actions.json",
            mime="application/json",
        )
    else:
        st.info("챗봇과 대화하면 A360 액션이 여기에 표시됩니다.")

    if st.button("🗑️ 초기화"):
        st.session_state.messages = []
        st.session_state.last_steps = []
        st.session_state.last_usage = None
        st.rerun()

# 푸터: 토큰 사용량 & 컨텍스트
usage = st.session_state.last_usage
if usage:
    model_name = usage.get("model", "unknown")
    prompt_tok = usage.get("prompt_tokens", 0)
    completion_tok = usage.get("completion_tokens", 0)
    total_tok = usage.get("total_tokens", 0)
    ctx_limit = usage.get("context_limit", 128000)
    ctx_pct = round(total_tok / ctx_limit * 100, 1) if ctx_limit else 0

    st.divider()
    st.caption(
        f"모델: `{model_name}` &nbsp;|&nbsp; "
        f"입력: `{prompt_tok:,}` 토큰 &nbsp;|&nbsp; "
        f"출력: `{completion_tok:,}` 토큰 &nbsp;|&nbsp; "
        f"합계: `{total_tok:,}` 토큰 &nbsp;|&nbsp; "
        f"컨텍스트: `{total_tok:,} / {ctx_limit:,}` ({ctx_pct}%)"
    )
