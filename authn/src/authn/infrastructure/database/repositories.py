from ...application.repositories import UserRepository
from ...domain.models import User


class UserRepositoryImpl(UserRepository):
    """Concrete implementation of the user repository."""

    async def get_by_username(self, username: str) -> User | None:
        pass

    async def save(self, user: User) -> None:
        pass
