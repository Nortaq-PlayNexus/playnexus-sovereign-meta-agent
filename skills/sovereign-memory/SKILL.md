---
name: sovereign-memory
description: "Use when saving or retrieving from the SOVEREIGN persistent memory system at ~/.sovereign/. Triggers on memory operations, knowledge consolidation, session logging, or cross-session context retrieval."
---

# SOVEREIGN Memory Skill

## Overview
This skill manages the SOVEREIGN persistent memory system located at `~/.sovereign/`. It provides structured operations for storing, retrieving, and consolidating knowledge across sessions.

## Directory Structure

```
~/.sovereign/
├── knowledge/
│   ├── facts/INDEX.md       # Verified information
│   ├── patterns/INDEX.md    # Recurring patterns
│   ├── lessons/INDEX.md     # Mistakes and corrections
│   ├── preferences/INDEX.md # User preferences
│   └── domain/INDEX.md      # Domain knowledge
├── memory/
│   ├── sessions/INDEX.md    # Session summaries
│   ├── decisions/INDEX.md   # Key decisions
│   └── goals/INDEX.md       # Active goals
├── workspace/
│   ├── projects/INDEX.md    # Project contexts
│   └── artifacts/INDEX.md   # Generated outputs
└── config/
    └── preferences.json     # System preferences
```

## Operations

### SAVE (when to write)
- Verified facts from research
- Patterns identified from work
- Lessons learned from failures/successes
- User preferences observed
- Important decisions made
- Session summaries after complex tasks

### RETRIEVE (when to read)
- Before starting any task (check lessons and patterns)
- When user asks about past context
- When researching a topic with existing knowledge
- When making decisions with historical precedent

### CONSOLIDATE (periodic cleanup)
- Merge duplicate entries
- Deprecate outdated information
- Strengthen confidence in well-supported knowledge
- Archive completed goals and old sessions

## Format Standards

### Fact Entry
```
### [TITLE]
- **Content:** [Verified statement]
- **Source:** [Where verified]
- **Confidence:** HIGH / MODERATE / LOW
- **Verified:** [Date]
- **Tags:** [topic1, topic2]
```

### Pattern Entry
```
### [NAME]
- **Domain:** [Area]
- **Description:** [What the pattern is]
- **When to use:** [Conditions]
- **Examples:** [Instances]
- **Confidence:** HIGH / MODERATE / LOW
```

### Lesson Entry
```
### [TITLE]
- **What happened:** [Event]
- **Root cause:** [Why]
- **What to do instead:** [Fix]
- **Severity:** CRITICAL / HIGH / MEDIUM / LOW
```

### Preference Entry
```
### [PREFERENCE]
- **Category:** [type]
- **Preference:** [What user prefers]
- **Context:** [When this applies]
- **Confidence:** CONFIRMED / INFERRED
```

## Anti-Hallucination Rules
- NEVER claim knowledge not in the files
- ALWAYS read before assuming existing content
- MARK uncertain entries explicitly
- When in doubt, research fresh
