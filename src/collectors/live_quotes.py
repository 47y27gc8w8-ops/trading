"""Live quote snapshots for the whole universe, every POLL_SECONDS (default 30 s).

Sources (all public, no API key):
  - Binance  GET /api/v3/ticker/24hr?symbols=[...]   all crypto pairs in one request
  - Yahoo    GET /v7/finance/quote?symbols=...       stocks, ETFs, indices, 150 per request
             (via yfinance's session, which handles Yahoo's cookie + crumb)
  - CoinGecko GET /api/v3/coins/markets               coin names, market cap, rank (every 5 min)

Outputs:
  data/quotes/latest.json                                    newest quote per symbol + feed status
  data/quotes/source=<S>/date=<YYYY-MM-DD>/hour=<HH>.parquet  snapshot history, key (symbol, time)

Rows are deduplicated on the exchange timestamp, so a closed market does not
store the same quote every 30 s. Polls are aligned to the wall clock (:00, :30).
Run: python -m src.collectors.live_quotes
"""
from __future__ import annotations

import json
import os
import signal
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import pandas as pd
import requests

from src.common.storage import QUOTES, load_config, merge_write, setup_logging, to_utc_ns

log = setup_logging("live_quotes")
POLL_SECONDS = int(os.environ.get("POLL_SECONDS", 30))
FLUSH_SECONDS = 300
COINGECKO_EVERY = 300
YAHOO_CHUNK = 150
LATEST = QUOTES / "latest.json"

BINANCE = "https://data-api.binance.vision/api/v3/ticker/24hr"
YAHOO = "https://query1.finance.yahoo.com/v7/finance/quote"
COINGECKO = "https://api.coingecko.com/api/v3/coins/markets"

COLUMNS = ["symbol", "time", "fetched", "price", "change_pct", "prev_close", "open", "day_high", "day_low",
           "volume", "quote_volume", "bid", "ask", "market_cap", "market_state", "currency"]
FLOATS = ["price", "change_pct", "prev_close", "open", "day_high", "day_low", "volume", "quote_volume",
          "bid", "ask", "market_cap"]

http = requests.Session()
http.headers["User-Agent"] = "homelab-trading-dashboard/1.0"


def _f(x):
    try:
        return None if x is None or x == "" else float(x)
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------ sources ---

def poll_binance(symbols: list[str], now: float) -> list[dict]:
    r = http.get(BINANCE, params={"symbols": json.dumps(symbols, separators=(",", ":")), "type": "FULL"}, timeout=20)
    r.raise_for_status()
    out = []
    for t in r.json():
        last, opn = _f(t["lastPrice"]), _f(t["openPrice"])
        out.append({
            "symbol": t["symbol"], "type": "crypto", "source": "binance", "time": t["closeTime"] / 1000, "fetched": now,
            "price": last, "open": opn, "prev_close": opn,  # 24 h rolling window: change vs price 24 h ago
            "change_pct": (last / opn - 1) if last and opn else None,
            "day_high": _f(t["highPrice"]), "day_low": _f(t["lowPrice"]),
            "volume": _f(t["volume"]), "quote_volume": _f(t["quoteVolume"]),
            "bid": _f(t.get("bidPrice")), "ask": _f(t.get("askPrice")),
            "market_state": "REGULAR", "currency": "USDT",
        })
    return out


_yf = None


def yahoo_session():
    global _yf
    if _yf is None:
        from yfinance.data import YfData  # imported lazily: heavy
        _yf = YfData()
    return _yf


def poll_yahoo(symbols: list[str], types: dict[str, str], now: float) -> list[dict]:
    out, errors = [], []
    for i in range(0, len(symbols), YAHOO_CHUNK):
        chunk = symbols[i:i + YAHOO_CHUNK]
        try:
            r = yahoo_session().get(YAHOO, params={"symbols": ",".join(chunk)}, timeout=20)
            if r.status_code != 200:
                raise requests.HTTPError(f"HTTP {r.status_code}: {r.text[:200]}")
            res = r.json()["quoteResponse"]["result"]
        except Exception as e:
            errors.append(f"chunk {i // YAHOO_CHUNK}: {e}")
            continue
        for q in res:
            s = q.get("symbol")
            if s not in types or q.get("regularMarketPrice") is None:
                continue
            pct = _f(q.get("regularMarketChangePercent"))
            vol, px = _f(q.get("regularMarketVolume")), _f(q.get("regularMarketPrice"))
            out.append({
                "symbol": s, "type": types[s], "source": "yahoo",
                "time": q.get("regularMarketTime") or now, "fetched": now,
                "price": px, "change_pct": None if pct is None else pct / 100,
                "prev_close": _f(q.get("regularMarketPreviousClose")), "open": _f(q.get("regularMarketOpen")),
                "day_high": _f(q.get("regularMarketDayHigh")), "day_low": _f(q.get("regularMarketDayLow")),
                "volume": vol, "quote_volume": vol * px if vol and px else None,
                "bid": _f(q.get("bid")), "ask": _f(q.get("ask")), "market_cap": _f(q.get("marketCap")),
                "market_state": q.get("marketState"), "currency": q.get("currency"),
                # static-ish metadata, only kept in latest.json
                "name": q.get("longName") or q.get("shortName") or s, "exchange": q.get("fullExchangeName"),
                "quote_type": q.get("quoteType"),
                "post_price": _f(q.get("postMarketPrice")), "pre_price": _f(q.get("preMarketPrice")),
            })
    if errors and not out:
        raise RuntimeError("; ".join(errors))
    if errors:
        log.warning("yahoo partial failure: %s", "; ".join(errors))
    return out


