"""
Test scraper service.
"""

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.job_offer import JobOffer
from app.services.scraper.manager import ScraperManager
from app.services.scraper.mock import MockScraper


@pytest.mark.asyncio
async def test_mock_scraper(db_session: AsyncSession):
    """Test mock scraper ingestion."""
    manager = ScraperManager(db_session)
    scraper = MockScraper()

    # 1. Scrape and Ingest
    count = await manager.ingest_jobs(scraper, limit=5)
    assert count == 5

    # 2. Verify Jobs in DB
    result = await db_session.execute(select(JobOffer))
    jobs = result.scalars().all()
    assert len(jobs) == 5
    
    first_job = jobs[0]
    assert first_job.source == "mock_board"
    assert "Software Engineer" in first_job.title
    assert first_job.duplicate_hash is not None

    # 3. Test Deduplication (Run again)
    # The MockScraper returns the SAME jobs every time.
    # Manager should detect duplicates and NOT insert them.
    count_retry = await manager.ingest_jobs(scraper, limit=5)
    assert count_retry == 0

    # DB count should still be 5
    result = await db_session.execute(select(JobOffer))
    jobs = result.scalars().all()
    assert len(jobs) == 5
