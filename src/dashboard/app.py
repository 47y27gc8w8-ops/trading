"""Local dashboard on :3000 — market overview, search, charts, paper portfolio, data health.

Reads the Parquet store directly with DuckDB (read-only); the only file it writes
is data/portfolio.json (the paper portfolio). /brokers reads the paper bots' SQLite store. Run: uvicorn src.dashboard.app:app --port 3000
"""
from __future__ import annotations

import glob
import json
import sqlite3
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

import duckdb
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from src.common.storage import CRYPTO_1M, DATA, ROOT, ETF_1D, ETF_1M, LOGS, QUOTES, etf_daily_path, load_config, safe_ticker

STATIC = Path(__file__).parent / "static"
PORTFOLIO = DATA / "portfolio.json"

# fallback names; the live quote feed (Yahoo longName / CoinGecko name) is the main source
NAMES = {"^GSPC": "S&P 500 Index", "CSSPX.SW": "iShares Core S&P 500 UCITS (SIX)"}
# extra search terms
ALIASES = {
    "SPY": "sp500 s&p500 smp500 s&p 500 sandp spx", "CSSPX.SW": "sp500 s&p500 smp500 s&p 500 ishares cspx six swiss",
    "^GSPC": "sp500 s&p500 smp500 s&p 500 spx index gspc", "QQQ": "nasdaq ndx tech", "^IXIC": "nasdaq composite",
    "^SSMI": "smi swiss market index", "^DJI": "dow jones", "^VIX": "volatility fear",
    "BTCUSDT": "btc xbt", "ETHUSDT": "eth ether", "SOLUSDT": "sol", "DOGEUSDT": "doge", "XRPUSDT": "ripple",
    "AVAXUSDT": "avax", "ADAUSDT": "ada", "LINKUSDT": "link", "BNBUSDT": "binance coin",
    "GOOGL": "google alphabet", "GOOG": "google alphabet", "META": "facebook", "BRK-B": "berkshire buffett",
}
TF_SECONDS = {"1m": 60, "5m": 300, "15m": 900, "1h": 3600, "4h": 14400, "1d": 86400, "1w": 604800}
TF_INTERVAL = {"1m": "1 minute", "5m": "5 minutes", "15m": "15 minutes", "1h": "1 hour", "4h": "4 hours",
               "1d": "1 day", "1w": "7 days"}

app = FastAPI(title="Trading dashboard")
app.add_middleware(GZipMiddleware, minimum_size=2000)
_cache: dict[str, tuple[float, object]] = {}
_cache_lock = threading.Lock()
_portfolio_lock = threading.Lock()


_refreshing: set[str] = set()


def cached(key: str, ttl: float, fn, stale_ok: bool = False):
    """TTL cache. stale_ok: once a value exists, an expired hit is returned at once and
    rebuilt in a background thread (for slow scans such as /api/health)."""
    with _cache_lock:
        hit = _cache.get(key)
        if hit and time.time() - hit[0] < ttl:
            return hit[1]
        if hit and stale_ok:
            if key not in _refreshing:
                _refreshing.add(key)
                threading.Thread(target=_refresh, args=(key, fn), daemon=True).start()
            return hit[1]
    val = fn()
    with _cache_lock:
        _cache[key] = (time.time(), val)
    return val


def _refresh(key: str, fn) -> None:
    try:
        val = fn()
        with _cache_lock:
            _cache[key] = (time.time(), val)
    finally:
        with _cache_lock:
            _refreshing.discard(key)


def q(sql: str, params: list | None = None) -> pd.DataFrame:
    con = duckdb.connect()
    try:
        con.execute("SET TimeZone='UTC'")
        df = con.execute(sql, params or []).df()
    finally:
        con.close()
    for c in df.columns:  # always hand back tz-aware UTC timestamps
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            df[c] = df[c].dt.tz_localize("UTC") if df[c].dt.tz is None else df[c].dt.tz_convert("UTC")
    return df


def universe() -> dict[str, str]:
    def build():
        cfg = load_config()
        out = {str(s): "crypto" for s in cfg.get("crypto", [])}
        out.update({str(t): "etf" for t in cfg.get("etf", [])})
        out.update({str(t): "stock" for t in cfg.get("stock", [])})
        return out
    return cached("universe", 60, build)


def asset_type(symbol: str) -> str:
    t = universe().get(symbol)
    if t is None:
        raise HTTPException(404, f"unknown symbol {symbol}")
    return t


def crypto_glob(symbol: str) -> str:
    return str(CRYPTO_1M / f"symbol={symbol}" / "*" / "*" / "data.parquet")


def etf_1m_glob(ticker: str) -> str:
    return str(ETF_1M / f"ticker={safe_ticker(ticker)}" / "*" / "data.parquet")


def has_files(pattern: str) -> bool:
    return bool(glob.glob(pattern))


