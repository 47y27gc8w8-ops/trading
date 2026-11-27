"""SQLite store shared by the bots (writers), the daily report and the dashboard (readers).

Standard library only, so the report can run on the host without the Docker image.
One file, WAL mode: each bot writes its own rows, readers never block writers.
All timestamps are UTC ISO-8601 strings ("2026-11-27T22:05:00Z"), money is CHF unless the
column name says _usd.
"""
from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get("APP_ROOT", Path(__file__).resolve().parents[2]))
DB_PATH = ROOT / "data" / "brokers" / "brokers.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS bots (
    id TEXT PRIMARY KEY,
    strategy TEXT NOT NULL,
    profile TEXT,
    asset_class TEXT,          -- crypto | etf
    timeframe TEXT,
    symbols TEXT,              -- JSON list
    params TEXT,               -- JSON object
    variant_file TEXT,
    backtest TEXT,             -- JSON: conservative_yearly_pct, worst_max_dd_pct
    start_balance REAL NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS state (
    bot_id TEXT PRIMARY KEY REFERENCES bots(id),
    cash REAL NOT NULL,
    status TEXT,               -- starting | running | idle | error
    message TEXT,
    fx_usdchf REAL,
    heartbeat TEXT,
    started_at TEXT,           -- this process's start (restarts reset it)
    peak REAL,                 -- highest equity ever recorded
    max_dd REAL                -- deepest drop from that peak, as a fraction (-0.12 = -12 %)
);
CREATE TABLE IF NOT EXISTS positions (
    bot_id TEXT NOT NULL,
    symbol TEXT NOT NULL,
    qty REAL NOT NULL,
    avg_price_usd REAL NOT NULL,
    cost REAL NOT NULL,        -- CHF paid incl. fees, reduced pro rata on partial sells
    sim_entry TEXT,            -- entry time of the strategy's simulated trade this position mirrors
    opened_at TEXT NOT NULL,
    last_price_usd REAL,
    PRIMARY KEY (bot_id, symbol)
);
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_id TEXT NOT NULL,
    ts TEXT NOT NULL,
    symbol TEXT NOT NULL,
    side TEXT NOT NULL,        -- buy | sell
    qty REAL NOT NULL,
    price_usd REAL NOT NULL,   -- fill price incl. slippage
    ref_price_usd REAL NOT NULL,
    fx_usdchf REAL NOT NULL,
    notional REAL NOT NULL,    -- CHF, before fee
    fee REAL NOT NULL,         -- CHF
    pnl REAL,                  -- CHF realised on sells
    reason TEXT
);
CREATE INDEX IF NOT EXISTS trades_bot_ts ON trades(bot_id, ts);
CREATE TABLE IF NOT EXISTS equity (
    bot_id TEXT NOT NULL,
    ts TEXT NOT NULL,
    equity REAL NOT NULL,
    cash REAL NOT NULL,
    PRIMARY KEY (bot_id, ts)
) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_id TEXT NOT NULL,
    ts TEXT NOT NULL,
    level TEXT NOT NULL,       -- info | warning | error
    kind TEXT NOT NULL,        -- start | stop | trade | data | error
    message TEXT
);
CREATE INDEX IF NOT EXISTS events_bot_ts ON events(bot_id, ts);
CREATE TABLE IF NOT EXISTS journal (    -- structured decision log, see src/brokers/journal.py
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_id TEXT NOT NULL,
    ts TEXT NOT NULL,
    kind TEXT NOT NULL,
    data TEXT NOT NULL         -- JSON
);
CREATE INDEX IF NOT EXISTS journal_bot_ts ON journal(bot_id, ts);
CREATE INDEX IF NOT EXISTS journal_kind_ts ON journal(kind, ts);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def migrate(con: sqlite3.Connection) -> None:
    """Add columns introduced after a database was created (CREATE TABLE IF NOT EXISTS won't)."""
    cols = {r[1] for r in con.execute("PRAGMA table_info(state)")}
    with con:
        for name in ("peak", "max_dd"):
            if name not in cols:
                con.execute(f"ALTER TABLE state ADD COLUMN {name} REAL")
        if not {"peak", "max_dd"} <= cols:   # backfill from the equity history once
            for (bid,) in con.execute("SELECT bot_id FROM state").fetchall():
                peak, mdd = None, 0.0
                for (v,) in con.execute("SELECT equity FROM equity WHERE bot_id=? ORDER BY ts", (bid,)):
                    peak = v if peak is None or v > peak else peak
                    mdd = min(mdd, v / peak - 1)
                con.execute("UPDATE state SET peak=?, max_dd=? WHERE bot_id=?", (peak, mdd, bid))


def connect(path: Path = DB_PATH, readonly: bool = False) -> sqlite3.Connection:
    if readonly:
        con = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=30)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        con = sqlite3.connect(path, timeout=30)
        con.execute("PRAGMA journal_mode=WAL")
        con.execute("PRAGMA synchronous=NORMAL")
        con.executescript(SCHEMA)
        migrate(con)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA busy_timeout=30000")
    return con
