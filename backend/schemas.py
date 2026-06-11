from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = []


class A360Action(BaseModel):
    package: str
    action: str
    data_item_name: str | None = None


class TokenUsage(BaseModel):
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    context_limit: int


class ChatResponse(BaseModel):
    steps: list[A360Action]
    message: str
    usage: TokenUsage | None = None
