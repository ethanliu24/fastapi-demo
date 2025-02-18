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
                <h4 id="connectionText"></h4>

                <form action="">
                    <label>Enter username: <input type="text" id="usernameInput" autocomplete="off" value=""/></label>
                    <button id="connectButton">Connect</button>
                    <hr>
                </form>

                <form action="">
                    <input type="text" id="messageText" autocomplete="off"/>
                    <button id="sendButton">Send</button>
                </form>

                <ul id='messages'>
                </ul>

                <script>
                    let ws;
                    let connected = false;

                    const connectBtn = document.getElementById("connectButton");
                    connectBtn.onclick = e => {{
                        e.preventDefault();

                        const usernameInput = document.getElementById("usernameInput");
                        const connectionText = document.getElementById("connectionText");

                        let username = usernameInput.value;
                        if (username === "") {{
                            alert("Please enter a name");
                            return;
                        }}

                        username = username.split(" ").join("_").toLowerCase();
                        connectBtn.disabled = true;
                        usernameInput.disabled = true;
                        connected = true;
                        connectionText.textContent = `You are connected as "${{username}}"`;
                        connectToWS(username);
                    }};

                    const msgText = document.getElementById("messageText");
                    const sendBtn = document.getElementById("sendButton");
                    sendBtn.onclick = e => {{
                        e.preventDefault();

                        if (!connected) {{
                            alert("Please connect first");
                            return;
                        }};

                        if (!ws) return;

                        ws.send(msgText.value);
                        msgText.value = "";
                    }};

                    connectToWS = username => {{
                        ws = new WebSocket(`ws://{DOMAIN_URL}/api/v1/chat/ws/${{username}}`);
                        ws.onmessage = e => {{
                            let messages = document.getElementById("messages");
                            let message = document.createElement("li");
                            let content = document.createTextNode(e.data);
                            console.log(e.data);
                            message.appendChild(content);
                            messages.appendChild(message);
                        }};
                    }};
                </script>
            </body>
        </html>
    """

    return HTMLResponse(html)

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
