"""Local dashboard on :3000 — market overview, search, charts, paper portfolio, data health.

Reads the Parquet store directly with DuckDB (read-only); the only file it writes
is data/portfolio.json (the paper portfolio). Run: uvicorn src.dashboard.app:app --port 3000
"""
from __future__ import annotations

import glob
import json
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

import duckdb
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from src.common.storage import CRYPTO_1M, DATA, ETF_1M, LOGS, etf_daily_path, load_config, safe_ticker

STATIC = Path(__file__).parent / "static"
PORTFOLIO = DATA / "portfolio.json"

NAMES = {
    "BTCUSDT": "Bitcoin", "ETHUSDT": "Ethereum", "BNBUSDT": "BNB", "XRPUSDT": "XRP", "SOLUSDT": "Solana",
    "TRXUSDT": "TRON", "HYPEUSDT": "Hyperliquid", "ZECUSDT": "Zcash", "DOGEUSDT": "Dogecoin",
    "LINKUSDT": "Chainlink", "ADAUSDT": "Cardano", "XLMUSDT": "Stellar", "BCHUSDT": "Bitcoin Cash",
    "NEARUSDT": "NEAR Protocol", "LTCUSDT": "Litecoin", "AVAXUSDT": "Avalanche",
    "SPY": "SPDR S&P 500 ETF", "CSSPX.SW": "iShares Core S&P 500 UCITS (SIX)", "^GSPC": "S&P 500 Index",
    "QQQ": "Invesco Nasdaq-100 ETF", "VOO": "Vanguard S&P 500 ETF", "IVV": "iShares Core S&P 500 ETF",
}
# extra search terms
ALIASES = {
    "SPY": "sp500 s&p500 smp500 s&p 500 sandp spx", "CSSPX.SW": "sp500 s&p500 smp500 s&p 500 ishares cspx six swiss",
    "^GSPC": "sp500 s&p500 smp500 s&p 500 spx index gspc", "QQQ": "nasdaq ndx tech",
    "BTCUSDT": "btc xbt", "ETHUSDT": "eth ether", "SOLUSDT": "sol", "DOGEUSDT": "doge", "XRPUSDT": "ripple",
    "AVAXUSDT": "avax", "ADAUSDT": "ada", "LINKUSDT": "link", "BNBUSDT": "binance coin",
}
TF_SECONDS = {"1m": 60, "5m": 300, "15m": 900, "1h": 3600, "4h": 14400, "1d": 86400, "1w": 604800}
TF_INTERVAL = {"1m": "1 minute", "5m": "5 minutes", "15m": "15 minutes", "1h": "1 hour", "4h": "4 hours",
               "1d": "1 day", "1w": "7 days"}

app = FastAPI(title="Trading dashboard")
_cache: dict[str, tuple[float, object]] = {}
_cache_lock = threading.Lock()
_portfolio_lock = threading.Lock()


def cached(key: str, ttl: float, fn):
    with _cache_lock:
        hit = _cache.get(key)
        if hit and time.time() - hit[0] < ttl:
            return hit[1]
    val = fn()
    with _cache_lock:
        _cache[key] = (time.time(), val)
    return val


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
    cfg = load_config()
    out = {s: "crypto" for s in cfg.get("crypto", [])}
    out.update({t: "etf" for t in cfg.get("etf", [])})
    return out


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


def is_tradable(symbol: str) -> bool:
    return not symbol.startswith("^")  # indices are not tradable


# ---------------------------------------------------------------- overview ---

def crypto_summary(symbol: str) -> dict:
    g = crypto_glob(symbol)
    if not has_files(g):
        return {"symbol": symbol, "type": "crypto", "name": NAMES.get(symbol, symbol), "price": None}
    since = datetime.now(timezone.utc) - timedelta(days=8)
    df = q(f"""
        SELECT open_time, close, high, low, quote_volume FROM read_parquet('{g}', hive_partitioning=false)
        WHERE open_time >= ? ORDER BY open_time""", [since])
    if df.empty:
        df = q(f"SELECT open_time, close, high, low, quote_volume FROM read_parquet('{g}', hive_partitioning=false) "
               "ORDER BY open_time DESC LIMIT 1")
    last = df.iloc[-1]
    t_last = last.open_time

    def change(delta):
        past = df[df.open_time <= t_last - delta]
        return None if past.empty else float(last.close / past.iloc[-1].close - 1)

    d24 = df[df.open_time > t_last - timedelta(hours=24)]
    spark = df.set_index("open_time").close.resample("1h").last().dropna().tail(168)
    return {
        "symbol": symbol, "type": "crypto", "name": NAMES.get(symbol, symbol), "currency": "USDT",
        "price": float(last.close), "time": int(t_last.timestamp()) + 60,
        "change_24h": change(timedelta(hours=24)), "change_7d": change(timedelta(days=7)),
        "high_24h": float(d24.high.max()), "low_24h": float(d24.low.min()),
        "volume_24h": float(d24.quote_volume.sum()),
        "spark": [round(float(x), 8) for x in spark.values],
        "tradable": True,
    }