def is_tradable(symbol: str, currency: str | None = None) -> bool:
    # indices are not tradable; the paper portfolio is in USD, so only USD/USDT-quoted assets
    return not symbol.startswith("^") and currency in (None, "USD", "USDT")


# ---------------------------------------------------------------- overview ---

_latest = {"mtime": 0.0, "data": {}}


def latest_quotes() -> dict:
    """data/quotes/latest.json from the live-quotes service (re-read when it changes)."""
    p = QUOTES / "latest.json"
    try:
        m = p.stat().st_mtime
        if m != _latest["mtime"]:
            _latest["data"], _latest["mtime"] = json.loads(p.read_text()), m
    except (OSError, ValueError):
        pass
    return _latest["data"]


def crypto_history() -> dict[str, pd.DataFrame]:
    """Hourly closes for the last 8 days of every coin, in one scan (cached 10 min)."""
    def build():
        now = datetime.now(timezone.utc)
        months = {(d.year, d.month) for d in (now, now - timedelta(days=9))}
        coins = [s for s, t in universe().items() if t == "crypto"]  # not the ~700 archive-only pairs
        files = [str(f) for s in coins for y, m in months
                 for f in CRYPTO_1M.glob(f"symbol={s}/year={y}/month={m:02d}/data.parquet")]
        if not files:
            return {}
        df = q(f"""
            SELECT regexp_extract(filename, 'symbol=([^/]+)', 1) AS symbol,
                   time_bucket(INTERVAL '1 hour', open_time) AS t, arg_max(close, open_time) AS close,
                   max(open_time) AS last
            FROM read_parquet({files!r}, filename=true, hive_partitioning=false)
            WHERE open_time >= ? GROUP BY 1, 2 ORDER BY 1, 2""", [now - timedelta(days=8)])
        return {s: g.reset_index(drop=True) for s, g in df.groupby("symbol")}
    return cached("crypto_history", 600, build)


def yahoo_history() -> dict[str, pd.DataFrame]:
    """Daily bars for the last ~100 days of every Yahoo symbol, in one scan (cached 10 min)."""
    def build():
        if not any(ETF_1D.glob("*.parquet")):
            return {}
        df = q(f"""
            SELECT regexp_extract(filename, '([^/]+)\.parquet$', 1) AS symbol, date, close, high, low, volume
            FROM read_parquet('{ETF_1D}/*.parquet', filename=true) WHERE date >= ? ORDER BY 1, 2""",
               [datetime.now(timezone.utc) - timedelta(days=100)])
        return {s: g.reset_index(drop=True) for s, g in df.groupby("symbol")}
    return cached("yahoo_history", 600, build)


def _num(x):
    return None if x is None or (isinstance(x, float) and x != x) else float(x)


def asset_summary(symbol: str, typ: str, quote: dict | None, hist: pd.DataFrame | None) -> dict:
    index = symbol.startswith("^")
    out = {"symbol": symbol, "type": typ, "name": NAMES.get(symbol, symbol), "price": None, "spark": [],
           "change_7d": None, "aliases": ALIASES.get(symbol, "")}
    if quote:
        out.update({
            "name": NAMES.get(symbol) or quote.get("name") or symbol,
            "currency": "pts" if index else quote.get("currency"),
            "price": quote.get("price"), "time": int(quote.get("time") or quote.get("fetched") or 0),
            "fetched": int(quote.get("fetched") or 0),
            "change_24h": quote.get("change_pct"), "high_24h": quote.get("day_high"), "low_24h": quote.get("day_low"),
            "volume_24h": quote.get("quote_volume"), "market_cap": quote.get("market_cap"), "rank": quote.get("rank"),
            "market_state": quote.get("market_state"), "exchange": quote.get("exchange"),
            "bid": quote.get("bid"), "ask": quote.get("ask"), "prev_close": quote.get("prev_close"),
        })
    if hist is not None:
        hist = hist.dropna(subset=["close"])  # Yahoo sometimes writes a bar with no close (e.g. ^N225): NaN breaks JSON
    if hist is not None and not hist.empty:
        last = hist.iloc[-1]
        if out["price"] is None:  # quote feed down: fall back to the stored bars
            out.update({"price": _num(last.close), "time": int(last.get("last", last.get("date")).timestamp()),
                        "currency": out.get("currency") or ("USDT" if typ == "crypto" else "pts" if index else "USD")})
            if typ != "crypto":
                out.update({"high_24h": _num(last.high), "low_24h": _num(last.low),
                            "volume_24h": _num(last.volume * last.close),
                            "change_24h": _num(last.close / hist.close.iloc[-2] - 1) if len(hist) > 1 else None})
        tcol = "t" if typ == "crypto" else "date"
        ref_t = hist[tcol].iloc[-1] - timedelta(days=7)
        past = hist[hist[tcol] <= ref_t]
        if not past.empty and out["price"]:
            out["change_7d"] = out["price"] / float(past.close.iloc[-1]) - 1
        vals = hist.close.tail(168 if typ == "crypto" else 60).to_numpy()
        if typ == "crypto":
            vals = vals[::-2][::-1]  # every 2nd hour, ending on the newest: keeps the payload small
        out["spark"] = [float(f"{v:.5g}") for v in vals]
    out["tradable"] = is_tradable(symbol, out.get("currency"))
    return out


