from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """
    Represents an application user.
    """
    id: str
    email: EmailStr
    username: str
    password: str
    created_at: datetime
    modified_at: datetime
