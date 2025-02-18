from fastapi import FastAPI
from .config.routes import api_router_v1
from fastapi.middleware.cors import CORSMiddleware
from .config.settings import DOMAIN_URL
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(api_router_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat")
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
                        ws = new WebSocket(`wss://{DOMAIN_URL}/api/v1/chat/ws/${{username}}`);
                        ws.onmessage = e => {{
                            let messages = document.getElementById("messages");
                            let message = document.createElement("li");
                            let content = document.createTextNode(e.data);
                            console.log(e.data);
                            message.appendChild(content);
                            messages.prepend(message);
                        }};
                    }};
                </script>
            </body>
        </html>
    """

    return HTMLResponse(html)
