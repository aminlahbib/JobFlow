"""
Pipeline database model for saved search filters.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


class Pipeline(Base):
    """Pipeline model for saved search configurations."""

    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    # Search filters stored as JSON
    filters = Column(Text, nullable=False)  # JSON string with filter criteria

    # Pipeline settings
    is_active = Column(String, default="true")  # 'true', 'false', 'paused'
    notification_frequency = Column(String, default="daily")  # 'immediate', 'daily', 'weekly'

    # Statistics
    job_count = Column(Integer, default=0)  # Cached count of matching jobs
    last_run_at = Column(DateTime(timezone=True), nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
