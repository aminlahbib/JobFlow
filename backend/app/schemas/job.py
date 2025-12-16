"""
Job Pydantic schemas.
"""

from datetime import datetime
from typing import Optional, Any, Dict

from pydantic import BaseModel, HttpUrl, Field


class JobBase(BaseModel):
    """Shared job properties."""
    title: str
    company: str
    location: Optional[str] = None
    employment_type: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    salary_currency: str = "EUR"
    url: str
    source: str
    posted_at: Optional[datetime] = None


class JobCreate(JobBase):
    """Properties to receive on item creation."""
    external_id: Optional[str] = None
    job_metadata: Optional[Dict[str, Any]] = None


class JobUpdate(JobBase):
    """Properties to receive on item update."""
    title: Optional[str] = None
    company: Optional[str] = None
    url: Optional[str] = None
    source: Optional[str] = None


class JobInDBBase(JobBase):
    """Properties shared by models stored in DB."""
    id: int
    external_id: Optional[str] = None
    job_metadata: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class Job(JobInDBBase):
    """Properties to return to client."""
    pass
