from ..repositories import UserRepository


class LoginUseCase:
    """Use case for user login."""

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, username: str, password: str) -> bool:
        """Executes the use case to log in a user."""
        return False
