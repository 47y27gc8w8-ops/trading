#!/usr/bin/env bash
# Yahoo 1m bars for every ETF/index/stock. Called by cron:
#   hourly on weekdays:  run_yahoo_intraday.sh --period 1d   (today's bars, fresh charts)
#   nightly 22:30 UTC:   via run_nightly.sh with the default 7d window (fills any missed day)
# flock: never runs twice at once (skips if the previous run is still busy). Logs to logs/cron.log.
cd "$(dirname "$0")/.." || exit 1
exec 9>logs/.yahoo_intraday.lock
flock -n 9 || { echo "=== $(date -u +%FT%TZ) yahoo-intraday skipped: previous run still busy ==="; exit 0; }
echo "=== $(date -u +%FT%TZ) yahoo-intraday $* ==="
/usr/bin/docker compose run --rm -T yahoo-intraday python -m src.collectors.yahoo_intraday "$@"
echo "=== exit $? ==="
