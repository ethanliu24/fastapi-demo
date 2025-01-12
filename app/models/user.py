from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class User(BaseModel):
    """
    Represents an application user.
    """
    _id: ObjectId
    email: EmailStr
    username: str
    password: str
    password_confirmation: str
    created_at: datetime
    modified_at: datetime

class StandardUserSignUp(BaseModel):
    email: EmailStr
    username: str
    password: str
    password_confirmation: str

    @field_validator("password")
    def validate_password(password: str) -> str:
        if len(password) < 2:
            raise ValueError("Password must be at least 2 characters long.")
        return password

    @field_validator("password_confirmation")
    def confirm_password(confirmation: str, fields: dict) -> str:
        password = fields.data.get("password")
        if confirmation != password:
            raise ValueError("Password doesn't match")
        return confirmation