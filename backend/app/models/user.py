"""
User database model.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    """User model for authentication and profile data."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)  # Nullable for OAuth users
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # OAuth fields
    oauth_provider = Column(String, nullable=True)  # 'google', 'linkedin'
    oauth_id = Column(String, nullable=True)
    oauth_access_token = Column(String, nullable=True)
    oauth_refresh_token = Column(String, nullable=True)

    # Profile fields
    resume_text = Column(Text, nullable=True)
    timezone = Column(String, default="UTC")
    preferences = Column(String, nullable=True)  # JSON string for user preferences

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
