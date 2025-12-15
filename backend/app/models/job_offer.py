"""
Job offer database model.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, JSON
from sqlalchemy.sql import func

from app.database import Base


class JobOffer(Base):
    """Job offer model for scraped job listings."""

    __tablename__ = "job_offers"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, index=True, nullable=True)  # ID from job board
    source = Column(String, nullable=False, index=True)  # 'indeed', 'stepstone', 'linkedin'

    # Basic job info
    title = Column(String, nullable=False, index=True)
    company = Column(String, nullable=False, index=True)
    location = Column(String, nullable=True)
    employment_type = Column(String, nullable=True)  # 'full-time', 'part-time', 'contract', etc.
    url = Column(String, unique=True, nullable=False)

    # Job details
    description = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True)
    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)
    salary_currency = Column(String, default="EUR")

    # Metadata
    job_metadata = Column(JSON, nullable=True)  # Additional data like company logo, benefits, etc.
    posted_at = Column(DateTime, nullable=True)
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    # Deduplication
    duplicate_hash = Column(String, index=True, nullable=True)  # Hash of title+company+url for deduplication

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
