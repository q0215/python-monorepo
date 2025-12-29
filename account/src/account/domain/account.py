"""Account domain model.

Improvements:
- Email normalization (lowercase + strip) and validation
- Name validation (length, trimming)
- Password hash non-empty check
- Convenience methods: to_dict / from_dict
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from . import AccountId, Email

EMAIL_REGEX: re.Pattern[str] = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$", re.ASCII)

INVALID_EMAIL_MSG = "Invalid email format: {}"
INVALID_NAME_MSG = "Name must be between {min} and {max} characters."
EMPTY_PASSWORD_MSG = "Password hash must not be empty."

NAME_MIN = 1
NAME_MAX = 50


@dataclass(slots=True)
class Account:
    """Aggregate root representing a user account."""

    id: AccountId
    email: Email
    name: str
    password_hash: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None
    last_login_at: datetime | None = None

    def __post_init__(self) -> None:
        """Validate and normalize name and ensure password/email invariants."""
        # normalize and validate name
        if self.name is None:
            raise ValueError(INVALID_NAME_MSG.format(min=NAME_MIN, max=NAME_MAX))
        name_norm = self.name.strip()
        if not (NAME_MIN <= len(name_norm) <= NAME_MAX):
            raise ValueError(INVALID_NAME_MSG.format(min=NAME_MIN, max=NAME_MAX))
        self.name = name_norm

        if not self.password_hash:
            raise ValueError(EMPTY_PASSWORD_MSG)

        if not isinstance(self.email, Email):
            # allow raw string by coercing
            self.email = Email(str(self.email))  # type: ignore[assignment]

    @classmethod
    def create(
        cls,
        email: Email,
        name: str | None = None,
        password_hash: str = "",
    ) -> Account:
        """Create a new account with validation and timestamps."""
        now = datetime.now(UTC)
        return cls(
            id=AccountId(uuid4()),
            email=email,
            name=name or email.value.split("@")[0],
            password_hash=password_hash,
            is_active=True,
            created_at=now,
        )

    def deactivate(self) -> None:
        """Deactivate the account and update timestamp."""
        self.is_active = False
        self.updated_at = datetime.now(UTC)

    def rename(self, new_name: str) -> None:
        """Change the account name after validating length and trimming."""
        if new_name is None:
            raise ValueError(INVALID_NAME_MSG.format(min=NAME_MIN, max=NAME_MAX))
        name_norm = new_name.strip()
        if not (NAME_MIN <= len(name_norm) <= NAME_MAX):
            raise ValueError(INVALID_NAME_MSG.format(min=NAME_MIN, max=NAME_MAX))
        self.name = name_norm
        self.updated_at = datetime.now(UTC)

    def mark_logged_in(self) -> None:
        """Update last_login_at and updated_at when account logs in."""
        now = datetime.now(UTC)
        self.last_login_at = now
        self.updated_at = now

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable representation of the account."""
        return {
            "id": str(self.id),
            "email": str(self.email),
            "name": self.name,
            "password_hash": self.password_hash,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "last_login_at": (
                self.last_login_at.isoformat() if self.last_login_at else None
            ),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Account:
        """Create an Account instance from a dict (basic support for persisted data)."""
        return cls(
            id=AccountId(UUID(data["id"])),
            email=Email(data["email"]),
            name=data["name"],
            password_hash=data["password_hash"],
            is_active=bool(data.get("is_active", True)),
            created_at=datetime.fromisoformat(data["created_at"]).astimezone(UTC),
            updated_at=(
                datetime.fromisoformat(data["updated_at"]).astimezone(UTC)
                if data.get("updated_at")
                else None
            ),
            last_login_at=(
                datetime.fromisoformat(data["last_login_at"]).astimezone(UTC)
                if data.get("last_login_at")
                else None
            ),
        )
