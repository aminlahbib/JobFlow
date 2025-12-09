# Product Requirements Document (PRD)
## Job Application Automation Platform

**Document Version:** 1.0  
**Last Updated:** December 8, 2025  
**Author:** Product Team  
**Status:** DRAFT → Ready for Review

---

## 1. Executive Summary

**Product Name:** JobFlow (Working Title)

**Tagline:** "Automate your job search. Land the right role faster."

**Vision:** A comprehensive automation platform that intelligently scrapes job listings from multiple sources, filters opportunities based on user preferences, generates personalized motivation letters, and tracks applications in a unified dashboard—saving job seekers hours of manual work while increasing application quality.

**Primary Use Case:** Job seekers, recent graduates, and career changers who apply to 5+ positions monthly and want to optimize their search strategy, quality of applications, and success rate.

**Target Launch:** Q2 2026 (MVP) / Q4 2026 (Full release)

---

## 2. Problem Statement

### The Current Pain

- **Manual scraping & compilation:** Job seekers manually visit 3-5 job boards daily, copying links and descriptions into spreadsheets.
- **Unfiltered noise:** Hundreds of irrelevant listings clutter results (wrong tech stack, location mismatch, overqualification, salary too low).
- **Repetitive applications:** Writing individualized cover letters / motivation letters for 20+ applications monthly is time-consuming.
- **Lost tracking:** Application status, company follow-ups, and recruiter responses scatter across Gmail, browser tabs, and notes.
- **Low quality submissions:** Speed-applied generic applications have lower response rates than tailored ones.
- **Market inefficiency:** Candidates waste time on dead-ends; employers receive low-intent applications.

### Market Validation

- **Global job market:** ~500M+ active job seekers globally; 50%+ use multiple job boards.
- **Time spent on job search:** Average 8–10 hours/week per active candidate.
- **Manual effort cost:** $5–15/hour × 5–10 hours/week = significant time loss.
- **Competitor landscape:** LinkedIn Easy Apply, automation scripts, and n8n DIY workflows exist, but no integrated, AI-driven SaaS product specializes in this.

---

## 3. Goals & Success Metrics

### Business Goals (Year 1)

| Goal | Target | Rationale |
|------|--------|-----------|
| User acquisition | 500 active users | Product-market fit validation |
| Monthly active users (MAU) | 60% retention | Habit-forming, regular use |
| Applications per user (month) | 15–25 | Metric of engagement & value |
| NPS score | 45+ | Strong product-market fit signal |
| Churn rate | <10% / month | Sticky product with clear ROI |
| Customer acquisition cost (CAC) | <$15 | Sustainable growth economics |

### Product Goals

| Goal | Metric | Timeline |
|------|--------|----------|
| Reduce manual job search time | 70% time savings vs. manual | MVP launch |
| Increase application quality | 2x cover letter customization rate | MVP + 3 months |
| Centralize tracking | 100% of applications in one DB | MVP launch |
| Multi-source coverage | 5+ job boards integrated | Q3 2026 |
| AI-driven filtering | 90%+ relevance (user satisfaction) | MVP + 6 months |

### Technical Goals

| Goal | Metric | Timeline |
|------|--------|----------|
| System uptime | 99.5% | Ongoing |
| API response time | <500ms (p95) | MVP |
| Data freshness | Job listings refreshed 2x daily | MVP |
| User data privacy | GDPR/CCPA compliant | MVP |
| Scalability | Support 10K concurrent users | Year 1 |

---

## 4. Target Personas

### Persona 1: "Career Changer" (Primary)
- **Name:** Alex, 28–35
- **Background:** Switching industries or career paths; 3–10 years of experience
- **Pain Points:**
  - Applies to 10–15 positions/month but gets few interviews
  - Uncertain which roles are best fit for their background
  - Spends 8+ hours/week on admin (scraping, cover letters, tracking)
- **Motivations:** 
  - Faster job search with higher quality
  - Tailored applications that highlight fit
  - Peace of mind with centralized tracking
- **Expected value:** Save 5–6 hours/week; increase interview rate by 3x
- **Budget:** $10–25/month for a product they use regularly

