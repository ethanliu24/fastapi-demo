from fastapi import APIRouter, Depends, status, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from ...services.chat import ChatServices
from ...config.dependencies import get_chat_services
from ...config.settings import DOMAIN_URL

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_chat_page():
    html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Chat</title>
            </head>
            <body>
                <h1>WebSocket Chat</h1>
                <h2>Your ID: <span id="ws-id"></span></h2>
                <form action="">
                    <input type="text" id="messageText" autocomplete="off"/>
                    <button id="sendButton">Send</button>
                </form>
                <ul id='messages'>
                </ul>
                <script>
                    var client_id = Date.now().toString().split('').reverse().join('')
                    document.querySelector("#ws-id").textContent = client_id

                    const ws = new WebSocket(`ws://{DOMAIN_URL}/api/v1/chat/ws/${{client_id}}`)
                    ws.onmessage = e => {{
                        let messages = document.getElementById('messages')
                        let message = document.createElement('li')
                        let content = document.createTextNode(e.data)
                        console.log(e.data)
                        message.appendChild(content)
                        messages.appendChild(message)
                    }};

                    const msgText = document.getElementById("messageText")
                    const sendBtn = document.getElementById("sendButton")
                    sendBtn.onclick = e => {{
                        e.preventDefault()
                        ws.send(msgText.value)
                        msgText.value = ""
                    }}
                </script>
            </body>
        </html>
    """

    return HTMLResponse(html)

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: int,
    chat_services: ChatServices = Depends(get_chat_services)
) -> None:
    await chat_services.connect(websocket)

    try:
        while True:
            # receive_text() -> str, receive_json() -> json, receive_bytes() -> binary
            msg = await websocket.receive_text()
            await chat_services.broadcast_msg(f"{client_id}: {msg}")
    except WebSocketDisconnect:
        chat_services.disconnect(websocket)
