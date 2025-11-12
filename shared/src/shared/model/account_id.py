"""Shared value object for representing an Account's unique identifier."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class AccountId:
    """Value object representing an Account's unique identifier."""

    value: UUID

    @classmethod
    def generate(cls) -> AccountId:
        """Generate a new AccountId."""
        return cls(value=uuid4())

    @classmethod
    def from_str(cls, value: str) -> AccountId:
        """Create an AccountId from a string."""
        return cls(UUID(value))

    def __str__(self) -> str:
        """Return the string representation of the AccountId."""
        return str(self.value)
