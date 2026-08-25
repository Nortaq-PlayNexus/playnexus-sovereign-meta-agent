# Troubleshooting

## Installation Issues

### Agent not found in opencode

**Symptom:** SOVEREIGN doesn't appear as an agent option.

**Check:**
```bash
ls ~/.config/opencode/agents/sovereign.md
```

**Fix:** If the file doesn't exist, re-copy it:
```bash
cp agent/sovereign.md ~/.config/opencode/agents/
```

Then **restart opencode** — config is loaded at startup, not hot-reloaded.

### Commands not recognized

**Symptom:** `/sovereign-save` etc. don't appear in opencode.

**Check:**
```bash
ls ~/.config/opencode/commands/sovereign-*.md
```

**Fix:** Re-copy command files and restart opencode.

### Skill not loaded

**Symptom:** The sovereign-memory skill doesn't activate.

**Check:**
```bash
ls ~/.config/opencode/skills/sovereign-memory/SKILL.md
```

**Fix:** Re-copy the skill directory and restart opencode.

## Memory System Issues

### Memory directory doesn't exist

**Symptom:** `~/.sovereign/` is missing or incomplete.

**Fix:**
```bash
python scripts/consolidate.py
```

This will create the directory structure if missing.

### Consolidation script fails

**Symptom:** Python error when running `consolidate.py`.

**Check Python version:**
```bash
python --version
```

SOVEREIGN requires Python 3.10+. If you have an older version, install a newer one.

**Run with verbose output:**
```bash
python scripts/consolidate.py --verbose
```

This shows exactly where the error occurs.

### Files are empty after consolidation

**Symptom:** INDEX.md files lost their content.

**Cause:** This shouldn't happen — consolidation only cleans up formatting and updates timestamps.

**Fix:** Restore from git if you committed the initial templates, or re-clone the repository.

### Memory not persisting between sessions

**Symptom:** SOVEREIGN doesn't recall previous conversations.

**Check:** Ensure SOVEREIGN is actually writing to files:
```bash
ls -la ~/.sovereign/memory/sessions/
```

**Fix:** Use `/sovereign-save` at the end of important sessions to explicitly save knowledge.

## Performance Issues

### SOVEREIGN is slow to respond

**Possible causes:**
- Complex reasoning protocols are being applied to simple questions
- Memory files are very large
- Too many specialist agents are being spawned

**Fix:** For simple tasks, SOVEREIGN should bypass deep reasoning (check the agent prompt's "trivial task" path).

### Consolidation takes too long

**Possible cause:** Very large knowledge files.

**Fix:** Run consolidation periodically rather than waiting for files to grow very large:
```bash
python scripts/consolidate.py
```

## Integration Issues

### SOVEREIGN conflicts with other agents

**Symptom:** Other opencode agents behave unexpectedly.

**Fix:** Ensure the sovereign agent file is in the correct location and doesn't override other agents' names. Check `~/.config/opencode/opencode.json` for conflicts.

### opencode.json errors after installation

**Symptom:** opencode fails to start with a config error.

**Fix:** Check your `opencode.json`/`opencode.jsonc` for JSON syntax errors. Use the escape hatch:
```bash
OPENCODE_DISABLE_PROJECT_CONFIG=1 opencode
```

Then fix the config file.

## Getting More Help

1. Check the [FAQ](FAQ.md)
2. Read the [Installation Guide](docs/INSTALLATION.md)
3. Open a [GitHub Issue](https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent/issues) with the bug report template
4. Start a [Discussion](https://github.com/Nortaq-PlayNexus/playnexus-sovereign-meta-agent/discussions)
