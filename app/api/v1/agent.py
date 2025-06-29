from fastapi import Request, APIRouter
from ...config.agent import graph, SYSTEM_PROMPT

router = APIRouter(
    prefix="/agent",
    tags=["agent"]
)

@router.post("")
async def agent_route(request: Request):
    # https://ai.google.dev/gemini-api/docs/langgraph-example
    user_input = (await request.json()).get("prompt", "Tell client that `prompt` field is not given.")

    inputs = {"messages": [("System", SYSTEM_PROMPT), ("user", user_input)]}  # Also, get message from DB
    for state in graph.stream(inputs, stream_mode="values"):
        last_message = state["messages"][-1]
        last_message.pretty_print()

    # SAVE TO DB: state["messages"].append(("user", "Would it be in Munich warmer?"))

    return {"response": last_message}
