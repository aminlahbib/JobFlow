# Project Context

## Purpose
JobFlow is a job application automation platform that helps job seekers automate their job search process. It intelligently scrapes job listings from multiple sources, filters opportunities based on user preferences, generates personalized motivation letters using AI, and tracks applications in a unified dashboard—saving job seekers hours of manual work while increasing application quality and success rates.

## Tech Stack
- **Frontend**: Next.js 15 + React 19 (Type-safe, SSR, Server Components, great DX)
- **Backend**: FastAPI (Python 3.12+) - Async, type hints, excellent ORM integration
- **Database**: PostgreSQL 16+ - ACID compliance, JSONB support for semi-structured data
- **Cache**: Redis 7+ / Valkey - Session storage, rate limiting, job ranking cache
- **Job Queue**: Celery + Redis (or Dramatiq as alternative) - Async tasks for scraping, email, LLM calls
- **Web Scraping**: httpx + BeautifulSoup / Playwright - Modern async HTTP client
- **LLM Integration**: OpenAI API (GPT-4o / GPT-4o-mini) for motivation letter generation - cost-effective with latest models
- **Authentication**: JWT + OAuth2 (Google, LinkedIn) with optional Passkeys/WebAuthn support
- **Hosting**: Docker + Kubernetes (or managed platforms like Vercel/Railway for MVP)
- **Monitoring**: Sentry, Better Stack (or Grafana Cloud) for error tracking and performance monitoring
- **CI/CD**: GitHub Actions with Docker for automated testing and deployment

## Project Conventions

### Code Style
- **File Naming**: Use kebab-case for API endpoints and component files
- **TypeScript**: Strict typing for all frontend code, Pydantic schemas for backend validation
- **API Design**: RESTful endpoints with consistent naming (plural nouns, HTTP verbs)
- **Error Handling**: Structured error responses with appropriate HTTP status codes
- **Documentation**: OpenAPI/Swagger for all backend endpoints
- **Code Organization**: Feature-based directory structure (modules per capability)

### Architecture Patterns
- **Microservices**: Separate services for job ingestion, application tracking, letter generation
- **Event-Driven**: Background job processing for scraping, LLM calls, email notifications
- **API-First**: All functionality accessible via REST API for future mobile/web extensions
- **Stateless**: Horizontal scaling support, no server-side session storage
- **Caching Strategy**: Redis for job rankings, user sessions, rate limiting

### Testing Strategy
- **Unit Tests**: 80%+ coverage for business logic, API endpoints, data models
- **Integration Tests**: End-to-end workflows for core user journeys
- **Load Testing**: 10K concurrent users target, performance benchmarks
- **Security Testing**: OWASP Top 10 validation, authentication flow testing
- **Scraper Testing**: Data quality validation, duplicate detection testing

### Git Workflow
- **Feature Branches**: Each feature/capability gets dedicated branch
- **Commit Convention**: Conventional commits (feat:, fix:, chore:, docs:)
- **Code Review**: Required for all changes affecting user data or core functionality
- **CI/CD**: GitHub Actions + Docker for automated testing, security scanning, staging deployment

## Domain Context
**Job Search Automation**: JobFlow addresses the inefficiencies in traditional job searching by automating repetitive tasks while maintaining quality and personalization. The platform serves job seekers who apply to 5+ positions monthly and want to optimize their search strategy.

**User Journey**: 
1. **Onboarding**: User signs up, uploads resume, creates search pipelines
2. **Discovery**: Automated job ingestion from multiple sources, intelligent filtering
3. **Application**: AI-generated personalized motivation letters, application tracking
4. **Follow-up**: Email sync, automated reminders, analytics insights

**Core Capabilities**:
- Multi-source job data ingestion with deduplication
- AI-powered job matching and ranking based on user preferences
- Personalized motivation letter generation using LLM technology
- Comprehensive application tracking with status workflow management
- Email integration for recruiter communication tracking

## Important Constraints
- **Legal Compliance**: Respect job board Terms of Service, robots.txt, fair use policies
- **Data Privacy**: GDPR/CCPA compliance, user data encryption, right to deletion within 30 days
- **Rate Limiting**: Respect external API limits, implement intelligent backoff (100 req/min per user, 1000 req/min per IP)
- **Cost Management**: LLM usage tracking (~$0.01-0.05 per letter), cost optimization for letter generation
- **Data Quality**: >95% data accuracy, <5% false negatives in job ingestion
- **Performance**: <500ms API response time (p95), <2s job ranking pipeline, <10s letter generation
- **Scalability**: Support 10K concurrent users (Year 1 target)
- **Availability**: 99.5% system uptime target

## External Dependencies
- **Job Board APIs**: Indeed, StepStone, LinkedIn (via official APIs where available)
- **OpenAI API**: GPT-4 for motivation letter generation and job scoring
- **OAuth Providers**: Google, LinkedIn for user authentication
- **Email Services**: Gmail API for recruiter communication tracking
- **Infrastructure**: Docker, Kubernetes, PostgreSQL, Redis, Celery
- **Monitoring**: Sentry (error tracking), DataDog (performance monitoring)

## Success Metrics
- **User Acquisition**: 500 active users (MVP validation)
- **Engagement**: 60% MAU retention, 15-25 applications per user monthly
- **Performance**: 70% time savings vs. manual job search
- **Quality**: 2x cover letter customization rate, 90%+ job relevance
- **Business**: NPS score 45+, <10% monthly churn, <$15 CAC

## Timeline
- **MVP Launch**: Q2 2026 (12 weeks development)
- **General Availability**: Q4 2026
- **Target Personas**: Career changers (primary), fresh graduates (secondary), power users (tertiary)
