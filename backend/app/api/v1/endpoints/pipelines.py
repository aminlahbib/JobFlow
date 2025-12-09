"""
Pipeline management endpoints.
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.api import deps
from app.database import get_db

router = APIRouter()


@router.get("/")
async def read_pipelines(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve user's pipelines.
    """
    # TODO: Implement pipeline listing
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Pipeline listing not yet implemented"
    )


@router.post("/")
async def create_pipeline(
    *,
    db: AsyncSession = Depends(get_db),
    pipeline_in: dict,  # TODO: Create pipeline schema
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new pipeline.
    """
    # TODO: Implement pipeline creation
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Pipeline creation not yet implemented"
    )
