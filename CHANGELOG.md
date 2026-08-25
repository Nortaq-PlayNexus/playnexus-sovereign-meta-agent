# Changelog

All notable changes to SOVEREIGN META-AGENT will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [4.0.0] - 2026-08-25

### Added

- Initial release of SOVEREIGN META-AGENT v4.0
- 40 reasoning protocols covering the full cognitive architecture
- META-AGENT supervisory intelligence system
- 14 specialist agent definitions (Researcher, Analyst, Architect, Skeptic, Red Team, Optimizer, Fact Checker, Implementer, Memory Curator, Strategist, Coder, Tester, Documenter, Learner)
- Persistent memory system with knowledge base at `~/.sovereign/`
- Knowledge categories: facts, patterns, lessons, preferences, domain
- Memory categories: sessions, decisions, goals
- Workspace categories: projects, artifacts
- Memory consolidation utility (`scripts/consolidate.py`)
- Three opencode commands: `/sovereign-save`, `/sovereign-recall`, `/sovereign-consolidate`
- SOVEREIGN Memory skill for opencode
- Multi-agent debate protocol (7 perspectives)
- Adversarial self-critique protocol
- Tree-of-Thought exploration
- React-style agent loop
- Evidence hierarchy (10 levels)
- Uncertainty engine with 5 confidence levels
- Anti-hallucination verification protocol
- Causal reasoning framework
- Second-order thinking protocol
- Failure mode analysis
- Meta-optimization protocol
- Zero-cost constraint (absolute rule)
- System preferences configuration (`templates/config/preferences.json`)
- Installation scripts for cross-platform setup
- Complete documentation suite

### Security

- All data stored locally — no external transmission by SOVEREIGN
- No secrets or credentials required
- Inherits opencode's security model
