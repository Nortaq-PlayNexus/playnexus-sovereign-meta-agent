# ACTIVE PROJECTS

Current project contexts and status tracking. This section captures the context, goals, status, and progress of active projects.

## Format

```
### [PROJECT NAME]
- **Description:** [What the project is about — one or two sentences]
- **Goal:** [What success looks like — the Definition of Done or success criteria]
- **Status:** ACTIVE / PAUSED / COMPLETED / ABANDONED
- **Dependencies:** [Required resources — tools, access, information, people]
- **Progress:** [Current state — percentage, milestone reached, or descriptive status]
- **Created:** [Date — YYYY-MM-DD]
- **Started:** [Date when work began — YYYY-MM-DD, leave blank if not yet started]
- **Expected completion:** [If applicable — YYYY-MM-DD or "ongoing"]
- **Actual completion:** [Date when completed — YYYY-MM-DD, leave blank if not completed]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Related projects:** [Links to other related projects by name or tag]
- **Risk level:** [LOW / MEDIUM / HIGH — based on uncertainties and risks]
- **Blockers:** [Current blocking issues — list them]
```

## Project Status Definitions

- **ACTIVE**: Work is currently ongoing
- **PAUSED**: Temporarily stopped, can be resumed
- **COMPLETED**: All goals achieved, project closing
- **ABANDONED**: Project no longer pursued, reasons documented

## Risk Level Guidelines

- **LOW**: Well-understood, few uncertainties, resources available
- **MEDIUM**: Some unknowns, manageable risks, monitoring needed
- **HIGH**: Significant uncertainties, potential for failure, contingency needed

## Example

```
### [Redesign Authentication System] — Priority: HIGH
- **Description:** Complete redesign of the user authentication system to support OAuth2 and improved security
- **Goal:** Secure authentication system with OAuth2, MFA, and social login by 2026-09-01
- **Status:** ACTIVE
- **Dependencies:** OAuth2 provider API access, frontend framework updates, database migration
- **Progress:** 40% — framework selected, login flow implemented, OAuth2 pending
- **Created:** 2026-05-20
- **Started:** 2026-06-01
- **Expected completion:** 2026-09-01
- **Tags:** authentication, security, infrastructure
- **Related projects:** [API security review, Deployment configuration]
- **Risk level:** MEDIUM
- **Blockers:** OAuth2 provider API keys not yet obtained
```