# JobFlow Docker Setup

This directory contains Docker configuration for running JobFlow services.

## Quick Start

### Start Database Services Only (Recommended for Development)

```bash
# Start PostgreSQL and Redis
docker-compose up -d

# Run backend locally
source venv/bin/activate
uvicorn app.main:app --reload
```

### Full Containerized Setup

Uncomment the `backend` service in `docker-compose.yml` and run:

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

## Services

### PostgreSQL (Port 5432)
- **Image**: postgres:16-alpine
- **Database**: jobflow
- **User**: jobflow
- **Password**: jobflow
- **Data**: Persisted in `postgres_data` volume

### Redis (Port 6379)
- **Image**: redis:7-alpine
- **Persistence**: AOF enabled
- **Data**: Persisted in `redis_data` volume

### Backend API (Port 8000) - Optional
- **Build**: From local Dockerfile
- **Environment**: Configured via docker-compose
- **Auto-reload**: Disabled in production mode

## Useful Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes (⚠️ deletes data)
docker-compose down -v

# Rebuild services
docker-compose build --no-cache

# Check service health
docker-compose ps

# Access PostgreSQL CLI
docker exec -it jobflow-postgres psql -U jobflow -d jobflow

# Access Redis CLI
docker exec -it jobflow-redis redis-cli

# Run migrations (if backend service is running)
docker-compose exec backend alembic upgrade head
```

## Environment Variables

The backend service uses environment variables from `.env` file. Make sure to create it:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Troubleshooting

### Port Already in Use

If you get "port already in use" errors:

```bash
# Check what's using the port
lsof -i :5432  # PostgreSQL
lsof -i :6379  # Redis
lsof -i :8000  # Backend

# Kill the process or change the port in docker-compose.yml
```

### Database Connection Issues

```bash
# Check if PostgreSQL is healthy
docker-compose ps

# View PostgreSQL logs
docker-compose logs postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### Reset Everything

```bash
# Stop all services and remove volumes
docker-compose down -v

# Remove all containers and images
docker system prune -a

# Start fresh
docker-compose up -d
```

## Production Deployment

For production, consider:

1. **Use secrets** instead of hardcoded passwords
2. **Enable SSL/TLS** for PostgreSQL
3. **Configure Redis password**
4. **Use environment-specific compose files**
5. **Set up proper logging** and monitoring
6. **Use orchestration** (Kubernetes, Docker Swarm)

Example production override:

```bash
# docker-compose.prod.yml
services:
  postgres:
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

Run with:
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
