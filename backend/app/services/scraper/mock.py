"""
Mock scraper for testing.
"""

from typing import List
from datetime import datetime, timedelta

from app.schemas.job import JobCreate
from app.services.scraper.base import BaseScraper


class MockScraper(BaseScraper):
    """Mock scraper that returns static job data."""

    def __init__(self):
        super().__init__(source_name="mock")

    async def scrape(self, limit: int = 10) -> List[JobCreate]:
        """Return a list of mock jobs."""
        print(f"MockScraper: extracting {limit} jobs...")
        
        jobs = []
        for i in range(min(limit, 5)):
            job = JobCreate(
                title=f"Software Engineer {i+1}",
                company=f"Mock Company {i+1}",
                location="Remote",
                employment_type="Full-time",
                description="This is a mock job description.",
                requirements="Python, FastAPI, React",
                salary_min=50000 + (i * 1000),
                salary_max=80000 + (i * 2000),
                url=f"https://mock-job-board.com/job/{i+1}",
                source="mock_board",
                external_id=f"mock-{i+1}",
                posted_at=datetime.utcnow() - timedelta(days=i)
            )
            jobs.append(job)
            
        return jobs