def overview() -> list[dict]:
    def build():
        quotes = latest_quotes().get("quotes", {})
        ch, yh = crypto_history(), yahoo_history()
        out = []
        for s, typ in universe().items():
            try:
                hist = ch.get(s) if typ == "crypto" else yh.get(safe_ticker(s))
                out.append(asset_summary(s, typ, quotes.get(s), hist))
            except Exception as e:  # never break the page for one symbol
                out.append({"symbol": s, "type": typ, "name": NAMES.get(s, s), "price": None, "error": str(e)})
        # default order: crypto by CoinGecko rank, stocks by market cap, ETFs as configured
        rank = {a["symbol"]: i for i, a in enumerate(out)}
        def key(a):
            if a["type"] == "crypto":
                return (0, a.get("rank") or 10**6, rank[a["symbol"]])
            if a["type"] == "stock":
                return (2, -(a.get("market_cap") or 0), rank[a["symbol"]])
            return (1, 0, rank[a["symbol"]])
        return sorted(out, key=key)
    return cached("overview", 10, build)


def feed_status() -> dict:
    lq = latest_quotes()
    return {"generated": lq.get("generated"), "poll_seconds": lq.get("poll_seconds"), "sources": lq.get("status", {})}


@app.get("/api/overview")
def api_overview():
    return {"assets": overview(), "now": int(time.time()), "feed": feed_status()}


@app.get("/api/search")
def api_search(q_: str = Query("", alias="q"), limit: int = 10):
    needle = q_.lower().strip()
    if not needle:
        return []
    def score(a):
        sym, name, al = a["symbol"].lower(), a["name"].lower(), a.get("aliases", "").lower()
        base = sym.replace("usdt", "")
        if needle in (sym, base):
            return 0
        if sym.startswith(needle) or base.startswith(needle):
            return 1
        if name.startswith(needle):
            return 2
        if needle in name or needle in sym or needle in al.split() or needle in al:
            return 3
        return None
    hits = [(score(a), a) for a in overview()]
    hits = sorted([h for h in hits if h[0] is not None], key=lambda h: (h[0], h[1]["symbol"]))
    return [h[1] for h in hits[:limit]]


# -------------------------------------------------------------------- bars ---

@app.get("/api/bars")
def api_bars(symbol: str, tf: str = "1h", end: int | None = None, limit: int = 1500):
    if tf not in TF_SECONDS:
        raise HTTPException(400, f"tf must be one of {list(TF_SECONDS)}")
    limit = max(10, min(limit, 5000))
    typ = asset_type(symbol)
    end_ts = datetime.fromtimestamp(end, timezone.utc) if end else datetime.now(timezone.utc) + timedelta(days=1)
    interval = TF_INTERVAL[tf]

    if typ == "crypto":
        src, tcol = f"read_parquet('{crypto_glob(symbol)}', hive_partitioning=false)", "open_time"
        agg = "sum(volume)"
        if not has_files(crypto_glob(symbol)):
            return {"bars": [], "has_more": False}
    elif tf in ("1d", "1w"):
        p = etf_daily_path(symbol)
        if not p.exists():
            return {"bars": [], "has_more": False}
        src, tcol, agg = f"read_parquet('{p}')", "date", "sum(volume)"
    else:
        if not has_files(etf_1m_glob(symbol)):
            return {"bars": [], "has_more": False}
        src, tcol, agg = f"read_parquet('{etf_1m_glob(symbol)}', hive_partitioning=false)", "timestamp", "sum(volume)"

    def run(lower):
        where = f"{tcol} < ?" + (f" AND {tcol} >= ?" if lower is not None else "")
        params = [end_ts] + ([lower] if lower is not None else [])
        return q(f"""
            SELECT epoch(time_bucket(INTERVAL '{interval}', {tcol}))::BIGINT AS time,
                   arg_min(open, {tcol}) AS open, max(high) AS high, min(low) AS low,
                   arg_max(close, {tcol}) AS close, {agg} AS volume
            FROM {src} WHERE {where}
            GROUP BY 1 ORDER BY 1 DESC LIMIT {limit}""", params)

    # fast path: only scan the window that should contain `limit` bars (Parquet stats prune the rest)
    df = run(end_ts - timedelta(seconds=TF_SECONDS[tf] * limit * 1.1))
    if len(df) < limit:
        df = run(None)
    df = df.sort_values("time")
    first = q(f"SELECT min({tcol}) AS t FROM {src}").t.iloc[0]
    has_more = bool(len(df)) and bool(pd.Timestamp(first).timestamp() < float(df.time.iloc[0]))
    return {"bars": df.to_dict("records"), "has_more": has_more}


