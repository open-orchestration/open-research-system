#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/scripts" "$TMP/ingest" "$TMP/docs/06-x/sources"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/junk.py" \
   "$ROOT/scripts/search_flow.sh" "$TMP/scripts/"

# Fake search: ignores args, prints two results (one good, one junk).
cat > "$TMP/scripts/fake_search.py" <<'PY'
import json
print(json.dumps([{"url": "http://x/good", "title": "Good Source"},
                  {"url": "http://x/junk", "title": "Junk Source"}]))
PY
# Fake fetch: clean markdown for /good, a JS-shell page for /junk.
cat > "$TMP/scripts/fake_fetch.py" <<'PY'
import sys
url = sys.argv[1]
if url.endswith("/good"):
    print("# Good Source\n\n" + ("real content " * 60))
else:
    print("Just a moment...")
PY

# Seed a queued gap.
REPO_ROOT="$TMP" python3 "$TMP/scripts/state.py" add-gap --root "$TMP" --topic 06-x --desc "hybrid retrieval" >/dev/null

PY=python3 SEARCH="$TMP/scripts/fake_search.py" FETCH="$TMP/scripts/fake_fetch.py" REPO_ROOT="$TMP" \
  bash "$TMP/scripts/search_flow.sh" --topic 06-x || { echo "MISS: search_flow exited nonzero"; exit 1; }