### Persona 2: "Fresh Graduate" (Secondary)
- **Name:** Jordan, 22–26
- **Background:** Recently graduated; entry-level position hunting
- **Pain Points:**
  - Overwhelmed by choice of platforms and application mechanics
  - No template for effective cover letters
  - Fear of forgetting follow-ups
- **Motivations:**
  - Structured, guided process
  - Professional letter generation
  - Confidence in not missing opportunities
- **Expected value:** Land first role faster; gain credibility with polished applications
- **Budget:** $5–15/month (price-sensitive)

### Persona 3: "Power User / Career Manager" (Tertiary)
- **Name:** Sam, 35–45
- **Background:** Mid-to-senior career move; strategic job search
- **Pain Points:**
  - Selective applications to high-impact roles only
  - Complex tracking across internal mobility, external recruiting agencies, direct referrals
  - Data-driven decision making on timing, salary, company culture fit
- **Motivations:**
  - Comprehensive insights & analytics
  - Advanced filtering on company/culture/growth
  - Integration with existing tools (calendars, email)
- **Expected value:** Optimize every application; strategic career decisions
- **Budget:** $25–50/month for premium features

---

## 5. Feature Requirements

### 5.1 Core Features (MVP)

#### Feature 1: Multi-Source Job Ingestion
**User Story:** "As a job seeker, I want JobFlow to automatically pull new job listings from multiple sources so I don't have to manually check each platform daily."

| Aspect | Requirement |
|--------|-------------|
| **Data Sources** | Indeed, StepStone, LinkedIn (if possible; fallback: email alerts), custom CSV import |
| **Refresh Frequency** | Every 6–12 hours |
| **Data Captured** | Title, company, location, employment type (full-time, internship, contract), job description, salary (if available), URL, company logo, posting date |
| **Deduplication** | Detect duplicate listings across sources by URL + title + company |
| **Error Handling** | Graceful handling of scraper failures; queue retries; notify user if source unavailable |
| **Constraints** | Respect robots.txt, rate limits, and TOS of job boards; no login bypass or CAPTCHA breaker |

**Acceptance Criteria:**
- [ ] Job listings from 3+ sources visible in JobFlow dashboard within 12 hours of posting
- [ ] No duplicate jobs in user's feed
- [ ] Data quality >95% (fields populated, no corruption)
- [ ] <5% false negatives (jobs missed due to scraper failure)

---

#### Feature 2: Smart Filtering & Ranking
**User Story:** "As a job seeker, I want to define search criteria once and have JobFlow show only relevant jobs, ranked by fit, so I only see opportunities worth my time."

| Aspect | Requirement |
|--------|-------------|
| **Filter Dimensions** | Location, employment type, position type (entry-level, mid, senior), salary range, company size, remote/hybrid, tech stack, industry, keywords |
| **Saved Searches / Pipelines** | User can create multiple pipelines (e.g., "Python engineer roles," "product manager—startups") |
| **Ranking / Scoring** | LLM-based scoring: resume fit (0–100) based on user's skills vs. JD + manual preference weights |
| **Learning** | Optional: track which jobs user clicks/applies to → improve ranking over time (future: ML model) |
| **Output** | "To apply," "Maybe," "Skip" suggestions; override controls |
| **Performance** | <2 sec to re-rank 100 jobs after filter change |

**Acceptance Criteria:**
- [ ] User can save 5+ distinct search pipelines
- [ ] Ranking shows top 10 jobs with >70% relevance (self-assessed by user)
- [ ] Filtering + ranking pipeline runs in <2 sec
- [ ] Users can override/tweak ranking manually

---

#### Feature 3: AI-Powered Motivation Letter Generation
**User Story:** "As a job seeker, I want JobFlow to generate a tailored motivation letter for each job using my resume and the job description, so I can save time and improve my chances without sounding generic."

