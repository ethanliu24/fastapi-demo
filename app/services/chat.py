from fastapi import WebSocket

class ChatServices:
    """
    Uses websockets for live chats - no chat history is stored atm.
    """

    _active_connections: list[WebSocket]
    _typing_users: set[str]

    def __init__(self):
        self._active_connections = []
        self._typing_users = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    async def broadcast_msg(self, msg: str):
        await self._send_to_all({"event": "public_chat", "message": msg})

    async def add_to_typing_users(self, user: str):
        self._typing_users.add(user)
        await self._send_to_all({"event": "typing", "typers": list(self._typing_users)})

    async def remove_from_typing_users(self, user: str):
        if user in self._typing_users: self._typing_users.remove(user)
        await self._send_to_all({"event": "typing", "typers": list(self._typing_users)})

    async def _send_to_all(self, data: dict):
        for connection in self._active_connections:
            await connection.send_json(data)
