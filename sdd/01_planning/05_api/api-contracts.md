# API Contracts: A360 Assistant Engine

## POST /chat

### Request
```json
{
  "message": "사용자 자연어 입력",
  "history": [
    {"role": "user", "content": "이전 메시지"},
    {"role": "assistant", "content": "이전 응답"}
  ]
}
```

### Response
```json
{
  "steps": [
    { "package": "브라우저", "action": "열기" },
    { "package": "브라우저", "action": "클릭" }
  ],
  "message": "브라우저 > 열기、브라우저 > 클릭"
}
```

## GET /tasks

### Response
```json
{
  "tasks": [
    { "package": "브라우저", "action": "열기" },
    { "package": "브라우저", "action": "클릭" }
  ]
}
```

## GET /health

```json
{"status": "ok"}
```