| Aspect | Requirement |
|--------|-------------|
| **Input Data** | User resume (PDF/text upload or resume.io import), job description, user's cover letter template(s) |
| **LLM Integration** | OpenAI GPT-4 or equivalent for generation |
| **Customization** | Letter tone (formal, casual), length (short, standard, long), language (English, DE, etc.) |
| **Output Options** | Plain text, Google Doc (auto-saved), PDF, email draft |
| **Versioning** | Store generated letters; user can regenerate, edit, and track versions |
| **Cost Management** | ~$0.01–0.05 per letter; track usage per user; implement rate limits (10/day for free, unlimited for paid) |
| **Legal / Compliance** | Disclose AI usage in letter; provide user option to review before sending; no false claims |

**Acceptance Criteria:**
- [ ] Generated letter is >80% unique per job (no template repetition)
- [ ] Letter generation takes <10 sec
- [ ] User satisfaction (rating) >4.0/5 for letter quality
- [ ] Letter can be exported to all major formats (text, PDF, Google Docs)

---

#### Feature 4: Unified Application Tracking Dashboard
**User Story:** "As a job seeker, I want a single dashboard showing all my job applications—status, company, date applied, follow-up notes—so I never lose track of where I stand."

| Aspect | Requirement |
|--------|-------------|
| **Data Model** | Job offer, application status, date applied, last updated, motivation letter link, notes, recruiter contact, next follow-up date |
| **Status Workflow** | New → To Apply → Applied → Interview (phone/video/in-person) → Offer/Rejected → Closed |
| **Views** | Table (sortable, filterable), Kanban (by status), Timeline (by application date), Analytics (summary stats) |
| **Notifications** | Email reminders for follow-ups, interview dates; in-app notifications for new matches |
| **Integration** | Sync with Gmail for incoming recruiter emails; optional Slack notifications |
| **Manual Entry** | User can add applications found outside JobFlow |
| **Export** | Download application list as CSV or PDF |

**Acceptance Criteria:**
- [ ] Dashboard loads in <2 sec with 50+ applications
- [ ] All CRUD operations (create, read, update, delete) work smoothly
- [ ] Email reminders sent accurately for scheduled follow-ups
- [ ] User can switch views without data loss

---

#### Feature 5: Authentication & User Management
**User Story:** "As a user, I want to create an account, log in securely, and have my data persist so I can use JobFlow across multiple devices without re-entering data."

| Aspect | Requirement |
|--------|-------------|
| **Sign-up** | Email + password or OAuth (Google, LinkedIn) |
| **Password** | Bcrypt hashing, minimum 8 characters, optional 2FA |
| **Session** | JWT tokens, 30-day expiry, refresh token rotation |
| **Data Isolation** | Per-user data access; no cross-user leakage |
| **GDPR** | Right to delete account + associated data within 30 days |
| **Account Settings** | Preferences (email frequency, timezone, language), API key generation (for power users), billing info |

**Acceptance Criteria:**
- [ ] Account creation & login work flawlessly
- [ ] Sessions persist across browser restarts
- [ ] User data fully deleted after account deletion request
- [ ] No auth vulnerabilities (tested via OWASP Top 10)

---

### 5.2 Phase 2 Features (Post-MVP, Q2–Q3 2026)

#### Feature 6: Email Sync & Recruiter Communication Tracking
**User Story:** "As a job seeker, I want JobFlow to monitor my Gmail for recruiter emails and auto-link them to applications, so I can see the full conversation timeline without manual copying."

| Aspect | Requirement |
|--------|-------------|
| **Gmail Integration** | OAuth 2.0 integration; read-only access to inbox; search for recruiter/company emails |
| **Auto-linking** | Match email to application by sender domain + company name |
| **Conversation Thread** | Display email timeline alongside application status |
| **Follow-up Trigger** | Alert if no response after N days; suggest follow-up actions |
| **Privacy** | Only index recruiter emails; don't store full email bodies; comply with Gmail ToS |

---

#### Feature 7: Advanced Analytics & Insights
**User Story:** "As a power user, I want analytics on my job search performance—response rate by company, time-to-interview, success rate by job type—so I can optimize my strategy."

| Aspect | Requirement |
|--------|-------------|
| **Metrics** | Application rate (per week), response rate (%), interview rate (%), offer rate (%), average time-to-response, offer salary distribution |
| **Segmentation** | By company size, industry, tech stack, location, employment type |
| **Trends** | Week-over-week application volume, month-over-month response rate |
| **Benchmarking** | Compare user's metrics to anonymized aggregate data (optional, privacy-preserving) |
| **Export** | Charts exportable to PDF/PNG; data to CSV |

