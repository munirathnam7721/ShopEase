from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    get_current_user,
    get_current_user_and_token,
)
from app.database.connection import get_db
from app.models.user_model import User
from app.schemas.auth_schema import (
    ChangePasswordRequest,
    LoginRequest,
    MessageResponse,
    RegisterRequest,
    TokenResponse,
    UserResponse,
    VerifyTokenResponse,
)
from app.services.auth_service import (
    authenticate_user,
    change_user_password,
    create_user_token,
    register_user,
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
) -> User:
    """Register a new user."""

    return register_user(db, request)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    """Authenticate a user and return a JWT access token."""

    user = authenticate_user(db, request)
    access_token = create_user_token(user)

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
    )


@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def get_me(
    current_user: User = Depends(get_current_user),
) -> User:
    """Return the currently authenticated user."""

    return current_user


@router.post(
    "/verify-token",
    response_model=VerifyTokenResponse,
    status_code=status.HTTP_200_OK,
)
def verify_token(
    user_and_token: tuple[User, dict] = Depends(
        get_current_user_and_token
    ),
) -> VerifyTokenResponse:
    """Verify the current user's JWT."""

    current_user, payload = user_and_token

    expires_at_timestamp = payload.get("exp")

    if expires_at_timestamp is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expiration is missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    expires_at = datetime.fromtimestamp(
        expires_at_timestamp,
        tz=timezone.utc,
    )

    return VerifyTokenResponse(
        valid=True,
        user_id=current_user.id,
        role=current_user.role,
        expires_at=expires_at,
    )


@router.post(
    "/change-password",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
)
def change_password(
    request: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> MessageResponse:
    """Change the authenticated user's password."""

    change_user_password(db, current_user, request)

    return MessageResponse(
        message="Password changed successfully",
    )