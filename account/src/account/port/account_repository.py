"""Account repository port."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared import AccountId

    from account import Account


class AccountRepository(ABC):
    """Abstract repository for managing Account aggregates."""

    @abstractmethod
    def save(self: AccountRepository, account: Account) -> None:
        """Save an account (create or update)."""

    @abstractmethod
    def find_by_id(self: AccountRepository, account_id: AccountId) -> Account | None:
        """Find an account by its ID."""

    @abstractmethod
    def find_by_email(self: AccountRepository, email: str) -> Account | None:
        """Find an account by its email address."""

    @abstractmethod
    def delete(self: AccountRepository, account: Account) -> None:
        """Delete an account."""