# ------------------------------------------------------------------ health ---

def health() -> dict:
    """Per-dataset coverage, gaps and freshness. One bulk query per dataset (cached 10 min)."""
    def build():
        rows, now = [], datetime.now(timezone.utc)
        uni = universe()
        coin_globs = [str(CRYPTO_1M / f"symbol={s}" / "year=*" / "month=*" / "data.parquet")
                      for s, t in uni.items() if t == "crypto" and (CRYPTO_1M / f"symbol={s}").exists()]
        if coin_globs:
            df = q(f"""
                WITH t AS (SELECT regexp_extract(filename, 'symbol=([^/]+)', 1) AS symbol, open_time,
                                  epoch(open_time) - lag(epoch(open_time)) OVER (PARTITION BY filename ORDER BY open_time) AS d
                           FROM read_parquet({coin_globs!r}, filename=true, hive_partitioning=false))
                SELECT symbol, min(open_time) AS first, max(open_time) AS last, count(*) AS rows,
                       count(*) FILTER (WHERE d > 60) AS gaps, coalesce(sum(d / 60 - 1) FILTER (WHERE d > 60), 0) AS missing
                FROM t GROUP BY 1""")
            for r in df.itertuples():
                if uni.get(r.symbol) != "crypto":
                    continue
                rows.append({"symbol": r.symbol, "dataset": "crypto 1m", "first": int(r.first.timestamp()),
                             "last": int(r.last.timestamp()), "rows": int(r.rows), "gaps": int(r.gaps),
                             "missing": int(r.missing), "lag_min": round((now - r.last).total_seconds() / 60 - 1, 1),
                             "size": sum(f.stat().st_size for f in (CRYPTO_1M / f"symbol={r.symbol}").rglob("*.parquet"))})
        yahoo = {safe_ticker(s): s for s, t in uni.items() if t != "crypto"}
        if any(ETF_1D.glob("*.parquet")):
            df = q(f"""SELECT regexp_extract(filename, '([^/]+)\.parquet$', 1) AS f, min(date) AS first, max(date) AS last,
                              count(*) AS rows FROM read_parquet('{ETF_1D}/*.parquet', filename=true) GROUP BY 1""")
            for r in df.itertuples():
                if r.f in yahoo:
                    rows.append({"symbol": yahoo[r.f], "dataset": f"{uni[yahoo[r.f]]} 1d", "first": int(r.first.timestamp()),
                                 "last": int(r.last.timestamp()), "rows": int(r.rows),
                                 "size": (ETF_1D / f"{r.f}.parquet").stat().st_size})
        if any(ETF_1M.glob("ticker=*/date=*/data.parquet")):
            df = q(f"""
                WITH t AS (SELECT regexp_extract(filename, 'ticker=([^/]+)', 1) AS f, timestamp,
                                  epoch(timestamp) - lag(epoch(timestamp)) OVER (PARTITION BY filename ORDER BY timestamp) AS d
                           FROM read_parquet('{ETF_1M}/ticker=*/date=*/data.parquet', filename=true, hive_partitioning=false))
                SELECT f, min(timestamp) AS first, max(timestamp) AS last, count(*) AS rows,
                       count(DISTINCT timestamp::DATE) AS days, count(*) FILTER (WHERE d > 60) AS gaps,
                       coalesce(sum(d / 60 - 1) FILTER (WHERE d > 60), 0) AS missing
                FROM t GROUP BY 1""")
            for r in df.itertuples():
                if r.f in yahoo:
                    rows.append({"symbol": yahoo[r.f], "dataset": f"{uni[yahoo[r.f]]} 1m", "first": int(r.first.timestamp()),
                                 "last": int(r.last.timestamp()), "rows": int(r.rows), "days": int(r.days),
                                 "gaps": int(r.gaps), "missing": int(r.missing),
                                 "size": sum(f.stat().st_size for f in (ETF_1M / f"ticker={r.f}").rglob("*.parquet"))})
        order = {s: i for i, s in enumerate(uni)}
        rows.sort(key=lambda r: (order.get(r["symbol"], 10**6), r["dataset"]))
        quotes_size = sum(f.stat().st_size for f in QUOTES.rglob("*.parquet")) if QUOTES.exists() else 0
        status_file = LOGS / "yahoo_intraday_status.json"
        status = json.loads(status_file.read_text()) if status_file.exists() else {}
        from src.common.budget import usage
        u = usage()
        archive = {
            "klines_pairs": sum(1 for _ in CRYPTO_1M.glob("symbol=*")),
            "trades_pairs": sum(1 for _ in (DATA / "crypto" / "trades").glob("symbol=*")),
            "trades_files": sum(1 for _ in (DATA / "crypto" / "trades").glob("symbol=*/*/*/*.parquet")),
            "book_days": sorted(p.name[5:] for p in (DATA / "crypto" / "book").glob("date=*")),
        }
        return {"rows": rows, "yahoo_intraday": status.get("_last_run"), "generated": int(time.time()),
                "quotes_size": quotes_size, "symbols": len(uni), "storage": u, "archive": archive}
    out = dict(cached("health", 600, build, stale_ok=True))
    out["feed"] = feed_status()  # always fresh
    return out


