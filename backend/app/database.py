"""
Database configuration and session management.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import settings

# Create async engine with psycopg (async)
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI.replace("postgresql://", "postgresql+psycopg://"),
    echo=True,
    future=True,
    poolclass=StaticPool,
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for all database models
Base = declarative_base()


async def get_db() -> AsyncSession:
    """Dependency for getting database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_db_and_tables():
    """Create database tables."""
    async with engine.begin() as conn:
        # Import all models here to ensure they are registered with Base
        from app.models import user, job_offer, pipeline, application, generated_letter  # noqa: F401

        await conn.run_sync(Base.metadata.create_all)


async def drop_db_and_tables():
    """Drop all database tables (for testing/development)."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
