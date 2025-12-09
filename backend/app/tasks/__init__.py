"""
Celery tasks package.
"""

# Import tasks to register them with Celery
from . import scraping, ai, notifications

__all__ = ["scraping", "ai", "notifications"]
