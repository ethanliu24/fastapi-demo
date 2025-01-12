from datetime import datetime
from bson import ObjectId
from ..repositories.repository import Repository
from ..models.user import User
from ..models.authentication import StandardUserSignUp

class UserServices:
    """
    Services for User
    """

    _user_repository: Repository

    def __init__(self, user_repository: Repository):
        self._user_repository = user_repository

    async def create_user(self, user_data: StandardUserSignUp) -> User:
        creation_time = datetime.now()
        user = User(
            _id = ObjectId(),
            username = user_data.username,
            email = user_data.email,
            password = user_data.password,
            created_at = creation_time,
            modified_at = creation_time
        )

        self._user_repository.insert(user)
        return user
