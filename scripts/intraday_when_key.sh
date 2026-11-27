#!/usr/bin/env bash
# Wait (up to 7 days) for ALPACA_KEY_ID / ALPACA_SECRET_KEY in /home/luca/trading/.env, then download
# 5-minute history for the six symbols and queue the 11 US 5-minute library specs.
#
#   setsid nohup bash scripts/intraday_when_key.sh >/dev/null 2>&1 &
set -u
WT="$(cd "$(dirname "$0")/.." && pwd)"
MAIN=/home/luca/trading
ENV=$MAIN/.env
LOG=$MAIN/logs/intraday-when-key.log
SEND=$HOME/.claude/skills/long-task-email/scripts/send_email.py
log() { echo "[$(date -u +%FT%TZ)] $*" >>"$LOG"; }
has_key() { [ -f "$ENV" ] && grep -q '^ALPACA_KEY_ID=..' "$ENV" && grep -q '^ALPACA_SECRET_KEY=..' "$ENV"; }

log "waiting for Alpaca key in $ENV"
for _ in $(seq 1 10080); do has_key && break; sleep 60; done
if ! has_key; then log "no key after 7 days, giving up"; exit 1; fi
log "key found, downloading 5-minute bars"
docker run --rm --user 1000:1000 --env-file "$ENV" -v "$MAIN/data:/app/data" -v "$WT/scripts:/opt/s:ro" -w /app \
  trading-pipeline:latest python /opt/s/fetch_alpaca_5m.py SPY QQQ IWM AAPL MSFT NVDA >>"$LOG" 2>&1
rc=$?
missing=""
for s in SPY QQQ IWM AAPL MSFT NVDA; do [ -f "$MAIN/data/etf/5m/$s.parquet" ] || missing="$missing $s"; done
if [ $rc -ne 0 ] || [ -n "$missing" ]; then
  log "download failed rc=$rc missing:${missing:- none}"
  python3 "$SEND" --subject "[Claude] Needs you: Alpaca 5-minute download failed" \
    --body "The Alpaca download for the US 5-minute strategies failed (rc=$rc, missing:${missing:- none}).
Check the key in $ENV (ALPACA_KEY_ID / ALPACA_SECRET_KEY) and the log:

$(tail -n 20 "$LOG")" >>"$LOG" 2>&1
  exit 1
fi
log "download ok, queueing the 11 intraday specs"
cd "$WT" && SLOTS=6 HOURS=1 bash scripts/portfolio_queue.sh intraday11 \
  opening_range_breakout session_vwap_deviation_reversion session_vwap_reclaim previous_day_high_intraday_break \
  session_vwap_trend_pullback opening_range_failed_breakdown afternoon_momentum_continuation intraday_lunch_compression_break \
  full_gap_up_continuation gap_down_reversal_strength partial_gap_down_fill
log "intraday queue finished"
