from abc import ABC, abstractmethod
from ..models.user import User

class UserRepository(ABC):
    """
    An interface for user repository. All "user repositories" mus implement this.
    """
    @abstractmethod
    def query_all_users(self, age: int | None, min_age: int | None, max_age: int | None) -> list[User]:
        pass
