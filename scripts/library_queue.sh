#!/usr/bin/env bash
# Run library optimizer chains one strategy at a time, each while holding one of the
# shared slot locks (/home/luca/trading/logs/tso-slot-{1,2,3}.lock; at most 3 optimizer
# containers machine-wide, agreed between the parallel library sessions).
#
#   setsid nohup bash scripts/library_queue.sh <label> name:universe [name:universe ...] >/dev/null 2>&1 &
#
# universe = "stock" or "etf" (= config etf list minus ^ indices).
# Per strategy: base run 0.5 h -> screen (60 samples, 2 workers) -> broad basket of every
# "ok" symbol, 1 h. A strategy is skipped if a dedicated worktree for it exists when its turn
# comes (another session owns it). Leaderboard at the end, then one summary email.
# Each stage is resumable: re-running the same command continues where it stopped.
set -u
WT="$(cd "$(dirname "$0")/.." && pwd)"
MAIN=/home/luca/trading
TSO=$MAIN/.claude/skills/trading-strategy-optimizer/scripts
SEND=$HOME/.claude/skills/long-task-email/scripts/send_email.py
if [ "${1:-}" = --container ]; then   # internal: run one container (called under a slot lock)
  name=$2; cmd=$3
  exec docker run --rm --name "$name" --user 1000:1000 -e TZ=UTC \
    -v "$WT:/app" -v "$MAIN/data:/app/data" -v "$MAIN/logs:/app/logs" \
    -v "$MAIN/config:/app/config:ro" -v "$TSO:/opt/tso:ro" -w /app \
    trading-pipeline:latest sh -c "$cmd" >>"$MAIN/logs/$name.console.log" 2>&1
fi
LABEL="${1:?label}"; shift
LOG=$MAIN/logs/library-queue-$LABEL.log
START=$(date +%s)
log() { echo "[$(date -u +%FT%TZ)] $*" >>"$LOG"; }

ETF_LIST=$(python3 -c "
import yaml; c=yaml.safe_load(open('$MAIN/config/symbols.yaml'))
print(','.join(s for s in c['etf'] if not str(s).startswith('^')))")

in_slot() {   # run "$@" while holding a free slot lock; wait until one is free
  while :; do
    for s in 1 2 3; do
      flock -n -E 75 "$MAIN/logs/tso-slot-$s.lock" "$@"
      rc=$?
      [ $rc -ne 75 ] && return $rc
    done
    sleep 120
  done
}

DONE=""; FAILED=""; SKIPPED=""
log "queue $LABEL start: $*"
for item in "$@"; do
  n=${item%%:*}; u=${item#*:}
  claim=$(echo "$n" | tr _ -)
  if git -C "$MAIN" worktree list | grep -q "/worktrees/$claim[[:space:]]"; then
    log "$n: skipped, dedicated worktree $claim exists"; SKIPPED="$SKIPPED $n"; continue
  fi
  [ "$u" = etf ] && U="$ETF_LIST" || U="$u"
  S=strategies/$n
  CHAIN="python /opt/tso/optimize.py $S --hours 0.5 &&
    python /opt/tso/screen.py $S --universe $U --samples 60 --workers 2 &&
    OK=\$(python -c \"import csv;print(','.join(r['symbol'] for r in csv.DictReader(open('$S/screen.csv')) if r['status']=='ok'))\") &&
    if [ -n \"\$OK\" ]; then python /opt/tso/optimize.py $S --symbols \$OK --tag broad --hours 1; else echo 'no ok symbols'; fi"
  log "$n: waiting for a slot"
  in_slot bash "$0" --container "tso-$n" "$CHAIN"
  rc=$?
  if [ $rc -eq 0 ]; then log "$n: done"; DONE="$DONE $n"; else log "$n: FAILED rc=$rc (see logs/tso-$n.console.log)"; FAILED="$FAILED $n"; fi
done

in_slot bash "$0" --container "tso-leaderboard-$LABEL" "python /opt/tso/leaderboard.py strategies"
log "queue $LABEL end (leaderboard rc=$?)"

SECS=$(( $(date +%s) - START ))
STATE=Done; [ -n "$FAILED" ] && STATE="Needs you"
BODY="Library queue $LABEL in $WT
Done:$DONE
Failed:${FAILED:- none}
Skipped (owned by another session):${SKIPPED:- none}
Duration: $((SECS/3600))h $((SECS%3600/60))min
Leaderboard: $WT/strategies/LEADERBOARD.md

Last log lines:
$(tail -n 25 "$LOG")

Next step: ask Claude to report on the library queue $LABEL (analyst notes, per-symbol runs where the screen was persistent)."
python3 "$SEND" --subject "[Claude] $STATE: library queue $LABEL ($((SECS/3600))h)" --body "$BODY" >>"$LOG" 2>&1 || log "email failed"
