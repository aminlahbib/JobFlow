-- Database initialization script
-- This file is executed when the PostgreSQL container starts

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create jobflow database (if not exists)
-- Note: This is handled by POSTGRES_DB environment variable in docker-compose.yml
