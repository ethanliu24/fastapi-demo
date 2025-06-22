from pydantic import BaseModel
from langchain.chat_models import init_chat_model
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import ChatPromptTemplate
import os

# LLM = init_chat_model("gpt-4o-mini", model_provider="openai", openai_api_key=os.environ["OPEN_AI_API_KEY"])
LLM = init_chat_model("gemini-2.0-flash", model_provider="google_genai", google_api_key=os.environ["GOOGLE_API_KEY"])
TOOLS = []

SYSTEM_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You will help me manage users with CRUD operations."
     "Pick up any information you need from the given prompts."
     "If there's not enough information to complete an action, tell so through you response.")
])

agent = initialize_agent(
    TOOLS,
    LLM,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    prompt=SYSTEM_PROMPT,
    verbose=True
)

class InputModel(BaseModel):
    input: str
    # chat_history: List[str]


