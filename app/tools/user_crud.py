
from fastapi import Depends
from langchain_core.tools import tool
from pydantic import EmailStr
from ..services.user import UserServices
from ..models.user import User, UserUpdate
from ..models.authentication import StandardUserSignUp
from ..config.db import DB
from ..config.settings import pw_context
import json

# NOTE: make a Config class with sigleton class pattern that inits an UserServices instead,
# then we could just do Config.user_service
user_services: UserServices = UserServices(DB().get_user_repository(), pw_context)

@tool("get_users", return_direct=True)
def get_users(
    age: int | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
) -> list[User]:
    """
    Gets all user records from the databse. Note that age, min_age and max_age is optional for querying.
    Do NOT put the json content in your response.
    """
    users = user_services.get_all_users(age, min_age, max_age)
    users_dict = [user.model_dump_json() for user in users]
    return json.dumps(users_dict)

@tool("get_users", args_schema=StandardUserSignUp, return_direct=True)
def create_user(
    email: EmailStr,
    username: str,
    age: int,
    password: str,
    password_confirmation: str,
) -> User | str:
    """
    Creates the user record and stores it in a database. user_data is a StandardUserSignUp object which
    has the attributes email, username, age, password, and password_confirmation (should match password).
    If there are any errors creating the user, tell the user what the error is and what they need to do.
    Do not include the return result in your response, especially the password and its confirmation.
    """
    user_data = {
      "email": email,
      "username": username,
      "age": age,
      "password": password,
      "password_confirmation": password_confirmation,
    }

    try:
        print(user_data)
        user = user_services.create_user(StandardUserSignUp(**user_data))
        return user.model_dump_json()
    except ValueError as e:
        return f"Error creating user: #{e}"


TOOLS = [get_users, create_user]
