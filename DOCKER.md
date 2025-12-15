# JobFlow - Full Docker Setup

Complete Docker orchestration for JobFlow with all services.

## Quick Start

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

Access:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Services

### Frontend (Next.js)
- **Port**: 3000
- **Container**: jobflow-frontend
- **Build**: Multi-stage optimized build

### Backend API (FastAPI)
- **Port**: 8000
- **Container**: jobflow-backend
- **Features**: REST API, JWT auth, async operations

### Celery Worker
- **Container**: jobflow-celery-worker
- **Purpose**: Background job processing (scraping, AI tasks)

### Celery Beat
- **Container**: jobflow-celery-beat
- **Purpose**: Scheduled tasks (periodic scraping)

### PostgreSQL
- **Port**: 5432
- **Container**: jobflow-postgres
- **Credentials**: jobflow/jobflow

### Redis
- **Port**: 6379
- **Container**: jobflow-redis
- **Purpose**: Cache & message broker

## Commands

```bash
# Build and start
docker-compose up --build -d

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Restart a service
docker-compose restart backend

# Run migrations
docker-compose exec backend alembic upgrade head

# Access database
docker-compose exec postgres psql -U jobflow -d jobflow

# Stop and remove everything
docker-compose down -v

# Scale workers
docker-compose up -d --scale celery-worker=3
```

## Environment Variables

Create `.env` in root directory:

```env
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-key-here
```

## Development vs Production

**Development** (current setup):
- Volume mounts for hot reload
- Debug logging enabled
- Exposed ports for direct access

**Production** (recommended changes):
- Remove volume mounts
- Use secrets for credentials
- Add nginx reverse proxy
- Enable SSL/TLS
- Use environment-specific configs

## Troubleshooting

**Services won't start:**
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

**Database connection errors:**
```bash
docker-compose logs postgres
docker-compose restart postgres
```

**Port conflicts:**
```bash
# Check what's using ports
lsof -i :3000
lsof -i :8000
lsof -i :5432
```

## Architecture

```
┌─────────────┐
│   Frontend  │ :3000
│  (Next.js)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────┐
│   Backend   │────▶│PostgreSQL│ :5432
│  (FastAPI)  │ :8000└──────────┘
└──────┬──────┘
       │          ┌─────────┐
       ├─────────▶│  Redis  │ :6379
       │          └─────────┘
       ▼
┌─────────────┐
│   Celery    │
│Worker + Beat│
└─────────────┘
```
