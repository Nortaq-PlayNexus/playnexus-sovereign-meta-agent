---
description: "SOVEREIGN memory save: capture lessons, patterns, and facts from the current session."
agent: sovereign
---
# SOVEREIGN Memory Save

Analyze the current session and save important knowledge to persistent memory.

## Step 1: Review Current Context

Read the conversation to identify:
- Verified facts established
- Patterns identified
- Lessons learned
- Decisions made
- User preferences observed
- Goals created or updated

## Step 2: Read Existing Knowledge

Read the relevant INDEX.md files under `~/.sovereign/` to avoid duplicates and check for related existing entries.

## Step 3: Save New Knowledge

For each item identified, choose the appropriate category:

### Facts (save to `~/.sovereign/knowledge/facts/INDEX.md`)

Format:
```
### [FACT TITLE]
- **Content:** [Verified statement]
- **Source:** [Where this was verified — include URL, book reference, document name, etc.]
- **Confidence:** HIGH / MODERATE / LOW
- **Verified:** [Date — YYYY-MM-DD]
- **Tags:** [topic1, topic2] — use lowercase, comma-separated
```

**When to save:**
- Verified information from research or analysis
- Facts established through code execution or tool results
- Important findings that may be useful in future sessions
- Information supported by evidence (not just assumptions)

### Patterns (save to `~/.sovereign/knowledge/patterns/INDEX.md`)

Format:
```
### [PATTERN NAME]
- **Domain:** [Area of application]
- **Description:** [What the pattern is — one paragraph]
- **When to use:** [Applicable conditions]
- **Not when to use:** [Conditions where this should NOT be used]
- **Examples:** [Concrete instances — 1-3 real-world examples]
- **Counter-examples:** [When the pattern fails — be explicit]
- **Confidence:** HIGH / MODERATE / LOW
- **Identified:** [Date — YYYY-MM-DD]
- **Tags:** [relevant tags]
```

**When to save:**
- Recurring solutions that worked well
- Patterns identified across multiple tasks
- Successful approaches worth remembering

### Lessons (save to `~/.sovereign/knowledge/lessons/INDEX.md`)

Format:
```
### [LESSON TITLE]
- **What happened:** [Description of the event — what, when, where]
- **Root cause:** [Why it happened — the underlying reason]
- **What went wrong:** [Specific failure mode — be concrete]
- **What to do instead:** [Corrective action — what should be done differently]
- **Prevention:** [How to prevent this in the future]
- **Severity:** CRITICAL / HIGH / MEDIUM / LOW
- **Lesson category:** [e.g., coding, research, communication]
- **Learned:** [Date — YYYY-MM-DD]
- **Tags:** [relevant tags]
```

**When to save:**
- Mistakes made during the task
- Insights gained from failures or successes
- Things to avoid in future similar tasks

### Preferences (save to `~/.sovereign/knowledge/preferences/INDEX.md`)

Format:
```
### [PREFERENCE]
- **Category:** [type — e.g., workflow, tool, communication, output format]
- **Preference:** [What user prefers]
- **Context:** [When this applies — task type, domain, context]
- **Confidence:** CONFIRMED / INFERRED
- **Identified:** [Date — YYYY-MM-DD]
- **Tags:** [relevant tags]
```

**When to save:**
- User preferences observed during the session
- Workflow preferences that make tasks easier
- Tool or format preferences

### Decisions (save to `~/.sovereign/memory/decisions/INDEX.md`)

Format:
```
### [DECISION TITLE] — [Date]
- **Context:** [Why this decision was needed]
- **Options considered:** [Alternatives evaluated]
- **Decision:** [What was chosen]
- **Reasoning:** [Why this option was selected]
- **Outcome:** [Result of the decision]
- **Confidence:** HIGH / MODERATE / LOW
- **Tags:** [relevant tags]
```

**When to save:**
- Important choices made during the task
- Strategic decisions with future impact
- Trade-off evaluations

### Goals (save to `~/.sovereign/memory/goals/INDEX.md`)

Format:
```
### [GOAL TITLE]
- **Description:** [What needs to be achieved]
- **Priority:** CRITICAL / HIGH / MEDIUM / LOW
- **Status:** NOT_STARTED / IN_PROGRESS / COMPLETED / BLOCKED / CANCELLED
- **Subtasks:** [List of sub-goals]
- **Created:** [Date — YYYY-MM-DD]
- **Expected deadline:** [If applicable — YYYY-MM-DD]
- **Notes:** [Additional context]
- **Tags:** [relevant tags]
```

**When to save:**
- New objectives created during the task
- Progress on existing goals
- Goals that were completed, blocked, or cancelled

## Step 4: Update Session Log

Add a session summary entry to `~/.sovereign/memory/sessions/INDEX.md`.

Format:
```
### Session [ID] — [Date]
- **Objective:** [What was attempted]
- **Outcome:** [What was achieved]
- **Key decisions:** [Important choices made]
- **Lessons:** [What was learned]
- **Duration:** [Approximate length]
- **Tags:** [relevant tags]
```

Use consistent ID format: `Session [YYYYMMDD]-[sequence]` or `Session [project-code]-[n]`

## Step 5: Confirm

Report what was saved and any potential conflicts with existing knowledge.

---

### Example Save Session

```
/sovereign-save

The command will:
1. Review the current conversation for verified facts, patterns, lessons, decisions, preferences, and goals
2. Check existing ~/.sovereign/ knowledge files for duplicates
3. Prompt you to save each identified item to the appropriate INDEX.md file
4. Add a session summary to the session log
5. Report what was saved and any conflicts
```

**Usage:** `/sovereign-save` — after any significant task to capture learnings