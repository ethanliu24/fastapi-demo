# Fast API will automatically inject these as its dependency injection feature
from .db import DB
from fastapi import Depends
from typing import Annotated

from ..repositories.repository import Repository

from ..services.user import UserServices
from ..services.chat import ChatServices
from ..services.auth import AuthenticationServices
from .settings import pw_context

def get_db() -> DB:
    return DB()


# Repositories
def get_user_repository(db: Annotated[DB, Depends(get_db)]) -> Repository:
    return db.get_user_repository()


# Services
def get_user_services(user_repository: Annotated[Repository, Depends(get_user_repository)]) -> UserServices:
    return UserServices(user_repository, pw_context)

_chat_services_instance = ChatServices()
def get_chat_services() -> ChatServices:
    return _chat_services_instance

def get_auth_services(user_services: UserServices = Depends(get_user_services)) -> AuthenticationServices:
    return AuthenticationServices(user_services)
