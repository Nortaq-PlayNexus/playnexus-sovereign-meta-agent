# ACTIVE GOALS

Current objectives, progress tracking, and blockers. This section tracks active goals with priorities, status, and subtasks.

## Format

```
### [GOAL TITLE]
- **Description:** [What needs to be achieved — clear, measurable if possible]
- **Priority:** CRITICAL / HIGH / MEDIUM / LOW
- **Status:** NOT_STARTED / IN_PROGRESS / COMPLETED / BLOCKED / CANCELLED
- **Subtasks:** [List of sub-goals — checkoff format or bullet list]
  - [ ] Sub-task 1
  - [x] Sub-task 2 (completed)
- **Created:** [Date — YYYY-MM-DD]
- **Started:** [Date when work began — YYYY-MM-DD, leave blank if NOT_STARTED]
- **Expected deadline:** [If applicable — YYYY-MM-DD, or "ongoing"]
- **Actual completion:** [Date when completed — YYYY-MM-DD, leave blank if not completed]
- **Notes:** [Additional context — blockers, dependencies, insights]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Related goals:** [Links to other goals this depends on or relates to]
- **Progress percentage:** [Optional — 0-100, e.g., 75]
```

## Priority Guidelines

- **CRITICAL**: Blocking other work, major consequence if not completed, user-facing deadline
- **HIGH**: Important but not immediately blocking, should be done soon
- **MEDIUM**: Nice to have, can wait for lower-priority work
- **LOW**: Optional, deferrable, "when I have time" category

## Status Progression

NOT_STARTED → IN_PROGRESS → (blocked or continuing) → COMPLETED / CANCELLED

## Goal Lifecycle

1. **Create**: New goal added with NOT_STARTED status and appropriate priority
2. **Start**: Move to IN_PROGRESS when work begins
3. **Progress**: Update subtasks and notes regularly
4. **Complete/Block/Cancel**: Move to final status with completion date or reason for cancellation
5. **Archive**: After some time, move completed goals to history (or keep in INDEX.md with "COMPLETED" noted)

## Example

```
### [Implement User Authentication] — Priority: HIGH
- **Description:** Add secure user authentication to the web application with login, registration, and password reset
- **Priority:** HIGH
- **Status:** IN_PROGRESS
- **Subtasks:**
  - [ ] Set up authentication framework
  - [ ] Implement login endpoint
  - [ ] Implement registration endpoint
  - [ ] Implement password reset flow
  - [ ] Write authentication tests
  - [ ] Add documentation
- **Created:** 2026-06-01
- **Started:** 2026-06-15
- **Expected deadline:** 2026-07-01
- **Notes:** Blocked on OAuth provider API setup; using development mode until resolved
- **Tags:** authentication, web, security
- **Related goals:** [API security review, Deployment configuration]
- **Progress percentage:** 60
```