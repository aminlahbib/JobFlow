"""
Authentication schemas.
"""

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Token response schema."""

    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Token payload schema."""

    sub: Optional[int] = None


class UserCreate(BaseModel):
    """User creation schema."""

    email: str
    password: str
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    """User update schema."""

    email: Optional[str] = None
    full_name: Optional[str] = None
    resume_text: Optional[str] = None
    timezone: Optional[str] = None


class User(BaseModel):
    """User response schema."""

    id: int
    email: str
    full_name: Optional[str]
    is_active: bool
    created_at: str

    class Config:
        from_attributes = True
