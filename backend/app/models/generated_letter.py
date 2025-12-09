"""
Generated letter database model for tracking AI-generated motivation letters.
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.sql import func

from app.database import Base


class GeneratedLetter(Base):
    """Generated letter model for tracking AI-generated motivation letters."""

    __tablename__ = "generated_letters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False, index=True)
    job_offer_id = Column(Integer, ForeignKey("job_offers.id"), nullable=False, index=True)

    # Letter content
    letter_text = Column(Text, nullable=False)
    tone = Column(String, default="professional")  # 'professional', 'casual', 'enthusiastic'
    length = Column(String, default="standard")  # 'short', 'standard', 'long'

    # Generation metadata
    llm_model = Column(String, nullable=False)  # 'gpt-4', 'gpt-4o-mini', etc.
    tokens_used = Column(Integer, nullable=True)
    cost_cents = Column(DECIMAL(10, 2), nullable=True)  # Cost in cents

    # Generation parameters
    prompt_used = Column(Text, nullable=True)  # The prompt template used
    generation_time_ms = Column(Integer, nullable=True)  # Time taken to generate

    # Quality tracking
    user_rating = Column(Integer, nullable=True)  # 1-5 star rating
    user_feedback = Column(Text, nullable=True)  # User comments on letter quality

    # Export options
    exported_formats = Column(String, nullable=True)  # JSON array of exported formats: ['pdf', 'docx', 'txt']

    # Timestamps
    generated_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
