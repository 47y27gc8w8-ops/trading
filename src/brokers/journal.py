#!/usr/bin/env python3
"""Decision journal of the paper bots: structured records for improving them later.

Every bot writes JSON records into the `journal` table of data/brokers/brokers.db (one row per
event, never updated). Kinds and their main fields:

  start            bot started: strategy, params, symbols, code hashes (strategy + broker code)
  snapshot         at start and whenever a bar completes: last closed bar per symbol (OHLCV), the
                   strategy's buy/sell flags on it, simulated open positions, the bot's holdings,
                   equity, cash, USDCHF
  target_seen      the simulation's positions differ from the bot's (first sighting)
  target_confirmed the change was still there one cycle later and gets traded
  target_dropped   the change vanished before confirmation (data blip / flicker)
  fill             a paper fill: side, qty, reference/fill price, the simulation's own price for the same
                   entry/exit, shortfall in bps against it (positive = worse than the backtest would
                   have filled) and seconds since the simulated bar opened
  sim_trade        a trade of the strategy's own simulation closed (shadow record: what the backtest
                   logic did on live data, to compare with the bot's real fills)
  retry            a data source failed and is retried (source, error, attempt, wait)
  error            a cycle failed (type, message, traceback)
  market           ETF bots: NYSE opened / closed
  stats            hourly: cycles ok / failed / idle, data and simulation time (avg / max ms)
  watchdog         the heartbeat watchdog restarted a hung bot

CLI (standard library only, runs on the host):
  python3 src/brokers/journal.py summary [--bot ID] [--since 2026-12-01]
  python3 src/brokers/journal.py export  [--bot ID] [--kind fill] [--since ...] [--format jsonl|csv] [-o FILE]
  python3 src/brokers/journal.py tail    [--bot ID] [-n 20]
SQL works too:  sqlite3 data/brokers/brokers.db "SELECT ts, json_extract(data,'$.shortfall_bps') FROM journal WHERE kind='fill'"
"""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "data" / "brokers" / "brokers.db"


def write(con: sqlite3.Connection, bot_id: str, ts: str, kind: str, data: dict) -> None:
    with con:
        con.execute("INSERT INTO journal(bot_id, ts, kind, data) VALUES (?,?,?,?)",
                    (bot_id, ts, kind, json.dumps(data, default=str, separators=(",", ":"))))


# --------------------------------------------------------------------- CLI ---
def _rows(con, bot, kind, since, limit=None, desc=False):
    sql, args = "SELECT id, bot_id, ts, kind, data FROM journal WHERE 1=1", []
    if bot:
        sql += " AND bot_id=?"; args.append(bot)
    if kind:
        sql += " AND kind=?"; args.append(kind)
    if since:
        sql += " AND ts>=?"; args.append(since)
    sql += " ORDER BY id" + (" DESC" if desc else "")
    if limit:
        sql += f" LIMIT {int(limit)}"
    return con.execute(sql, args)


def cmd_export(con, a) -> None:
    out = open(a.output, "w", newline="") if a.output else sys.stdout
    rows = _rows(con, a.bot, a.kind, a.since)
    if a.format == "jsonl":
        for r in rows:
            out.write(json.dumps({"id": r[0], "bot_id": r[1], "ts": r[2], "kind": r[3], **json.loads(r[4])}) + "\n")
    else:   # csv: one column per top-level key of the data (nested values as JSON)
        recs = [{"id": r[0], "bot_id": r[1], "ts": r[2], "kind": r[3], **json.loads(r[4])} for r in rows]
        keys = list(dict.fromkeys(k for rec in recs for k in rec))
        w = csv.DictWriter(out, fieldnames=keys)
        w.writeheader()
        for rec in recs:
            w.writerow({k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in rec.items()})
    if a.output:
        out.close()
        print(f"wrote {a.output}", file=sys.stderr)


def cmd_tail(con, a) -> None:
    for r in reversed(list(_rows(con, a.bot, a.kind, a.since, a.n, desc=True))):
        d = json.loads(r[4])
        brief = {k: v for k, v in d.items() if k not in ("bars", "signals", "sim_open", "held", "params", "symbols", "traceback")}
        print(f"{r[2]} {r[1]:24} {r[3]:16} {json.dumps(brief, default=str)[:180]}")


def cmd_summary(con, a) -> None:
    """Per bot: how live trading compares with the strategy's own simulation."""
    agg = defaultdict(lambda: defaultdict(list))
    for _id, bot, ts, kind, data in _rows(con, a.bot, None, a.since):
        d = json.loads(data)
        g = agg[bot]
        g[kind].append(d)
    if not agg:
        print("no journal records yet")
        return
    fmt = lambda xs: f"{statistics.mean(xs):+.1f}/{statistics.median(xs):+.1f}" if xs else "–"  # noqa: E731
    print(f"{'bot':24} {'fills':>5} {'shortfall bps mean/med':>22} {'delay s med':>11} {'flicker':>7} "
          f"{'retries':>7} {'errors':>6} {'sim trades':>10} {'sim win%':>8} {'sim avg%':>8} {'restarts':>8}")
    for bot in sorted(agg):
        g = agg[bot]
        fills = [f for f in g["fill"] if not f.get("adopt")]
        sb = [f["shortfall_bps"] for f in fills if f.get("shortfall_bps") is not None]
        dl = [f["delay_s"] for f in fills if f.get("delay_s") is not None]
        st = g["sim_trade"]
        win = (100 * sum(1 for t in st if t["pnl_pct"] > 0) / len(st)) if st else None
        avg = statistics.mean(t["pnl_pct"] for t in st) if st else None
        print(f"{bot:24} {len(g['fill']):>5} {fmt(sb):>22} {(f'{statistics.median(dl):.0f}' if dl else '–'):>11} "
              f"{len(g['target_dropped']):>7} {len(g['retry']):>7} {len(g['error']):>6} {len(st):>10} "
              f"{(f'{win:.0f}' if win is not None else '–'):>8} {(f'{avg:+.2f}' if avg is not None else '–'):>8} "
              f"{len(g['start']):>8}")
    print("\nshortfall: fill vs the simulation's price for the same entry/exit (+ = live filled worse); "
          "delay: seconds from the simulated fill bar's open to the paper fill; flicker: target changes that "
          "vanished before confirmation; sim trades: trades the strategy's own logic closed on live data.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("summary", "export", "tail"):
        p = sub.add_parser(name)
        p.add_argument("--bot")
        p.add_argument("--since", help="UTC date or timestamp, e.g. 2026-12-01")
        if name != "summary":
            p.add_argument("--kind")
        if name == "export":
            p.add_argument("--format", choices=["jsonl", "csv"], default="jsonl")
            p.add_argument("-o", "--output")
        if name == "tail":
            p.add_argument("-n", type=int, default=20)
    a = ap.parse_args()
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True, timeout=30)
    {"summary": cmd_summary, "export": cmd_export, "tail": cmd_tail}[a.cmd](con, a)


if __name__ == "__main__":
    main()
