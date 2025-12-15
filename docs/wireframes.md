# Wireframes & UI Specifications
## JobFlow - Job Application Automation Platform

**Document Version:** 1.0  
**Last Updated:** December 2025  
**Author:** Design & Engineering Team

---

## Table of Contents
1. [Layout Structure](#layout-structure)
2. [Authentication Pages](#authentication-pages)
3. [Onboarding Flow](#onboarding-flow)
4. [Dashboard](#dashboard)
5. [Job Listings](#job-listings)
6. [Application Tracking](#application-tracking)
7. [Pipeline Management](#pipeline-management)
8. [Letter Generation](#letter-generation)
9. [Analytics Dashboard](#analytics-dashboard)
10. [Settings](#settings)
11. [Mobile Responsive Design](#mobile-responsive-design)

---

## Layout Structure

### Main Application Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  JobFlow Logo                    [Search...]    [Notifications] [Avatar] │
├──────────┬──────────────────────────────────────────────────────────────┤
│          │                                                               │
│ Sidebar  │                    Main Content Area                          │
│          │                                                               │
│ • New    │                                                               │
│   Matches│                                                               │
│   (12)   │                                                               │
│          │                                                               │
│ • Jobs   │                                                               │
│          │                                                               │
│ •        │                                                               │
│   Applica│                                                               │
│   tions  │                                                               │
│          │                                                               │
│ •        │                                                               │
│   Pipelin│                                                               │
│   es     │                                                               │
│          │                                                               │
│ •        │                                                               │
│   Analyti│                                                               │
│   cs     │                                                               │
│          │                                                               │
│ •        │                                                               │
│   Setting│                                                               │
│   s      │                                                               │
│          │                                                               │
└──────────┴──────────────────────────────────────────────────────────────┘
```

**Sidebar Specifications:**
- Width: 240px (desktop), collapsible to 64px
- Fixed position on left
- Badge counts for "New Matches" and notifications
- Active state highlighting
- Mobile: Hamburger menu, overlay sidebar

**Header Specifications:**
- Height: 64px
- Fixed position at top
- Search bar: 400px width, centered
- Right side: Notifications bell (with badge) + User avatar dropdown

---

## Authentication Pages

### 1. Landing Page

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│                          [JobFlow Logo]                                  │
│                                                                           │
│                    "Automate your job search.                            │
│                     Land the right role faster."                         │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │  [Hero Image: Dashboard Preview]                                 │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌──────────────┐  ┌──────────────┐                                     │
│  │  Get Started │  │  Learn More  │                                     │
│  └──────────────┘  └──────────────┘                                     │
│                                                                           │
│  Features:                                                                │
│  • Multi-source job aggregation                                          │
│  • AI-powered letter generation                                          │
│  • Application tracking                                                  │
│  • Smart filtering & ranking                                             │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Pricing                                                         │   │
│  │  Free | Professional $12/mo | Premium $29/mo                    │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2. Sign Up Page

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│                          [JobFlow Logo]                                  │
│                                                                           │
│                    Create your account                                   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │  Email Address                                                    │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ user@example.com                                          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Password                                                         │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ ••••••••••                                                │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  [Show password]  Password must be at least 8 characters        │   │
│  │                                                                   │   │
│  │  Confirm Password                                                │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ ••••••••••                                                │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  Create Account                                            │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  ────────────────  or  ────────────────                          │   │
│  │                                                                   │   │
│  │  ┌──────────────┐  ┌──────────────┐                             │   │
│  │  │ [G] Continue │  │ [in] Continue│                             │   │
│  │  │  with Google │  │  with LinkedIn│                            │   │
│  │  └──────────────┘  └──────────────┘                             │   │
│  │                                                                   │   │
│  │  Already have an account? [Sign In]                              │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Form validation on blur
- Password strength indicator
- OAuth buttons with provider icons
- Error messages inline below fields
- Loading state on submit button

### 3. Login Page

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│                          [JobFlow Logo]                                  │
│                                                                           │
│                    Welcome back                                          │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │  Email Address                                                    │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ user@example.com                                          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Password                                                         │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ ••••••••••                                                │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  [Show password]  [Forgot password?]                            │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  Sign In                                                   │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  ────────────────  or  ────────────────                          │   │
│  │                                                                   │   │
│  │  ┌──────────────┐  ┌──────────────┐                             │   │
│  │  │ [G] Continue │  │ [in] Continue│                             │   │
│  │  │  with Google │  │  with LinkedIn│                            │   │
│  │  └──────────────┘  └──────────────┘                             │   │
│  │                                                                   │   │
│  │  Don't have an account? [Sign Up]                                │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Onboarding Flow

### Step 1: Welcome Screen

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  [Progress: ●○○○]  Step 1 of 4                                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │              Welcome to JobFlow! 👋                               │   │
│  │                                                                   │   │
│  │  We'll help you automate your job search and land your           │   │
│  │  dream role faster. Let's get started!                           │   │
│  │                                                                   │   │
│  │  What we'll set up:                                               │   │
│  │  ✓ Upload your resume                                            │   │
│  │  ✓ Create your first job search pipeline                         │   │
│  │  ✓ Find matching jobs                                            │   │
│  │  ✓ Generate your first motivation letter                         │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  Get Started                                              │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Step 2: Resume Upload

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  [Progress: ●●○○]  Step 2 of 4                                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │              Upload Your Resume                                   │   │
│  │                                                                   │   │
│  │  We'll use your resume to generate personalized                  │   │
│  │  motivation letters for each job application.                    │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │                                                           │  │   │
│  │  │              📄                                           │  │   │
│  │  │                                                           │  │   │
│  │  │        Drag & drop your resume here                       │  │   │
│  │  │        or click to browse                                 │  │   │
│  │  │                                                           │  │   │
│  │  │        Supported: PDF, DOC, DOCX, TXT                     │  │   │
│  │  │        Max size: 5MB                                      │  │   │
│  │  │                                                           │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Or import from: [resume.io] [LinkedIn]                         │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  [Skip for now]  [Continue]                               │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

**After Upload:**
- Show resume preview
- Extract key information (name, email, skills, experience)
- Allow editing of extracted data
- "Continue" button enabled

### Step 3: Create First Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  [Progress: ●●●○]  Step 3 of 4                                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │              Create Your First Pipeline                           │   │
│  │                                                                   │   │
│  │  Pipelines help us find jobs that match your preferences.        │   │
│  │                                                                   │   │
│  │  Pipeline Name                                                    │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Python Backend Developer                                   │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Location                                                         │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ [Berlin, Germany ▼]  [Remote ▼]                          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Job Type                                                         │   │
│  │  ☑ Full-time  ☐ Part-time  ☐ Contract  ☐ Internship            │   │
│  │                                                                   │   │
│  │  Tech Stack / Keywords                                            │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Python  FastAPI  React  [×]                               │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  Type to add keywords...                                         │   │
│  │                                                                   │   │
│  │  Salary Range (optional)                                         │   │
│  │  ┌──────────┐  to  ┌──────────┐                                │   │
│  │  │ €60,000  │      │ €100,000 │                                │   │
│  │  └──────────┘      └──────────┘                                │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  Create Pipeline                                          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Step 4: Onboarding Complete

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│  [Progress: ●●●●]  Step 4 of 4                                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │              🎉 You're all set!                                   │   │
│  │                                                                   │   │
│  │  We're finding jobs that match your pipeline.                    │   │
│  │  This may take a few minutes...                                  │   │
│  │                                                                   │   │
│  │  [Loading spinner]                                               │   │
│  │                                                                   │   │
│  │  Meanwhile, you can:                                             │   │
│  │  • Explore the dashboard                                         │   │
│  │  • Create additional pipelines                                   │   │
│  │  • Review your profile settings                                  │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  Go to Dashboard                                          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Dashboard

### Main Dashboard - New Matches View

```
┌─────────────────────────────────────────────────────────────────────────┐
│  JobFlow  [Search jobs...]                    🔔(3)  [Avatar ▼]         │
├──────────┬──────────────────────────────────────────────────────────────┤
│          │                                                               │
│ New      │  New Matches (12)                                            │
│ Matches  │  ────────────────────────────────────────────────────────    │
│ (12)     │                                                               │
│          │  ┌─────────────────────────────────────────────────────┐    │
│ Jobs     │  │ [Company Logo]  Senior Python Developer              │    │
│          │  │ TechCorp • Berlin, Germany • Full-time              │    │
│ Applica- │  │ ⭐ Fit Score: 92%                                    │    │
│ tions    │  │                                                       │    │
│          │  │ Python, FastAPI, React, PostgreSQL...                │    │
│ Pipelines│  │                                                       │    │
│          │  │ [View Details]  [Generate Letter]  [Mark Applied]   │    │
│ Analytics│  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│ Settings │  ┌─────────────────────────────────────────────────────┐    │
│          │  │ [Company Logo]  Backend Engineer                     │    │
│          │  │ StartupXYZ • Remote • Full-time                     │    │
│          │  │ ⭐ Fit Score: 88%                                    │    │
│          │  │                                                       │    │
│          │  │ FastAPI, Docker, AWS, Microservices...               │    │
│          │  │                                                       │    │
│          │  │ [View Details]  [Generate Letter]  [Mark Applied]   │    │
│          │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│          │  [Load More]  Showing 12 of 47 matches                       │
│          │                                                               │
└──────────┴──────────────────────────────────────────────────────────────┘
```

**Job Card Specifications:**
- Company logo (64x64px, fallback icon)
- Job title (bold, 18px)
- Company name, location, employment type
- Fit score badge (color-coded: 90+ green, 70-89 yellow, <70 gray)
- Tech stack tags (max 5, scrollable)
- Action buttons: View Details, Generate Letter, Mark Applied
- Hover state: Slight elevation, border highlight

### Dashboard - Filter Bar

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Filters:                                                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐  │
│  │ Pipeline:    │ │ Location:    │ │ Salary:      │ │ Sort by:     │  │
│  │ All Pipelines│ │ All Locations│ │ Any          │ │ Fit Score ▼  │  │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘  │
│                                                                           │
│  [Clear Filters]                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Job Listings

### Job Detail Modal

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ×                                                                        │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  [Company Logo]  Senior Python Developer                         │   │
│  │  TechCorp • Berlin, Germany • Full-time • €70k-90k              │   │
│  │  ⭐ Fit Score: 92%                                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  About the Role                                                  │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  We are looking for an experienced Python developer to join      │   │
│  │  our backend team. You will work on building scalable APIs       │   │
│  │  using FastAPI and PostgreSQL...                                 │   │
│  │                                                                   │   │
│  │  Requirements                                                     │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  • 3+ years of Python experience                                 │   │
│  │  • Experience with FastAPI or Flask                              │   │
│  │  • Knowledge of PostgreSQL                                       │   │
│  │  • Experience with Docker and AWS                                │   │
│  │                                                                   │   │
│  │  Tech Stack                                                       │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  [Python] [FastAPI] [PostgreSQL] [Docker] [AWS] [React]         │   │
│  │                                                                   │   │
│  │  [View Original Posting] →                                       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  [Generate Letter]  [Mark as Applied]  [Save for Later]         │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

**Modal Specifications:**
- Width: 800px (desktop), 100% (mobile)
- Scrollable content area
- Fixed action buttons at bottom
- Close button (X) in top-right
- Backdrop overlay (50% opacity)

---

## Application Tracking

### Applications - Kanban View

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Applications  [Kanban ▼] [Table] [Timeline]                            │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  New (3)    To Apply (5)    Applied (12)    Interview (2)    Offer (1)  │
│  ────────   ────────────    ────────────    ─────────────    ────────   │
│                                                                           │
│  ┌──────┐   ┌──────┐        ┌──────┐        ┌──────┐        ┌──────┐   │
│  │[Logo]│   │[Logo]│        │[Logo]│        │[Logo]│        │[Logo]│   │
│  │Python│   │React │        │Backend│       │Senior│        │Lead  │   │
│  │Dev   │   │Dev   │        │Engineer│      │Python│        │Engineer│ │
│  │      │   │      │        │        │      │      │        │        │ │
│  │TechCo│   │Startup│       │BigTech │      │ScaleUp│       │Unicorn│ │
│  │      │   │      │        │        │      │      │        │        │ │
│  │92%   │   │85%   │        │Applied │      │Phone │        │Offer  │ │
│  │      │   │      │        │2 days  │      │Interview│     │€95k   │ │
│  │      │   │      │        │ago     │      │Tomorrow│      │       │ │
│  └──────┘   └──────┘        └──────┘        └──────┘        └──────┘   │
│                                                                           │
│  ┌──────┐   ┌──────┐        ┌──────┐        ┌──────┐                   │
│  │[Logo]│   │[Logo]│        │[Logo]│        │[Logo]│                   │
│  │Full  │   │Node  │        │DevOps│        │Frontend│                 │
│  │Stack │   │Dev   │        │Engineer│      │Lead   │                 │
│  │      │   │      │        │        │      │       │                 │
│  │MidCo │   │Startup│       │CloudCo│      │TechCo │                 │
│  │      │   │      │        │        │      │       │                 │
│  │78%   │   │82%   │        │Applied │      │Applied│                 │
│  │      │   │      │        │1 week  │      │3 days │                 │
│  │      │   │      │        │ago     │      │ago    │                 │
│  └──────┘   └──────┘        └──────┘        └──────┘                   │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

**Kanban Card Specifications:**
- Width: 280px per column
- Card height: auto (min 120px)
- Drag & drop enabled
- Click to open detail view
- Color-coded by fit score
- Status badge on card

### Applications - Table View

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Applications  [Kanban] [Table ▼] [Timeline]                            │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ ☐ Job Title        Company    Status      Applied    Fit   Actions│ │
│  ├───────────────────────────────────────────────────────────────────┤ │
│  │ ☐ Senior Python    TechCorp   Applied     2d ago    92%   [⋯]    │ │
│  │ ☐ Backend Engineer BigTech    Interview   1w ago    88%   [⋯]    │ │
│  │ ☐ React Developer  Startup    To Apply    -         85%   [⋯]    │ │
│  │ ☐ Full Stack Dev   MidCo      Applied     3d ago    78%   [⋯]    │ │
│  │ ☐ Node.js Dev      Startup    Applied     5d ago    82%   [⋯]    │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  [Bulk Actions ▼]  [Export CSV]  Showing 1-5 of 23                      │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

**Table Specifications:**
- Sortable columns
- Row selection (checkbox)
- Bulk actions dropdown
- Responsive: Stack on mobile
- Pagination: 25 per page

### Application Detail View

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Back to Applications                                                  │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  [Company Logo]  Senior Python Developer                         │   │
│  │  TechCorp • Berlin, Germany • Full-time                          │   │
│  │  Status: [Applied ▼]  Applied 2 days ago                         │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Application Details                                             │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │  Applied Date: January 15, 2025                                  │   │
│  │  Follow-up Date: January 22, 2025                                │   │
│  │  Application Method: Manual                                      │   │
│  │                                                                   │   │
│  │  Motivation Letter                                               │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  [View Letter] [Download PDF] [Regenerate]                       │   │
│  │                                                                   │   │
│  │  Notes                                                            │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Great company culture, interesting tech stack...          │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  [Save Notes]                                                    │   │
│  │                                                                   │   │
│  │  Recruiter Contact                                               │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  Name: [John Doe                    ]                            │   │
│  │  Email: [john.doe@techcorp.com      ]                            │   │
│  │  Phone: [+49 30 12345678            ]                            │   │
│  │                                                                   │   │
│  │  Email Timeline (Gmail Sync)                                      │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │  • Jan 15 - Application confirmation email                       │   │
│  │  • Jan 16 - Thank you for your application                      │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Pipeline Management

### Pipelines List View

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Pipelines  [+ Create New Pipeline]                                      │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Python Backend Developer                                        │   │
│  │  Berlin, Remote • Full-time • Python, FastAPI                   │   │
│  │  47 matches • Last updated: 2 hours ago                         │   │
│  │  [Active ▼]  [View Jobs]  [Edit]  [Delete]                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  React Frontend Developer                                        │   │
│  │  Remote • Full-time • React, TypeScript                         │   │
│  │  23 matches • Last updated: 5 hours ago                         │   │
│  │  [Active ▼]  [View Jobs]  [Edit]  [Delete]                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Product Manager - Startups                                     │   │
│  │  Berlin, Munich • Full-time • Product, B2B                      │   │
│  │  12 matches • Last updated: 1 day ago                          │   │
│  │  [Paused ▼]  [View Jobs]  [Edit]  [Delete]                     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Create/Edit Pipeline Modal

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Create New Pipeline  ×                                                  │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │  Pipeline Name *                                                 │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Python Backend Developer                                   │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Description (optional)                                          │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Looking for Python backend roles in Berlin or remote...   │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  │  Location *                                                       │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ [Berlin, Germany ▼]  [+ Add Location]                     │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  ☑ Include remote positions                                     │   │
│  │                                                                   │   │
│  │  Employment Type *                                               │   │
│  │  ☑ Full-time  ☐ Part-time  ☐ Contract  ☐ Internship            │   │
│  │                                                                   │   │
│  │  Tech Stack / Keywords                                           │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │ Python  FastAPI  React  [×]                               │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │  Type to add keywords...                                         │   │
│  │                                                                   │   │
│  │  Salary Range (optional)                                         │   │
│  │  ┌──────────┐  to  ┌──────────┐                                │   │
│  │  │ €60,000  │      │ €100,000 │                                │   │
│  │  └──────────┘      └──────────┘                                │   │
│  │                                                                   │   │
│  │  Notification Settings                                           │   │
│  │  Frequency: [Daily ▼]  [Immediate] [Weekly]                     │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  [Cancel]  [Save Pipeline]                                │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Letter Generation

### Letter Generation Modal

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Generate Motivation Letter  ×                                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Job: Senior Python Developer at TechCorp                        │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │  Letter Settings                                                  │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │   │
│  │  │ Tone:        │  │ Length:      │  │ Language:    │          │   │
│  │  │ Professional │  │ Standard     │  │ English      │          │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘          │   │
│  │                                                                   │   │
│  │  ┌───────────────────────────────────────────────────────────┐  │   │
│  │  │  [Generate Letter]  Estimated cost: $0.03                 │  │   │
│  │  └───────────────────────────────────────────────────────────┘  │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  [Loading spinner] Generating your personalized letter...                │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Letter Preview & Edit

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Your Motivation Letter  ×                                               │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  [Regenerate]  [Edit]  [Export ▼]  [Save]                       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │  Dear Hiring Manager,                                            │   │
│  │                                                                   │   │
│  │  I am writing to express my strong interest in the Senior        │   │
│  │  Python Developer position at TechCorp. With over 5 years of     │   │
│  │  experience in Python development and a passion for building     │   │
│  │  scalable backend systems, I am excited about the opportunity    │   │
│  │  to contribute to your team.                                     │   │
│  │                                                                   │   │
│  │  In my current role at [Previous Company], I have successfully   │   │
│  │  developed and maintained REST APIs using FastAPI, working       │   │
│  │  with PostgreSQL databases and deploying applications on AWS.    │   │
│  │  My experience aligns perfectly with the requirements outlined   │   │
│  │  in your job posting...                                          │   │
│  │                                                                   │   │
│  │  [Editable text area - full content]                             │   │
│  │                                                                   │   │
│  │  Best regards,                                                    │   │
│  │  [Your Name]                                                      │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  Generation Info:                                                        │   │
│  • Model: GPT-4                                                          │   │
│  • Cost: $0.03                                                           │   │
│  • Generated: 2 minutes ago                                              │   │
│  • [Rate this letter: ⭐⭐⭐⭐⭐]                                        │   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  [Cancel]  [Save & Mark as Applied]  [Export & Continue]        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

**Export Options Dropdown:**
- Export as PDF
- Export as DOCX
- Copy to Clipboard
- Send to Email
- Export to Google Docs

---

## Analytics Dashboard

### Analytics Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Analytics  [This Week ▼] [This Month] [Last 3 Months] [Custom Range]   │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Summary Statistics                                              │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │   │
│  │  │   23     │  │   12%    │  │   8%     │  │   2      │        │   │
│  │  │Applications│ │Response │  │Interview │  │  Offers  │        │   │
│  │  │  This Week│ │  Rate    │  │   Rate   │  │Received  │        │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Application Trends                                              │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │    25│                                                           │   │
│  │    20│     ●                                                     │   │
│  │    15│  ●     ●     ●                                           │   │
│  │    10│     ●     ●     ●                                       │   │
│  │     5│  ●                                                       │   │
│  │     0└─────────────────────────────────────────────────────     │   │
│  │       Mon  Tue  Wed  Thu  Fri  Sat  Sun                         │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Response Rate by Source                                        │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │  Indeed        ████████████░░░░░░░░  60%                         │   │
│  │  StepStone     ████████░░░░░░░░░░░░  40%                         │   │
│  │  LinkedIn      ██████████████░░░░░░  70%                         │   │
│  │  Direct        ████████████████████  85%                         │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Top Performing Pipelines                                       │   │
│  │  ────────────────────────────────────────────────────────────    │   │
│  │                                                                   │   │
│  │  1. Python Backend Developer - 12 applications, 3 interviews    │   │
│  │  2. React Frontend Developer - 8 applications, 2 interviews     │   │
│  │  3. Product Manager - 3 applications, 1 interview               │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  [Export Report] [Share Analytics]                                       │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Settings

### Settings Page

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Settings                                                                 │
├──────────┬──────────────────────────────────────────────────────────────┤
│          │                                                               │
│ Profile  │  Profile Settings                                            │
│          │  ────────────────────────────────────────────────────────    │
│ Notifica-│                                                               │
│ tions    │  Full Name                                                   │   │
│          │  ┌─────────────────────────────────────────────────────┐    │
│ Integra- │  │ John Doe                                            │    │
│ tions    │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│ Billing  │  Email                                                       │
│          │  ┌─────────────────────────────────────────────────────┐    │
│ Security │  │ john.doe@example.com                                │    │
│          │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│          │  Resume                                                      │
│          │  ┌─────────────────────────────────────────────────────┐    │
│          │  │ resume_john_doe.pdf  [Upload New] [Download]        │    │
│          │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│          │  Timezone                                                    │
│          │  ┌─────────────────────────────────────────────────────┐    │
│          │  │ Europe/Berlin (UTC+1) ▼                            │    │
│          │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
│          │  ┌─────────────────────────────────────────────────────┐    │
│          │  │  Save Changes                                       │    │
│          │  └─────────────────────────────────────────────────────┘    │
│          │                                                               │
└──────────┴──────────────────────────────────────────────────────────────┘
```

### Notification Settings

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Notification Settings                                                   │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  Email Notifications                                                     │
│  ────────────────────────────────────────────────────────────────────    │
│                                                                           │
│  ☑ New job matches                                                       │
│     Frequency: [Daily ▼]                                                 │
│                                                                           │
│  ☑ Application status updates                                            │
│     ☑ Interview scheduled                                                │
│     ☑ Offer received                                                     │
│     ☑ Application rejected                                               │
│                                                                           │
│  ☑ Follow-up reminders                                                   │
│     Remind me: [7 days before ▼]                                         │
│                                                                           │
│  ☐ Weekly summary                                                        │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Save Preferences                                                │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Mobile Responsive Design

### Mobile Dashboard (375px width)

```
┌─────────────────────────────┐
│ ☰  JobFlow        🔔  [👤]  │
├─────────────────────────────┤
│                             │
│  New Matches (12)           │
│  ─────────────────────      │
│                             │
│  ┌───────────────────────┐ │
│  │ [Logo]                │ │
│  │ Senior Python Dev     │ │
│  │ TechCorp              │ │
│  │ Berlin • Full-time    │ │
│  │ ⭐ 92%                │ │
│  │                       │ │
│  │ [View] [Generate]     │ │
│  └───────────────────────┘ │
│                             │
│  ┌───────────────────────┐ │
│  │ [Logo]                │ │
│  │ Backend Engineer      │ │
│  │ BigTech               │ │
│  │ Remote • Full-time    │ │
│  │ ⭐ 88%                │ │
│  │                       │ │
│  │ [View] [Generate]     │ │
│  └───────────────────────┘ │
│                             │
│  [Load More]                │
│                             │
└─────────────────────────────┘
```

**Mobile Specifications:**
- Hamburger menu (☰) replaces sidebar
- Stacked layout for all components
- Touch-friendly buttons (min 44x44px)
- Swipe gestures for navigation
- Bottom navigation bar (optional)
- Simplified filters (accordion style)

---

## Component Specifications

### Buttons

**Primary Button:**
- Background: #3B82F6 (blue)
- Text: White
- Padding: 12px 24px
- Border radius: 8px
- Hover: Darker shade (#2563EB)
- Disabled: 50% opacity

**Secondary Button:**
- Background: Transparent
- Border: 1px solid #E5E7EB
- Text: #374151
- Hover: Background #F9FAFB

**Danger Button:**
- Background: #EF4444 (red)
- Text: White
- Use for destructive actions

### Typography

- **Heading 1**: 32px, Bold, #111827
- **Heading 2**: 24px, Bold, #111827
- **Heading 3**: 20px, Semi-bold, #111827
- **Body**: 16px, Regular, #374151
- **Small**: 14px, Regular, #6B7280
- **Caption**: 12px, Regular, #9CA3AF

### Colors

- **Primary**: #3B82F6 (Blue)
- **Success**: #10B981 (Green)
- **Warning**: #F59E0B (Amber)
- **Error**: #EF4444 (Red)
- **Background**: #FFFFFF (White)
- **Surface**: #F9FAFB (Light Gray)
- **Border**: #E5E7EB (Gray)
- **Text Primary**: #111827 (Dark Gray)
- **Text Secondary**: #6B7280 (Medium Gray)

### Spacing

- Base unit: 4px
- Common spacing: 8px, 16px, 24px, 32px, 48px
- Card padding: 24px
- Section margin: 32px

---

## Interaction States

### Hover States
- Buttons: Slight elevation, color change
- Cards: Border highlight, shadow
- Links: Underline, color change

### Loading States
- Skeleton screens for content loading
- Spinner for actions
- Progress bars for multi-step processes

### Error States
- Inline error messages below fields
- Toast notifications for API errors
- Error pages for critical failures

### Empty States
- Illustrations with helpful messages
- Call-to-action buttons
- Guidance text

---

## Accessibility

- **WCAG 2.1 AA Compliance**
- Keyboard navigation support
- Screen reader friendly
- Focus indicators visible
- Color contrast ratios met
- Alt text for images
- ARIA labels where needed

---

**Next Steps:**
- Create high-fidelity mockups in Figma
- Develop component library
- Implement responsive breakpoints
- Conduct usability testing
