"""
Scraper manager service.
"""

import hashlib
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.job_offer import JobOffer
from app.schemas.job import JobCreate
from app.services.scraper.base import BaseScraper


class ScraperManager:
    """Orchestrates specific scrapers and handles data persistence."""

    def __init__(self, session: AsyncSession):
        self.session = session

    def _generate_duplicate_hash(self, job: JobCreate) -> str:
        """Generate a hash for deduplication (Title + Company + URL)."""
        content = f"{job.title}{job.company}{job.url}".lower().encode('utf-8')
        return hashlib.md5(content).hexdigest()

    async def ingest_jobs(self, scraper: BaseScraper, limit: int = 10) -> int:
        """
        Run the scraper and save new jobs to the database.
        
        Returns:
            Count of new jobs ingested.
        """
        try:
            scraped_jobs = await scraper.scrape(limit=limit)
        except Exception as e:
            print(f"Error scraping {scraper.source_name}: {e}")
            return 0

        new_count = 0
        for job_data in scraped_jobs:
            dup_hash = self._generate_duplicate_hash(job_data)

            # Check for duplicates using the hash
            stmt = select(JobOffer).where(JobOffer.duplicate_hash == dup_hash)
            result = await self.session.execute(stmt)
            existing = result.scalar_one_or_none()

            if not existing:
                # Create new job offer
                new_job = JobOffer(
                    title=job_data.title,
                    company=job_data.company,
                    location=job_data.location,
                    employment_type=job_data.employment_type,
                    description=job_data.description,
                    requirements=job_data.requirements,
                    salary_min=job_data.salary_min,
                    salary_max=job_data.salary_max,
                    salary_currency=job_data.salary_currency,
                    url=job_data.url,
                    source=job_data.source,
                    external_id=job_data.external_id,
                    posted_at=job_data.posted_at,
                    job_metadata=job_data.job_metadata,
                    duplicate_hash=dup_hash
                )
                self.session.add(new_job)
                new_count += 1
        
        if new_count > 0:
            await self.session.commit()
            
        return new_count
