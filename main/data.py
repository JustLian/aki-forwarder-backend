from fastapi import WebSocket


active_sessions: dict[str, WebSocket] = {}
session_to_uid: dict[str, int] = {}
