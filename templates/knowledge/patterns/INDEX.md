# PATTERNS & RECURRING SOLUTIONS

Patterns identified across tasks and domains. Used for future reference when encountering similar situations. Each pattern should capture the context, the solution, and why it works.

## Format

```
### [PATTERN NAME]
- **Domain:** [Area of application — e.g., python, javascript, systems, research, workflow]
- **Description:** [What the pattern is — one paragraph summary]
- **When to use:** [Applicable conditions — when does this pattern apply?]
- **Not when to use:** [Conditions where this pattern should NOT be used]
- **Examples:** [Concrete instances — 1-3 real-world examples]
- **Counter-examples:** [When the pattern fails — be explicit]
- **Confidence:** HIGH / MODERATE / LOW
- **Identified:** [Date — YYYY-MM-DD]
- **Last Applied:** [Date — when this pattern was last used]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Variations:** [Known variations of this pattern]
```

## Pattern Confidence Scale

- **HIGH**: Pattern validated multiple times across different contexts, strong theoretical backing
- **MODERATE**: Pattern worked in 2-3 contexts, reasonable theoretical basis, some edge cases
- **LOW**: Pattern worked once, weak theoretical basis, many edge cases unknown

## Anti-Pattern Notes

Each pattern entry should also consider:
- What made the pattern succeed
- What conditions are critical for it to work
- What are the failure modes
- Are there competing patterns for the same problem

## Example

```
### [Circular Dependency Detection]
- **Domain:** software architecture, python modules
- **Description:** Detecting circular imports by analyzing module import graphs and identifying cycles
- **When to use:** When facing "ImportError: circular import" or designing module systems
- **Not when to use:** When imports are intentionally forward-declared or using lazy loading
- **Examples:** 
  - Project X: Used import graph analysis to resolve 7 circular imports
  - Project Y: Pattern failed because of dynamic imports not captured statically
- **Counter-examples:** Lazy import patterns that appear circular but aren't
- **Confidence:** MODERATE
- **Identified:** 2026-03-10
- **Last Applied:** 2026-06-15
- **Tags:** programming, python, architecture, imports
- **Variations:** Lazy import pattern, dependency injection
```

---

## Patterns

_No patterns identified yet. Patterns will be extracted from task experiences._

---

*Last updated: 2026-08-25 18:20*