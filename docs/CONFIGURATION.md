# Configuration

## Agent Configuration

The SOVEREIGN agent is defined in `agent/sovereign.md`. This file contains the complete system prompt that defines SOVEREIGN's behavior, reasoning protocols, and memory management.

### Frontmatter

```yaml
---
description: "SOVEREIGN META-AGENT: Autonomous intelligence orchestrator..."
mode: primary
color: gold
---
```

| Field | Value | Description |
|-------|-------|-------------|
| `description` | (text) | Shown in agent selection |
| `mode` | `primary` | Available as a primary agent |
| `color` | `gold` | Visual identifier in UI |

### Modifying the Agent

Edit `agent/sovereign.md` to customize behavior. After editing, restart opencode.

Key sections you might want to modify:

- **Section 2 (META-AGENT)** — Add or remove specialist agents
- **Section 3 (PERSISTENT MEMORY)** — Change memory paths or structure
- **Section 9 (MULTI-AGENT DEBATE)** — Adjust debate perspectives
- **Section 22 (TOOL SELECTION)** — Modify tool priorities

## Memory Configuration

### Directory Structure

SOVEREIGN stores data at `~/.sovereign/`. The structure is:

```
~/.sovereign/
├── knowledge/       # Categorized knowledge
├── memory/          # Session and decision history
├── workspace/       # Project and artifact tracking
├── config/          # System preferences
└── consolidate.py   # Consolidation utility (also in repo scripts/)
```

### Preferences

Edit `~/.sovereign/config/preferences.json` to customize:

```json
{
  "version": "4.0",
  "constraints": {
    "cost": "ZERO"
  },
  "reasoning": {
    "self_critique": true,
    "multi_agent_debate": true,
    "tree_of_thought": true
  }
}
```

## opencode.json Integration

### As Default Agent

```json
{
  "default_agent": "sovereign"
}
```

### With References

```json
{
  "references": {
    "sovereign-knowledge": {
      "path": "~/.sovereign/knowledge",
      "description": "SOVEREIGN knowledge base: facts, patterns, lessons, preferences"
    },
    "sovereign-memory": {
      "path": "~/.sovereign/memory",
      "description": "SOVEREIGN memory: sessions, decisions, goals"
    }
  }
}
```

### Agent Override

```json
{
  "agent": {
    "sovereign": {
      "description": "Custom description",
      "mode": "all",
      "color": "gold",
      "permission": {
        "edit": "allow",
        "bash": "ask"
      }
    }
  }
}
```

## Commands

| Command | File | Description |
|---------|------|-------------|
| `/sovereign-save` | `commands/sovereign-save.md` | Save session knowledge to memory |
| `/sovereign-recall` | `commands/sovereign-recall.md` | Retrieve past knowledge |
| `/sovereign-consolidate` | `commands/sovereign-consolidate.md` | Run memory consolidation |

## Skill

The SOVEREIGN Memory skill (`skills/sovereign-memory/SKILL.md`) provides structured knowledge about the memory system that opencode can reference during operations.
