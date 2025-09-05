# Aki Forwarder – Backend

FastAPI + aiogram backend. Provides:
- WebSocket `/ws` for session IDs and status updates
- HTTP `POST /upload` to receive a file (≤ 8 MB) and forward to Telegram DM
- Aiogram bot handles `/start <sessionId>` to link the session

## Requirements
- [astral-sh/uv](https://github.com/astral-sh/uv)
- A Telegram bot token

## Environment
Set via environment variables or `.env`:
```
PORT=8000
HOST=localhost
TOKEN=telegram bot token
```

## Run
```bash
uv run -m main
```

## Links
- [Aki Forwarder - frontend (github)](https://github.com/JustLian/aki-forwarder-frontend)
- [aki.rian.moe (CF deployment)](https://aki.rian.moe)