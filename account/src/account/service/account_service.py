"""Account Service."""

from __future__ import annotations

from typing import TYPE_CHECKING

from account.domain import Account, Email

if TYPE_CHECKING:
    from shared import AccountId

    from account import AccountRepository


class AccountService:
    """Service layer for account-related operations."""

    def __init__(self, account_repository: AccountRepository) -> None:
        """Initialize the account service."""
        self._account_repository = account_repository

    def create_account(self, email: str) -> Account:
        """Create a new account.

        Args:
            email: The email address for the new account.

        Returns:
            The created account.

        Raises:
            ValueError: If an account with the given email already exists.

        """
        if self._account_repository.find_by_email(email):
            msg = f"Account with email {email} already exists."
            raise ValueError(msg)

        new_account = Account.create(email=Email(email))
        self._account_repository.save(new_account)
        return new_account

    def find_account_by_id(self, account_id: AccountId) -> Account | None:
        """Find an account by its ID."""
        return self._account_repository.find_by_id(account_id)

    def find_account_by_email(self, email: str) -> Account | None:
        """Find an account by its email address."""
        return self._account_repository.find_by_email(email)

    def update_account(self, account: Account) -> None:
        """Update an existing account."""
        self._account_repository.save(account)

    def delete_account(self, account_id: AccountId) -> None:
        """Delete an account by its ID."""
        account = self._account_repository.find_by_id(account_id)
        if account:
            self._account_repository.delete(account)
