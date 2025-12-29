import uuid

from pydantic import BaseModel


class UserRead(BaseModel):
    """Schema for user data in response."""

    id: uuid.UUID
    username: str
