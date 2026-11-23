#!/usr/bin/env bash
# Run an evolution step for one strategy and commit the result (kept or not).
#
#   scripts/evolve.sh <strategy> --generations 20          # random parameter mutations
#   scripts/evolve.sh <strategy> --set fast=40 --note "why" # one hand-picked change
#   scripts/evolve.sh <strategy> --code-change --note "why" # after editing strategy.py
#
# For --code-change: if the edit is worse than the champion, the edit is saved
# to strategies/<name>/rejected/<id>.patch, strategy.py + config.json are
# restored from git, and the rejection is committed together with the log.
set -euo pipefail
cd "$(dirname "$0")/.."
name="$1"; shift
dir="strategies/$name"
[ -d "$dir" ] || { echo "no such strategy: $dir" >&2; exit 1; }

set +e
out=$(docker compose run --rm -T backtest python -m src.backtest.evolve "$name" "$@" | tee /dev/stderr)
rc=${PIPESTATUS[0]}
set -e
[ "$rc" -eq 0 ] || [ "$rc" -eq 3 ] || exit "$rc"

id=$(sed -n 's/^EXPERIMENT_ID: //p' <<<"$out" | tail -1)
msg=$(sed -n 's/^COMMIT_MSG: //p' <<<"$out" | tail -1)
[ -n "$msg" ] || exit 0

if [ "$rc" -eq 3 ]; then
  mkdir -p "$dir/rejected"
  git diff -- "$dir/strategy.py" "$dir/config.json" > "$dir/rejected/$id.patch"
  git checkout -- "$dir/strategy.py" "$dir/config.json"
fi

git add -- "$dir"
git commit -q -m "$msg" -- "$dir" && git log --oneline -1
