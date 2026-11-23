#!/usr/bin/env bash
# Big one-off archive backfill (resumable: re-run to continue, finished files are skipped):
#   - every trade of the top-N coins (config history.trades_*)        ~150-200 GB
#   - 1m klines of every USDT pair incl. delisted (history.klines_all_usdt)  ~60 GB
# Both stop by themselves at 95 % of the storage budget. Logs to logs/backfill_archive.log.
cd "$(dirname "$0")/.." || exit 1
exec >> logs/backfill_archive.log 2>&1
exec 9>logs/.backfill_archive.lock
flock -n 9 || { echo "$(date -u +%FT%TZ) already running"; exit 0; }
echo "=== $(date -u +%FT%TZ) archive backfill start ==="
/usr/bin/docker compose run --rm -T binance-trades & tpid=$!
# let a still-running backfill_new_symbols.sh finish its Binance part first (same files)
while pgrep -f backfill_new_symbols.sh >/dev/null; do sleep 60; done
/usr/bin/docker compose run --rm -T binance-history; echo "binance-history (all USDT) exit $?"
wait $tpid; echo "binance-trades exit $?"
echo "=== $(date -u +%FT%TZ) archive backfill done ==="
