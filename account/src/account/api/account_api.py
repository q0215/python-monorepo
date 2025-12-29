"""Account API endpoints."""

from typing import Annotated, Any
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, BeforeValidator, EmailStr
from shared.model import AccountId

from account.container import Container
from account.domain import Email
from account.service import AccountService


def email_to_str(v: Any) -> str:
    """Convert Email value object to string for validation."""
    if isinstance(v, Email):
        return v.value
    return str(v)


class AccountCreateRequest(BaseModel):
    """Request model for creating an account."""

    email: EmailStr


class AccountResponse(BaseModel):
    """Response model for an account."""

    id: AccountId
    email: Annotated[EmailStr, BeforeValidator(email_to_str)]

    class Config:
        """Pydantic configuration."""

        from_attributes = True


router = APIRouter()


@router.post(
    "/accounts",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
)
@inject
def create_account(
    request: AccountCreateRequest,
    account_service: AccountService = Depends(Provide[Container.account_service]),
) -> AccountResponse:
    """Create a new account."""
    try:
        account = account_service.create_account(email=request.email)
        return AccountResponse.model_validate(account)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) from e


@router.get("/accounts/{account_id}", response_model=AccountResponse)
@inject
def get_account(
    account_id: UUID,
    account_service: AccountService = Depends(Provide[Container.account_service]),
) -> AccountResponse:
    """Get an account by its ID."""
    account = account_service.find_account_by_id(AccountId(account_id))
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account with id {account_id} not found",
        )
    return AccountResponse.model_validate(account)


@router.delete("/accounts/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_account(
    account_id: UUID,
    account_service: AccountService = Depends(Provide[Container.account_service]),
) -> None:
    """Delete an account by its ID."""
    account_service.delete_account(AccountId(account_id))


def wire_container(container: Container) -> None:
    """Wire the container to the API module."""
    container.wire(modules=[__name__])
