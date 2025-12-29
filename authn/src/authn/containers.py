from dependency_injector import containers, providers

from .application.use_cases.login import LoginUseCase
from .config import Settings
from .infrastructure.database.repositories import UserRepositoryImpl
from .infrastructure.security.password import PasswordManager


class Container(containers.DeclarativeContainer):
    """DI container for the application."""

    config = providers.Singleton(Settings)

    password_manager = providers.Factory(PasswordManager)

    user_repository = providers.Factory(
        UserRepositoryImpl,
        # db_session_factory=... # This would be provided by a db provider
    )

    login_use_case = providers.Factory(
        LoginUseCase,
        user_repository=user_repository,
    )
