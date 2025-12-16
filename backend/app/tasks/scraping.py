"""
Job scraping background tasks.
"""

import asyncio

from app.core.celery_app import celery_app
from app.database import AsyncSessionLocal
from app.services.scraper.manager import ScraperManager
from app.services.scraper.mock import MockScraper


@celery_app.task(name="app.tasks.scrape_job_listings")
def scrape_job_listings():
    """
    Scheduled task to scrape job listings from multiple sources.
    """
    async def _run_scraping():
        """Async implementation of scraping task."""
        async with AsyncSessionLocal() as session:
            manager = ScraperManager(session)
            
            # Scrape Mock Source
            mock_scraper = MockScraper()
            print(f"Starting scrape for {mock_scraper.source_name}...")
            count = await manager.ingest_jobs(mock_scraper)
            print(f"Completed {mock_scraper.source_name}: {count} new jobs.")

    # Run async code in sync Celery task
    try:
        asyncio.run(_run_scraping())
    except Exception as e:
        print(f"Error in scraping task: {e}")
        # Re-raise to let Celery know it failed
        raise e


@celery_app.task(name="app.tasks.scrape_single_source")
def scrape_single_source(source: str, filters: dict = None):
    """
    Scrape job listings from a single source.

    Args:
        source: Job board source ('indeed', 'stepstone', 'linkedin')
        filters: Optional filters for targeted scraping
    """
    # TODO: Implement single source scraping
    pass
