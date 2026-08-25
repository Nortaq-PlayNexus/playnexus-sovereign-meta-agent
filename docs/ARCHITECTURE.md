# Architecture

## System Overview

SOVEREIGN is a cognitive architecture system consisting of three layers:

```
┌─────────────────────────────────────────────────────┐
│                  USER INTERFACE                      │
│              (opencode CLI / TUI)                    │
├─────────────────────────────────────────────────────┤
│               AGENT LAYER (opencode)                 │
│  ┌──────────────────────────────────────────────┐   │
│  │           SOVEREIGN AGENT (24KB)              │   │
│  │  ┌────────────────────────────────────────┐   │   │
│  │  │         META-AGENT (Router)             │   │   │
│  │  │  Problem → Strategy → Agents → Result   │   │   │
│  │  └────────────────────────────────────────┘   │   │
│  │  ┌─────────┐ ┌──────────┐ ┌──────────────┐   │   │
│  │  │ SPECIALIST AGENTS (14)  │                │   │   │
│  │  │ Researcher, Analyst,    │                │   │   │
│  │  │ Architect, Skeptic,     │                │   │   │
│  │  │ Red Team, Optimizer,    │                │   │   │
│  │  │ Fact Checker, etc.      │                │   │   │
│  │  └─────────────────────────┘                │   │
│  └──────────────────────────────────────────────┘   │
│  ┌──────────┐ ┌────────────┐ ┌──────────────────┐   │
│  │ COMMANDS │ │   SKILLS   │ │  TOOLS (opencode) │   │
│  │ 3 cmds   │ │ 1 skill    │ │  read/write/bash/ │   │
│  └──────────┘ └────────────┘ │  grep/glob/web    │   │
│                               └──────────────────┘   │
├─────────────────────────────────────────────────────┤
│              PERSISTENCE LAYER                       │
│  ┌──────────────────────────────────────────────┐   │
│  │         ~/.sovereign/ (Filesystem)           │   │
│  │  knowledge/  memory/  workspace/  config/    │   │
│  └──────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────┐   │
│  │       consolidate.py (Python Utility)        │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## Agent Layer

### META-AGENT

The META-AGENT is the supervisory intelligence. It does not solve problems directly — it manages the reasoning process:

1. **Classifies** the problem type
2. **Selects** the appropriate reasoning strategy
3. **Spawns** specialist agents as needed
4. **Monitors** for weak reasoning and contradictions
5. **Synthesizes** results from specialist agents
6. **Self-critiques** the final conclusion
7. **Stores** knowledge for future reference

### Specialist Agents

| Agent | Role | When Activated |
|-------|------|---------------|
| RESEARCHER | Find and evaluate evidence | Information gaps |
| ANALYST | Extract patterns and insights | Data processing |
| ARCHITECT | Design systems and solutions | Build tasks |
| SKEPTIC | Attempt to falsify conclusions | High-stakes decisions |
| RED TEAM | Search for catastrophic weaknesses | Security/reliability |
| OPTIMIZER | Find superior alternatives | Performance tuning |
| FACT CHECKER | Verify claims against sources | Uncertain facts |
| IMPLEMENTER | Convert conclusions to code | Execution tasks |
| MEMORY CURATOR | Manage persistent knowledge | After significant work |
| STRATEGIST | Evaluate second-order effects | Long-term planning |
| CODER | Write and debug code | Programming tasks |
| TESTER | Design and run tests | Validation |
| DOCUMENTER | Create documentation | Documentation |
| LEARNER | Identify patterns across tasks | Continuous improvement |

## Reasoning Protocols

SOVEREIGN implements 40 reasoning protocols organized into:

### Input Processing
- First-Principles Decomposition (Section 5)
- Tree-of-Thought Exploration (Section 6)

### Hypothesis Management
- Self-Consistency (Section 7)
- Hypothesis Management (Section 15)
- Causal Reasoning (Section 17)

### Execution
- React-Style Agent Loop (Section 8)
- Multi-Agent Debate (Section 9)
- Solution Generation (Section 19)

### Quality Control
- Adversarial Self-Critique (Section 10)
- Anti-Hallucination Protocol (Section 22)
- Failure Mode Analysis (Section 20)

### Knowledge Management
- Knowledge-Graph Memory (Section 11)
- Memory Consolidation (Section 12)
- Evidence Hierarchy (Section 13)

### Meta-Cognition
- Uncertainty Engine (Section 14)
- Information Value (Section 16)
- Second-Order Thinking (Section 18)
- Meta-Optimization (Section 21)

## Data Flow

```
User Query
    │
    ▼
META-AGENT classifies problem
    │
    ├── Trivial → Solve directly → Respond
    │
    └── Complex → Full Protocol
         │
         ├── Load Memory (read ~/.sovereign/)
         │
         ├── First-Principles Decomposition
         │
         ├── Generate Hypotheses (Tree-of-Thought)
         │
         ├── Spawn Specialist Agents
         │    ├── RESEARCHER → gather evidence
         │    ├── ANALYZER → extract patterns
         │    ├── SKEPTIC → challenge conclusions
         │    └── ... (as needed)
         │
         ├── Multi-Agent Debate (if uncertain)
         │
         ├── Adversarial Self-Critique
         │
         ├── Synthesize Conclusion
         │
         ├── Store Knowledge (write ~/.sovereign/)
         │
         └── Respond
```

## Memory Architecture

### Knowledge Categories

| Category | File | Purpose |
|----------|------|---------|
| Facts | `knowledge/facts/INDEX.md` | Verified information with sources |
| Patterns | `knowledge/patterns/INDEX.md` | Recurring solutions |
| Lessons | `knowledge/lessons/INDEX.md` | Mistakes and corrections |
| Preferences | `knowledge/preferences/INDEX.md` | User's preferred workflows |
| Domain | `knowledge/domain/INDEX.md` | Domain-specific expertise |

### Memory Categories

| Category | File | Purpose |
|----------|------|---------|
| Sessions | `memory/sessions/INDEX.md` | Session summaries |
| Decisions | `memory/decisions/INDEX.md` | Key decisions and reasoning |
| Goals | `memory/goals/INDEX.md` | Active objectives |

### Data Format

All knowledge entries follow a structured Markdown format:

```markdown
### [ENTRY TITLE]
- **Content:** [The knowledge]
- **Source:** [Where it came from]
- **Confidence:** HIGH / MODERATE / LOW
- **Date:** [When it was recorded]
- **Tags:** [topic1, topic2]
```

## Zero-Cost Constraint

Every layer of the architecture operates under the zero-cost constraint:

| Layer | Cost Enforcement |
|-------|-----------------|
| Agent | Prompt explicitly prohibits paid tools |
| Commands | Only invoke free operations |
| Skills | Reference only free resources |
| Memory | Local filesystem only |
| Consolidation | Local Python execution only |
| Web access | Free search and fetch only |
