"""
Job management endpoints.
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.api import deps
from app.database import get_db

router = APIRouter()


@router.get("/")
async def read_jobs(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    search: str = Query(None, description="Search query"),
    location: str = Query(None, description="Job location filter"),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve jobs with optional filtering.
    """
    # TODO: Implement job listing with filtering
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Job listing not yet implemented"
    )


@router.get("/{job_id}")
async def read_job(
    *,
    db: AsyncSession = Depends(get_db),
    job_id: int,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get job by ID.
    """
    # TODO: Implement job retrieval by ID
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Job retrieval not yet implemented"
    )
