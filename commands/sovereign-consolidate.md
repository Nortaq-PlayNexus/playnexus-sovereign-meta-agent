---
description: "Run SOVEREIGN memory consolidation: review, merge, and optimize the persistent knowledge base."
agent: sovereign
---
# SOVEREIGN Memory Consolidation

Review and consolidate the SOVEREIGN persistent memory system. Execute the following steps:

## Step 1: Load Current State

Read all INDEX.md files under `~/.sovereign/` to understand the current memory state. This gives you a complete picture of what knowledge exists, how many entries there are, and the distribution of confidence levels.

**Read these files:**
- `knowledge/facts/INDEX.md` — Verified facts and their confidence levels
- `knowledge/patterns/INDEX.md` — Recurring patterns and their confidence
- `knowledge/lessons/INDEX.md` — Mistakes and insights captured
- `knowledge/preferences/INDEX.md` — User preferences
- `knowledge/domain/INDEX.md` — Domain-specific expertise
- `memory/sessions/INDEX.md` — Session summaries
- `memory/decisions/INDEX.md` — Key decisions and reasoning
- `memory/goals/INDEX.md` — Active goals and progress

## Step 2: Consolidate Knowledge

For each knowledge category (facts, patterns, lessons, preferences, domain), perform the following:

### Identify Redundant Entries
- Look for entries with the same or very similar titles
- Check for duplicate content across entries

### Merge Related Concepts
- Combine entries that cover related topics
- Consolidate related patterns into more general patterns
- Merge lessons that teach similar principles

### Strengthen Well-Supported Conclusions
- Boost confidence for entries with strong evidence
- Add supporting sources or additional verification where missing

### Deprecate Unreliable Information
- Mark entries with LOW confidence that are contradicted by new evidence
- Add "Deprecated" notes to entries that should be re-evaluated
- Consider removing entries that are no longer valid

### Remove Outdated Entries
- Archive entries older than 12 months that are no longer relevant
- Keep a record of removed entries in a changelog or notes

## Step 3: Consolidate Memory

For each memory category (sessions, decisions, goals), perform the following:

### Archive Completed Goals Older Than 30 Days
- Move completed goals to a "completed" section or mark them as archived
- Update status and add completion date

### Summarize Old Session Logs into Key Takeaways
- Identify the most important outcomes from old sessions
- Create condensed summaries for sessions older than 90 days
- Preserve the core lessons while removing granular detail

### Archive Resolved Decisions
- Move archived decisions to a historical section
- Keep the reasoning and outcome for future reference

### Update Active Goals with Current Status
- Review progress on active goals
- Update priority if circumstances changed
- Adjust deadlines or scope as needed

## Step 4: Report

Generate a summary of the consolidation results:

- **Knowledge items consolidated**: How many entries were merged, deprecates, or removed
- **Entries deprecated**: How many entries were marked as unreliable or outdated
- **Patterns identified**: Any new patterns captured during consolidation
- **Lessons captured**: Any new lessons added from the review process
- **Recommendations for improvement**: Suggestions for better memory management going forward

The report should be concise and scannable, focusing on what changed and why.

## Step 5: Update

Write consolidated results back to the appropriate INDEX.md files. This ensures the in-memory knowledge is up-to-date and optimized for the next recall session.

---

### Consolidation Commands

```
# View memory statistics (verbose output)
python scripts/consolidate.py --verbose

# Dry run (preview changes without modifying files)
python scripts/consolidate.py --dry-run

# Run consolidation live
python scripts/consolidate.py

# With merge mode (consolidate duplicate entries across categories)
python scripts/consolidate.py --merge

# With link mode (detect cross-category connections)
python scripts/consolidate.py --link

# Verbose dry run with merging
python scripts/consolidate.py --verbose --dry-run --merge
```

---

### Example Consolidation Report

```
SOVEREIGN Memory Consolidation Report
=====================================

Knowledge Consolidation:
  - Facts: 2 entries merged (related Python concurrency facts)
  - Patterns: 1 entry deprecated (low-confidence pattern)
  - Lessons: 0 new lessons, 1 reviewed
  - Preferences: 0 changes
  - Domain: 0 changes

Memory Consolidation:
  - Goals: 2 completed goals archived (from June 2026)
  - Decisions: 0 changes
  - Sessions: 3 sessions summarized (older than 90 days)

Cross-Category Linking:
  - Fact "Python GIL behavior" linked to Pattern "Circular import detection"
  - Lesson "Premature optimization" linked to Fact "Performance measurement anti-pattern"

Total entries before: 47
Total entries after: 42
Changes: 5 entries merged/removed, 3 entries deprecated

Consolidation complete. Memory optimized for next session.
```