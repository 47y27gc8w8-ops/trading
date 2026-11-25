#!/usr/bin/env bash
# Run the optimizer chain (base 0.5 h -> screen -> broad basket 1 h) for each strategy in turn,
# one chain at a time. A chain starts only while it holds one of the shared slot locks
# (logs/tso-slot-{1,2,3}.lock, agreed between the library sessions) AND fewer than 3 tso-
# containers are running, so the 8 cores stay shared with the collectors and other sessions.
# Each chain gets the skill's email watcher. Resumable: finished stages end at once on a rerun.
#
#   cd <repo or worktree root>
#   setsid nohup bash scripts/strategy_library/run_queue.sh name1 name2 ... >logs/library-queue.log 2>&1 &
set -u
REPO="$(pwd)"
TSO="${TSO:-/home/luca/trading/.claude/skills/trading-strategy-optimizer/scripts}"
LOCKS="${LOCKS:-/home/luca/trading/logs}"
MAX_RUNNING="${MAX_RUNNING:-3}"
N=$#; I=0

chain() {   # $1 = strategy name; runs while the caller holds a slot lock
  local name=$1 S="strategies/$1"
  docker compose run -d --rm --name "tso-$name" -v "$TSO:/opt/tso:ro" backtest sh -c "
    python /opt/tso/optimize.py $S --hours 0.5 &&
    python /opt/tso/screen.py $S --universe crypto --samples 60 --workers 2 &&
    OK=\$(python -c \"import csv;print(','.join(r['symbol'] for r in csv.DictReader(open('$S/screen.csv')) if r['status']=='ok'))\") &&
    if [ -n \"\$OK\" ]; then python /opt/tso/optimize.py $S --symbols \$OK --tag broad --hours 1; else echo 'no ok symbols: broad basket skipped'; fi" || return 1
  bash "$TSO/notify_when_done.sh" "tso-$name" "$S" "library chain $I/$N (base, screen, broad)"
}

for name in "$@"; do
  I=$((I + 1))
  while true; do
    if [ "$(docker ps -q --filter name=tso- | wc -l)" -lt "$MAX_RUNNING" ]; then
      for n in 1 2 3; do
        flock -n -E 75 "$LOCKS/tso-slot-$n.lock" bash -c "$(declare -f chain); I=$I N=$N TSO=$TSO; chain $name"
        rc=$?
        [ $rc -ne 75 ] && break
      done
      [ "${rc:-75}" -ne 75 ] && { echo "$(date -u +%FT%TZ) $name done (rc=$rc)"; break; }
    fi
    sleep 120
  done
done
docker compose run --rm -T -v "$TSO:/opt/tso:ro" backtest python /opt/tso/leaderboard.py strategies
echo "$(date -u +%FT%TZ) queue finished"
