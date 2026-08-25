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
Read the relevant INDEX.md files under `~/.sovereign/` to avoid duplicates.

## Step 3: Save New Knowledge
For each item identified:

### Facts (save to `~/.sovereign/knowledge/facts/INDEX.md`)
Format: fact title, content, source, confidence, verification date, tags

### Patterns (save to `~/.sovereign/knowledge/patterns/INDEX.md`)
Format: pattern name, domain, description, when to use, examples, confidence

### Lessons (save to `~/.sovereign/knowledge/lessons/INDEX.md`)
Format: lesson title, what happened, root cause, corrective action, severity

### Preferences (save to `~/.sovereign/knowledge/preferences/INDEX.md`)
Format: preference, category, context, confidence

### Decisions (save to `~/.sovereign/memory/decisions/INDEX.md`)
Format: decision title, context, options, decision, reasoning, outcome

## Step 4: Update Session Log
Add a session summary entry to `~/.sovereign/memory/sessions/INDEX.md`.

## Step 5: Confirm
Report what was saved and any potential conflicts with existing knowledge.
