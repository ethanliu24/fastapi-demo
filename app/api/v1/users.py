from fastapi import APIRouter, Depends, HTTPException
from repositories.repository import Repository
from ...dependencies import get_user_repository

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/")
async def get_users(user_repository: Repository = Depends(get_user_repository)):
    pass


@router.post("/")
async def create_user(user_repository: Repository = Depends(get_user_repository)):
    pass


@router.get("/{user_id}")
async def get_user(user_repository: Repository = Depends(get_user_repository)):
    pass


@router.put("/{user_id}")
async def get_user(user_repository: Repository = Depends(get_user_repository)):
    pass


@router.delete("/{user_id}")
async def get_user(user_repository: Repository = Depends(get_user_repository)):
    pass
