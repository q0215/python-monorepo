from __future__ import annotations

import re
from dataclasses import dataclass

EMAIL_REGEX: re.Pattern[str] = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$", re.ASCII)

INVALID_EMAIL_MSG = "Invalid email format: {}"


@dataclass(frozen=True, slots=True)
class Email:
    """Value object representing a valid email address.

    The email is normalized to lower-case and stripped of surrounding whitespace.
    """

    value: str

    def __post_init__(self) -> None:
        """Normalize and validate the email value."""
        normalized = self.value.strip().lower()
        if not EMAIL_REGEX.match(normalized):
            raise ValueError(INVALID_EMAIL_MSG.format(self.value))
        # set the normalized value on the frozen dataclass
        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:  # pragma: no cover - trivial
        """Return the normalized email as string."""
        return self.value
