from fastapi import APIRouter, Depends, HTTPException, status
from ...config.dependencies import get_user_services
from ...services.user import UserServices
from ...models.user import User, UserUpdate
from ...models.authentication import StandardUserSignUp

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_users(
    age: int | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    user_services: UserServices = Depends(get_user_services)
) -> list[User]:
    return await user_services.get_all_users(age, min_age, max_age)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: StandardUserSignUp,
    user_services: UserServices = Depends(get_user_services)
) -> None:
    try:
        user = await user_services.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(
    user_id: str,
    user_services: UserServices = Depends(get_user_services)
) -> User:
    try:
        user = await user_services.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: str,
    new_data: UserUpdate,
    user_services: UserServices = Depends(get_user_services)
) -> None:
    await user_services.update_user(user_id, new_data)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: str,
    user_services: UserServices = Depends(get_user_services)
) -> None:
    try:
        await user_services.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
