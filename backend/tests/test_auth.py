"""
Test authentication endpoints.
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security


class TestAuth:
    """Test authentication endpoints."""

    @pytest.mark.asyncio
    async def test_register_user(self, client: AsyncClient):
        """Test user registration."""
        response = await client.post(
            "/api/v1/auth/register",
            json={
                "email": "test@example.com",
                "password": "testpassword123",
                "full_name": "Test User"
            }
        )
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "test@example.com"
        assert data["full_name"] == "Test User"
        assert "id" in data
        assert data["is_active"] is True

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client: AsyncClient):
        """Test registration with duplicate email fails."""
        # Register first user
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "duplicate@example.com",
                "password": "password123",
            }
        )
        
        # Try to register again with same email
        response = await client.post(
            "/api/v1/auth/register",
            json={
                "email": "duplicate@example.com",
                "password": "password456",
            }
        )
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    @pytest.mark.asyncio
    async def test_login_success(self, client: AsyncClient):
        """Test successful login."""
        # Register user first
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "login@example.com",
                "password": "password123",
            }
        )
        
        # Login
        response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": "login@example.com",
                "password": "password123",
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    @pytest.mark.asyncio
    async def test_login_wrong_password(self, client: AsyncClient):
        """Test login with wrong password fails."""
        # Register user
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "wrongpass@example.com",
                "password": "correctpassword",
            }
        )
        
        # Try to login with wrong password
        response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": "wrongpass@example.com",
                "password": "wrongpassword",
            }
        )
        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_get_current_user(self, client: AsyncClient):
        """Test getting current user info."""
        # Register and login
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "current@example.com",
                "password": "password123",
                "full_name": "Current User"
            }
        )
        
        login_response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": "current@example.com",
                "password": "password123",
            }
        )
        token = login_response.json()["access_token"]
        
        # Get current user
        response = await client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "current@example.com"
        assert data["full_name"] == "Current User"

    @pytest.mark.asyncio
    async def test_update_user_profile(self, client: AsyncClient):
        """Test updating user profile."""
        # Register and login
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "update@example.com",
                "password": "password123",
            }
        )
        
        login_response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": "update@example.com",
                "password": "password123",
            }
        )
        token = login_response.json()["access_token"]
        
        # Update profile
        response = await client.put(
            "/api/v1/users/me",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "full_name": "Updated Name",
                "timezone": "Europe/Berlin"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["full_name"] == "Updated Name"
        assert data["timezone"] == "Europe/Berlin"
