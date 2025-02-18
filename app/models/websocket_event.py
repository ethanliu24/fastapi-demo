from pydantic import BaseModel

class PublicChatEvent(BaseModel):
    event: str
    message: str


class TypingEvent(BaseModel):
    event: str
    user: str
    is_typing: bool
    