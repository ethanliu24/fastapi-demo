from fastapi import APIRouter, Depends, status, WebSocket, WebSocketDisconnect
from ...services.chat import ChatServices
from ...config.dependencies import get_chat_services

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.websocket("/ws/{client_name}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_name: str,
    chat_services: ChatServices = Depends(get_chat_services)
) -> None:
    await chat_services.connect(websocket)

    try:
        while True:
            # receive_text() -> str, receive_json() -> json, receive_bytes() -> binary
            msg = await websocket.receive_text()
            await chat_services.broadcast_msg(f"{client_name}: {msg}")
    except WebSocketDisconnect:
        chat_services.disconnect(websocket)