---

#### Feature 8: Browser Extension (Optional)
**User Story:** "As a frequent job board browser, I want a browser extension that captures a job listing with one click and sends it to JobFlow, so I don't interrupt my browsing flow."

| Aspect | Requirement |
|--------|-------------|
| **Functionality** | One-click capture of job title, company, URL, and description; preview in sidebar |
| **Auto-fill** | Extract job data from page DOM (parse job board HTML) |
| **Sync** | Send to JobFlow backend; appear in dashboard instantly |
| **Supported Browsers** | Chrome, Firefox, Safari |

---

### 5.3 Out of Scope (Won't Do - MVP)

- Direct application submission (e.g., auto-filling forms, clicking "Apply" button) → too risky legally/ToS-wise
- Interview scheduling or calendar sync → separate tool; can integrate later
- CV optimization / ATS keyword matching → future feature
- Salary negotiation coaching → out of scope
- Job board search UI (own Elasticsearch, etc.) → use external APIs + filtering
- Mobile native apps (iOS/Android) → web-responsive design first

---

## 6. User Flows & Interaction Design

### 6.1 Core User Journey: "New User Onboarding & First Search"

```
1. Sign Up (email + password or OAuth)
   ↓
2. Resume Upload (PDF or text; or import from resume.io)
   ↓
3. Create First Pipeline (select filters: location, role type, tech stack, remote?)
   ↓
4. View Matching Jobs (ranked by fit; ~20–50 initial results)
   ↓
5. Review Top Job; See Generated Motivation Letter
   ↓
6. Click "Mark as Applied" → Auto-populate dashboard entry with timestamp
   ↓
7. Email motivation letter to user / export as PDF
   ↓
8. View Application Tracker Dashboard (shows 1 application)
   ↓
9. Set Follow-up Reminder (7 days)
   ↓
10. Explore UI: other pipelines, analytics, settings
```

**Time to first action:** 5–8 minutes

### 6.2 Repeat User Journey: "Daily / Weekly Check-In"

```
1. Log in (or stay logged in)
   ↓
2. View "New Matches" section (jobs matching any of user's pipelines)
   ↓
3. Scan list; click on 3–5 interesting jobs
   ↓
4. Review generated motivation letter for each; adjust tone if needed
   ↓
5. Click "Generate & Send Letter to Email" for each
   ↓
6. Dashboard auto-updates applications to "Applied"
   ↓
7. Check "Follow-ups Needed" section; send brief follow-up emails to 2–3 companies
   ↓
8. View analytics: "20 applications this week; 2 interviews scheduled"
```

**Time per session:** 10–20 minutes, 3–5x per week

### 6.3 Wireframe / UI Sketch Placeholders

*(These are described in text; actual Figma/design mockups to be created in design phase)*

**Main Dashboard:**
- Top nav: Logo, user name, settings, logout
- Left sidebar: "New Matches" (badge count), "Applications," "Pipelines," "Analytics," "Settings"
- Main content: 
  - "New Matches" tab: Grid/list of 10–20 jobs with rank score, company logo, title, location, "View Letter" / "Apply" buttons
  - "Applications" tab: Kanban board (columns: New, To Apply, Applied, Interview, Offer, Rejected) with card per application
  - "Analytics" tab: Summary stats (applications/week, response rate, etc.) + charts

**Letter Generation Modal:**
- Shows job title, company, and "suggested" letter
- Button to regenerate with different tone
- Preview + edit text box
- "Copy to Clipboard," "Send to Email," "Export as PDF"

---

## 7. Technical Architecture & Requirements

### 7.1 System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interfaces                         │
│  - Web Dashboard (React/Next.js)                            │
│  - Browser Extension (Chrome/Firefox)                        │
└──────────────────┬──────────────────────────────────────────┘
                   │ HTTPS / REST API
