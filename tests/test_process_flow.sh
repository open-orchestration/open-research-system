#!/usr/bin/env bash
# Smoke: seed corpus -> draft cites a real id -> cite_check passes -> add-draft ->
# promote moves the file + grows SYNTHESIS -> integrity clean.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPTS="$(cd "$HERE/.." && pwd)/scripts"
ROOT="$(mktemp -d)"
trap 'rm -rf "$ROOT"' EXIT
fail() { echo "FAIL: $1"; exit 1; }

SP="python3 $SCRIPTS/state.py"

# Open the phase so process is not gated off, then seed 3 sources for one topic.
$SP set-phase --root "$ROOT" --phase synthesize >/dev/null
for i in 1 2 3; do
  mkdir -p "$ROOT/.research/docs/05-ai/sources"
  printf "# Source $i\n\nContent from https://ex/$i\n" > "$ROOT/.research/docs/05-ai/sources/$i.md"
  $SP add-corpus --root "$ROOT" --title "src$i" --source "https://ex/$i" \
    --topic "05-ai" --native "ingest/$i.md" --extracted ".research/docs/05-ai/sources/$i.md" >/dev/null
done

CID="$($SP gen-id c "https://ex/1")"
[ -n "$CID" ] || fail "no corpus id"

# A candidate topic should now be offered.
$SP candidates --root "$ROOT" | grep -q "05-ai" || fail "no candidate topic"

# Write a draft that cites a real corpus id.
ID="$($SP gen-id d "05-ai|AI deep research")"
DRAFTS="$ROOT/.research/docs/findings/_drafts"; mkdir -p "$DRAFTS"
DRAFT="$DRAFTS/$ID-ai-deep-research.md"
printf '# AI deep research\n\nstatus: draft\n\nClaim grounded in a source [%s].\n' "$CID" > "$DRAFT"

# Success check must pass.
python3 "$SCRIPTS/cite_check.py" "$DRAFT" --root "$ROOT" || fail "cite_check rejected a valid draft"

# A dangling cite must be rejected (negative check).
BAD="$DRAFTS/bad.md"; printf 'x [cffffffff]\n' > "$BAD"
if python3 "$SCRIPTS/cite_check.py" "$BAD" --root "$ROOT" >/dev/null 2>&1; then
  fail "cite_check passed a dangling cite"
fi
rm -f "$BAD"

# Record the draft + emit a gap.
$SP add-draft --root "$ROOT" --id "$ID" --topic "05-ai" --title "AI deep research" \
  --path ".research/docs/findings/_drafts/$ID-ai-deep-research.md" --cites "$CID" >/dev/null
$SP add-gap --root "$ROOT" --topic "05-ai" --desc "unanswered question" --origin process >/dev/null

# Draft shows in the review queue.
python3 "$SCRIPTS/promote.py" queue --root "$ROOT" | grep -q "$ID" || fail "draft not in review queue"

# Promote: file moves, SYNTHESIS grows, status flips.
python3 "$SCRIPTS/promote.py" promote "$ID" --root "$ROOT" >/dev/null || fail "promote failed"
[ ! -f "$DRAFT" ] || fail "draft file not moved out of _drafts"
[ -f "$ROOT/.research/docs/findings/$ID-ai-deep-research.md" ] || fail "promoted file missing"
grep -q "AI deep research" "$ROOT/.research/docs/findings/SYNTHESIS.md" || fail "SYNTHESIS not updated"

# Integrity stays clean (promoted draft's file moved; cite resolves).
python3 "$SCRIPTS/check_integrity.py" --root "$ROOT" || fail "integrity reported problems"

echo "PASS: process flow smoke"
