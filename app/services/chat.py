from fastapi import WebSocket

class ChatServices:
    """
    Uses websockets for live chats - no chat history is stored atm.
    """

    _active_connections: list[WebSocket]

    def __init__(self):
        self._active_connnections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    async def broadcast_msg(self, msg: str):
        for connection in self._active_connections:
            connection.send_text(msg)
