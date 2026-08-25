#!/usr/bin/env python3
"""
SOVEREIGN Memory Consolidation Utility
Runs independently to consolidate and maintain the persistent memory system.
Usage: python consolidate.py [--dry-run] [--verbose]
"""

import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

SOVEREIGN_HOME = Path.home() / ".sovereign"

def log(msg, verbose=False):
    if verbose:
        print(f"[SOVEREIGN] {msg}")

def read_file(path, verbose=False):
    log(f"Reading: {path}", verbose)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def write_file(path, content, dry_run=False, verbose=False):
    if dry_run:
        log(f"[DRY RUN] Would write: {path}", verbose)
        return True
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"Wrote: {path}", verbose)
        return True
    except Exception as e:
        print(f"Error writing {path}: {e}")
        return False

def count_entries(content):
    """Count ### entries in markdown content."""
    return len(re.findall(r"^### ", content, re.MULTILINE))

def consolidate_index(path, dry_run=False, verbose=False):
    """Consolidate a single INDEX.md file."""
    content = read_file(path, verbose)
    if not content:
        return 0, 0

    before_count = count_entries(content)
    log(f"{path.name}: {before_count} entries", verbose)

    # Remove duplicate blank lines (basic cleanup)
    cleaned = re.sub(r"\n{4,}", "\n\n\n", content)

    # Update timestamp
    cleaned = re.sub(
        r"\*Last updated:.*?\*",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        cleaned
    )

    if cleaned != content:
        write_file(path, cleaned, dry_run, verbose)
        after_count = count_entries(cleaned)
        return before_count, after_count

    return before_count, before_count

def consolidate_sessions(verbose=False):
    """Summarize old session logs."""
    sessions_file = SOVEREIGN_HOME / "memory" / "sessions" / "INDEX.md"
    content = read_file(sessions_file, verbose)

    if not content:
        return

    log(f"Session log has {count_entries(content)} entries", verbose)
    # Session consolidation would require parsing dates
    # and creating summaries - placeholder for when sessions exist

def get_memory_stats(verbose=False):
    """Generate memory statistics."""
    stats = {}
    categories = {
        "knowledge/facts": SOVEREIGN_HOME / "knowledge" / "facts",
        "knowledge/patterns": SOVEREIGN_HOME / "knowledge" / "patterns",
        "knowledge/lessons": SOVEREIGN_HOME / "knowledge" / "lessons",
        "knowledge/preferences": SOVEREIGN_HOME / "knowledge" / "preferences",
        "knowledge/domain": SOVEREIGN_HOME / "knowledge" / "domain",
        "memory/sessions": SOVEREIGN_HOME / "memory" / "sessions",
        "memory/decisions": SOVEREIGN_HOME / "memory" / "decisions",
        "memory/goals": SOVEREIGN_HOME / "memory" / "goals",
    }

    total = 0
    for name, path in categories.items():
        index_file = path / "INDEX.md"
        content = read_file(index_file, verbose)
        count = count_entries(content)
        stats[name] = count
        total += count

    return stats, total

def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("SOVEREIGN Memory Consolidation")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Home: {SOVEREIGN_HOME}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("=" * 60)

    # Create directory structure if it doesn't exist
    if not SOVEREIGN_HOME.exists():
        print(f"Creating {SOVEREIGN_HOME}...")
        dirs = [
            "knowledge/facts", "knowledge/patterns", "knowledge/lessons",
            "knowledge/preferences", "knowledge/domain",
            "memory/sessions", "memory/decisions", "memory/goals",
            "workspace/projects", "workspace/artifacts", "config"
        ]
        for d in dirs:
            (SOVEREIGN_HOME / d).mkdir(parents=True, exist_ok=True)
        print(f"Created directory structure at {SOVEREIGN_HOME}")

    # Get stats
    stats, total = get_memory_stats(verbose)
    print("\n--- Memory Statistics ---")
    for name, count in stats.items():
        status = "EMPTY" if count == 0 else f"{count} entries"
        print(f"  {name:30s} {status}")
    print(f"  {'TOTAL':30s} {total} entries")

    # Consolidate each index
    print("\n--- Consolidating ---")
    all_indexes = list(SOVEREIGN_HOME.rglob("INDEX.md"))
    total_before = 0
    total_after = 0

    for index_path in sorted(all_indexes):
        before, after = consolidate_index(index_path, dry_run, verbose)
        total_before += before
        total_after += after
        if before != after:
            print(f"  UPDATED: {index_path.relative_to(SOVEREIGN_HOME)} ({before} -> {after})")

    # Consolidate sessions
    consolidate_sessions(verbose)

    print(f"\n--- Summary ---")
    print(f"  Total entries: {total_before}")
    print(f"  Entries after consolidation: {total_after}")
    print(f"  Changes made: {'None' if total_before == total_after else 'Yes'}")

    if dry_run:
        print("\n  (Dry run - no files were modified)")
    else:
        print("\n  Memory consolidated successfully.")

    print("=" * 60)

if __name__ == "__main__":
    main()
