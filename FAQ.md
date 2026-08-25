# Frequently Asked Questions

## General

### What is SOVEREIGN?

SOVEREIGN is a cognitive architecture configuration for [opencode](https://opencode.ai) that provides autonomous reasoning, persistent memory, multi-agent debate, and structured knowledge management — all using zero-cost tools.

### Is SOVEREIGN a new application?

No. SOVEREIGN is an agent definition, memory system, and set of commands for opencode. It enhances your existing opencode installation without requiring any additional software.

### Does SOVEREIGN cost money?

No. SOVEREIGN operates under an absolute zero-cost constraint. Every tool, resource, and capability is free. No paid API keys, subscriptions, or premium tools are required or recommended.

### What platforms does SOVEREIGN support?

SOVEREIGN works wherever opencode works: Windows, macOS, and Linux. The memory consolidation utility requires Python 3.10+.

## Installation

### How do I install SOVEREIGN?

See the [Installation Guide](docs/INSTALLATION.md) for detailed instructions. The basic steps are:

1. Clone the repository
2. Copy `agent/sovereign.md` to your opencode agents directory
3. Copy commands and skills to their respective directories
4. Run `python scripts/consolidate.py` to initialize the memory system
5. Restart opencode

### Where does SOVEREIGN store data?

All data is stored locally at `~/.sovereign/`. This includes:

- Knowledge base (facts, patterns, lessons, preferences, domain)
- Memory system (sessions, decisions, goals)
- Workspace (projects, artifacts)

### Can I move the data directory?

The default location is `~/.sovereign/`. If you need to change this, update the paths in the agent configuration and consolidation script.

## Usage

### How do I activate SOVEREIGN?

After installation and restarting opencode, SOVEREIGN appears as a primary agent. You can:

1. Set it as your default agent in `opencode.json`: `"default_agent": "sovereign"`
2. Reference it directly: `@sovereign analyze this codebase`
3. Use its commands: `/sovereign-save`, `/sovereign-recall`, `/sovereign-consolidate`

### What does SOVEREIGN do differently from regular opencode?

SOVEREIGN adds:

- **Structured reasoning protocols** — systematic approach to complex problems
- **Persistent memory** — knowledge that survives across sessions
- **Multi-agent debate** — competing perspectives on uncertain conclusions
- **Self-critique** — systematic bias detection and falsification
- **Knowledge management** — organized storage and retrieval of information

### How does the memory system work?

SOVEREIGN maintains Markdown files organized by category:

- **Facts** — Verified information with sources and confidence levels
- **Patterns** — Recurring solutions to common problems
- **Lessons** — Mistakes and how to avoid them
- **Preferences** — User's preferred styles and workflows
- **Domain** — Domain-specific expertise

The consolidation utility periodically cleans up, merges, and optimizes these files.

### Can I manually edit the knowledge base?

Yes. All files are plain Markdown. You can edit them directly. The consolidation utility will respect your changes.

## Troubleshooting

### SOVEREIGN doesn't appear in opencode

1. Verify the agent file exists: `ls ~/.config/opencode/agents/sovereign.md`
2. Restart opencode (config is loaded at startup)
3. Check for syntax errors in the agent file

### Memory consolidation fails

1. Ensure Python 3.10+ is installed: `python --version`
2. Run with verbose output: `python scripts/consolidate.py --verbose`
3. Check file permissions on `~/.sovereign/`

### SOVEREIGN doesn't seem to use its memory

1. Ensure the memory system is initialized: `python scripts/consolidate.py`
2. Use `/sovereign-recall` to verify memory is accessible
3. Check that knowledge files are not empty

## Technical

### How is SOVEREIGN different from a regular system prompt?

SOVEREIGN is a comprehensive cognitive architecture with:

- 40 structured reasoning protocols
- Persistent file-based memory
- Multiple specialist agent definitions
- Dedicated commands and skills
- A standalone consolidation utility

A regular system prompt is a single set of instructions. SOVEREIGN is an integrated system.

### Does SOVEREIGN work with all opencode providers?

Yes. SOVEREIGN is provider-agnostic. It works with any model configured in opencode, whether local (Ollama) or remote (OpenRouter, Google, etc.).

### Can I customize SOVEREIGN?

Yes. All files are plain text (Markdown, JSON, Python). You can:

- Modify the agent prompt to adjust reasoning protocols
- Add specialist agent definitions
- Create domain-specific knowledge templates
- Extend the consolidation utility
- Add custom commands and skills
