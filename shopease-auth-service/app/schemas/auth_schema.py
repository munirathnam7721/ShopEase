from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=72,
    )
    confirm_password: str = Field(
        ...,
        min_length=8,
        max_length=72,
    )


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        min_length=1,
        max_length=72,
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class MessageResponse(BaseModel):
    message: str


class VerifyTokenResponse(BaseModel):
    valid: bool
    user_id: int
    role: str
    expires_at: datetime


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(
        ...,
        min_length=1,
        max_length=72,
    )
    new_password: str = Field(
        ...,
        min_length=8,
        max_length=72,
    )
    confirm_new_password: str = Field(
        ...,
        min_length=8,
        max_length=72,
    )
