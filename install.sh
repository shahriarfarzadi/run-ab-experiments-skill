#!/bin/sh
set -eu

SKILL_NAME="run-ab-experiments"
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SOURCE="$SCRIPT_DIR/skills/$SKILL_NAME"
HARNESS=""
FORCE=0

usage() {
  cat <<'EOF'
Usage: ./install.sh <codex|claude|agy|antigravity|all> [--force]

Installs the run-ab-experiments skill for one or more user-level agent clients.
Existing non-identical installations are left untouched unless --force is used.
With --force, the installer moves the old skill to a timestamped backup first.
EOF
}

for argument in "$@"; do
  case "$argument" in
    codex|claude|agy|antigravity|all)
      if [ -n "$HARNESS" ]; then
        echo "error: choose exactly one harness target" >&2
        usage >&2
        exit 2
      fi
      HARNESS="$argument"
      ;;
    --force)
      FORCE=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown argument: $argument" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [ -z "$HARNESS" ]; then
  usage >&2
  exit 2
fi

if [ ! -f "$SOURCE/SKILL.md" ]; then
  echo "error: bundled skill is missing: $SOURCE/SKILL.md" >&2
  exit 1
fi

install_skill() {
  label=$1
  target=$2
  parent=$(dirname -- "$target")

  if [ -e "$target" ] || [ -L "$target" ]; then
    if diff -qr "$SOURCE" "$target" >/dev/null 2>&1; then
      echo "$label: already up to date at $target"
      return
    fi

    if [ "$FORCE" -ne 1 ]; then
      echo "$label: existing skill differs at $target" >&2
      echo "Re-run with --force to back it up and install this version." >&2
      return 3
    fi

    timestamp=$(date +%Y%m%d-%H%M%S)
    backup="$target.backup.$timestamp"
    mv "$target" "$backup"
    echo "$label: backed up existing skill to $backup"
  fi

  mkdir -p "$parent"
  cp -R "$SOURCE" "$target"
  echo "$label: installed at $target"
}

install_codex() {
  install_skill "Codex" "$HOME/.agents/skills/$SKILL_NAME"
}

install_claude() {
  claude_home=${CLAUDE_CONFIG_DIR:-"$HOME/.claude"}
  install_skill "Claude Code" "$claude_home/skills/$SKILL_NAME"
}

install_agy() {
  install_skill "Antigravity CLI (agy)" "$HOME/.gemini/config/skills/$SKILL_NAME"
}

case "$HARNESS" in
  codex)
    install_codex
    ;;
  claude)
    install_claude
    ;;
  agy|antigravity)
    install_agy
    ;;
  all)
    install_codex
    install_claude
    install_agy
    ;;
esac

echo "Installation complete. Open a new session if the skill is not visible immediately."
