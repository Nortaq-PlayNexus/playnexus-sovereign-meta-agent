---
description: "SOVEREIGN memory recall: retrieve relevant knowledge from persistent memory for the current context."
agent: sovereign
---

# SOVEREIGN Memory Recall

Retrieve relevant knowledge from the SOVEREIGN persistent memory system.

## Step 1: Analyze Context
Read the current conversation to understand:
- What topic is being discussed
- What domain knowledge is relevant
- What past lessons might apply
- What patterns might be useful

## Step 2: Load Memory
Read the following files under `~/.sovereign/`:

1. `knowledge/lessons/INDEX.md` — Check for relevant past lessons
2. `knowledge/patterns/INDEX.md` — Check for applicable patterns
3. `knowledge/facts/INDEX.md` — Check for related verified facts
4. `knowledge/preferences/INDEX.md` — Check for user preferences
5. `knowledge/domain/INDEX.md` — Check for domain-specific knowledge
6. `memory/decisions/INDEX.md` — Check for relevant past decisions
7. `memory/sessions/INDEX.md` — Check for similar past sessions

## Step 3: Synthesize
Combine relevant knowledge into a useful summary:
- What past knowledge is relevant
- What lessons should guide current work
- What patterns suggest approaches
- What user preferences should be respected

## Step 4: Present
Provide a concise summary of retrieved knowledge to inform the current task.
