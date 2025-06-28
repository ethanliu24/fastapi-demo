from typing import Annotated,Sequence, TypedDict
from pydantic import BaseModel, Field
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, END
import os

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """
    Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd).
    Returns a float the represents temperature in Celsius.
    Format your response like this:
    "The weather at `location` on `date` is `temperate`"
    """
    print("weather is 30")
    return 30

TOOLS = [get_weather_forecast]
tools_by_name = {tool.name: tool for tool in TOOLS}
api_key = os.environ["GEMINI_API_KEY"]
llm = ChatGoogleGenerativeAI(
    model= "gemini-2.0-flash",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)
model = llm.bind_tools(TOOLS)
agent = create_react_agent(llm, tools=TOOLS)

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int

# SYSTEM_PROMPT = ChatPromptTemplate.from_messages([
#     ("system",
#      "You will help me manage users with CRUD operations."
#      "Pick up any information you need from the given prompts."
#      "If there's not enough information to complete an action, tell so through you response.")
# ])

PROMPT = \
    "You will help me manage users with CRUD operations. " \
    "Pick up any information you need from the given prompts. " \
    "If there's not enough information to complete an action, tell so through you response."

messages = [
    SystemMessage(content="You are a helpful assistant that tells the user the weather."),
    HumanMessage(content="What is the weather in Berlin on 2025-06-28?")
]

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # We return a list, because this will get added to the existing messages state using the add_messages reducer
    return {"messages": [response]}

def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then we finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"


# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add our nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return, and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()

# res = model.invoke("Whats the weather in Berlin on 2020-05-05")
# print(res)

inputs = {"messages": [("user", f"What is the weather in Toronto on 2020, may 5th?")]}
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()

state["messages"].append(("user", "Would it be in Munich warmer?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
