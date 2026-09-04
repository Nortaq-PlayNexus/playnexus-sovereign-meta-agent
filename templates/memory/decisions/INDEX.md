# DECISION LOG

Key decisions, reasoning, and outcomes for important choices. This log captures the context, options, reasoning, and results of significant decisions made during tasks.

## Format

```
### [DECISION TITLE] — [Date]
- **Context:** [Why this decision was needed — the problem or opportunity that prompted the decision]
- **Options considered:** [Alternatives evaluated — list all reasonable options, even if rejected]
- **Decision:** [What was chosen — the selected option]
- **Reasoning:** [Why this option was selected — the key factors, evidence, and trade-offs]
- **Outcome:** [Result of the decision — what actually happened, metrics if available]
- **Confidence:** HIGH / MODERATE / LOW [in hindsight]
- **Date:** [YYYY-MM-DD]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Follow-up:** [If any — what to review, metrics to track, when to reassess]
- **Related decisions:** [Links to other related decisions by title or tag]
```

## Decision Quality Criteria

A good decision record should capture:
- The actual problem being solved (context)
- All reasonable options considered, not just the winner
- The specific factors that tipped the scale
- What actually happened vs. what was expected
- Confidence in hindsight (helps calibrate future confidence estimates)
- Tags for cross-referencing with lessons and patterns

## Decision Confidence Calibration

After some time has passed, review the confidence you recorded:
- If the outcome was unexpectedly good, note that and consider future confidence bumps
- If the outcome was unexpectedly poor, analyze why the confidence was miscalibrated
- Use this to improve your uncertainty engine over time

## Example

```
### [Technology Stack Choice for New Project] — 2026-06-20
- **Context:** Need to select a tech stack for a new web application requiring real-time features and good documentation
- **Options considered:**
  1. Node.js + Socket.io + Express
  2. Python + FastAPI + Socket.io
  3. Go + Goreleaft + NATS
  4. Rust + Actix-web + Tokio
- **Decision:** Selected option 2 (Python + FastAPI + Socket.io)
- **Reasoning:** Team has most Python expertise; FastAPI provides best developer experience; Socket.io has best browser fallback; zero-cost constraint satisfied
- **Outcome:** Development proceeded smoothly; real-time features working; performance adequate for expected load; would choose same again
- **Confidence:** HIGH (in hindsight)
- **Tags:** architecture, decision-making, tech-stack
- **Follow-up:** Review in 6 months for scalability assessment
- **Related decisions:** [Database choice, CI/CD setup]
```