def poll_coingecko() -> dict[str, dict]:
    """Top 250 coins -> {BINANCE_SYMBOL: {name, market_cap, rank}} (highest market cap wins a ticker clash)."""
    r = http.get(COINGECKO, params={"vs_currency": "usd", "per_page": 250, "page": 1}, timeout=30)
    r.raise_for_status()
    out: dict[str, dict] = {}
    for c in r.json():
        key = c["symbol"].upper() + "USDT"
        if key not in out:
            out[key] = {"name": c["name"], "market_cap": c.get("market_cap"), "rank": c.get("market_cap_rank")}
    return out


# --------------------------------------------------------------- collector ---

class Poller:
    def __init__(self):
        cfg = load_config()
        self.crypto = list(cfg.get("crypto", []))
        self.yahoo_types = {s: "etf" for s in cfg.get("etf", [])}
        self.yahoo_types.update({s: "stock" for s in cfg.get("stock", [])})
        self.latest: dict[str, dict] = {}
        if LATEST.exists():
            try:
                self.latest = json.loads(LATEST.read_text()).get("quotes", {})
            except Exception:
                log.warning("could not read %s, starting empty", LATEST)
        self.status: dict[str, dict] = {}
        self.cg: dict[str, dict] = {}
        self.cg_time = 0.0
        self.buffer: dict[str, list[dict]] = {"binance": [], "yahoo": []}
        self.stop = threading.Event()
        self.pool = ThreadPoolExecutor(3)

    def _run(self, name: str, fn, *args):
        t0 = time.time()
        st = self.status.setdefault(name, {})
        try:
            res = fn(*args)
            st.update(last_ok=t0, ms=round((time.time() - t0) * 1000), error=None,
                      count=len(res) if hasattr(res, "__len__") else None)
            return res
        except Exception as e:
            st.update(last_error=t0, error=f"{type(e).__name__}: {e}"[:300])
            log.warning("%s failed: %s", name, st["error"])
            return None

    def poll_once(self) -> None:
        now = time.time()
        futs = {"binance": self.pool.submit(self._run, "binance", poll_binance, self.crypto, now),
                "yahoo": self.pool.submit(self._run, "yahoo", poll_yahoo, list(self.yahoo_types), self.yahoo_types, now)}
        if now - self.cg_time >= COINGECKO_EVERY:
            cg = self._run("coingecko", poll_coingecko)
            if cg:
                self.cg, self.cg_time = cg, now
        for src, fut in futs.items():
            rows = fut.result() or []
            for r in rows:
                if src == "binance":
                    meta = self.cg.get(r["symbol"]) or {}
                    old = self.latest.get(r["symbol"], {})
                    r["name"] = meta.get("name") or old.get("name") or r["symbol"]
                    r["market_cap"] = meta.get("market_cap", old.get("market_cap"))
                    r["rank"] = meta.get("rank", old.get("rank"))
                self.latest[r["symbol"]] = r
            self.buffer[src].extend(rows)
        self.write_latest()

    def write_latest(self) -> None:
        QUOTES.mkdir(parents=True, exist_ok=True)
        tmp = LATEST.with_name(".latest.json.tmp")
        tmp.write_text(json.dumps({"generated": time.time(), "poll_seconds": POLL_SECONDS,
                                   "status": self.status, "quotes": self.latest}, separators=(",", ":")))
        os.replace(tmp, LATEST)

    def flush(self) -> None:
        for src, rows in self.buffer.items():
            if not rows:
                continue
            self.buffer[src] = []
            df = pd.DataFrame(rows)
            for c in COLUMNS:
                if c not in df:
                    df[c] = None
            df = df[COLUMNS]
            df[FLOATS] = df[FLOATS].astype("float64")
            df["time"] = to_utc_ns(pd.to_datetime(df.time, unit="s", utc=True)).dt.floor("s")
            df["fetched"] = to_utc_ns(pd.to_datetime(df.fetched, unit="s", utc=True)).dt.floor("s")
            df = df.drop_duplicates(["symbol", "time"], keep="last")
            added = 0
            for (d, h), part in df.groupby([df.fetched.dt.strftime("%Y-%m-%d"), df.fetched.dt.hour]):
                path = QUOTES / f"source={src}" / f"date={d}" / f"hour={h:02d}.parquet"
                added += merge_write(path, part.reset_index(drop=True), ["symbol", "time"])
            log.info("%s: flushed %d snapshot rows (%d new)", src, len(df), added)

    def run(self) -> None:
        signal.signal(signal.SIGTERM, lambda *_: self.stop.set())
        signal.signal(signal.SIGINT, lambda *_: self.stop.set())
        log.info("polling %d crypto + %d Yahoo symbols every %ds", len(self.crypto), len(self.yahoo_types), POLL_SECONDS)
        last_flush, polls = time.time(), 0
        while not self.stop.is_set():
            t0 = time.time()
            self.poll_once()
            polls += 1
            if polls % 20 == 1:
                log.info("poll %d: %s", polls, {k: (v.get("count"), v.get("ms"), v.get("error")) for k, v in self.status.items()})
            if time.time() - last_flush >= FLUSH_SECONDS:
                self.flush()
                last_flush = time.time()
            # sleep until the next wall-clock multiple of POLL_SECONDS
            nxt = (int(t0 // POLL_SECONDS) + 1) * POLL_SECONDS
            self.stop.wait(max(1.0, nxt - time.time()))
        self.flush()
        log.info("stopped cleanly")


def main() -> None:
    Poller().run()


if __name__ == "__main__":
    main()
