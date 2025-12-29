"""Account container."""

from dependency_injector import containers, providers

from account.adapter import InMemoryAccountRepository
from account.service import AccountService


class Container(containers.DeclarativeContainer):
    """Account container."""

    account_repository = providers.Singleton(
        InMemoryAccountRepository,
    )

    account_service = providers.Factory(
        AccountService,
        account_repository=account_repository,
    )
