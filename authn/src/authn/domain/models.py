import uuid

from pydantic import BaseModel, Field


class User(BaseModel, frozen=True):
    """Domain model for a user. This model is immutable."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    hashed_password: str
