from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# NOTE: Should add attribute descriptions with pydantic Field
class User(BaseModel):
    """
    Represents an application user.
    """
    id: str
    email: EmailStr
    username: str
    password: str
    age: int
    created_at: datetime
    modified_at: datetime

class UserUpdate(BaseModel):
    """
    Information to send for updating user
    """
    # should validate password as well, maybe make a util function
    email: EmailStr
    username: str
    password: str
    password_confirmation: str
    age: int