@app.get("/api/health")
def api_health():
    return health()


# --------------------------------------------------------------- portfolio ---

class Trade(BaseModel):
    symbol: str
    side: str = Field(pattern="^(buy|sell)$")
    qty: float = Field(gt=0)
    price: float | None = Field(default=None, gt=0)   # default: latest stored price
    fee_pct: float = Field(default=0.1, ge=0, le=5)  # % of notional
    note: str = ""


class Settings(BaseModel):
    starting_cash: float = Field(gt=0)
    reset: bool = False  # True deletes all trades


def load_portfolio() -> dict:
    if PORTFOLIO.exists():
        return json.loads(PORTFOLIO.read_text())
    return {"base_currency": "USD", "starting_cash": 10_000.0, "created": int(time.time()), "trades": []}


def save_portfolio(p: dict) -> None:
    tmp = PORTFOLIO.with_name("." + PORTFOLIO.name + ".tmp")
    tmp.write_text(json.dumps(p, indent=2))
    tmp.replace(PORTFOLIO)


def replay(p: dict) -> tuple[float, dict, float]:
    """Return (cash, positions{symbol: {qty, cost}}, realized_pnl) after all trades."""
    cash, pos, realized = p["starting_cash"], {}, 0.0
    for t in sorted(p["trades"], key=lambda t: t["time"]):
        notional, fee = t["qty"] * t["price"], t["fee"]
        ps = pos.setdefault(t["symbol"], {"qty": 0.0, "cost": 0.0, "fees": 0.0})
        ps["fees"] += fee
        if t["side"] == "buy":
            cash -= notional + fee
            ps["qty"] += t["qty"]
            ps["cost"] += notional + fee
        else:
            avg = ps["cost"] / ps["qty"] if ps["qty"] else 0
            cash += notional - fee
            realized += notional - fee - avg * t["qty"]
            ps["cost"] -= avg * t["qty"]
            ps["qty"] -= t["qty"]
    return cash, {s: v for s, v in pos.items() if v["qty"] > 1e-12}, realized


def prices() -> dict[str, dict]:
    return {a["symbol"]: a for a in overview() if a.get("price") is not None}


def daily_closes(symbol: str, since: datetime) -> pd.Series:
    if universe().get(symbol) == "crypto":
        df = q(f"""SELECT time_bucket(INTERVAL '1 day', open_time) AS d, arg_max(close, open_time) AS c
                   FROM read_parquet('{crypto_glob(symbol)}', hive_partitioning=false)
                   WHERE open_time >= ? GROUP BY 1 ORDER BY 1""", [since])
    else:
        df = pd.read_parquet(etf_daily_path(symbol), columns=["date", "close"]).rename(columns={"date": "d", "close": "c"})
        df = df[df.d >= since - timedelta(days=10)]
    return df.set_index("d").c


