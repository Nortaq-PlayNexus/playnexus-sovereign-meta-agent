# GENERATED ARTIFACTS

Outputs, files, and deliverables produced during tasks. This section tracks what was created, where it's stored, and its current status.

## Format

```
### [ARTIFACT NAME]
- **Type:** [Code / Document / Data / Config / Analysis / Design / Test / Other]
- **Location:** [File path — relative to ~/.sovereign/workspace/ or absolute]
- **Created:** [Date — YYYY-MM-DD]
- **Purpose:** [What it was created for — the problem it solves or the deliverable it provides]
- **Status:** CURRENT / DEPRECATED / SUPERSEDED / ARCHIVED
- **Version:** [Version number — optional, e.g., 1.0, 2.3-beta]
- **Tags:** [relevant tags — lowercase, comma-separated]
- **Related artifacts:** [Links to other artifacts this builds on or relates to]
- **License:** [If applicable — e.g., MIT, GPL, CC-BY, or "proprietary/free"]
```

## Artifact Type Guidelines

- **Code**: Source files, scripts, programs, libraries
- **Document**: Markdown files, PDFs, reports, specifications
- **Data**: Datasets, CSV files, JSON databases, results dumps
- **Config**: Configuration files, scripts, setup utilities
- **Analysis**: Analysis results, charts, graphs, reports
- **Design**: UI sketches, architecture diagrams, system designs
- **Test**: Test suites, test reports, validation results
- **Other**: Any other type of output

## Status Definitions

- **CURRENT**: Currently in use, the latest version, actively maintained
- **DEPRECATED**: No longer the preferred version, kept for reference, may be removed later
- **SUPERSEDED**: Replaced by a newer version, the old one should be archived
- **ARCHIVED**: Historical, no longer relevant, preserved for record-keeping

## Example

```
### [Authentication Module] — v1.2
- **Type:** Code
- **Location:** ~/.sovereign/workspace/projects/auth-module/auth.py
- **Created:** 2026-06-20
- **Purpose:** User authentication module with OAuth2 support and password hashing
- **Status:** CURRENT
- **Version:** 1.2
- **Tags:** authentication, oauth2, security
- **Related artifacts:** [Auth design diagram, Auth test suite]
- **License:** MIT
```