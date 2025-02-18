from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from ...services.chat import ChatServices
from ...config.dependencies import get_chat_services
from ...models.websocket_event import PublicChatEvent, TypingEvent

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
            data = await websocket.receive_json()
            event_type = data.get("event")

            if event_type == "public_chat":
                event = PublicChatEvent(**data)
                await chat_services.broadcast_msg(f"{client_name}: {event.message}")
            elif event_type == "typing":
                event = TypingEvent(**data)
                if event.is_typing:
                    await chat_services.add_to_typing_users(client_name)
                else:
                    await chat_services.remove_from_typing_users(client_name)
    except WebSocketDisconnect:
        chat_services.disconnect(websocket)
