# Authentication System

## Overview

The JobFlow authentication system provides secure user registration, login, and profile management using JWT tokens and bcrypt password hashing.

## Features

### ✅ Implemented

- **User Registration** (`POST /api/v1/auth/register`)
  - Email validation
  - Password hashing with bcrypt
  - Duplicate email prevention
  
- **User Login** (`POST /api/v1/auth/login`)
  - OAuth2-compatible password flow
  - JWT token generation
  - 30-day token expiration
  
- **Token Refresh** (`POST /api/v1/auth/refresh-token`)
  - Refresh access tokens without re-login
  
- **User Profile** (`GET /api/v1/auth/me`)
  - Get current authenticated user info
  
- **Profile Management** (`PUT /api/v1/users/me`)
  - Update email, name, password, timezone, resume
  - Password changes are automatically hashed
  
- **Account Deletion** (`DELETE /api/v1/users/me`)
  - GDPR-compliant account deletion

### 🔜 OAuth Integration (Ready for Credentials)

OAuth endpoints are scaffolded and ready. To enable:

1. Add credentials to `.env`:
   ```env
   GOOGLE_CLIENT_ID=your_client_id
   GOOGLE_CLIENT_SECRET=your_client_secret
   LINKEDIN_CLIENT_ID=your_client_id
   LINKEDIN_CLIENT_SECRET=your_client_secret
   ```

2. Implement OAuth callback handlers in `auth.py`

## API Endpoints

### Register New User

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123",
    "full_name": "John Doe"
  }'
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "created_at": "2025-12-15T20:00:00Z"
}
```

### Login

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Get Current User

```bash
curl -X GET http://localhost:8000/api/v1/auth/me \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Update Profile

```bash
curl -X PUT http://localhost:8000/api/v1/users/me \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "Jane Doe",
    "timezone": "Europe/Berlin"
  }'
```

### Delete Account

```bash
curl -X DELETE http://localhost:8000/api/v1/users/me \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Security Features

- **Password Hashing**: Bcrypt with 12 rounds
- **JWT Tokens**: HS256 algorithm with configurable expiration
- **Token Validation**: Automatic verification on protected endpoints
- **Active User Check**: Inactive accounts cannot authenticate
- **GDPR Compliance**: User data deletion on request

## Configuration

Edit `.env` or `app/config.py`:

```python
SECRET_KEY = "your-secret-key"  # Change in production!
ACCESS_TOKEN_EXPIRE_MINUTES = 43200  # 30 days
BCRYPT_ROUNDS = 12
```

## Testing

Run authentication tests:

```bash
cd backend
pytest tests/test_auth.py -v
```

Tests cover:
- User registration
- Duplicate email handling
- Login success/failure
- Token authentication
- Profile updates
- Account deletion

## Next Steps

1. **OAuth Implementation**: Add Google/LinkedIn OAuth handlers
2. **Email Verification**: Send verification emails on registration
3. **Password Reset**: Implement forgot password flow
4. **Rate Limiting**: Add rate limiting to prevent brute force
5. **2FA**: Optional two-factor authentication

## Files Modified

- `app/api/v1/endpoints/auth.py` - Authentication endpoints
- `app/api/v1/endpoints/users.py` - User management endpoints
- `app/core/security.py` - JWT and password utilities
- `app/schemas/auth.py` - Request/response schemas
- `tests/test_auth.py` - Authentication tests
- `tests/conftest.py` - Test fixtures
