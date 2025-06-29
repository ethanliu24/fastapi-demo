from fastapi import Request, APIRouter
import json
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from ...config.agent import graph, SYSTEM_PROMPT

router = APIRouter(
    prefix="/agent",
    tags=["agent"]
)

@router.post("")
async def agent_route(request: Request):
    # https://ai.google.dev/gemini-api/docs/langgraph-example

    user_input = (await request.json()).get("prompt", "Tell client that `prompt` field is not given.")
    # possible message types: 'human', 'user', 'ai', 'assistant', 'function', 'tool', 'system', or 'developer'.
    inputs = {
        "messages": [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_input)
        ],
        "number_of_steps": 0,
    }

    data = {}
    # Determin if tool is sync or async in a dict to decide whether to use astream or stream
    # async for state in graph.astream(inputs, stream_mode="values"), modify the node functions too
    for state in graph.stream(inputs, stream_mode="values"):
        last_message = state["messages"][-1]
        for _, v in state.items():
            if isinstance(v, list):
              # One problem, state.items() contains all history messages, so if we have tools from
              # previous calls it might be an issue. One way could be if we dont store tool messages
              # in database or dont include it when constructing state.
              for msg in v:
                if isinstance(msg, ToolMessage):
                    try:
                        parsed = json.loads(msg.content)
                        data = parsed
                    except Exception as e:
                        continue

    # SAVE TO DB: state["messages"].append(("user", "Would it be in Munich warmer?"))

    return {"response": last_message, "data": data}
