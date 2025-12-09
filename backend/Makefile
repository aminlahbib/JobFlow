# JobFlow Backend Development Commands

.PHONY: help install dev up down build clean test lint format

help: ## Show this help message
	@echo "JobFlow Backend Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install Python dependencies
	pip install -r requirements.txt

dev: ## Start development environment with Docker
	docker-compose -f docker-compose.dev.yml up --build

up: ## Start services with Docker Compose
	docker-compose up -d

down: ## Stop all services
	docker-compose down

build: ## Build Docker images
	docker-compose build

clean: ## Clean up containers and volumes
	docker-compose down -v --remove-orphans
	docker system prune -f

test: ## Run tests
	pytest app/tests/ -v --cov=app --cov-report=html

lint: ## Run linting
	black --check app/
	isort --check-only app/

format: ## Format code
	black app/
	isort app/

shell: ## Open shell in API container
	docker-compose exec api bash

logs: ## Show logs
	docker-compose logs -f

db-shell: ## Open PostgreSQL shell
	docker-compose exec postgres psql -U jobflow -d jobflow

redis-shell: ## Open Redis shell
	docker-compose exec redis redis-cli

migrate: ## Run database migrations
	alembic upgrade head

migrate-create: ## Create new migration
	alembic revision --autogenerate -m "$(msg)"
