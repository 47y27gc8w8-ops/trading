#!/usr/bin/env bash
# Run base optimizations of the library's month-end portfolio specs IN PARALLEL, each container
# holding one slot lock /home/luca/trading/logs/tso-slot-<n>.lock (n = 1..SLOTS), then refresh the
# leaderboard of this worktree and send ONE summary email.
#
#   SLOTS=6 HOURS=1 setsid nohup bash scripts/portfolio_queue.sh <label> name[:optimizer flags] ... >/dev/null 2>&1 &
#
# A portfolio spec is one fixed basket, so there is no per-symbol screen or broad-basket stage:
# the base run on CONFIG["symbols"] is the whole optimization. Resumable: re-run the same command.
set -u
WT="$(cd "$(dirname "$0")/.." && pwd)"
MAIN=/home/luca/trading
TSO=$MAIN/.claude/skills/trading-strategy-optimizer/scripts
SEND=$HOME/.claude/skills/long-task-email/scripts/send_email.py
SLOTS=${SLOTS:-3}
HOURS=${HOURS:-1}
LABEL="${1:?label}"; shift
LOG=$MAIN/logs/portfolio-queue-$LABEL.log
START=$(date +%s)
log() { echo "[$(date -u +%FT%TZ)] $*" >>"$LOG"; }

container() {   # name cmd
  docker run --rm --name "$1" --user 1000:1000 -e TZ=UTC \
    -v "$WT:/app" -v "$MAIN/data:/app/data" -v "$MAIN/logs:/app/logs" \
    -v "$MAIN/config:/app/config:ro" -v "$TSO:/opt/tso:ro" -w /app \
    trading-pipeline:latest sh -c "$2" >>"$MAIN/logs/$1.console.log" 2>&1
}
export -f container
export WT MAIN TSO

in_slot() {     # run "$@" while holding a free slot lock; wait until one is free
  while :; do
    for s in $(seq 1 "$SLOTS"); do
      flock -n -E 75 "$MAIN/logs/tso-slot-$s.lock" "$@"
      rc=$?
      [ $rc -ne 75 ] && return $rc
    done
    sleep 20
  done
}

one() {         # item -> result line in $RES
  item=$1; n=${item%%:*}; F=""; [ "$item" != "$n" ] && F=${item#*:}
  log "$n: waiting for a slot"
  in_slot bash -c "container tso-$n 'python /opt/tso/optimize.py strategies/$n --hours $HOURS $F'"
  rc=$?
  if [ $rc -eq 0 ]; then log "$n: done"; echo "ok $n" >>"$RES"; else log "$n: FAILED rc=$rc (logs/tso-$n.console.log)"; echo "fail $n" >>"$RES"; fi
}

RES=$(mktemp "$MAIN/logs/.portfolio-queue-$LABEL.XXXX")
log "queue $LABEL start: $SLOTS slots, $HOURS h per strategy: $*"
for item in "$@"; do
  one "$item" &
  sleep 3        # stagger lock attempts
done
wait

in_slot bash -c "container tso-leaderboard-$LABEL 'python /opt/tso/leaderboard.py strategies'"
log "queue $LABEL end (leaderboard rc=$?)"

DONE=$(awk '$1=="ok"{printf " %s",$2}' "$RES"); FAILED=$(awk '$1=="fail"{printf " %s",$2}' "$RES"); rm -f "$RES"
SECS=$(( $(date +%s) - START ))
STATE=Done; [ -n "$FAILED" ] && STATE="Needs you"
BODY="Portfolio queue $LABEL in $WT
Done:$DONE
Failed:${FAILED:- none}
Duration: $((SECS/3600))h $((SECS%3600/60))min
Leaderboard: $WT/strategies/LEADERBOARD.md

Last log lines:
$(tail -n 25 "$LOG")

Next step: ask Claude to report on portfolio queue $LABEL (analyst notes, leaderboard, merge the branch)."
python3 "$SEND" --subject "[Claude] $STATE: portfolio queue $LABEL ($((SECS/3600))h $((SECS%3600/60))min)" --body "$BODY" >>"$LOG" 2>&1 || log "email failed"
