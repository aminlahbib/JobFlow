# User Stories
## JobFlow - Job Application Automation Platform

**Document Version:** 1.0  
**Last Updated:** December 2025  
**Author:** Product & Engineering Team

---

## Table of Contents
1. [Authentication & Onboarding](#authentication--onboarding)
2. [Job Discovery & Matching](#job-discovery--matching)
3. [Pipeline Management](#pipeline-management)
4. [Application Tracking](#application-tracking)
5. [Letter Generation](#letter-generation)
6. [Analytics & Insights](#analytics--insights)
7. [Settings & Preferences](#settings--preferences)
8. [Integrations](#integrations)
9. [Admin & System](#admin--system)

---

## User Story Format

Each user story follows the format:
- **As a** [persona/role]
- **I want to** [action/feature]
- **So that** [benefit/value]
- **Acceptance Criteria:** [specific conditions]
- **Priority:** [High/Medium/Low]
- **Story Points:** [1-8]

---

## Authentication & Onboarding

### US-001: User Registration
**As a** new user  
**I want to** create an account with email and password  
**So that** I can access JobFlow and start my job search automation

**Acceptance Criteria:**
- [ ] User can enter email, password, and confirm password
- [ ] Email format is validated
- [ ] Password must be at least 8 characters
- [ ] Password confirmation must match
- [ ] Error messages display for invalid inputs
- [ ] Success message shown after registration
- [ ] User is redirected to onboarding flow

**Priority:** High  
**Story Points:** 3  
**Epic:** Authentication

---

### US-002: OAuth Registration
**As a** new user  
**I want to** sign up using Google or LinkedIn  
**So that** I can quickly create an account without entering credentials

**Acceptance Criteria:**
- [ ] User can click "Continue with Google" button
- [ ] User can click "Continue with LinkedIn" button
- [ ] OAuth flow redirects to provider
- [ ] User can authorize JobFlow access
- [ ] Account is created with OAuth provider data
- [ ] User is redirected to onboarding flow

**Priority:** High  
**Story Points:** 5  
**Epic:** Authentication

---

### US-003: User Login
**As a** returning user  
**I want to** log in with my email and password  
**So that** I can access my dashboard and applications

**Acceptance Criteria:**
- [ ] User can enter email and password
- [ ] Invalid credentials show error message
- [ ] Successful login redirects to dashboard
- [ ] JWT token is stored securely
- [ ] Session persists across browser restarts
- [ ] "Remember me" option extends session duration

**Priority:** High  
**Story Points:** 3  
**Epic:** Authentication

---

### US-004: Resume Upload (Onboarding)
**As a** new user  
**I want to** upload my resume during onboarding  
**So that** JobFlow can generate personalized motivation letters

**Acceptance Criteria:**
- [ ] User can drag and drop resume file
- [ ] User can click to browse and select file
- [ ] Supported formats: PDF, DOC, DOCX, TXT
- [ ] File size limit: 5MB
- [ ] Resume is parsed and key information extracted
- [ ] User can review and edit extracted information
- [ ] User can skip this step and upload later
- [ ] Resume is stored securely

**Priority:** High  
**Story Points:** 5  
**Epic:** Onboarding

---

### US-005: Create First Pipeline (Onboarding)
**As a** new user  
**I want to** create my first job search pipeline during onboarding  
**So that** JobFlow can start finding relevant jobs immediately

**Acceptance Criteria:**
- [ ] User can enter pipeline name
- [ ] User can select location(s)
- [ ] User can choose employment type(s)
- [ ] User can add tech stack keywords
- [ ] User can set salary range (optional)
- [ ] User can enable/disable remote positions
- [ ] Pipeline is saved and activated
- [ ] Initial job scraping is triggered
- [ ] User sees progress indicator

**Priority:** High  
**Story Points:** 5  
**Epic:** Onboarding

---

## Job Discovery & Matching

### US-006: View New Job Matches
**As a** user  
**I want to** see new jobs that match my pipelines  
**So that** I can discover relevant opportunities

**Acceptance Criteria:**
- [ ] Dashboard shows "New Matches" section
- [ ] Badge displays count of new matches
- [ ] Jobs are displayed in cards with key information
- [ ] Each job shows: title, company, location, fit score
- [ ] Jobs are sorted by fit score (highest first)
- [ ] User can click to view job details
- [ ] User can filter by pipeline
- [ ] Pagination or infinite scroll for large lists

**Priority:** High  
**Story Points:** 5  
**Epic:** Job Discovery

---

### US-007: View Job Details
**As a** user  
**I want to** see detailed information about a job posting  
**So that** I can decide if I want to apply

**Acceptance Criteria:**
- [ ] Job detail modal/page shows full description
- [ ] Displays: company, location, salary, employment type
- [ ] Shows fit score and explanation
- [ ] Lists required skills and tech stack
- [ ] Shows link to original job posting
- [ ] User can generate letter from detail view
- [ ] User can mark as applied from detail view
- [ ] User can save job for later

**Priority:** High  
**Story Points:** 3  
**Epic:** Job Discovery

---

### US-008: Filter Jobs
**As a** user  
**I want to** filter jobs by various criteria  
**So that** I can find exactly what I'm looking for

**Acceptance Criteria:**
- [ ] User can filter by pipeline
- [ ] User can filter by location
- [ ] User can filter by salary range
- [ ] User can filter by employment type
- [ ] User can filter by company size
- [ ] Multiple filters can be applied simultaneously
- [ ] Filter state persists during session
- [ ] Clear filters button resets all filters
- [ ] Results update in real-time

**Priority:** Medium  
**Story Points:** 5  
**Epic:** Job Discovery

---

### US-009: Search Jobs
**As a** user  
**I want to** search for jobs by keywords  
**So that** I can quickly find specific positions

**Acceptance Criteria:**
- [ ] Search bar is accessible from header
- [ ] User can type keywords to search
- [ ] Search queries job title, company, description
- [ ] Results update as user types (debounced)
- [ ] Search highlights matching terms
- [ ] Search history is saved (optional)
- [ ] User can clear search
- [ ] Search works across all pipelines

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Job Discovery

---

### US-010: View Job Fit Score
**As a** user  
**I want to** see how well a job matches my profile  
**So that** I can prioritize which jobs to apply for

**Acceptance Criteria:**
- [ ] Fit score (0-100%) is displayed on each job card
- [ ] Score is color-coded (green: 90+, yellow: 70-89, gray: <70)
- [ ] User can click to see score breakdown
- [ ] Breakdown shows: skills match, experience match, location match
- [ ] Score is calculated using LLM analysis
- [ ] Score is cached for performance
- [ ] Score updates if user updates resume

**Priority:** High  
**Story Points:** 8  
**Epic:** Job Discovery

---

## Pipeline Management

### US-011: Create Pipeline
**As a** user  
**I want to** create a new job search pipeline  
**So that** I can search for different types of positions

**Acceptance Criteria:**
- [ ] User can click "Create Pipeline" button
- [ ] Modal/form opens with pipeline creation fields
- [ ] User can set pipeline name and description
- [ ] User can configure all filter criteria
- [ ] User can set notification preferences
- [ ] Pipeline is saved and activated
- [ ] Jobs matching pipeline are fetched
- [ ] Pipeline appears in pipelines list

**Priority:** High  
**Story Points:** 5  
**Epic:** Pipeline Management

---

### US-012: Edit Pipeline
**As a** user  
**I want to** edit an existing pipeline  
**So that** I can update my search criteria

**Acceptance Criteria:**
- [ ] User can click "Edit" on any pipeline
- [ ] Edit form opens with current values pre-filled
- [ ] User can modify any field
- [ ] Changes are saved on submit
- [ ] Job matching is re-triggered with new criteria
- [ ] User sees confirmation message
- [ ] Pipeline statistics update

**Priority:** High  
**Story Points:** 3  
**Epic:** Pipeline Management

---

### US-013: Delete Pipeline
**As a** user  
**I want to** delete a pipeline  
**So that** I can remove outdated search criteria

**Acceptance Criteria:**
- [ ] User can click "Delete" on any pipeline
- [ ] Confirmation dialog appears
- [ ] User must confirm deletion
- [ ] Pipeline is removed from list
- [ ] Associated applications are not deleted
- [ ] User sees success message

**Priority:** Medium  
**Story Points:** 2  
**Epic:** Pipeline Management

---

### US-014: Pause/Activate Pipeline
**As a** user  
**I want to** pause or activate a pipeline  
**So that** I can temporarily stop receiving matches without deleting

**Acceptance Criteria:**
- [ ] User can toggle pipeline active/inactive status
- [ ] Paused pipelines don't generate new matches
- [ ] Paused pipelines are visually distinct
- [ ] User can reactivate paused pipelines
- [ ] Status change is immediate
- [ ] User sees confirmation

**Priority:** Medium  
**Story Points:** 2  
**Epic:** Pipeline Management

---

### US-015: View Pipeline Jobs
**As a** user  
**I want to** see all jobs matching a specific pipeline  
**So that** I can review opportunities for that search

**Acceptance Criteria:**
- [ ] User can click "View Jobs" on a pipeline
- [ ] Jobs list filters to show only pipeline matches
- [ ] Jobs are sorted by fit score
- [ ] Pipeline name is displayed in header
- [ ] User can see pipeline statistics (total matches, new matches)
- [ ] User can apply filters on top of pipeline filter

**Priority:** High  
**Story Points:** 3  
**Epic:** Pipeline Management

---

## Application Tracking

### US-016: Mark Job as Applied
**As a** user  
**I want to** mark a job as applied  
**So that** I can track my applications

**Acceptance Criteria:**
- [ ] User can click "Mark as Applied" on any job
- [ ] Application is created in "Applied" status
- [ ] Applied date is automatically set
- [ ] Application appears in Applications dashboard
- [ ] User can optionally generate letter before marking
- [ ] Confirmation message is shown
- [ ] Job card updates to show applied status

**Priority:** High  
**Story Points:** 3  
**Epic:** Application Tracking

---

### US-017: View Applications Dashboard
**As a** user  
**I want to** see all my job applications in one place  
**So that** I can track my job search progress

**Acceptance Criteria:**
- [ ] Applications are displayed in Kanban board view
- [ ] Columns: New, To Apply, Applied, Interview, Offer, Rejected, Closed
- [ ] Each application shows: job title, company, status, date
- [ ] User can switch to table or timeline view
- [ ] Applications can be filtered by status, date, pipeline
- [ ] Applications can be sorted by various criteria
- [ ] User can search applications

**Priority:** High  
**Story Points:** 5  
**Epic:** Application Tracking

---

### US-018: Update Application Status
**As a** user  
**I want to** update the status of an application  
**So that** I can track my progress through the hiring process

**Acceptance Criteria:**
- [ ] User can drag and drop applications between columns
- [ ] User can click status dropdown to change status
- [ ] Status workflow is enforced (e.g., can't skip from Applied to Offer)
- [ ] Date is automatically updated based on status
- [ ] Status change triggers notifications (if enabled)
- [ ] User sees confirmation
- [ ] Status history is tracked

**Priority:** High  
**Story Points:** 5  
**Epic:** Application Tracking

---

### US-019: View Application Details
**As a** user  
**I want to** see detailed information about an application  
**So that** I can review all relevant information

**Acceptance Criteria:**
- [ ] User can click on any application to view details
- [ ] Detail view shows: job info, status, dates, notes
- [ ] Shows generated motivation letter
- [ ] Shows recruiter contact information
- [ ] Shows email timeline (if Gmail synced)
- [ ] User can edit all fields
- [ ] User can add notes
- [ ] User can schedule follow-ups

**Priority:** High  
**Story Points:** 5  
**Epic:** Application Tracking

---

### US-020: Add Notes to Application
**As a** user  
**I want to** add notes to an application  
**So that** I can remember important details about the process

**Acceptance Criteria:**
- [ ] User can add notes in application detail view
- [ ] Notes support multi-line text
- [ ] Notes are saved automatically or on "Save" button
- [ ] Notes are timestamped
- [ ] User can edit existing notes
- [ ] Notes are displayed in chronological order
- [ ] Notes are searchable

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Application Tracking

---

### US-021: Schedule Follow-up
**As a** user  
**I want to** schedule a follow-up reminder for an application  
**So that** I don't forget to follow up with recruiters

**Acceptance Criteria:**
- [ ] User can set follow-up date in application detail
- [ ] Date picker is provided
- [ ] User can set time (optional)
- [ ] Reminder notification is scheduled
- [ ] User receives email/notification on follow-up date
- [ ] Follow-ups appear in "Follow-ups Needed" section
- [ ] User can mark follow-up as completed

**Priority:** High  
**Story Points:** 5  
**Epic:** Application Tracking

---

### US-022: Add Recruiter Contact
**As a** user  
**I want to** save recruiter contact information  
**So that** I can easily reach out when needed

**Acceptance Criteria:**
- [ ] User can add recruiter name, email, phone
- [ ] Contact info is saved in application detail
- [ ] User can edit contact information
- [ ] Contact info is used for email matching (Gmail sync)
- [ ] User can click to send email (opens email client)
- [ ] Contact info is searchable

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Application Tracking

---

### US-023: Export Applications
**As a** user  
**I want to** export my applications as CSV or PDF  
**So that** I can share or backup my application data

**Acceptance Criteria:**
- [ ] User can click "Export" button
- [ ] User can choose format: CSV or PDF
- [ ] Export includes: job title, company, status, dates, notes
- [ ] Export can be filtered (e.g., by date range, status)
- [ ] File downloads automatically
- [ ] Export is generated asynchronously for large datasets
- [ ] User receives notification when export is ready

**Priority:** Low  
**Story Points:** 5  
**Epic:** Application Tracking

---

## Letter Generation

### US-024: Generate Motivation Letter
**As a** user  
**I want to** generate a personalized motivation letter for a job  
**So that** I can save time while maintaining quality

**Acceptance Criteria:**
- [ ] User can click "Generate Letter" on any job
- [ ] User can select tone: Professional, Casual, Enthusiastic
- [ ] User can select length: Short, Standard, Long
- [ ] User can select language
- [ ] Estimated cost is displayed
- [ ] Letter is generated using LLM (GPT-4)
- [ ] Generation takes <10 seconds
- [ ] Letter is displayed in preview modal
- [ ] Letter is saved to application

**Priority:** High  
**Story Points:** 8  
**Epic:** Letter Generation

---

### US-025: Edit Generated Letter
**As a** user  
**I want to** edit a generated motivation letter  
**So that** I can customize it to my preferences

**Acceptance Criteria:**
- [ ] User can click "Edit" on generated letter
- [ ] Letter opens in editable text area
- [ ] User can modify any part of the letter
- [ ] Changes are saved on "Save" button
- [ ] Original version is preserved (versioning)
- [ ] User can revert to original
- [ ] Edited letter is marked as "edited"

**Priority:** High  
**Story Points:** 3  
**Epic:** Letter Generation

---

### US-026: Regenerate Letter
**As a** user  
**I want to** regenerate a motivation letter with different settings  
**So that** I can get alternative versions

**Acceptance Criteria:**
- [ ] User can click "Regenerate" button
- [ ] User can change tone, length, or language
- [ ] New letter is generated
- [ ] Previous version is saved in history
- [ ] User can compare versions
- [ ] Cost is charged for each generation
- [ ] User sees generation progress

**Priority:** Medium  
**Story Points:** 5  
**Epic:** Letter Generation

---

### US-027: Export Letter
**As a** user  
**I want to** export my motivation letter in various formats  
**So that** I can use it in my application

**Acceptance Criteria:**
- [ ] User can click "Export" dropdown
- [ ] Options: PDF, DOCX, TXT, Copy to Clipboard
- [ ] PDF is formatted professionally
- [ ] DOCX maintains formatting
- [ ] File downloads automatically
- [ ] User can also send to email
- [ ] Export formats are tracked

**Priority:** High  
**Story Points:** 5  
**Epic:** Letter Generation

---

### US-028: Rate Letter Quality
**As a** user  
**I want to** rate the quality of generated letters  
**So that** JobFlow can improve future generations

**Acceptance Criteria:**
- [ ] User can rate letter 1-5 stars
- [ ] User can provide optional feedback text
- [ ] Rating is saved with letter
- [ ] Ratings are used for ML model improvement
- [ ] User can update rating later
- [ ] Rating is anonymous (for analytics)

**Priority:** Low  
**Story Points:** 2  
**Epic:** Letter Generation

---

## Analytics & Insights

### US-029: View Application Statistics
**As a** user  
**I want to** see statistics about my job applications  
**So that** I can understand my job search performance

**Acceptance Criteria:**
- [ ] Dashboard shows: total applications, response rate, interview rate, offer rate
- [ ] Statistics can be filtered by time period
- [ ] Statistics are displayed in cards with numbers
- [ ] User can see trends over time (charts)
- [ ] Statistics update in real-time
- [ ] User can export statistics

**Priority:** Medium  
**Story Points:** 5  
**Epic:** Analytics

---

### US-030: View Application Trends
**As a** user  
**I want to** see trends in my application activity  
**So that** I can identify patterns and optimize my strategy

**Acceptance Criteria:**
- [ ] Chart shows applications over time (line/bar chart)
- [ ] User can view by day, week, or month
- [ ] Chart shows response rate trends
- [ ] Chart shows interview rate trends
- [ ] User can compare different time periods
- [ ] Chart is interactive (hover for details)
- [ ] Chart can be exported as image

**Priority:** Medium  
**Story Points:** 5  
**Epic:** Analytics

---

### US-031: View Performance by Source
**As a** user  
**I want to** see which job sources perform best  
**So that** I can focus on the most effective channels

**Acceptance Criteria:**
- [ ] Chart shows response rate by source (Indeed, LinkedIn, etc.)
- [ ] Chart shows interview rate by source
- [ ] Chart shows offer rate by source
- [ ] Data is displayed in bar chart or pie chart
- [ ] User can filter by time period
- [ ] User can see number of applications per source

**Priority:** Low  
**Story Points:** 5  
**Epic:** Analytics

---

### US-032: View Pipeline Performance
**As a** user  
**I want to** see which pipelines generate the best results  
**So that** I can optimize my search criteria

**Acceptance Criteria:**
- [ ] List shows pipelines ranked by performance
- [ ] Performance metrics: applications, response rate, interview rate
- [ ] User can see total matches per pipeline
- [ ] User can compare pipelines side-by-side
- [ ] User can click to view pipeline details
- [ ] Recommendations are shown for underperforming pipelines

**Priority:** Low  
**Story Points:** 5  
**Epic:** Analytics

---

## Settings & Preferences

### US-033: Update Profile
**As a** user  
**I want to** update my profile information  
**So that** my account information is current

**Acceptance Criteria:**
- [ ] User can update full name
- [ ] User can update email (with verification)
- [ ] User can update timezone
- [ ] User can upload new resume
- [ ] Changes are saved on "Save" button
- [ ] User sees confirmation message
- [ ] Email change requires password confirmation

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Settings

---

### US-034: Configure Notifications
**As a** user  
**I want to** configure my notification preferences  
**So that** I receive updates when I want them

**Acceptance Criteria:**
- [ ] User can enable/disable email notifications
- [ ] User can set frequency: Immediate, Daily, Weekly
- [ ] User can choose notification types: new matches, status updates, follow-ups
- [ ] Settings are saved automatically
- [ ] User can test notification
- [ ] User sees confirmation

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Settings

---

### US-035: Change Password
**As a** user  
**I want to** change my password  
**So that** I can keep my account secure

**Acceptance Criteria:**
- [ ] User can enter current password
- [ ] User can enter new password
- [ ] User must confirm new password
- [ ] Password requirements are validated
- [ ] Password is updated on submit
- [ ] User is logged out and must log in again
- [ ] User sees confirmation message

**Priority:** Medium  
**Story Points:** 3  
**Epic:** Settings

---

### US-036: Delete Account
**As a** user  
**I want to** delete my account  
**So that** I can remove my data from JobFlow

**Acceptance Criteria:**
- [ ] User can access "Delete Account" in settings
- [ ] User must enter password to confirm
- [ ] Warning message explains data deletion
- [ ] User must check confirmation checkbox
- [ ] Account and all data are deleted
- [ ] Deletion is permanent (GDPR compliant)
- [ ] User receives confirmation email

**Priority:** Medium  
**Story Points:** 5  
**Epic:** Settings

---

## Integrations

### US-037: Connect Gmail Account
**As a** user  
**I want to** connect my Gmail account  
**So that** JobFlow can automatically link recruiter emails to applications

**Acceptance Criteria:**
- [ ] User can click "Connect Gmail" in settings
- [ ] OAuth flow redirects to Google
- [ ] User authorizes JobFlow access
- [ ] Connection is established
- [ ] Gmail sync starts automatically
- [ ] User sees connection status
- [ ] User can disconnect Gmail

**Priority:** Medium (Phase 2)  
**Story Points:** 8  
**Epic:** Integrations

---

### US-038: View Email Timeline
**As a** user  
**I want to** see email correspondence linked to applications  
**So that** I can track all communication in one place

**Acceptance Criteria:**
- [ ] Application detail shows "Email Timeline" section
- [ ] Emails are displayed chronologically
- [ ] Shows: sender, subject, date, excerpt
- [ ] User can click to view full email (opens Gmail)
- [ ] Emails are automatically matched to applications
- [ ] User can manually link emails
- [ ] Email privacy is maintained (only excerpts stored)

**Priority:** Medium (Phase 2)  
**Story Points:** 5  
**Epic:** Integrations

---

## Admin & System

### US-039: Job Scraping (Background)
**As a** system  
**I want to** automatically scrape jobs from multiple sources  
**So that** users always have fresh job listings

**Acceptance Criteria:**
- [ ] Scraping runs every 6 hours
- [ ] Multiple sources are scraped: Indeed, StepStone, LinkedIn
- [ ] Jobs are deduplicated across sources
- [ ] New jobs are stored in database
- [ ] Existing jobs are updated if changed
- [ ] Scraping failures are logged and retried
- [ ] Rate limits are respected

**Priority:** High  
**Story Points:** 13  
**Epic:** System

---

### US-040: Job Ranking (Background)
**As a** system  
**I want to** rank jobs by fit score for each user  
**So that** users see the most relevant jobs first

**Acceptance Criteria:**
- [ ] Jobs are matched to user pipelines
- [ ] Fit score is calculated using LLM
- [ ] Score considers: skills, experience, location, preferences
- [ ] Scores are cached for performance
- [ ] Ranking updates when user updates resume
- [ ] Ranking runs after new jobs are scraped

**Priority:** High  
**Story Points:** 13  
**Epic:** System

---

### US-041: Send Notifications
**As a** system  
**I want to** send email notifications based on user preferences  
**So that** users stay informed about their job search

**Acceptance Criteria:**
- [ ] Notifications are sent for new job matches
- [ ] Notifications are sent for application status updates
- [ ] Follow-up reminders are sent on scheduled date
- [ ] Notification frequency respects user preferences
- [ ] Emails are formatted professionally
- [ ] Users can unsubscribe from emails
- [ ] Notification failures are logged

**Priority:** High  
**Story Points:** 8  
**Epic:** System

---

## User Story Summary

### By Priority
- **High Priority:** 20 stories
- **Medium Priority:** 15 stories
- **Low Priority:** 6 stories

### By Epic
- **Authentication:** 3 stories
- **Onboarding:** 2 stories
- **Job Discovery:** 5 stories
- **Pipeline Management:** 5 stories
- **Application Tracking:** 8 stories
- **Letter Generation:** 5 stories
- **Analytics:** 4 stories
- **Settings:** 4 stories
- **Integrations:** 2 stories (Phase 2)
- **System:** 3 stories

### Total Story Points
- **MVP (Phase 1):** ~180 story points
- **Phase 2:** ~13 additional story points

---

## Definition of Done

Each user story is considered "Done" when:
- [ ] Code is written and reviewed
- [ ] Unit tests are written and passing
- [ ] Integration tests are written and passing
- [ ] UI/UX matches wireframes
- [ ] Acceptance criteria are met
- [ ] Documentation is updated
- [ ] Feature is deployed to staging
- [ ] QA testing is passed
- [ ] Product owner approval received

---

**Next Steps:**
- Prioritize stories for MVP sprint planning
- Break down large stories (8+ points) into smaller tasks
- Create technical tasks for each story
- Assign stories to development sprints
