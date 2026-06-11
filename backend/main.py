from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from a360_tasks import A360_TASKS
from llm_client import chat_with_llm
from schemas import ChatRequest, ChatResponse, A360Action, TokenUsage

# (package, action) → data_item_name 룩업 (actions.json 기반 실제 값)
_ITEM_NAME_MAP = {(t["package"], t["action"]): t["data_item_name"] for t in A360_TASKS}

app = FastAPI(title="A360 Assistant Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return {"tasks": A360_TASKS}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        history = [{"role": m.role, "content": m.content} for m in request.history]
        result = chat_with_llm(request.message, history)
        steps = [
            A360Action(
                package=s["package"],
                action=s["action"],
                data_item_name=_ITEM_NAME_MAP.get((s["package"], s["action"])),
            )
            for s in result["steps"]
        ]
        llm_message = result.get("message", "")
        if not llm_message:
            llm_message = "、".join(f"{s.package} > {s.action}" for s in steps) or "추천 액션이 없습니다."
        usage = TokenUsage(**result["usage"]) if result.get("usage") else None
        return ChatResponse(steps=steps, message=llm_message, usage=usage)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
