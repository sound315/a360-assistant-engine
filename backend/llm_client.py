import json
import os
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv

from a360_tasks import A360_TASKS, ALLOWED_PAIRS, PACKAGES

load_dotenv()

SYSTEM_PROMPT = """당신은 A360 RPA 전문가 어시스턴트입니다.
사용자의 자연어 입력을 분석하여 필요한 A360 액션을 추천합니다.

규칙:
1. 반드시 아래 허용 목록의 패키지명과 액션명 조합만 사용하세요.
2. 응답은 반드시 아래 형식의 JSON 객체여야 합니다.
3. message: 사용자에게 보여줄 자연스러운 한국어 설명 (어떤 작업을 어떤 순서로 수행하는지)
4. steps: 실행 순서대로 정렬된 액션 목록

허용된 A360 패키지 및 액션 목록:
{task_list}

응답 형식:
{{
  "message": "웹사이트를 열고 로그인 버튼을 클릭하는 자동화를 구성했습니다. 먼저 브라우저를 실행하여 URL을 열고, 이후 마우스 클릭으로 버튼을 선택합니다.",
  "steps": [
    {{"package": "브라우저", "action": "열기"}},
    {{"package": "마우스", "action": "클릭"}}
  ]
}}"""


def _build_system_prompt() -> str:
    pkg_desc_map = {p["name"]: p.get("description", "") for p in PACKAGES}

    grouped: dict[str, list[str]] = {}
    for t in A360_TASKS:
        desc = t.get("description", "").strip()
        entry = t["action"] + (f" ({desc})" if desc else "")
        grouped.setdefault(t["package"], []).append(entry)

    lines = []
    for pkg, actions in grouped.items():
        pkg_desc = pkg_desc_map.get(pkg, "").strip()
        header = f"[{pkg}]" + (f" — {pkg_desc}" if pkg_desc else "")
        lines.append(header)
        for act in actions:
            lines.append(f"  - {act}")

    return SYSTEM_PROMPT.format(task_list="\n".join(lines))


def _get_client():
    if os.getenv("AZURE_OPENAI_API_KEY"):
        return AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
        ), os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY")), os.getenv("OPENAI_MODEL", "gpt-4o")


def chat_with_llm(message: str, history: list[dict]) -> dict:
    client, model = _get_client()

    messages = [{"role": "system", "content": _build_system_prompt()}]
    for h in history:
        messages.append({"role": h["role"], "content": h["content"]})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
        temperature=0.2,
    )

    raw = response.choices[0].message.content
    parsed = json.loads(raw)

    # steps 추출
    if isinstance(parsed, list):
        steps = parsed
        llm_message = ""
    elif isinstance(parsed, dict):
        llm_message = parsed.get("message", "")
        if "steps" in parsed:
            steps = parsed["steps"]
        elif "actions" in parsed:
            steps = parsed["actions"]
        elif "package" in parsed and "action" in parsed:
            steps = [parsed]
        else:
            steps = []
    else:
        steps = []
        llm_message = ""

    # 허용 조합만 통과
    filtered = [
        s for s in steps
        if isinstance(s, dict) and (s.get("package"), s.get("action")) in ALLOWED_PAIRS
    ]

    return {"steps": filtered, "message": llm_message}
