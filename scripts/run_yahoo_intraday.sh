#!/usr/bin/env bash
# Daily ETF 1m collector (called by cron at 22:30 UTC). Logs to logs/cron.log.
cd "$(dirname "$0")/.." || exit 1
echo "=== $(date -u +%FT%TZ) yahoo-intraday ==="
/usr/bin/docker compose run --rm yahoo-intraday
echo "=== exit $? ==="
