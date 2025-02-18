from fastapi import FastAPI
from .config.routes import api_router_v1
from fastapi.middleware.cors import CORSMiddleware
from .config.settings import DOMAIN_URL, ENVIORNMENT
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

                <div id="isTyping"></div>
                <br>

                <form action="">
                    <input type="text" id="messageText" autocomplete="off"/>
                    <button id="sendButton">Send</button>
                </form>

                <ul id='messages'></ul>

                <script>
                    let ws;
                    let username;
                    let connected = false;

                    const connectBtn = document.getElementById("connectButton");
                    connectBtn.onclick = e => {{
                        e.preventDefault();

                        const usernameInput = document.getElementById("usernameInput");
                        const connectionText = document.getElementById("connectionText");

                        username = usernameInput.value;
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

                    let onTypingCheckTimeout = false;
                    const msgText = document.getElementById("messageText");
                    msgText.oninput = async (e) => {{
                        if (!ws) return;
                        if (!username) return;

                        typingEvent = JSON.stringify({{
                            event: "typing",
                            user: username,
                            is_typing: msgText.value !== "",
                        }});

                        ws.send(typingEvent);

                        if (msgText.value !== "" && !onTypingCheckTimeout) {{
                            onTypingCheckTimeout = true;

                            await new Promise(() => {{
                                setTimeout(() => {{
                                    onTypingCheckTimeout = false;
                                    msgText.dispatchEvent(new Event("input"));
                                }}, 1000);
                            }});
                        }}
                    }};

                    const sendBtn = document.getElementById("sendButton");
                    sendBtn.onclick = e => {{
                        e.preventDefault();

                        if (!connected) {{
                            alert("Please connect first");
                            return;
                        }};

                        if (!ws) return;
                        if (msgText.value === "") return;

                        ws.send(JSON.stringify({{
                            event: "public_chat",
                            message: msgText.value,
                        }}));
                        msgText.value = "";

                        document.getElementById("isTyping").innerText = "";
                        onTypingCheckTimeout = false;
                    }};

                    connectToWS = username => {{
                        ws = new WebSocket(`{"wss" if ENVIORNMENT == "production" else "ws"}://{DOMAIN_URL}/api/v1/chat/ws/${{username}}`);
                        ws.onmessage = e => {{
                            const data = JSON.parse(e.data);
                            switch (data.event) {{
                                case "public_chat":
                                    handleSendMessage(data.message);
                                    break;
                                case "typing":
                                    handleIsTyping(data.typers);
                                    break;
                                default:
                                    console.warn("Unknown websocket event type");
                            }};
                        }};
                    }};

                    handleSendMessage = msg => {{
                        const messages = document.getElementById("messages");
                        const message = document.createElement("li");
                        const content = document.createTextNode(msg);
                        message.appendChild(content);
                        messages.prepend(message);
                    }}

                    handleIsTyping = typers => {{
                        const isTypingText = document.getElementById("isTyping");
                        let typerStr;

                        if (typers.length === 0) {{
                            isTypingText.innerText = "";
                            return;
                        }} else if (typers.length >= 4) {{
                            typeStr = "Many people are";
                        }} else {{
                            typeStr = `${{typers.join(", ")}} ${{typers.length === 1 ? "is" : "are"}}`;
                        }}

                        isTypingText.innerText = `${{typeStr}} typing...`;
                    }};
                </script>
            </body>
        </html>
    """

    return HTMLResponse(html)
