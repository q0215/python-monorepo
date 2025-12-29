from ..repositories import UserRepository


class RegisterUserUseCase:
    """Use case for registering a new user."""

    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, username: str, password: str) -> None:
        """Executes the use case to register a user."""
