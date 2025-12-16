"""
Base scraper interface.
"""

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

from app.schemas.job import JobCreate


class BaseScraper(ABC):
    """Abstract base class for job scrapers."""

    def __init__(self, source_name: str):
        self.source_name = source_name

    @abstractmethod
    async def scrape(self, limit: int = 10) -> List[JobCreate]:
        """
        Scrape jobs from the source.
        
        Args:
            limit: Maximum number of jobs to fetch.
            
        Returns:
            List of JobCreate objects.
        """
        pass

    def normalize_salary(self, raw_salary: str):
        """Helper to normalize salary data."""
        # TODO: Implement common salary parsing logic
        pass

    def normalize_date(self, raw_date: str) -> datetime:
        """Helper to normalize date strings."""
        # TODO: Implement date parsing
        return datetime.utcnow()
