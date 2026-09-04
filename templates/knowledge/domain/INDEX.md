# DOMAIN KNOWLEDGE

Domain-specific expertise organized by topic area. This section captures structured knowledge about the domains you work in, including key concepts, conventions, tools, and references.

## Format

```
### [TOPIC]
- **Domain:** [Area of expertise — e.g., python, javascript, machine learning, legal, medical, finance]
- **Key concepts:** [Important ideas, theories, frameworks — list format]
- **Conventions:** [Standard practices, naming conventions, architecture patterns]
- **Tools:** [Commonly used tools, libraries, frameworks — with versions if relevant]
- **References:** [Source materials — books, papers, documentation, courses]
- **Confidence:** HIGH / MODERATE / LOW
- **Updated:** [Date — YYYY-MM-DD]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Related domains:** [Other domains this connects to]
```

## Confidence Guidelines

- **HIGH**: Expert-level knowledge, years of experience, widely-accepted fundamentals
- **MODERATE**: Working knowledge, has solved problems in this domain, some gaps
- **LOW**: Familiarity surface-level, still learning, consult experts for important decisions

## Domain Organization Tips

- Add new topics as you encounter them in your work
- Update confidence as you gain more experience or verify knowledge
- Link related domains using tags and "Related domains" field
- Mark outdated knowledge with a "Deprecated:" note and date

## Example

```
### [Python Async IO]
- **Domain:** programming, python
- **Key concepts:** event loop, coroutines, async/await, task scheduling, futures
- **Conventions:** use asyncio.run() at top level, avoid blocking calls in async code, use aiohttp for HTTP
- **Tools:** Python 3.8+, asyncio, aiohttp, pytest-asyncio, uvloop for performance
- **References:** 
  - "Python Async IO" – Real Python tutorial
  - asyncio documentation – docs.python.org/3/library/asyncio.html
  - "Fluent Python" – Luciano Ramalho, Chapter 18
- **Confidence:** HIGH
- **Updated:** 2026-07-10
- **Tags:** programming, python, async, concurrency
- **Related domains:** networking, web scraping, distributed systems
```