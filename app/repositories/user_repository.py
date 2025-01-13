from abc import ABC, abstractmethod
from ..models.user import User

class UserRepository(ABC):
    """
    An interface for user repository. All "user repositories" mus implement this.
    """
    @abstractmethod
    def query_all_users(self, age: int | None, min_age: int | None, max_age: int | None) -> list[User]:
        pass

    @abstractmethod
    def email_exists(self, email: str) -> bool:
        pass

    @abstractmethod
    def user_id_exists(self, user_id: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def update_user(self, user_id: str) -> None:
        pass
