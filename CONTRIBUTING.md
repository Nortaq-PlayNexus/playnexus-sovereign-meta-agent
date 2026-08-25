# Contributing to SOVEREIGN META-AGENT

Thank you for your interest in contributing to SOVEREIGN.

## How to Contribute

### Reporting Issues

- Use the [bug report template](https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent/issues/new?template=bug_report.md)
- Include your opencode version, Python version, and OS
- Describe the issue clearly with steps to reproduce

### Suggesting Features

- Use the [feature request template](https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent/issues/new?template=feature_request.md)
- Explain the use case and expected behavior
- Consider whether the feature fits the zero-cost constraint

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with a clear message
6. Push to your fork
7. Open a Pull Request

### Contribution Areas

**Specialist Agents** — New agent definitions for specific domains or capabilities.

**Knowledge Templates** — Domain-specific knowledge base templates for industries or use cases.

**Memory Improvements** — Better consolidation algorithms, search, or retrieval.

**Documentation** — Tutorials, guides, examples, translations.

**Testing** — Test scripts that validate the memory system and agent configuration.

**Integrations** — Connections to additional free tools and services.

## Guidelines

- **Zero-cost only** — All contributions must work with free tools and resources
- **No fabricated features** — Only document and support functionality that actually exists
- **Preserve existing behavior** — Don't break existing workflows
- **Test your changes** — Run `python scripts/consolidate.py --verbose` to verify
- **Document changes** — Update CHANGELOG.md and relevant docs

## Code Style

- Markdown: Use standard GitHub-flavored Markdown
- Python: Follow PEP 8
- JSON: Use 2-space indentation
- Agent prompts: Use clear, actionable language

## Pull Request Checklist

- [ ] Changes follow the zero-cost constraint
- [ ] No fabricated features or capabilities
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Memory consolidation script still works
- [ ] No secrets or credentials included
- [ ] Clear commit messages

## Questions?

Open a [discussion](https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent/discussions) for general questions about the project.
