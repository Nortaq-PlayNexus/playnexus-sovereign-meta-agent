# Installation Guide

## Prerequisites

| Requirement | Version | Purpose |
|------------|---------|---------|
| [opencode](https://opencode.ai) | Latest | Agent runtime |
| [Python](https://python.org) | 3.10+ | Memory consolidation utility |
| [Git](https://git-scm.com) | Any recent | Repository management |

## Quick Install

### Linux / macOS

```bash
# Clone the repository
git clone https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent.git
cd playnexus-sovereign-meta-agent

# Create directories if they don't exist
mkdir -p ~/.config/opencode/agents
mkdir -p ~/.config/opencode/commands
mkdir -p ~/.config/opencode/skills

# Install agent
cp agent/sovereign.md ~/.config/opencode/agents/

# Install commands
cp commands/sovereign-*.md ~/.config/opencode/commands/

# Install skill
cp -r skills/sovereign-memory ~/.config/opencode/skills/

# Initialize memory system
python3 scripts/consolidate.py
```

### Windows (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent.git
cd playnexus-sovereign-meta-agent

# Create directories if they don't exist
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode\agents"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode\commands"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode\skills"

# Install agent
Copy-Item agent\sovereign.md "$env:USERPROFILE\.config\opencode\agents\"

# Install commands
Copy-Item commands\sovereign-*.md "$env:USERPROFILE\.config\opencode\commands\"

# Install skill
Copy-Item -Recurse skills\sovereign-memory "$env:USERPROFILE\.config\opencode\skills\"

# Initialize memory system
python scripts\consolidate.py
```

## Verify Installation

```bash
# Check agent exists
ls ~/.config/opencode/agents/sovereign.md

# Check commands exist
ls ~/.config/opencode/commands/sovereign-*.md

# Check skill exists
ls ~/.config/opencode/skills/sovereign-memory/SKILL.md

# Check memory system
ls ~/.sovereign/

# Test consolidation
python scripts/consolidate.py --verbose
```

## Activate SOVEREIGN

### Option 1: Set as Default Agent

Add to your `~/.config/opencode/opencode.json`:

```json
{
  "default_agent": "sovereign"
}
```

### Option 2: Use on Demand

Reference the agent in opencode:

```
@sovereign analyze this codebase
```

### Option 3: Use Commands

Use the built-in commands:

```
/sovereign-save
/sovereign-recall
/sovereign-consolidate
```

## Restart opencode

**Important:** opencode loads configuration at startup. After installing SOVEREIGN, you must quit and restart opencode for the changes to take effect.

## Optional: Add to opencode.json References

To make the SOVEREIGN knowledge base available as a reference in opencode, add to your `opencode.json`:

```json
{
  "references": {
    "sovereign-knowledge": {
      "path": "~/.sovereign/knowledge",
      "description": "SOVEREIGN knowledge base"
    },
    "sovereign-memory": {
      "path": "~/.sovereign/memory",
      "description": "SOVEREIGN session memory"
    }
  }
}
```

## Uninstall

```bash
# Remove agent
rm ~/.config/opencode/agents/sovereign.md

# Remove commands
rm ~/.config/opencode/commands/sovereign-*.md

# Remove skill
rm -rf ~/.config/opencode/skills/sovereign-memory

# Optionally remove memory system (this deletes all stored knowledge)
rm -rf ~/.sovereign/
```

Restart opencode after removal.
