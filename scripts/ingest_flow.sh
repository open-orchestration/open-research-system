#!/usr/bin/env bash
# Drain ingest/, normalize each item, record in state.json, flag graph dirty.
# Usage: ingest_flow.sh <topic>
set -uo pipefail   # NOT -e: a single bad item must not abort the cycle; failures are guarded per item.
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/lib.sh"
ROOT="${REPO_ROOT:-$(cd "$HERE/.." && pwd)}"
PY="python3"
RL="python3 $HERE/runlog.py"

topic="${1:-}"; [ -n "$topic" ] || { echo "usage: ingest_flow.sh <topic> [--inbox DIR]" >&2; exit 2; }
shift
INBOX="$ROOT/ingest"
while [ $# -gt 0 ]; do
  case "$1" in --inbox) INBOX="${2:?--inbox requires a DIR}"; shift 2 ;; *) shift ;; esac
done
INBOX_REL="$("$PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$INBOX" "$ROOT")"
dest="$(resolve_topic_dir "$ROOT" "$topic")/sources" || exit 1; mkdir -p "$dest"

# Fail one item: move its native to _failed and skip to the next.
fail_item() { echo "$2" >&2; mv "$1" "$INBOX/_failed/" 2>/dev/null; \
  $RL log --root "$ROOT" --flow ingest --step normalize --status fail --data "{\"reason\":\"$2\"}"; }

shopt -s nullglob
items=("$INBOX"/*)
real=(); for f in "${items[@]+"${items[@]}"}"; do
  b="$(basename "$f")"; [ "$b" = ".gitkeep" ] || [ "$b" = "_done" ] || [ "$b" = "_failed" ] || real+=("$f")
done
[ "${#real[@]}" -gt 0 ] || { echo "no new sources in $INBOX"; exit 0; }

mkdir -p "$INBOX/_done" "$INBOX/_failed"
added=0
for f in "${real[@]}"; do
  name="$(basename "$f")"
  type="$("$PY" "$HERE/ingest_lib.py" detect "$name")"
  title="${name%.*}"
  slug="$(slugify "$title")"

  # Determine the stable seed + human-readable source per type.
  case "$type" in
    link)
      url="$(cat "$f")" || { fail_item "$f" "unreadable .url: $f"; continue; }
      seed="$url"; source_disp="$url" ;;
    *)
      seed="$("$PY" -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" "$f")" \
        || { fail_item "$f" "hash failed: $f"; continue; }
      source_disp="file://$name" ;;
  esac
  id="$("$PY" "$HERE/state.py" gen-id c "$seed")"
  out="$dest/${id}-${slug}.md"
  rel="$("$PY" -c "import os,sys;print(os.path.relpath(sys.argv[1],sys.argv[2]))" "$out" "$ROOT")"

  if [ "${DRY_RUN:-}" = "1" ]; then echo "would ingest [$type] $source_disp -> $out"; continue; fi

  case "$type" in
    rawtext)  cp "$f" "$out" || { fail_item "$f" "copy failed: $f"; continue; } ;;
    link)
      case "$url" in
        *youtube.com*|*youtu.be*) transcribe_video "$url" > "$out" || { fail_item "$f" "transcribe failed: $url"; continue; } ;;
        *)                        fetch_link "$url"       > "$out" || { fail_item "$f" "fetch failed: $url"; continue; } ;;
      esac ;;
    document) "$MARKITDOWN" "$f" > "$out" 2>/dev/null || { fail_item "$f" "markitdown failed: $f"; continue; } ;;
  esac

  "$PY" "$HERE/state.py" add-corpus --root "$ROOT" --id "$id" --title "$title" --source "$source_disp" \
        --topic "$topic" --native "$INBOX_REL/_done/$name" --extracted "$rel" >/dev/null \
        || { fail_item "$f" "record failed: $f"; rm -f "$out"; continue; }
  mv "$f" "$INBOX/_done/" || { echo "warning: could not archive $f" >&2; }
  added=$((added+1))
  $RL log --root "$ROOT" --flow ingest --step normalize --status ok \
    --data "{\"corpus_id\":\"$id\",\"type\":\"$type\"}"
  echo "ingested [$type]: $source_disp -> $out"
done
$RL log --root "$ROOT" --flow ingest --step summary --status ok \
  --data "{\"corpus_added\":$added,\"graph_dirty\":true}"
echo "Done. Graph marked dirty; run the graph-update step next."
