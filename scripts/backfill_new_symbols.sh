#!/usr/bin/env bash
# One-off / after editing config/symbols.yaml: backfill history for every configured symbol.
# Already-ingested data is skipped, so re-running is cheap. Logs to logs/backfill.log.
#   - Binance 1m archive (data.binance.vision) for all coins, in parallel with
#   - Yahoo daily full history, then Yahoo 1m (~30 days, Yahoo's limit) for every ETF/index/stock.
cd "$(dirname "$0")/.." || exit 1
exec >> logs/backfill.log 2>&1
echo "=== $(date -u +%FT%TZ) backfill start ==="
/usr/bin/docker compose run --rm binance-history & bpid=$!
/usr/bin/docker compose run --rm yahoo-daily;     echo "yahoo-daily exit $?"
/usr/bin/docker compose run --rm yahoo-intraday;  echo "yahoo-intraday exit $?"
wait $bpid;                                        echo "binance-history exit $?"
echo "=== $(date -u +%FT%TZ) backfill done ==="
