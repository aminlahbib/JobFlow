"""
Application database model for tracking job applications.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


class Application(Base):
    """Application model for tracking user job applications."""

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    job_offer_id = Column(Integer, ForeignKey("job_offers.id"), nullable=False, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"), nullable=True)  # Optional link to pipeline

    # Application status workflow
    status = Column(String, default="new", nullable=False)
    # Status values: 'new', 'to_apply', 'applied', 'interview', 'rejected', 'offer', 'closed'

    # Application details
    applied_at = Column(DateTime(timezone=True), nullable=True)
    motivation_letter_text = Column(Text, nullable=True)
    motivation_letter_url = Column(String, nullable=True)  # Link to generated PDF/doc

    # Follow-up tracking
    notes = Column(Text, nullable=True)
    follow_up_date = Column(DateTime(timezone=True), nullable=True)
    last_follow_up_at = Column(DateTime(timezone=True), nullable=True)

    # Recruiter contact info
    recruiter_name = Column(String, nullable=True)
    recruiter_email = Column(String, nullable=True)
    recruiter_phone = Column(String, nullable=True)

    # Application metadata
    source_url = Column(String, nullable=True)  # Original job posting URL
    application_method = Column(String, default="manual")  # 'manual', 'auto', 'api'

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
