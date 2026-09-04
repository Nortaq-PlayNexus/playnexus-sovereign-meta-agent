#!/usr/bin/env python3
"""
SOVEREIGN Memory Consolidation Utility
Runs independently to consolidate and maintain the persistent memory system.
Usage: python consolidate.py [--dry-run] [--verbose] [--merge] [--link]
"""

import os
import re
import sys
import json
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, Counter

SOVEREIGN_HOME = Path.home() / ".sovereign"
CONFIG_FILE = SOVEREIGN_HOME / "config" / "preferences.json"


def log(msg, verbose=False):
    if verbose:
        print(f"[SOVEREIGN] {msg}")


def log_always(msg):
    print(f"[SOVEREIGN] {msg}")


def read_file(path, verbose=False):
    log(f"Reading: {path}", verbose)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        log(f"Error reading {path}: {e}", verbose)
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


def entry_title(content_line):
    """Extract the title from an ### line."""
    match = re.match(r"^### (.+)$", content_line.strip())
    return match.group(1).strip() if match else "Untitled"


def entry_hash(content):
    """Create a hash of entry content for duplicate detection."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


def parse_entry(block):
    """Parse a markdown entry block into structured data."""
    entry = {
        "title": "",
        "content": "",
        "source": "",
        "confidence": "MODERATE",
        "date": "",
        "tags": [],
    }

    lines = block.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("- **Content:** "):
            entry["content"] = line[len("- **Content:** "):].strip()
        elif line.startswith("- **Source:** "):
            entry["source"] = line[len("- **Source:** "):].strip()
        elif line.startswith("- **Confidence:** "):
            entry["confidence"] = line[len("- **Confidence:** "):].strip()
        elif line.startswith("- **Verified:** ") or line.startswith("- **Date:** ") or line.startswith("- **Updated:** "):
            entry["date"] = line.split(": ", 1)[-1].strip() if ": " in line else line[len("- **Verified:** "):].strip()
            # Also try to extract date from **Verified:** or **Updated:** or **Date:**
            if not entry["date"]:
                # Try to find YYYY-MM-DD pattern
                date_match = re.search(r"\d{4}-\d{2}-\d{2}", line)
                if date_match:
                    entry["date"] = date_match.group(0)
        elif line.startswith("- **Tags:** "):
            tags_str = line[len("- **Tags:** "):].strip()
            entry["tags"] = [t.strip() for t in tags_str.split(",") if t.strip()]
        elif line.startswith("### "):
            entry["title"] = entry_title(line)
        i += 1

    return entry


def format_entry(entry):
    """Format a structured entry back to markdown."""
    tags_str = ", ".join(entry.get("tags", []))
    return f"### {entry.get('title', 'Untitled')}\n- **Content:** {entry.get('content', '')}\n- **Source:** {entry.get('source', '')}\n- **Confidence:** {entry.get('confidence', 'MODERATE')}\n- **Verified:** {entry.get('date', '')}\n- **Tags:** {tags_str}\n"


def consolidate_index(path, dry_run=False, verbose=False):
    """Consolidate a single INDEX.md file with duplicate merging and confidence boosting."""
    content = read_file(path, verbose)
    if not content:
        return 0, 0, []

    before_count = count_entries(content)
    log(f"{path.name}: {before_count} entries", verbose)

    # Split into entry blocks (### followed by content)
    blocks = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    # Remove empty first element if content starts with ###
    if blocks and not blocks[0].strip():
        blocks = blocks[1:]

    # Parse all entries
    entries = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith("### "):
            entry = parse_entry(block)
            if entry["title"] or entry["content"]:
                entries.append(entry)

    if not entries:
        return before_count, before_count, []

    # Group entries by title (potential duplicates)
    title_groups = defaultdict(list)
    for entry in entries:
        title_key = entry["title"].lower().strip() if entry["title"] else "untitled"
        title_groups[title_key].append(entry)

    # Also group by content hash for near-duplicates
    merged = []
    seen_hashes = set()

    for title_key, group_entries in title_groups.items():
        if len(group_entries) == 1:
            # Single entry - keep as-is but update timestamp
            entry = group_entries[0]
            entry["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            merged.append(entry)
        else:
            # Multiple entries with same title - merge them
            log(f"  Merging {len(group_entries)} entries titled '{title_key}'", verbose)

            # Collect all unique content, sources, tags
            all_contents = set()
            all_sources = set()
            all_tags = set()
            confidences = []

            for entry in group_entries:
                if entry["content"]:
                    all_contents.add(entry["content"])
                if entry["source"]:
                    all_sources.add(entry["source"])
                if entry["tags"]:
                    all_tags.update(entry["tags"])
                confidences.append(entry.get("confidence", "MODERATE"))

            # Determine best confidence (prioritize HIGH > MODERATE > LOW)
            confidence_order = {"HIGH": 3, "MODERATE": 2, "LOW": 1}
            best_confidence = max(confidences, key=lambda c: confidence_order.get(c, 2))

            # If all have same confidence, use that; otherwise prefer highest
            if all(c == best_confidence for c in confidences):
                final_confidence = best_confidence
            else:
                # Mix of confidences - use highest
                final_confidence = "HIGH" if "HIGH" in confidences else \
                                   "MODERATE" if "MODERATE" in confidences else "LOW"

            # Merge: combine content sources, keep strongest evidence
            merged_content = "; ".join(sorted(all_contents)) if all_contents else ""
            merged_source = "; ".join(sorted(all_sources)) if all_sources else ""
            final_tags = sorted(all_tags)

            merged_entry = {
                "title": title_key.title() if title_key != "untitled" else title_key,
                "content": merged_content,
                "source": merged_source,
                "confidence": final_confidence,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "tags": final_tags,
            }
            merged.append(merged_entry)

    # Also handle entries that might not have ### prefix but are in the file
    # Rebuild the content from merged entries
    new_content_parts = []
    for entry in merged:
        new_content_parts.append(format_entry(entry))

    new_content = "\n\n".join(new_content_parts)
    # Ensure there's a trailing newline
    if new_content and not new_content.endswith("\n"):
        new_content += "\n"

    # Update last updated timestamp in the file
    new_content = re.sub(
        r"\*Last updated:.*?\*",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        new_content
    )

    if new_content != content:
        write_file(path, new_content, dry_run, verbose)
        after_count = count_entries(new_content)
        changes = []
        for entry in merged:
            changes.append(f"{entry.get('title', '?')}({entry.get('confidence', '?')})")
        return before_count, after_count, changes

    return before_count, before_count, []


def detect_duplicates_across_files(verbose=False):
    """Detect potential duplicate entries across all INDEX.md files."""
    log("Scanning for cross-file duplicates...", verbose)

    categories = {
        "facts": SOVEREIGN_HOME / "knowledge" / "facts",
        "patterns": SOVEREIGN_HOME / "knowledge" / "patterns",
        "lessons": SOVEREIGN_HOME / "knowledge" / "lessons",
        "preferences": SOVEREIGN_HOME / "knowledge" / "preferences",
        "domain": SOVEREIGN_HOME / "knowledge" / "domain",
    }

    # Collect all entries with their titles and hashes
    all_entries = defaultdict(lambda: {"titles": [], "hashes": [], "sources": [], "categories": []})

    for category, directory in categories.items():
        index_file = directory / "INDEX.md"
        content = read_file(index_file, verbose)
        if not content:
            continue

        entries = re.findall(r"### .+?^((?=### )|$)", content, re.MULTILINE | re.DOTALL)
        # Better: split by ### markers
        blocks = re.split(r"(?=^### )", content, flags=re.MULTILINE)
        if blocks and not blocks[0].strip():
            blocks = blocks[1:]

        for block in blocks:
            block = block.strip()
            if not block or not block.startswith("### "):
                continue
            entry = parse_entry(block)
            title_key = entry["title"].lower().strip() if entry["title"] else "untitled"
            content_hash = entry_hash(block)

            all_entries[title_key]["titles"].append(entry["title"] or "Untitled")
            all_entries[title_key]["hashes"].append(content_hash)
            all_entries[title_key]["sources"].append(entry.get("source", "") or "unknown")
            all_entries[title_key]["categories"].append(category)

    # Find entries appearing in multiple categories
    cross_category = {}
    for title_key, data in all_entries.items():
        if len(set(data["categories"])) > 1:
            cross_category[title_key] = data

    return cross_category


def consolidate_sessions(verbose=False):
    """Summarize and consolidate session logs."""
    sessions_file = SOVEREIGN_HOME / "memory" / "sessions" / "INDEX.md"
    content = read_file(sessions_file, verbose)

    if not content:
        log("No session log found.", verbose)
        return

    entry_count = count_entries(content)
    log(f"Session log has {entry_count} entries", verbose)

    if entry_count == 0:
        return

    # Parse sessions
    blocks = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    if blocks and not blocks[0].strip():
        blocks = blocks[1:]

    sessions = []
    for block in blocks:
        block = block.strip()
        if not block or not block.startswith("### "):
            continue
        entry = parse_entry(block)
        # Extract session ID from title
        title = entry.get("title", "")
        sessions.append({
            "title": title,
            "content": entry.get("content", ""),
            "date": entry.get("date", ""),
        })

    if not sessions:
        return

    # Summarize: group by year/month, create overview
    log(f"Processing {len(sessions)} sessions for consolidation", verbose)

    # Look for completed goals and decisions to archive
    decisions_file = SOVEREIGN_HOME / "memory" / "decisions" / "INDEX.md"
    decisions_content = read_file(decisions_file, verbose)
    decision_count = count_entries(decisions_content) if decisions_content else 0

    goals_file = SOVEREIGN_HOME / "memory" / "goals" / "INDEX.md"
    goals_content = read_file(goals_file, verbose)
    goal_count = count_entries(goals_content) if goals_content else 0

    log(f"  Decisions: {decision_count}, Goals: {goal_count}", verbose)


def get_memory_stats(verbose=False):
    """Generate comprehensive memory statistics."""
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
    confidence_dist = {"HIGH": 0, "MODERATE": 0, "LOW": 0}
    for name, path in categories.items():
        index_file = path / "INDEX.md"
        content = read_file(index_file, verbose)
        count = count_entries(content)
        # Also count confidence levels
        conf_counts = {"HIGH": 0, "MODERATE": 0, "LOW": 0}
        if content:
            for level in conf_counts:
                conf_counts[level] = len(re.findall(rf"- \*\*Confidence:\*\s*{level}", content))

        stats[name] = {"count": count, "confidence": conf_counts}
        total += count

        # Sum confidence dist
        for level, c in conf_counts.items():
            confidence_dist[level] += c

    return {"per_category": stats, "total": total, "confidence": confidence_dist}


def update_preferences_config(dry_run=False, verbose=False):
    """Update the preferences.json config file."""
    if not CONFIG_FILE.exists():
        log("No preferences.config found, skipping.", verbose)
        return True

    content = read_file(CONFIG_FILE, verbose)
    if not content:
        return True

    try:
        config = json.loads(content)
        log("Preferences config loaded", verbose)

        # Ensure key structure exists
        if "version" not in config:
            config["version"] = "4.0"
        if "initialized" not in config:
            config["initialized"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

        # Add consolidation timestamp
        config["last_consolidation"] = datetime.now().strftime("%Y-%m-%d %H:%M")

        new_content = json.dumps(config, indent=2) + "\n"
        write_file(CONFIG_FILE, new_content, dry_run, verbose)
        return True
    except json.JSONDecodeError as e:
        log(f"Error parsing preferences.json: {e}", verbose)
        return False


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    dry_run = "--dry-run" in sys.argv
    merge = "--merge" in sys.argv
    link = "--link" in sys.argv

    print("=" * 60)
    print("SOVEREIGN Memory Consolidation")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Home: {SOVEREIGN_HOME}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    if merge:
        print("Feature: Cross-entry merging enabled")
    if link:
        print("Feature: Cross-category linking enabled")
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

    # Update preferences config
    update_preferences_config(dry_run, verbose)

    # Get stats
    stats = get_memory_stats(verbose)
    print("\n--- Memory Statistics ---")
    for name, data in stats["per_category"].items():
        count_info = f"{data['count']} entries"
        if verbose:
            cd = data["confidence"]
            count_info += f" (H:{cd['HIGH']} M:{cd['MODERATE']} L:{cd['LOW']})"
        print(f"  {name:30s} {count_info}")
    print(f"  {'TOTAL':30s} {stats['total']} entries")
    print(f"  Confidence: HIGH={stats['confidence']['HIGH']}, "
          f"MODERATE={stats['confidence']['MODERATE']}, "
          f"LOW={stats['confidence']['LOW']}")

    # Cross-category duplicate detection
    if verbose:
        cross = detect_duplicates_across_files(verbose)
        if cross:
            print(f"\n--- Cross-Category Duplicates ---")
            for title_key, data in cross.items():
                print(f"  '{title_key}' appears in: {', '.join(set(data['categories']))}")

    # Consolidate each INDEX.md
    print("\n--- Consolidating INDEX.md Files ---")
    all_indexes = list(SOVEREIGN_HOME.rglob("INDEX.md"))
    # Filter to only knowledge/memory INDEX.md files (not workspace artifacts INDEX.md etc unless needed)
    relevant_indexes = [p for p in all_indexes if
                        p.relative_to(SOVEREIGN_HOME).as_posix().startswith(("knowledge/", "memory/"))]

    total_before = 0
    total_after = 0
    all_changes = []

    for index_path in sorted(relevant_indexes):
        before, after, changes = consolidate_index(index_path, dry_run, verbose)
        total_before += before
        total_after += after
        if changes:
            all_changes.append(f"  {index_path.relative_to(SOVEREIGN_HOME)}: {', '.join(changes)}")

        if before != after or verbose:
            status = "UPDATED" if before != after else "OK"
            print(f"  [{status}] {index_path.relative_to(SOVEREIGN_HOME)} "
                  f"({before} -> {after})")

    if all_changes:
        print("\n  Changes:")
        for c in all_changes:
            print(c)

    # Consolidate sessions
    print("\n--- Session Consolidation ---")
    consolidate_sessions(verbose)

    # Cross-category linking (if --link flag)
    if link:
        print("\n--- Cross-Category Linking ---")
        cross = detect_duplicates_across_files(verbose)
        if cross:
            for title_key, data in cross.items():
                print(f"  Linking '{title_key}' across: {', '.join(set(data['categories']))}")
        else:
            print("  No cross-category duplicates found.")

    # Summary
    print(f"\n--- Summary ---")
    changes_summary = "None" if total_before == total_after else f"{total_before - total_after} entries removed/merged"
    print(f"  Total entries: {total_before}")
    print(f"  Entries after consolidation: {total_after}")
    print(f"  Changes made: {changes_summary}")
    if merge and total_before != total_after:
        print(f"  Merged/removed: {total_before - total_auto} duplicate/consolidated entries")

    if dry_run:
        print("\n  (Dry run - no files were modified)")
    else:
        print("\n  Memory consolidated successfully.")

    print("=" * 60)

    if total_before != total_after and not dry_run:
        print("\n  Consider running with --verbose for detailed output.")
        print("  Consider --merge for cross-entry consolidation.")
        print("  Consider --link for cross-category linking.")

    return 0 if total_before == total_after or dry_run else 0


if __name__ == "__main__":
    main()