from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """
    Represents an application user.
    """
    _id: ObjectId
    email: EmailStr
    username: str
    password: str
    created_at: datetime
    modified_at: datetime
