#!/usr/bin/env bash
# Nightly after the US close (cron 22:30 UTC): Yahoo 1m (7 day window), Yahoo daily history,
# the Binance archive (1m klines for all USDT pairs + fills any gap the websocket missed) and
# yesterday's trades for the top coins. Logs to logs/cron.log.
cd "$(dirname "$0")/.." || exit 1
"$(dirname "$0")/run_yahoo_intraday.sh"
echo "=== $(date -u +%FT%TZ) yahoo-daily ==="
/usr/bin/docker compose run --rm -T yahoo-daily;     echo "=== exit $? ==="
echo "=== $(date -u +%FT%TZ) binance-history ==="
/usr/bin/docker compose run --rm -T binance-history; echo "=== exit $? ==="
echo "=== $(date -u +%FT%TZ) binance-trades ==="
/usr/bin/docker compose run --rm -T binance-trades; echo "=== exit $? ==="
