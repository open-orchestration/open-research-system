#!/usr/bin/env bash
# Idempotently provision ORS research deps: a python venv (crawl4ai + markitdown +
# chromium) and the graphify skill. Safe to re-run. Prints a ✓/✗ checklist.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"

# 1. venv: reuse if already resolvable, else pick a target and build.
if venv="$(ors_venv 2>/dev/null)"; then
  echo "✓ venv already provisioned: $venv"
else
  target="${ORS_VENV:-${CLAUDE_PLUGIN_DATA:+$CLAUDE_PLUGIN_DATA/venv}}"
  target="${target:-$HOME/.venvs/crawl4ai}"
  echo "→ creating venv at $target"
  python3 -m venv "$target" || { echo "✗ venv create failed"; exit 1; }
  "$target/bin/pip" install -U crawl4ai "markitdown[all]" || { echo "✗ pip install failed"; exit 1; }
  "$target/bin/crawl4ai-setup" || echo "✗ crawl4ai-setup (chromium) failed — web fetch may not work"
  venv="$target"
fi

# 2. graphify skill: install via its official MIT installer if absent.
if command -v graphify >/dev/null 2>&1; then
  echo "✓ graphify present"
else
  echo "→ installing graphify (graphifyy, MIT — github.com/safishamsi/graphify)"
  if command -v uv >/dev/null 2>&1; then
    uv tool install graphifyy || echo "✗ uv tool install graphifyy failed"
  else
    python3 -m pip install --user graphifyy || echo "✗ pip install graphifyy failed"
  fi
  if command -v graphify >/dev/null 2>&1; then
    graphify install
  elif [ -x "$HOME/.local/bin/graphify" ]; then
    echo "note: graphify installed to ~/.local/bin — add it to PATH"
  else
    echo "✗ graphify not installed — the knowledge-graph step will be skipped"
  fi
fi

# 3. verify checklist
echo "── verify ──"
vpy="$venv/bin/python"; [ -x "$vpy" ] || vpy="$venv/bin/python3"
"$vpy" -c "import crawl4ai" 2>/dev/null && echo "✓ crawl4ai" || echo "✗ crawl4ai"
{ [ -x "$venv/bin/markitdown" ] || command -v markitdown >/dev/null 2>&1; } && echo "✓ markitdown" || echo "✗ markitdown"
command -v graphify >/dev/null 2>&1 && echo "✓ graphify" || echo "✗ graphify (optional)"
echo "venv: $venv"
