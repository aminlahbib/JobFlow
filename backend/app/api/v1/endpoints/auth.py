"""
Authentication endpoints.
"""

from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.api import deps
from app.config import settings
from app.core import security
from app.database import get_db

router = APIRouter()


@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def register_user(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user account.
    
    - **email**: Valid email address (must be unique)
    - **password**: Minimum 8 characters
    - **full_name**: Optional full name
    """
    # Check if user already exists
    result = await db.execute(
        select(models.User).where(models.User.email == user_in.email)
    )
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )
    
    # Create new user with hashed password
    hashed_password = security.get_password_hash(user_in.password)
    db_user = models.User(
        email=user_in.email,
        hashed_password=hashed_password,
        full_name=user_in.full_name,
        is_active=True,
        is_superuser=False,
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    
    return db_user


@router.post("/login", response_model=schemas.Token)
async def login_access_token(
    db: AsyncSession = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    
    - **username**: User's email address
    - **password**: User's password
    
    Returns a JWT access token for authenticated requests.
    """
    # Find user by email (OAuth2 form uses 'username' field)
    result = await db.execute(
        select(models.User).where(models.User.email == form_data.username)
    )
    user = result.scalar_one_or_none()
    
    # Verify user exists and password is correct
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user account"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=user.id, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/refresh-token", response_model=schemas.Token)
async def refresh_access_token(
    *,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Refresh access token for authenticated user.
    
    Requires valid authentication token in Authorization header.
    Returns a new JWT access token.
    """
    # Create new access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=current_user.id, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=schemas.User)
async def get_current_user_info(
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current authenticated user information.
    
    Requires valid authentication token in Authorization header.
    """
    return current_user
