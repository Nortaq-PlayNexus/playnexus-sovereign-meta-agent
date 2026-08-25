# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability in SOVEREIGN META-AGENT, please report it responsibly.

**Do not** open a public GitHub issue for security vulnerabilities.

Instead, please email security concerns to the maintainers via GitHub's private vulnerability reporting.

## Scope

SOVEREIGN is an agent configuration and memory system for opencode. It does not:
- Run a network server
- Accept incoming connections
- Process untrusted input from external sources
- Store credentials (beyond what opencode itself manages)

SOVEREIGN stores data locally on the filesystem. The primary security considerations are:

### Local Filesystem Access

- SOVEREIGN reads and writes to `~/.sovereign/`
- All data is stored in plaintext Markdown and JSON files
- No encryption is applied to stored knowledge
- Users should ensure appropriate filesystem permissions

### Integration with opencode

- SOVEREIGN inherits opencode's security model
- SOVEREIGN does not bypass opencode's permission system
- SOVEREIGN does not make network requests directly (opencode handles this)
- SOVEREIGN does not execute arbitrary code without user permission

### Zero-Cost Constraint

- SOVEREIGN never requires paid API keys or credentials
- SOVEREIGN never sends data to external paid services
- All reasoning happens through opencode's configured providers

## Best Practices

1. **Filesystem permissions** — Ensure `~/.sovereign/` is not world-readable if it contains sensitive project knowledge
2. **No secrets in knowledge base** — Never store API keys, passwords, or tokens in the SOVEREIGN knowledge files
3. **Review before sharing** — If sharing your `~/.sovereign/` directory, review contents for sensitive information
4. **Keep opencode updated** — SOVEREIGN inherits security fixes from opencode

## Data Storage

All SOVEREIGN data is stored locally at:

```
~/.sovereign/
```

No data is transmitted externally by SOVEREIGN itself. Network access is handled entirely by opencode based on its own configuration.

## Changes to This Policy

Any changes to this security policy will be documented in the CHANGELOG.