def etf_summary(ticker: str) -> dict:
    p = etf_daily_path(ticker)
    base = {"symbol": ticker, "type": "etf", "name": NAMES.get(ticker, ticker), "tradable": is_tradable(ticker)}
    if not p.exists():
        return {**base, "price": None}
    d = pd.read_parquet(p).sort_values("date")
    price, t = float(d.close.iloc[-1]), int(d.date.iloc[-1].timestamp())
    # newer intraday bar (e.g. during the trading day) wins
    g = etf_1m_glob(ticker)
    if has_files(g):
        m = q(f"SELECT timestamp, close FROM read_parquet('{g}', hive_partitioning=false) ORDER BY timestamp DESC LIMIT 1")
        if not m.empty and m.timestamp.iloc[0] > d.date.iloc[-1] + timedelta(days=1):
            price, t = float(m.close.iloc[0]), int(m.timestamp.iloc[0].timestamp()) + 60

    def change(n):
        return None if len(d) <= n else float(price / d.close.iloc[-1 - n] - 1)

    last_day = d.date.iloc[-1]
    return {
        **base, "currency": "USD" if not ticker.startswith("^") else "pts",
        "price": price, "time": t,
        "change_24h": change(1) if price == float(d.close.iloc[-1]) else float(price / d.close.iloc[-1] - 1),
        "change_7d": float(price / d[d.date <= last_day - timedelta(days=7)].close.iloc[-1] - 1) if len(d) > 7 else None,
        "high_24h": float(d.high.iloc[-1]), "low_24h": float(d.low.iloc[-1]),
        "volume_24h": float(d.volume.iloc[-1] * d.close.iloc[-1]),
        "spark": [round(float(x), 4) for x in d.close.tail(60).values],
    }


def overview() -> list[dict]:
    def build():
        out = []
        for s, typ in universe().items():
            try:
                out.append(crypto_summary(s) if typ == "crypto" else etf_summary(s))
            except Exception as e:  # never break the page for one symbol
                out.append({"symbol": s, "type": typ, "name": NAMES.get(s, s), "price": None, "error": str(e)})
        for o in out:
            o["aliases"] = ALIASES.get(o["symbol"], "")
        return out
    return cached("overview", 20, build)


@app.get("/api/overview")
def api_overview():
    return {"assets": overview(), "now": int(time.time())}


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

def health() -> list[dict]:
    def build():
        rows, now = [], datetime.now(timezone.utc)
        for s, typ in universe().items():
            if typ == "crypto":
                g = crypto_glob(s)
                if not has_files(g):
                    rows.append({"symbol": s, "dataset": "crypto 1m", "rows": 0})
                    continue
                r = q(f"""
                    WITH t AS (SELECT open_time, epoch(open_time) - lag(epoch(open_time)) OVER (ORDER BY open_time) AS d
                               FROM read_parquet('{g}', hive_partitioning=false))
                    SELECT min(open_time) AS first, max(open_time) AS last, count(*) AS rows,
                           count(*) FILTER (WHERE d > 60) AS gaps,
                           coalesce(sum(d / 60 - 1) FILTER (WHERE d > 60), 0) AS missing
                    FROM t""").iloc[0]
                rows.append({"symbol": s, "dataset": "crypto 1m", "first": int(r["first"].timestamp()),
                             "last": int(r["last"].timestamp()), "rows": int(r["rows"]), "gaps": int(r.gaps),
                             "missing": int(r.missing), "lag_min": round((now - r["last"]).total_seconds() / 60 - 1, 1),
                             "size": sum(f.stat().st_size for f in (CRYPTO_1M / f"symbol={s}").rglob("*.parquet"))})
            else:
                p = etf_daily_path(s)
                if p.exists():
                    d = pd.read_parquet(p, columns=["date"])
                    rows.append({"symbol": s, "dataset": "etf 1d", "first": int(d.date.min().timestamp()),
                                 "last": int(d.date.max().timestamp()), "rows": len(d), "size": p.stat().st_size})
                g = etf_1m_glob(s)
                if has_files(g):
                    r = q(f"""
                        WITH t AS (SELECT timestamp, epoch(timestamp) - lag(epoch(timestamp)) OVER (
                                       PARTITION BY timestamp::DATE ORDER BY timestamp) AS d
                                   FROM read_parquet('{g}', hive_partitioning=false))
                        SELECT min(timestamp) AS first, max(timestamp) AS last, count(*) AS rows,
                               count(DISTINCT timestamp::DATE) AS days,
                               count(*) FILTER (WHERE d > 60) AS gaps,
                               coalesce(sum(d / 60 - 1) FILTER (WHERE d > 60), 0) AS missing
                        FROM t""").iloc[0]
                    rows.append({"symbol": s, "dataset": "etf 1m", "first": int(r["first"].timestamp()),
                                 "last": int(r["last"].timestamp()), "rows": int(r["rows"]), "days": int(r.days),
                                 "gaps": int(r.gaps), "missing": int(r.missing),
                                 "size": sum(f.stat().st_size for f in (ETF_1M / f"ticker={safe_ticker(s)}").rglob("*.parquet"))})
        status_file = LOGS / "yahoo_intraday_status.json"
        status = json.loads(status_file.read_text()) if status_file.exists() else {}
        return {"rows": rows, "yahoo_intraday": status.get("_last_run"), "generated": int(time.time())}
    return cached("health", 300, build)


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
        positions.append({"symbol": s, "name": NAMES.get(s, s), "qty": v["qty"], "avg_cost": avg, "price": last,
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
    if not is_tradable(sym):
        raise HTTPException(400, f"{sym} is an index and can't be traded — use SPY or CSSPX.SW")
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


# ------------------------------------------------------------------ static ---

app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")
