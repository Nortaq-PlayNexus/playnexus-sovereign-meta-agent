#!/bin/bash
# SOVEREIGN META-AGENT — Installer
# Usage: bash install.sh

set -e

SOVEREIGN_HOME="$HOME/.sovereign"
OPENCODE_AGENTS="$HOME/.config/opencode/agents"
OPENCODE_COMMANDS="$HOME/.config/opencode/commands"
OPENCODE_SKILLS="$HOME/.config/opencode/skills"

echo "============================================"
echo "  SOVEREIGN META-AGENT — Installer"
echo "  Version 4.0 — Zero-Cost, Maximum Autonomy"
echo "============================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3.10+ is required but not found."
    echo "Install Python: https://python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "Python version: $PYTHON_VERSION"

# Check opencode directory
if [ ! -d "$HOME/.config/opencode" ]; then
    echo "WARNING: ~/.config/opencode/ not found."
    echo "Make sure opencode is installed first."
    echo "Continuing anyway..."
fi

# Create directories
echo ""
echo "Creating directories..."
mkdir -p "$OPENCODE_AGENTS"
mkdir -p "$OPENCODE_COMMANDS"
mkdir -p "$OPENCODE_SKILLS"
mkdir -p "$SOVEREIGN_HOME/knowledge/facts"
mkdir -p "$SOVEREIGN_HOME/knowledge/patterns"
mkdir -p "$SOVEREIGN_HOME/knowledge/lessons"
mkdir -p "$SOVEREIGN_HOME/knowledge/preferences"
mkdir -p "$SOVEREIGN_HOME/knowledge/domain"
mkdir -p "$SOVEREIGN_HOME/memory/sessions"
mkdir -p "$SOVEREIGN_HOME/memory/decisions"
mkdir -p "$SOVEREIGN_HOME/memory/goals"
mkdir -p "$SOVEREIGN_HOME/workspace/projects"
mkdir -p "$SOVEREIGN_HOME/workspace/artifacts"
mkdir -p "$SOVEREIGN_HOME/config"

# Install files
echo "Installing agent..."
cp agent/sovereign.md "$OPENCODE_AGENTS/"
echo "  -> $OPENCODE_AGENTS/sovereign.md"

echo "Installing commands..."
cp commands/sovereign-*.md "$OPENCODE_COMMANDS/"
echo "  -> $OPENCODE_COMMANDS/sovereign-consolidate.md"
echo "  -> $OPENCODE_COMMANDS/sovereign-recall.md"
echo "  -> $OPENCODE_COMMANDS/sovereign-save.md"

echo "Installing skill..."
cp -r skills/sovereign-memory "$OPENCODE_SKILLS/"
echo "  -> $OPENCODE_SKILLS/sovereign-memory/SKILL.md"

# Copy template files if memory is empty
if [ ! -f "$SOVEREIGN_HOME/knowledge/facts/INDEX.md" ] || [ ! -s "$SOVEREIGN_HOME/knowledge/facts/INDEX.md" ]; then
    echo "Initializing memory from templates..."
    cp templates/knowledge/*/INDEX.md "$SOVEREIGN_HOME/knowledge/facts/" 2>/dev/null || true
    cp templates/knowledge/*/INDEX.md "$SOVEREIGN_HOME/knowledge/patterns/" 2>/dev/null || true
    cp templates/knowledge/*/INDEX.md "$SOVEREIGN_HOME/knowledge/lessons/" 2>/dev/null || true
    cp templates/knowledge/*/INDEX.md "$SOVEREIGN_HOME/knowledge/preferences/" 2>/dev/null || true
    cp templates/knowledge/*/INDEX.md "$SOVEREIGN_HOME/knowledge/domain/" 2>/dev/null || true
    cp templates/memory/*/INDEX.md "$SOVEREIGN_HOME/memory/sessions/" 2>/dev/null || true
    cp templates/memory/*/INDEX.md "$SOVEREIGN_HOME/memory/decisions/" 2>/dev/null || true
    cp templates/memory/*/INDEX.md "$SOVEREIGN_HOME/memory/goals/" 2>/dev/null || true
    cp templates/workspace/*/INDEX.md "$SOVEREIGN_HOME/workspace/projects/" 2>/dev/null || true
    cp templates/workspace/*/INDEX.md "$SOVEREIGN_HOME/workspace/artifacts/" 2>/dev/null || true
fi

# Copy config
if [ ! -f "$SOVEREIGN_HOME/config/preferences.json" ]; then
    cp templates/config/preferences.json "$SOVEREIGN_HOME/config/"
    echo "  -> $SOVEREIGN_HOME/config/preferences.json"
fi

# Run consolidation
echo ""
echo "Running memory consolidation..."
python3 scripts/consolidate.py --verbose

echo ""
echo "============================================"
echo "  Installation complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "  1. Restart opencode to load the SOVEREIGN agent"
echo "  2. Set default agent (optional):"
echo "     Add to ~/.config/opencode/opencode.json:"
echo '     "default_agent": "sovereign"'
echo "  3. Or use on demand: @sovereign <your task>"
echo ""
echo "Commands:"
echo "  /sovereign-save        — Save session knowledge"
echo "  /sovereign-recall      — Retrieve past knowledge"
echo "  /sovereign-consolidate — Optimize memory"
echo ""
