from fastapi import APIRouter, Depends, HTTPException, status
from ...dependencies import get_user_services
from ...services.user import UserServices
from ...models.user import User
from ...models.authentication import StandardUserSignUp

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("")
async def get_users(
    age: int | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    user_services: UserServices = Depends(get_user_services)
) -> list[User]:
    return user_services.get_all_users(age, min_age, max_age)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: StandardUserSignUp,
    user_services: UserServices = Depends(get_user_services)
) -> None:
    try:
        user = user_services.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{user_id}")
def get_user(
    user_id: str,
    user_services: UserServices = Depends(get_user_services)
) -> User:
    try:
        user = user_services.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{user_id}")
async def get_user():
    pass


@router.delete("/{user_id}")
async def get_user():
    pass
