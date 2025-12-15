"""
User management endpoints.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.api import deps
from app.core import security
from app.database import get_db

router = APIRouter()


@router.get("/me", response_model=schemas.User)
async def read_user_me(
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user profile.
    
    Returns the authenticated user's profile information.
    """
    return current_user


@router.put("/me", response_model=schemas.User)
async def update_user_me(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update current user profile.
    
    Allows updating:
    - Email address
    - Full name
    - Password (will be hashed)
    - Timezone
    - Resume text
    """
    # Update email if provided
    if user_in.email is not None:
        current_user.email = user_in.email
    
    # Update full name if provided
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    
    # Update password if provided (hash it first)
    if user_in.password is not None:
        current_user.hashed_password = security.get_password_hash(user_in.password)
    
    # Update timezone if provided
    if user_in.timezone is not None:
        current_user.timezone = user_in.timezone
    
    # Update resume text if provided
    if user_in.resume_text is not None:
        current_user.resume_text = user_in.resume_text
    
    db.add(current_user)
    await db.commit()
    await db.refresh(current_user)
    
    return current_user


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_me(
    *,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> None:
    """
    Delete current user account (GDPR compliance).
    
    Permanently deletes the user account and all associated data.
    This action cannot be undone.
    """
    await db.delete(current_user)
    await db.commit()
    return None

