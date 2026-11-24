#!/usr/bin/env bash
# Waits until fewer than 3 tso-* optimizer containers run (8 cores shared with the live
# collectors), then starts the unattended first run of bollinger_squeeze_release and the
# email watcher. Run from the worktree root:
#   setsid nohup bash strategies/bollinger_squeeze_release/queue_run.sh >logs/tso-bollinger_squeeze_release-queue.log 2>&1 &
set -u
TSO=/home/luca/trading/.claude/skills/trading-strategy-optimizer/scripts
S=strategies/bollinger_squeeze_release
NAME=tso-bollinger_squeeze_release

while [ "$(docker ps --filter name=tso- -q | wc -l)" -ge 3 ]; do
  sleep 120
done
echo "$(date -u +%FT%TZ) slot free, starting $NAME"

docker compose run -d --rm --name "$NAME" -v "$TSO:/opt/tso:ro" backtest sh -c "
  python /opt/tso/optimize.py $S --hours 6 &&
  python /opt/tso/screen.py $S --universe crypto --samples 60 --workers 2 &&
  OK=\$(python -c \"import csv;print(','.join(r['symbol'] for r in csv.DictReader(open('$S/screen.csv')) if r['status']=='ok'))\") &&
  python /opt/tso/optimize.py $S --symbols \$OK --tag broad --hours 14 &&
  python /opt/tso/leaderboard.py strategies"
setsid nohup bash "$TSO/notify_when_done.sh" "$NAME" "$S" "Base + screen + broad basket" >/dev/null 2>&1 &
echo "$(date -u +%FT%TZ) started container and watcher"
