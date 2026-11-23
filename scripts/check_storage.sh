#!/usr/bin/env bash
# Daily (cron): storage budget check for ./data (config storage.budget_gb = 750 GB).
# Prunes the rolling book-tick window, then emails admin@luca-greutert.ch at >= 80 % (warning)
# or >= 95 % (critical: backfills stop themselves at that level).
cd "$(dirname "$0")/.." || exit 1
out=$(/usr/bin/docker compose run --rm -T storage python -m src.tools.storage prune 2>/dev/null)
/usr/bin/docker compose run --rm -T storage python -m src.tools.storage check >/dev/null 2>&1; level=$?
echo "$(date -u +%FT%TZ) level=$level"; echo "$out"
if [ "$level" -ge 1 ]; then
  EMAIL="admin@luca-greutert.ch"
  { echo "From: Trading Homelab <$EMAIL>"; echo "To: $EMAIL"
    echo "Subject: Trading homelab storage $([ "$level" -ge 2 ] && echo CRITICAL || echo warning)"
    echo; echo "$out"
    [ "$level" -ge 2 ] && { echo; echo "At >= 95 % the archive backfills stop by themselves."; }
  } | msmtp "$EMAIL"
fi
