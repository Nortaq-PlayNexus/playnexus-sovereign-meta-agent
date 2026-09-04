# LESSONS LEARNED

Mistakes, failures, and insights from past experiences. Used to avoid repeating errors and to improve future task performance. Lessons are critical for continuous improvement.

## Format

```
### [LESSON TITLE]
- **What happened:** [Description of the event — what, when, where]
- **Root cause:** [Why it happened — the underlying reason, not just the symptom]
- **What went wrong:** [Specific failure mode — be concrete]
- **What to do instead:** [Corrective action — what should be done differently]
- **Prevention:** [How to prevent this in the future]
- **Severity:** CRITICAL / HIGH / MEDIUM / LOW
- **Lesson category:** [e.g., coding, research, communication, resource management, planning]
- **Learned:** [Date — YYYY-MM-DD]
- **Applied to:** [What tasks/projects this lesson applies to]
- **Applicable domains:** [Where this lesson is relevant]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Related lessons:** [Links to other related lessons by title or tag]
```

## Severity Guidelines

- **CRITICAL**: Complete task failure, data loss, security breach, major timeline impact
- **HIGH**: Significant rework needed, major feature delayed, substantial cost overrun
- **MEDIUM**: Minor rework, small feature affected, slight timeline impact
- **LOW**: Inconvenience, minor fix needed, no real impact on outcome

## Lesson Categories

- **Coding**: Bugs, design patterns, refactoring, performance
- **Research**: Source evaluation, evidence quality, assumption checking
- **Communication**: Misunderstandings, documentation gaps, stakeholder alignment
- **Resource**: Tool availability, time estimation, dependency management
- **Planning**: Scope creep, requirement gaps, timeline unrealism
- **General**: Any other category

## Anti-Hallucination Rule for Lessons

- NEVER claim a lesson was learned from a task you did not personally perform
- If the lesson is second-hand, mark it as " heard from " or " reported by "
- Always distinguish between "I learned this" and "This is reported"

## Example

```
### [Premature Optimization]
- **What happened:** Optimized a function early in development before profiling, resulting in over-engineered code that was later rewritten
- **Root cause:** Assumed performance would be an issue without measurement; fell for "premature optimization" trap
- **What went wrong:** Spent 4 hours optimizing a function that ran in 10ms; the real bottleneck was elsewhere
- **What to do instead:** Always profile first, optimize only bottlenecks identified by measurement
- **Prevention:** Add "profile before optimize" checklist to task initiation
- **Severity:** MEDIUM
- **Lesson category:** coding
- **Learned:** 2026-02-20
- **Applied to:** All code development tasks
- **Applicable domains:** software development, system design
- **Tags:** optimization, performance, anti-pattern
- **Related lessons:** [Early testing, Scope creep]
```