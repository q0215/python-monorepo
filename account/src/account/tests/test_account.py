"""Legacy placeholder for old test location.

Left intentionally empty to avoid import name collisions with the
`tests/` package which contains the real tests.
"""

import pytest

from account.domain import Account


def test_name_validation_on_rename():
    acc = Account.create("a@b.com", "Bob", "h")
    with pytest.raises(ValueError):
        acc.rename("")
    acc.rename("Robert")
    assert acc.name == "Robert"


def test_deactivate_and_login_timestamps():
    acc = Account.create("c@d.com", "C", "h2")
    acc.mark_logged_in()
    assert acc.last_login_at is not None
    assert acc.updated_at is not None
    acc.deactivate()
    assert not acc.is_active


def test_to_from_dict_roundtrip():
    acc = Account.create("x@y.com", "X", "h3")
    acc.mark_logged_in()
    d = acc.to_dict()
    acc2 = Account.from_dict(d)
    assert acc2.email.value == acc.email.value
    assert acc2.name == acc.name
    assert isinstance(acc2.id, type(acc.id))
    assert acc2.id == acc.id
    assert acc2.last_login_at is not None