fail=0
# Exactly one good source dropped into ingest/ (junk excluded).
n=$(find "$TMP/ingest" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
[ "$n" = "1" ] && echo "ok: one non-junk source in ingest/" || { echo "MISS: ingest .md count=$n"; fail=1; }
# Gap marked done; budget spent by 1.
python3 - "$TMP" <<'PY' || fail=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
assert st["gaps"][0]["status"] == "done", st["gaps"][0]
assert st["budget"]["spent"]["sources"] == 1, st["budget"]["spent"]
print("ok: gap done, budget spent=1")
PY
[ "$fail" = 0 ] && echo "ALL OK (scenario 1)" || { echo "FAILED (scenario 1)"; exit "$fail"; }

# ---------------------------------------------------------------------------
# Scenario 2: junk-only gap — one attempt per run, failed after 3 runs.
# ---------------------------------------------------------------------------
TMP2="$(mktemp -d)"
trap 'rm -rf "$TMP" "$TMP2"' EXIT

mkdir -p "$TMP2/scripts" "$TMP2/ingest"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/junk.py" \
   "$ROOT/scripts/search_flow.sh" "$TMP2/scripts/"

cat > "$TMP2/scripts/fake_search2.py" <<'PY'
import json
print(json.dumps([{"url": "http://x/junk1", "title": "J1"},
                  {"url": "http://x/junk2", "title": "J2"}]))
PY
cat > "$TMP2/scripts/fake_fetch2.py" <<'PY'
import sys
print("Just a moment...")
PY

REPO_ROOT="$TMP2" python3 "$TMP2/scripts/state.py" add-gap --root "$TMP2" --topic 06-j --desc "junk only" >/dev/null

fail2=0
# Run 1 — gap must stay queued with attempts==1, no ingest files.
PY=python3 SEARCH="$TMP2/scripts/fake_search2.py" FETCH="$TMP2/scripts/fake_fetch2.py" REPO_ROOT="$TMP2" \
  bash "$TMP2/scripts/search_flow.sh" --topic 06-j || { echo "MISS s2r1: nonzero exit"; fail2=1; }
python3 - "$TMP2" <<'PY' || fail2=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
g = st["gaps"][0]
assert g["status"] == "queued", f"run1 status: {g}"
assert g["attempts"] == 1, f"run1 attempts: {g}"
print("ok s2r1: queued, attempts=1")
PY
n2=$(find "$TMP2/ingest" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
[ "$n2" = "0" ] && echo "ok s2r1: no ingest files" || { echo "MISS s2r1: ingest count=$n2"; fail2=1; }

# Run 2 — attempts==2, still queued.
PY=python3 SEARCH="$TMP2/scripts/fake_search2.py" FETCH="$TMP2/scripts/fake_fetch2.py" REPO_ROOT="$TMP2" \
  bash "$TMP2/scripts/search_flow.sh" --topic 06-j || { echo "MISS s2r2: nonzero exit"; fail2=1; }
python3 - "$TMP2" <<'PY' || fail2=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
g = st["gaps"][0]
assert g["status"] == "queued", f"run2 status: {g}"
assert g["attempts"] == 2, f"run2 attempts: {g}"
print("ok s2r2: queued, attempts=2")
PY

# Run 3 — attempts==3, status must be failed.
PY=python3 SEARCH="$TMP2/scripts/fake_search2.py" FETCH="$TMP2/scripts/fake_fetch2.py" REPO_ROOT="$TMP2" \
  bash "$TMP2/scripts/search_flow.sh" --topic 06-j || { echo "MISS s2r3: nonzero exit"; fail2=1; }
python3 - "$TMP2" <<'PY' || fail2=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
g = st["gaps"][0]
assert g["status"] == "failed", f"run3 status: {g}"
assert g["attempts"] == 3, f"run3 attempts: {g}"
print("ok s2r3: failed after 3 runs, attempts=3")
PY
[ "$fail2" = 0 ] && echo "ALL OK (scenario 2)" || { echo "FAILED (scenario 2)"; exit 1; }

# ---------------------------------------------------------------------------
# Scenario 3: two gaps in one snapshot — clean goes done, junk stays queued.
# ---------------------------------------------------------------------------
TMP3="$(mktemp -d)"
trap 'rm -rf "$TMP" "$TMP2" "$TMP3"' EXIT

mkdir -p "$TMP3/scripts" "$TMP3/ingest"
cp "$ROOT/scripts/lib.sh" "$ROOT/scripts/state.py" "$ROOT/scripts/junk.py" \
   "$ROOT/scripts/search_flow.sh" "$TMP3/scripts/"

cat > "$TMP3/scripts/fake_search3.py" <<'PY'
import json, sys
# Return one URL whose path matches the query keyword.
q = sys.argv[1] if len(sys.argv) > 1 else ""
print(json.dumps([{"url": f"http://x/{q.split()[0]}", "title": "Result"}]))
PY
cat > "$TMP3/scripts/fake_fetch3.py" <<'PY'
import sys
url = sys.argv[1]
if "clean" in url:
    print("# Clean Source\n\n" + ("real content " * 60))
else:
    print("Just a moment...")
PY

REPO_ROOT="$TMP3" python3 "$TMP3/scripts/state.py" add-gap --root "$TMP3" --topic 06-mix --desc "clean gap" >/dev/null
REPO_ROOT="$TMP3" python3 "$TMP3/scripts/state.py" add-gap --root "$TMP3" --topic 06-mix --desc "junk gap"  >/dev/null

fail3=0
PY=python3 SEARCH="$TMP3/scripts/fake_search3.py" FETCH="$TMP3/scripts/fake_fetch3.py" REPO_ROOT="$TMP3" \
  bash "$TMP3/scripts/search_flow.sh" --topic 06-mix || { echo "MISS s3: nonzero exit"; fail3=1; }

n3=$(find "$TMP3/ingest" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
[ "$n3" = "1" ] && echo "ok s3: one ingest file (clean gap)" || { echo "MISS s3: ingest count=$n3"; fail3=1; }

python3 - "$TMP3" <<'PY' || fail3=1
import json, sys
st = json.load(open(sys.argv[1] + "/.research/state.json"))
clean = next(g for g in st["gaps"] if g["desc"] == "clean gap")
junk  = next(g for g in st["gaps"] if g["desc"] == "junk gap")
assert clean["status"] == "done",   f"clean status: {clean}"
assert junk["status"]  == "queued", f"junk status: {junk}"
assert junk["attempts"] == 1,       f"junk attempts: {junk}"
print(f"ok s3: clean=done, junk=queued/attempts=1")
PY
[ "$fail3" = 0 ] && echo "ALL OK (scenario 3)" || { echo "FAILED (scenario 3)"; exit 1; }

echo "ALL SCENARIOS OK"
