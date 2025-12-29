"""In-memory implementation of the account repository."""

from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

from account.port import AccountRepository

if TYPE_CHECKING:
    from shared.model import AccountId

    from account.domain import Account


class InMemoryAccountRepository(AccountRepository):
    """In-memory repository for managing Account aggregates."""

    def __init__(self) -> None:
        """Initialize the in-memory repository."""
        self._accounts: dict[AccountId, Account] = {}
        self._email_index: dict[str, AccountId] = {}

    def save(self: InMemoryAccountRepository, account: Account) -> None:
        """Save an account (create or update)."""
        # Store a copy to prevent modifications to the object outside the repository
        # from affecting the repository's state.
        account_copy = deepcopy(account)
        self._accounts[account_copy.id] = account_copy
        self._email_index[account_copy.email.value] = account_copy.id

    def find_by_id(
        self: InMemoryAccountRepository,
        account_id: AccountId,
    ) -> Account | None:
        """Find an account by its ID."""
        account = self._accounts.get(account_id)
        return deepcopy(account) if account else None

    def find_by_email(self: InMemoryAccountRepository, email: str) -> Account | None:
        """Find an account by its email address."""
        normalized_email = email.strip().lower()
        account_id = self._email_index.get(normalized_email)
        if account_id:
            return self.find_by_id(account_id)
        return None

    def delete(self: InMemoryAccountRepository, account: Account) -> None:
        """Delete an account."""
        if account.id in self._accounts:
            del self._email_index[account.email.value]
            del self._accounts[account.id]