┌──────────────────▼──────────────────────────────────────────┐
│              FastAPI Backend (Python)                        │
│  - Authentication (JWT, OAuth)                              │
│  - Job Management (ingest, filter, rank)                    │
│  - Application Tracking (CRUD)                              │
│  - LLM Integration (cover letter generation)                │
│  - Email & integrations (Gmail sync, webhooks)              │
└──────────────────┬──────────────────────────────────────────┘
                   │
       ┌───────────┼────────────┬──────────────┐
       ▼           ▼            ▼              ▼
   PostgreSQL   Redis       OpenAI API    Job Board APIs
   (data)      (cache)      (GPT-4)       (Indeed, etc.)
```

### 7.2 Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Frontend** | Next.js 14 + React 18 | Type-safe, SSR, great DX, scales to product UI |
| **Backend** | FastAPI (Python) | Async, type hints, excellent ORM + DB integration, fast to iterate |
| **Database** | PostgreSQL 15+ | ACID, JSONB support, excellent for relational + semi-structured data |
| **Cache** | Redis | Session storage, rate limiting, job ranking cache |
| **Job Queue** | Celery + Redis | Async tasks (email, scraping, LLM calls) |
| **Scraping** | Requests + BeautifulSoup / Playwright | Python ecosystem; Playwright for dynamic sites if needed |
| **LLM** | OpenAI API (GPT-4) | Quality, reliability, cost-effective for MVP |
| **Auth** | JWT + OAuth2 | Industry standard, secure, multi-provider support |
| **Hosting** | Docker + Kubernetes (or managed platform like Render/Railway) | Scalable, reproducible, DevOps-friendly |
| **Monitoring** | Sentry, DataDog (or Prometheus + Grafana) | Error tracking, performance monitoring |
| **CI/CD** | GitHub Actions + Docker | Automated testing, staging, production deployment |

### 7.3 Database Schema (Core Tables)

```sql
-- Users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR,
  oauth_provider VARCHAR,
  oauth_id VARCHAR,
  resume_text TEXT,
  timezone VARCHAR DEFAULT 'UTC',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Pipelines (saved searches)
