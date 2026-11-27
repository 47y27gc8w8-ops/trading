#!/usr/bin/env bash
# After portfolio queue "pairs8" ends: borrow-cost stress test of every saved pair variant (notes in each optimization.log).
set -u
WT="$(cd "$(dirname "$0")/.." && pwd)"
MAIN=/home/luca/trading
TSO=$MAIN/.claude/skills/trading-strategy-optimizer/scripts
until grep -q "queue pairs8 end" "$MAIN/logs/portfolio-queue-pairs8.log" 2>/dev/null; do sleep 60; done
docker run --rm --user 1000:1000 -e TZ=UTC -v "$WT:/app" -v "$MAIN/data:/app/data" -v "$MAIN/logs:/app/logs" \
  -v "$MAIN/config:/app/config:ro" -v "$TSO:/opt/tso:ro" -w /app trading-pipeline:latest \
  python scripts/portfolio_lib/pair_stress.py >>"$MAIN/logs/pairs8-stress.log" 2>&1
echo "[$(date -u +%FT%TZ)] stress done rc=$?" >>"$MAIN/logs/pairs8-stress.log"
