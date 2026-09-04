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
- What user preferences should be respected

## Step 2: Load Memory

Read the following files under `~/.sovereign/` in order of relevance:

### 1. `knowledge/lessons/INDEX.md` — Check for relevant past lessons
Look for lessons related to the current topic or problem. Lessons capture mistakes and successes from past experiences that can guide current work.

### 2. `knowledge/patterns/INDEX.md` — Check for applicable patterns
Look for patterns that match the current situation. Patterns are recurring solutions that have worked well in similar contexts.

### 3. `knowledge/facts/INDEX.md` — Check for related verified facts
Look for facts that are directly relevant to the current topic. Facts are verified pieces of information with sources and confidence levels.

### 4. `knowledge/preferences/INDEX.md` — Check for user preferences
Check if the user has expressed any preferences that should guide the current task. This includes workflow preferences, tool preferences, format preferences, etc.

### 5. `knowledge/domain/INDEX.md` — Check for domain-specific knowledge
Look for domain expertise that may be relevant. This captures structured knowledge about the domains you work in.

### 6. `memory/decisions/INDEX.md` — Check for relevant past decisions
Review past decisions that may inform the current choice. This helps avoid repeating the same decision-making process and preserves the reasoning behind previous choices.

### 7. `memory/sessions/INDEX.md` — Check for similar past sessions
Look for past sessions that tackled similar problems. Session summaries capture what was attempted, what was achieved, and key lessons learned.

## Step 3: Synthesize

Combine relevant knowledge into a useful summary:

- **What past knowledge is relevant**: List the most applicable lessons, patterns, facts, and decisions
- **What lessons should guide current work**: Highlight the top 1-3 lessons most relevant to the current task
- **What patterns suggest approaches**: Identify patterns that match the current situation and what they suggest
- **What user preferences should be respected**: Note any preferences that affect how the task should be approached

Provide a concise summary of retrieved knowledge to inform the current task. Format the summary as a brief overview that can be referenced at the start of the current work session.

---

### Example Recall Session

```
/sovereign-recall

The command will:
1. Read all seven knowledge and memory categories under ~/.sovereign/
2. Identify entries relevant to the current conversation topic
3. Provide a synthesized summary of the most applicable knowledge
4. Highlight lessons, patterns, facts, and decisions to consider
5. Note any user preferences or domain expertise to respect
6. Present the findings in a concise, structured format

**Usage:** `/sovereign-recall` — before starting a task or when needing past context