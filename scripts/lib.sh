#!/usr/bin/env bash
# Shared helpers for spike scripts.
set -euo pipefail

slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g'; }

# Resolve a topic arg (slug or NN prefix) to its docs dir; echo path or exit 1.
resolve_topic_dir() {
  local root="$1" arg="$2" match
  match=$(find "$root/docs" -maxdepth 1 -type d -name "*${arg}*" | grep -E '/[0-9]{2}-' | head -1)
  [ -n "$match" ] || { echo "no topic dir matches '$arg'" >&2; return 1; }
  echo "$match"
}

MARKITDOWN="${MARKITDOWN:-$HOME/.local/bin/markitdown}"
