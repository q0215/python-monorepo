from abc import ABC, abstractmethod

from ..domain.models import User


class UserRepository(ABC):
    """Abstract repository for user data."""

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None:
        """Get a user by username."""
        raise NotImplementedError

    @abstractmethod
    async def save(self, user: User) -> None:
        """Save a user."""
        raise NotImplementedError