CREATE TABLE pipelines (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  name VARCHAR NOT NULL,
  filters JSONB, -- { location, tech_stack, min_salary, max_salary, remote, ... }
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Job Offers
CREATE TABLE job_offers (
  id SERIAL PRIMARY KEY,
  source VARCHAR NOT NULL, -- 'indeed', 'stepstone', etc.
  external_id VARCHAR, -- ID from job board
  title VARCHAR NOT NULL,
  company VARCHAR NOT NULL,
  location VARCHAR,
  employment_type VARCHAR, -- 'full-time', 'internship', etc.
  url VARCHAR UNIQUE NOT NULL,
  raw_description TEXT,
  metadata JSONB, -- { salary_min, salary_max, company_logo, ... }
  scraped_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Applications (user's applications)
CREATE TABLE applications (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  job_offer_id INTEGER NOT NULL REFERENCES job_offers(id),
  status VARCHAR DEFAULT 'new', -- 'new', 'to_apply', 'applied', 'interview', 'rejected', 'offer'
  applied_at TIMESTAMP,
  motivation_letter_text TEXT,
  motivation_letter_url VARCHAR,
  notes TEXT,
  follow_up_date TIMESTAMP,
  recruiter_name VARCHAR,
  recruiter_email VARCHAR,
  last_update_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, job_offer_id) -- prevent duplicate applications
);

-- Generated Letters (history)
CREATE TABLE generated_letters (
  id SERIAL PRIMARY KEY,
  application_id INTEGER NOT NULL REFERENCES applications(id),
  user_id INTEGER NOT NULL REFERENCES users(id),
  job_offer_id INTEGER NOT NULL REFERENCES job_offers(id),
  letter_text TEXT NOT NULL,
  tone VARCHAR, -- 'formal', 'casual', etc.
  length VARCHAR, -- 'short', 'standard', 'long'
  llm_model VARCHAR, -- 'gpt-4', etc.
  tokens_used INTEGER,
  cost_cents DECIMAL(10,2),
  generated_at TIMESTAMP DEFAULT NOW()
);

-- Email Sync Events (Gmail)
CREATE TABLE email_sync_events (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  gmail_message_id VARCHAR,
  from_email VARCHAR,
  from_name VARCHAR,
  subject VARCHAR,
  body_excerpt TEXT,
  linked_application_id INTEGER REFERENCES applications(id),
  received_at TIMESTAMP,
  synced_at TIMESTAMP DEFAULT NOW()
);
```

### 7.4 API Endpoints (MVP)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/auth/signup` | POST | Register new user |
| `/auth/login` | POST | Authenticate user |
| `/auth/logout` | POST | Invalidate session |
| `/auth/me` | GET | Fetch current user data |
| `/users/{id}/resume` | PUT | Upload/update resume |
| `/pipelines` | GET, POST | List/create saved searches |
| `/pipelines/{id}` | PUT, DELETE | Update/delete pipeline |
| `/jobs` | GET | List jobs (with filters applied) |
| `/jobs/{id}/score` | GET | Get ML/LLM score for a job |
| `/jobs/{id}/generate-letter` | POST | Generate motivation letter |
| `/applications` | GET, POST | List/create applications |
| `/applications/{id}` | GET, PUT, DELETE | View/update/delete application |
| `/applications/{id}/letter` | GET | Fetch saved motivation letter |
| `/applications/{id}/follow-up` | POST | Schedule follow-up |
| `/analytics/summary` | GET | Get KPI summary (week/month) |
| `/integrations/gmail/callback` | GET | OAuth callback for Gmail |
| `/integrations/gmail/sync` | POST | Trigger Gmail sync |

### 7.5 Performance & Scalability

| Requirement | Target | Implementation |
|-------------|--------|-----------------|
| **API response time (p95)** | <500ms | Database indexing, caching, async processing |
| **Job listing refresh** | Every 6–12 hours | Celery background job, queue-based ingestion |
| **Concurrent users** | 10K+ on day 1 | Horizontal scaling (Kubernetes), stateless API |
| **Data freshness** | <12h for listings | Scheduled scraper; deduplication |
| **Storage** | <500GB year 1 | PostgreSQL with partitioning if needed |
| **LLM cost efficiency** | <$0.05 per letter | Prompt optimization, caching, batching |

### 7.6 Security & Compliance

| Requirement | Implementation |
|-------------|-----------------|
| **Data encryption** | TLS 1.3 in transit; AES-256 for sensitive fields at rest |
| **Authentication** | JWT + optional 2FA; no password storage in plain text |
| **Authorization** | RBAC (role-based access control); users only see own data |
| **GDPR** | Right to delete; data portability endpoint; privacy policy + DPA |
| **CCPA** | Right to know, delete, opt-out; privacy notice |
| **PCI DSS** | If accepting payments: Stripe integration (handled by Stripe) |
| **API rate limiting** | 100 req/min per user; 1000 req/min per IP |
| **Input validation** | Pydantic schemas; SQL injection prevention via ORM |
| **Logging & monitoring** | All auth events logged; no sensitive data in logs |
| **Third-party risks** | OpenAI API calls logged; Gmail OAuth scoped narrowly |

---

## 8. Roadmap & Release Strategy

### Phase 1: MVP (Q1–Q2 2026, 12 weeks)
**Goal:** Validate core value proposition with early adopters.

| Week | Milestone | Deliverables |
|------|-----------|--------------|
| 1–2 | Scaffolding | FastAPI project, PostgreSQL schema, basic auth |
| 3–4 | Job ingestion | Scraper for 1 source (Indeed); deduplication; storage |
| 5–6 | Filtering & ranking | Pipeline UI; basic LLM scoring |
| 7–8 | Letter generation | OpenAI integration; letter UI; export |
| 9–10 | Application tracker | Dashboard; status workflow; notes |
| 11–12 | Testing & polish | Load testing; security audit; UX polish; beta launch |

**Beta Release Criteria:**
- [ ] 3+ job sources working
- [ ] <2% scraper failure rate
- [ ] <5 sec to generate letter
- [ ] 50+ beta users signed up
- [ ] NPS >30

### Phase 2: Early Adopter (Q2–Q3 2026, 8 weeks)
**Goal:** Refine based on feedback; add integrations.

- Add 2 more job sources (LinkedIn, others)
- Gmail sync & email tracking
- Improved LLM prompts (50+ templates by company type)
- Advanced filtering (company size, culture fit)
- Analytics MVP (application rate, response rate)

### Phase 3: General Availability (Q4 2026, 12 weeks)
**Goal:** Broader market launch; freemium model.

- Browser extension
- Advanced analytics + benchmarking
- Multi-language support
- API docs for power users
- Billing + pricing tiers

### Phase 4: Scale (2027+)
- Additional integrations (Slack, Calendar, HubSpot)
- AI interview prep module
- Candidate pooling / talent marketplace
- Enterprise features (team management)

---

## 9. Go-to-Market Strategy

### 9.1 Positioning
**"Land the right job faster."**  
For job seekers tired of wasting time on irrelevant applications and repetitive cover letters.

### 9.2 Pricing Model (Freemium)

| Tier | Price | Features | Target User |
|------|-------|----------|-------------|
| **Free** | $0/mo | 5 applications/mo, 1 pipeline, basic letter generation, no email sync | Casual job seeker |
| **Professional** | $12/mo | Unlimited applications, 5 pipelines, advanced filtering, email sync, full analytics | Active job seeker |
| **Premium** | $29/mo | Everything in Pro + API access, priority support, custom integrations, 50% discount on extra LLM tokens | Power user / recruiter |

**Rationale:**
- Freemium captures users; free tier demonstrates value.
- Monthly subscription model; low churn expected if product delivers.
- CAC <$15 means payback period <1 month for Pro tier.

### 9.3 Acquisition Channels (Launch Phase)

| Channel | Tactics | Expected Reach |
|---------|---------|-----------------|
| **Organic / SEO** | Blog posts ("How to Apply to 50 Jobs Efficiently"), Reddit, Product Hunt | 200–500 signups / month |
| **Communities** | r/jobsearch, r/recruiting, Discord communities for career changers | 100–300 signups |
| **Direct outreach** | Email to bootcamp graduates, university career offices | 50–100 signups |
| **Referral** | Friend referral bonus (free month for both) | 50–200 signups |
| **Paid (later)** | Google Ads, LinkedIn ads | Scale to 1K signups / month in Q3 |

**Y1 Goal:** 500 paid subscribers by end of year.

### 9.4 Metrics to Track

- **Acquisition:** Signups, free-to-paid conversion (target: 5–10%)
- **Activation:** First 10 minutes: resume uploaded, first pipeline created, first application tracked
- **Engagement:** MAU/DAU, applications per user, letters generated
- **Retention:** Monthly churn rate (target: <10%)
- **Revenue:** MRR (monthly recurring revenue), ARPU (average revenue per user)
- **Satisfaction:** NPS, support ticket volume, feature request trends

---

## 10. Success Criteria & Key Milestones

### MVP Launch (End Q2 2026)
- [ ] 50+ beta users actively using platform
- [ ] Average 10+ applications logged per user
- [ ] Uptime >98%
- [ ] NPS ≥30
- [ ] <10% critical bugs
- [ ] GDPR compliance audit passed

### General Availability (End Q4 2026)
- [ ] 500 paid subscribers
- [ ] 60% retention rate (month-over-month)
- [ ] 5+ job sources integrated
- [ ] Free tier has >2000 users
- [ ] Browser extension >1000 installs
- [ ] Customer acquisition cost <$15
- [ ] NPS ≥45

### End of Year 1 (End Q4 2026)
- [ ] $5K+ monthly recurring revenue (MRR)
- [ ] 1000+ paying subscribers
- [ ] <10% monthly churn
- [ ] Available in 3+ languages
- [ ] 99.5% uptime
- [ ] Product is self-sustaining (revenue > operational costs)

---

## 11. Risks & Mitigation

| Risk | Severity | Mitigation |
|------|----------|-----------|
| **Job board ToS violations** | High | Legal review; stay within fair use; focus on public scraping + APIs; clear TOS for JobFlow |
| **LLM cost spiral** | Medium | Monitor token usage; cache responses; optimize prompts; implement rate limits |
| **User privacy / data breaches** | High | Security audit; GDPR compliance; encryption; DPA with OpenAI; insurance |
| **Poor job match quality** | Medium | Iterate on LLM prompts; gather user feedback; A/B test scoring; build ML model |
| **Low adoption / product-market fit** | High | Early beta validation; talk to users weekly; iterate fast; pivot if needed |
| **Competitor entry** | Medium | Build strong network effects (community, referrals); deepen integrations; improve UX |
| **Dependency on OpenAI** | Medium | Evaluate Claude, local models as backup; implement fallback letter templates |
| **Scaling job scraping** | Medium | Invest in resilient infra; use managed scraping services (Apify) if needed; monitor failures |
| **GDPR / hiring law changes** | Low | Monitor regulation; legal consul on retention, non-discrimination, automated decisions |

---

## 12. Assumptions

**Business Assumptions:**
- Job seekers will pay $10–30/mo for a quality tool that saves 5+ hours/week.
- Email + password registration is sufficient for MVP (OAuth can come later).
- Freemium model will lead to 5–10% free-to-paid conversion.

**Technical Assumptions:**
- Python + FastAPI can handle 10K concurrent users with standard infrastructure.
- Postgres can store 10+ years of job listings (500M+) with proper indexing.
- OpenAI API will remain reliable; cost per letter stays under $0.05.
- Job board scraping will remain legally feasible if following ToS.

**User Assumptions:**
- Active job seekers spend 5–10 hours/week on applications (validated by surveys).
- Users prefer tailored letters over generic ones.
- Users trust AI-generated letters with manual review option.
- Email-based notifications are preferred over push/SMS.

---

## 13. Out of Scope (For MVP)

- Direct form-filling / auto-submission to job boards (ToS risk)
- Interview scheduling (out of MVP scope; future integration)
- Salary negotiation coaching (separate product idea)
- ATS keyword optimization (future; partner integration)
- Mobile native apps (web-responsive design sufficient)
- Multilingual support (English-only for MVP)
- Interview prep / coding challenges (separate scope)

---

## 14. Glossary

| Term | Definition |
|------|-----------|
| **Pipeline** | A saved search with filters; multiple per user |
| **Application** | A record of a job the user has applied to (or marked for application) |
| **Motivation Letter** | AI-generated cover letter tailored to a job posting |
| **Scraping** | Automated extraction of job data from public job boards |
| **Deduplication** | Identifying and merging duplicate job listings across sources |
| **Email Sync** | Automatic linking of recruiter emails to applications |
| **Uptime** | Percentage of time the service is available to users |
| **NPS** | Net Promoter Score; measure of user satisfaction (0–100) |
| **MRR** | Monthly Recurring Revenue; sum of all active subscriptions per month |
| **Churn** | Percentage of users who cancel subscription in a given period |

---

## 15. Document History & Approvals

| Version | Date | Author | Changes | Status |
|---------|------|--------|---------|--------|
| 1.0 | Dec 8, 2025 | Product Team | Initial draft | DRAFT → Review |
| — | — | — | — | — |

**Next Steps:**
1. Stakeholder review & feedback (1–2 weeks)
2. Engineering estimation & feasibility review
3. Design mockups & user flow validation
4. Budget & resource allocation
5. Kick-off engineering phase

---

**End of Document**

---

## Appendix: Competitive Analysis (Brief)

| Product | Strengths | Weaknesses | Opportunity |
|---------|-----------|-----------|-------------|
| **LinkedIn Easy Apply** | Integrated into platform; reduces friction | Generic; no personalization; limited filtering | JobFlow adds customization + tracking |
| **DIY n8n workflows** | Highly customizable | Requires technical skill; no UI; no support | JobFlow: easy UX + support |
| **ChatGPT prompts + spreadsheets** | Free; flexible | Manual; scattered; no tracking | JobFlow: unified, automated platform |
| **Recruiting agencies** | Human touch; networking | Expensive (fee-based); slower | JobFlow: DIY + self-service |

**Why JobFlow wins:** Combines **ease of use** (no coding), **personalization** (AI-driven), **efficiency** (multi-source + automation), and **affordability** (SaaS pricing).

