
from fastapi import Depends
from langchain_core.tools import tool
from ..services.user import UserServices
from ..models.user import User, UserUpdate
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

# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_user(
#     user_data: StandardUserSignUp,
#     user_services: UserServices = Depends(get_user_services)
# ) -> None:
#     try:
#         user = await user_services.create_user(user_data)
#         return user
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @router.get("/{user_id}", status_code=status.HTTP_200_OK)
# async def get_user(
#     user_id: str,
#     user_services: UserServices = Depends(get_user_services)
# ) -> User:
#     try:
#         user = await user_services.get_user(user_id)
#         return user
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


# @router.put("/{user_id}", status_code=status.HTTP_200_OK)
# async def update_user(
#     user_id: str,
#     new_data: UserUpdate,
#     user_services: UserServices = Depends(get_user_services)
# ) -> None:
#     await user_services.update_user(user_id, new_data)


# @router.delete("/{user_id}", status_code=status.HTTP_200_OK)
# async def delete_user(
#     user_id: str,
#     user_services: UserServices = Depends(get_user_services)
# ) -> None:
#     try:
#         await user_services.delete_user(user_id)
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
