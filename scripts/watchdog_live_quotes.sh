#!/usr/bin/env bash
# Cron, every minute: the live-quotes service must have rewritten data/quotes/latest.json
# within the last 120 s (it polls every 30 s). If not, restart it (or start it if it is down).
cd "$(dirname "$0")/.." || exit 1
f=data/quotes/latest.json
age=$(( $(date +%s) - $(stat -c %Y "$f" 2>/dev/null || echo 0) ))
if [ "$age" -gt 120 ]; then
  echo "$(date -u +%FT%TZ) live-quotes stale (${age}s) -> restarting"
  /usr/bin/docker compose up -d live-quotes && /usr/bin/docker compose restart live-quotes
fi
