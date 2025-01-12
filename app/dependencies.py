# Fast API will automatically inject these as its dependency injection feature
from .db import DB
from fastapi import Depends
from typing import Annotated
from .repositories.repository import Repository


def get_db() -> DB:
    return DB()


def get_user_repository(db: Annotated[DB, Depends(get_db)]) -> Repository:
    return db.get_user_repository()
