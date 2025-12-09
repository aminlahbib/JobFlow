"""
Celery application configuration for background job processing.
"""

from celery import Celery
from celery.schedules import crontab

from app.config import settings

# Create Celery app
celery_app = Celery(
    "jobflow",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.tasks"]
)

# Celery configuration
celery_app.conf.update(
    # Task serialization
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,

    # Worker settings
    worker_prefetch_multiplier=1,
    task_acks_late=True,
    worker_max_tasks_per_child=50,

    # Beat scheduler settings
    beat_schedule={
        "scrape-job-listings": {
            "task": "app.tasks.scrape_job_listings",
            "schedule": crontab(hour="*/6"),  # Every 6 hours
        },
    },
)

# Task routing
celery_app.conf.task_routes = {
    "app.tasks.scrape_job_listings": {"queue": "scraping"},
    "app.tasks.generate_motivation_letter": {"queue": "ai"},
    "app.tasks.send_notification": {"queue": "notifications"},
}
