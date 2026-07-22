#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

echo "Validating repository contract..."
python3 scripts/validate_repo.py

echo "Checking shell syntax..."
sh -n install.sh
sh -n scripts/validate.sh
sh -n scripts/package-release.sh

echo "Testing calculator..."
python3 -m unittest discover -s tests -p 'test_*.py'

echo "Testing installers..."
TEMP_ROOT=$(mktemp -d "${TMPDIR:-/tmp}/run-ab-experiments.XXXXXX")
trap 'rm -rf "$TEMP_ROOT"' EXIT HUP INT TERM

HOME="$TEMP_ROOT/home" sh ./install.sh all
diff -qr skills/run-ab-experiments "$TEMP_ROOT/home/.agents/skills/run-ab-experiments"
diff -qr skills/run-ab-experiments "$TEMP_ROOT/home/.claude/skills/run-ab-experiments"
diff -qr skills/run-ab-experiments "$TEMP_ROOT/home/.gemini/config/skills/run-ab-experiments"

HOME="$TEMP_ROOT/home" sh ./install.sh all

CLAUDE_CONFIG_DIR="$TEMP_ROOT/claude-custom" HOME="$TEMP_ROOT/home" \
  sh ./install.sh claude
diff -qr skills/run-ab-experiments "$TEMP_ROOT/claude-custom/skills/run-ab-experiments"

printf '\nlocal change\n' >> \
  "$TEMP_ROOT/home/.agents/skills/run-ab-experiments/SKILL.md"
if HOME="$TEMP_ROOT/home" sh ./install.sh codex >/dev/null 2>&1; then
  echo "error: installer overwrote a different skill without --force" >&2
  exit 1
fi
HOME="$TEMP_ROOT/home" sh ./install.sh codex --force
diff -qr skills/run-ab-experiments "$TEMP_ROOT/home/.agents/skills/run-ab-experiments"

BACKUP_COUNT=$(find "$TEMP_ROOT/home/.agents/skills" -maxdepth 1 \
  -type d -name 'run-ab-experiments.backup.*' | wc -l | tr -d ' ')
if [ "$BACKUP_COUNT" -ne 1 ]; then
  echo "error: forced install did not preserve exactly one backup" >&2
  exit 1
fi

echo "All validation checks passed."
