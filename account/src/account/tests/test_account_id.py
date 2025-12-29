"""Tests for the AccountId value object."""

from dataclasses import FrozenInstanceError
from uuid import UUID

import pytest

from account.domain import AccountId


def test_account_id_creation_and_equality() -> None:
    """Verify that AccountId can be created and compared for equality."""
    id1 = AccountId.from_str("123e4567-e89b-12d3-a456-426614174000")
    id2 = AccountId.from_str("123e4567-e89b-12d3-a456-426614174000")
    id3 = AccountId.from_str("00000000-0000-0000-0000-000000000000")

    assert id1 == id2
    assert id1 != id3
    assert hash(id1) == hash(id2)
    assert hash(id1) != hash(id3)


def test_account_id_is_immutable() -> None:
    """Verify that AccountId is immutable."""
    account_id = AccountId.generate()
    with pytest.raises(FrozenInstanceError):
        account_id.value = UUID("123e4567-e89b-12d3-a456-426614174001")


def test_account_id_string_representation() -> None:
    """Verify the string representation of AccountId."""
    uuid_str = "123e4567-e89b-12d3-a456-426614174000"
    account_id = AccountId.from_str(uuid_str)
    assert str(account_id) == uuid_str


def test_generate_creates_valid_account_id() -> None:
    """Verify that `generate` creates a valid AccountId."""
    account_id = AccountId.generate()
    assert isinstance(account_id, AccountId)
    assert isinstance(account_id.value, UUID)


def test_from_str_with_invalid_uuid_raises_error() -> None:
    """Verify that `from_str` raises ValueError for an invalid UUID string."""
    with pytest.raises(ValueError):
        AccountId.from_str("not-a-valid-uuid")
