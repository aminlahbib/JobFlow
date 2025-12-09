"""
Redis client configuration and utilities.
"""

import redis.asyncio as redis

from app.config import settings


class RedisClient:
    """Redis client wrapper for caching and job queue operations."""

    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            decode_responses=True,
        )

    async def get(self, key: str) -> str:
        """Get value from Redis."""
        return await self.client.get(key)

    async def set(self, key: str, value: str, expire: int = None) -> bool:
        """Set value in Redis with optional expiration."""
        return await self.client.set(key, value, ex=expire)

    async def delete(self, key: str) -> int:
        """Delete key from Redis."""
        return await self.client.delete(key)

    async def exists(self, key: str) -> bool:
        """Check if key exists in Redis."""
        return await self.client.exists(key)

    async def ping(self) -> bool:
        """Ping Redis server."""
        try:
            await self.client.ping()
            return True
        except redis.ConnectionError:
            return False

    async def close(self):
        """Close Redis connection."""
        await self.client.close()


# Global Redis client instance
redis_client = RedisClient()
