from fastapi import APIRouter, WebSocket
import uuid
from main.data import session_to_uid, active_sessions
from main.bot.client import bot


router = APIRouter()


@router.websocket("/ws")
async def websocket_connect(ws: WebSocket) -> None:

    await ws.accept()

    sess_id = str(uuid.uuid4())
    active_sessions[sess_id] = ws
    await ws.send_json({"sessionId": sess_id})

    try:

        while True:
            await ws.receive_json()
            # might be used later?

    except Exception:
        del active_sessions[sess_id]

        if sess_id in session_to_uid:
            await bot.send_message(session_to_uid[sess_id], "🛑 Session closed")
            del session_to_uid[sess_id]
