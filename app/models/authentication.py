from pydantic import BaseModel, EmailStr, field_validator

class StandardUserSignUp(BaseModel):
    email: EmailStr
    username: str
    age: int
    password: str
    password_confirmation: str

    @field_validator("age")
    def is_old_enough(age: int) -> int:
        if age < 13:
            raise ValueError("You must be over 13 to register.")
        return age

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