def equity_curve(p: dict) -> list[dict]:
    trades = sorted(p["trades"], key=lambda t: t["time"])
    if not trades:
        return []
    start = datetime.fromtimestamp(trades[0]["time"], timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    days = pd.date_range(start, datetime.now(timezone.utc), freq="1D", tz="UTC")
    closes = {s: daily_closes(s, start).reindex(days, method="ffill") for s in {t["symbol"] for t in trades}}
    out = [{"time": int((start - timedelta(days=1)).timestamp()), "value": round(p["starting_cash"], 2)}]
    for d in days:
        sub = {**p, "trades": [t for t in trades if t["time"] < (d + timedelta(days=1)).timestamp()]}
        cash, pos, _ = replay(sub)
        value = sum(v["qty"] * (closes[s].get(d) if pd.notna(closes[s].get(d)) else v["cost"] / v["qty"])
                    for s, v in pos.items())
        out.append({"time": int(d.timestamp()), "value": round(cash + value, 2)})
    # final point at live prices
    cash, pos, _ = replay(p)
    px = prices()
    out[-1]["value"] = round(cash + sum(v["qty"] * px.get(s, {}).get("price", v["cost"] / v["qty"])
                                        for s, v in pos.items()), 2)
    return out


@app.get("/api/portfolio")
def api_portfolio():
    with _portfolio_lock:
        p = load_portfolio()
    cash, pos, realized = replay(p)
    px = prices()
    positions, value = [], 0.0
    for s, v in sorted(pos.items()):
        last = px.get(s, {}).get("price")
        mv = v["qty"] * last if last is not None else None
        value += mv or 0
        avg = v["cost"] / v["qty"]
        positions.append({"symbol": s, "name": px.get(s, {}).get("name", NAMES.get(s, s)), "qty": v["qty"], "avg_cost": avg, "price": last,
                          "value": mv, "pnl": None if mv is None else mv - v["cost"],
                          "pnl_pct": None if last is None else last / avg - 1,
                          "change_24h": px.get(s, {}).get("change_24h")})
    equity = cash + value
    for ps in positions:
        ps["weight"] = (ps["value"] or 0) / equity if equity else 0
    return {
        "base_currency": p["base_currency"], "starting_cash": p["starting_cash"], "cash": cash,
        "positions_value": value, "equity": equity, "realized_pnl": realized,
        "unrealized_pnl": sum(ps["pnl"] or 0 for ps in positions),
        "total_return": equity / p["starting_cash"] - 1,
        "fees_paid": sum(t["fee"] for t in p["trades"]),
        "positions": positions,
        "trades": sorted(p["trades"], key=lambda t: t["time"], reverse=True),
        "equity_curve": equity_curve(p),
    }


@app.post("/api/portfolio/trades")
def api_trade(t: Trade):
    sym = t.symbol.strip().upper() if not t.symbol.startswith("^") else t.symbol
    asset_type(sym)
    cur = prices().get(sym, {}).get("currency")
    if not is_tradable(sym, cur):
        raise HTTPException(400, f"{sym} is an index and can't be traded — use SPY or CSSPX.SW" if sym.startswith("^")
                            else f"{sym} trades in {cur}; the paper portfolio only holds USD/USDT assets for now")
    price = t.price or prices().get(sym, {}).get("price")
    if price is None:
        raise HTTPException(400, f"no price available for {sym}")
    fee = t.qty * price * t.fee_pct / 100
    with _portfolio_lock:
        p = load_portfolio()
        cash, pos, _ = replay(p)
        if t.side == "buy" and t.qty * price + fee > cash + 1e-9:
            raise HTTPException(400, f"not enough cash: need {t.qty * price + fee:,.2f}, have {cash:,.2f}")
        if t.side == "sell" and t.qty > pos.get(sym, {}).get("qty", 0) + 1e-12:
            raise HTTPException(400, f"can't sell {t.qty} {sym}: you hold {pos.get(sym, {}).get('qty', 0)} (no shorting)")
        trade = {"id": uuid.uuid4().hex[:12], "time": int(time.time()), "symbol": sym, "side": t.side,
                 "qty": t.qty, "price": price, "fee": round(fee, 6), "note": t.note}
        p["trades"].append(trade)
        save_portfolio(p)
    return trade


@app.delete("/api/portfolio/trades/{trade_id}")
def api_delete_trade(trade_id: str):
    with _portfolio_lock:
        p = load_portfolio()
        trades = [t for t in p["trades"] if t["id"] != trade_id]
        if len(trades) == len(p["trades"]):
            raise HTTPException(404, "trade not found")
        trial = {**p, "trades": trades}
        # removing a buy that a later sell depends on would create a negative position
        running: dict[str, float] = {}
        for t in sorted(trades, key=lambda t: t["time"]):
            running[t["symbol"]] = running.get(t["symbol"], 0) + (t["qty"] if t["side"] == "buy" else -t["qty"])
            if running[t["symbol"]] < -1e-12:
                raise HTTPException(400, "deleting this trade would leave a later sell without a position")
        save_portfolio(trial)
    return {"ok": True}


@app.put("/api/portfolio/settings")
def api_settings(s: Settings):
    with _portfolio_lock:
        p = load_portfolio()
        p["starting_cash"] = s.starting_cash
        if s.reset:
            p["trades"], p["created"] = [], int(time.time())
        else:
            p_cash, _, _ = replay(p)
            if p_cash < -1e-9:
                raise HTTPException(400, "starting cash too low for the existing trades")
        save_portfolio(p)
    return {"ok": True}


# ------------------------------------------------------------- leaderboard ---
# strategies/leaderboard.json is written by the optimizer's leaderboard.py; the dashboard only reads it.

LEADERBOARD = ROOT / "strategies" / "leaderboard.json"
_lb_cache: dict = {"mtime": None, "data": None}


@app.get("/api/leaderboard")
def api_leaderboard():
    try:
        mtime = LEADERBOARD.stat().st_mtime
    except FileNotFoundError:
        raise HTTPException(404, "strategies/leaderboard.json not found (run leaderboard.py)")
    if _lb_cache["mtime"] != mtime:
        raw = json.loads(LEADERBOARD.read_text())
        kinds = universe()
        # leaderboard.py writes one entry per profile, so a parameter set that wins several profiles
        # appears several times with identical numbers. Show it once and list every profile it won.
        merged: dict = {}
        for e in raw.get("entries", []):
            key = (e.get("strategy"), e.get("tag"), json.dumps(e.get("params") or {}, sort_keys=True))
            if key in merged:
                merged[key]["_profiles"].append(e.get("profile"))
                merged[key]["_files"].append(e.get("variant_file"))
            else:
                merged[key] = {**e, "_profiles": [e.get("profile")], "_files": [e.get("variant_file")]}
        entries = []
        for i, e in enumerate(merged.values()):
            syms = [str(s) for s in e.get("symbols") or []]
            classes = sorted({kinds.get(s) or ("crypto" if s.endswith("USDT") else "other") for s in syms})
            longs = (e.get("signal_now") or {}).get("long") or []
            entries.append({
                "id": i, "strategy": e.get("strategy"), "tag": e.get("tag"), "profile": e.get("profile"), "profiles": e["_profiles"],
                "kind": e.get("kind"), "symbols": syms, "classes": classes,
                "low_confidence": bool(e.get("confidence_note")), "stale": bool(e.get("stale")),
                "params": e.get("params") or {}, "variant_file": e.get("variant_file"), "variant_files": e["_files"],
                **{k: e.get(k) for k in (
                    "is_yearly_pct", "oos_yearly_pct", "conservative_yearly_pct", "worst_max_dd_pct",
                    "position_pct_for_10pct_dd", "is_win_rate", "oos_win_rate", "is_trades", "oos_trades",
                    "oos_efficiency", "largest_loss_pct", "robust_frac", "oos_period")},
                "signal": {"long": [{"symbol": x.get("symbol"), "since": (x.get("since") or "")[:10]} for x in longs],
                           "data_until": ((e.get("signal_now") or {}).get("data_until") or "")[:10]},
            })
        _lb_cache.update(mtime=mtime, data={
            "generated": raw.get("generated"), "ranking": raw.get("ranking"), "note": raw.get("note"),
            "best": raw.get("best", {}), "entries": entries})
    return _lb_cache["data"]


# ----------------------------------------------------------------- brokers ---
# Paper-trading bots (src/brokers) write data/brokers/brokers.db; this side only reads it.

BROKERS_DB = DATA / "brokers" / "brokers.db"
BROKER_STALE_S = 300   # no heartbeat for 5 minutes = the bot is down


def _bdb() -> sqlite3.Connection:
    if not BROKERS_DB.exists():
        raise HTTPException(404, "no broker database yet (data/brokers/brokers.db): start the bots")
    con = sqlite3.connect(f"file:{BROKERS_DB}?mode=ro", uri=True, timeout=10)
    con.row_factory = sqlite3.Row
    return con


@app.get("/api/brokers")
def api_brokers():
    con = _bdb()
    try:
        now = datetime.now(timezone.utc)
        day_ago = (now - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
        bots = []
        for b in con.execute("SELECT b.*, s.cash, s.status, s.message, s.fx_usdchf, s.heartbeat, s.started_at, s.max_dd"
                             " FROM bots b LEFT JOIN state s ON s.bot_id = b.id ORDER BY b.rowid"):
            bid, start = b["id"], b["start_balance"]
            last = con.execute("SELECT equity FROM equity WHERE bot_id=? ORDER BY ts DESC LIMIT 1", (bid,)).fetchone()
            prev = con.execute("SELECT equity FROM equity WHERE bot_id=? AND ts<=? ORDER BY ts DESC LIMIT 1", (bid, day_ago)).fetchone()
            eq = last["equity"] if last else start
            prev_eq = prev["equity"] if prev else start
            mdd = b["max_dd"] or 0.0   # maintained by the bot on every equity row
            lt = con.execute("SELECT ts, symbol, side, notional, pnl, reason FROM trades WHERE bot_id=? ORDER BY id DESC LIMIT 1",
                             (bid,)).fetchone()
            fx = b["fx_usdchf"] or 0
            pos = [{"symbol": p["symbol"], "qty": p["qty"], "value": p["qty"] * (p["last_price_usd"] or p["avg_price_usd"]) * fx,
                    "pnl": p["qty"] * (p["last_price_usd"] or p["avg_price_usd"]) * fx - p["cost"], "since": p["opened_at"]}
                   for p in con.execute("SELECT * FROM positions WHERE bot_id=? ORDER BY symbol", (bid,))]
            hb_age = (now - datetime.strptime(b["heartbeat"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)).total_seconds() \
                if b["heartbeat"] else None
            status = b["status"] or "never ran"
            if hb_age is not None and hb_age > BROKER_STALE_S and status != "stopped":
                status = "down"
            bots.append({
                "id": bid, "strategy": b["strategy"], "profile": b["profile"], "asset_class": b["asset_class"],
                "timeframe": b["timeframe"], "symbols": json.loads(b["symbols"] or "[]"), "params": json.loads(b["params"] or "{}"),
                "backtest": json.loads(b["backtest"] or "{}"), "start_balance": start,
                "status": status, "message": b["message"], "heartbeat": b["heartbeat"], "heartbeat_age_s": hb_age,
                "started_at": b["started_at"], "equity": eq, "cash": b["cash"], "fx_usdchf": b["fx_usdchf"],
                "pnl_day": eq - prev_eq, "pnl_day_pct": (eq / prev_eq - 1) * 100 if prev_eq else 0.0,
                "pnl_total": eq - start, "pnl_total_pct": (eq / start - 1) * 100,
                "max_dd_pct": mdd * 100, "positions": pos,
                "trades": con.execute("SELECT count(*) FROM trades WHERE bot_id=?", (bid,)).fetchone()[0],
                "errors_24h": con.execute("SELECT count(*) FROM events WHERE bot_id=? AND level='error' AND ts>?",
                                          (bid, day_ago)).fetchone()[0],
                "last_trade": dict(lt) if lt else None,
            })
        return {"generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "bots": bots}
    finally:
        con.close()


@app.get("/api/brokers/equity")
def api_brokers_equity(range_: str = Query("all", alias="range", pattern="^(1d|1w|1m|all)$"), points: int = 400):
    """Every bot's equity curve, downsampled to about `points` buckets (last value per bucket), cached 60 s."""
    return cached(f"brokers-equity-{range_}-{points}", 60, lambda: _brokers_equity(range_, points))


def _brokers_equity(range_: str, points: int):
    con = _bdb()
    try:
        since = {"1d": timedelta(days=1), "1w": timedelta(weeks=1), "1m": timedelta(days=31)}.get(range_)
        lo = (datetime.now(timezone.utc) - since).strftime("%Y-%m-%dT%H:%M:%SZ") if since else "0"
        out = {}
        for (bid,) in con.execute("SELECT id FROM bots ORDER BY rowid"):
            first = con.execute("SELECT min(ts), max(ts) FROM equity WHERE bot_id=? AND ts>=?", (bid, lo)).fetchone()
            if not first[0]:
                out[bid] = []
                continue
            t0 = datetime.strptime(first[0], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
            t1 = datetime.strptime(first[1], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
            bucket = max(60, int((t1 - t0) / max(10, min(points, 2000))) + 1)
            rows = con.execute(
                "SELECT CAST(strftime('%s', ts) AS INTEGER) / ? AS b, max(ts) AS ts, equity FROM equity"
                " WHERE bot_id=? AND ts>=? GROUP BY b ORDER BY b", (bucket, bid, lo)).fetchall()
            out[bid] = [[int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()),
                         round(r["equity"], 2)] for r in rows]
        return {"range": range_, "curves": out}
    finally:
        con.close()


@app.get("/api/brokers/trades")
def api_brokers_trades(bot: str | None = None, limit: int = Query(50, le=500)):
    con = _bdb()
    try:
        sql = "SELECT * FROM trades" + (" WHERE bot_id=?" if bot else "") + " ORDER BY id DESC LIMIT ?"
        return {"trades": [dict(r) for r in con.execute(sql, ((bot,) if bot else ()) + (limit,))]}
    finally:
        con.close()


try:
    import psutil
    psutil.cpu_percent(interval=None)   # prime: the first call has no reference point
except ImportError:  # image built before psutil was added to requirements.txt
    psutil = None


@app.get("/api/system")
def api_system():
    """Host CPU, RAM and disk. /proc is not namespaced for these, so the container sees the host;
    disk is the volume holding data/ (the root LV)."""
    if psutil is None:
        raise HTTPException(503, "psutil missing: rebuild the image (docker compose build dashboard)")
    vm, sw = psutil.virtual_memory(), psutil.swap_memory()
    du = psutil.disk_usage(str(DATA))
    temps = {}
    try:
        for name, entries in (psutil.sensors_temperatures() or {}).items():
            for t in entries:
                if t.current:
                    temps[name] = max(temps.get(name, 0), t.current)
    except Exception:  # noqa: BLE001 - sensors are optional
        pass
    return {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cpu_pct": psutil.cpu_percent(interval=None), "cpu_count": psutil.cpu_count(),
        "per_cpu": psutil.cpu_percent(interval=None, percpu=True), "load": list(psutil.getloadavg()),
        "mem_total": vm.total, "mem_used": vm.total - vm.available, "mem_pct": vm.percent,
        "swap_total": sw.total, "swap_used": sw.used,
        "disk_total": du.total, "disk_used": du.used, "disk_pct": du.percent,
        "uptime_s": time.time() - psutil.boot_time(), "temp_c": max(temps.values()) if temps else None,
    }


# ------------------------------------------------------------------ static ---

app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.on_event("startup")
def _warm() -> None:  # build the slow health scan in the background right after start
    threading.Thread(target=lambda: api_health(), daemon=True).start()


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/leaderboard")
def leaderboard_page():
    return FileResponse(STATIC / "leaderboard.html")


@app.get("/brokers")
def brokers_page():
    return FileResponse(STATIC / "brokers.html")
