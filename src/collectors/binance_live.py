"""Live 1m klines from the Binance public websocket (no key).

- Stores a bar only when the kline is closed (`x` == true).
- Buffers bars and flushes to Parquet every FLUSH_SECONDS (and on shutdown).
- On every (re)connect, fills the gap since the last stored bar via the public
  REST endpoint, so restarts and disconnects don't leave holes.
- Reconnects with exponential backoff.
"""
from __future__ import annotations

import asyncio
import json
import signal
import time

import pandas as pd
import requests
import websockets

from src.common.storage import CRYPTO_COLUMNS, last_crypto_open_time, load_config, setup_logging, to_utc_ns, write_crypto

log = setup_logging("binance_live")
WS = "wss://data-stream.binance.vision:443/stream?streams="
REST = "https://data-api.binance.vision/api/v3/klines"
FLUSH_SECONDS = 120
MINUTE_MS = 60_000
MAX_REST_FILL_MS = 3 * 24 * 3600 * 1000  # older gaps are filled by binance_history (archive)


def klines_to_df(rows: list[list]) -> pd.DataFrame:
    df = pd.DataFrame([r[:11] for r in rows], columns=CRYPTO_COLUMNS)
    df["open_time"] = to_utc_ns(pd.to_datetime(df.open_time.astype("int64"), unit="ms", utc=True))
    df["close_time"] = to_utc_ns(pd.to_datetime(df.close_time.astype("int64"), unit="ms", utc=True))
    for c in ["open", "high", "low", "close", "volume", "quote_volume", "taker_buy_base", "taker_buy_quote"]:
        df[c] = df[c].astype("float64")
    df["trades"] = df["trades"].astype("int64")
    return df


def rest_fill(symbol: str) -> int:
    """Fetch closed bars since the last stored bar, at most MAX_REST_FILL_MS back."""
    last = last_crypto_open_time(symbol)
    now_ms = int(time.time() * 1000)
    if last is None:
        start = now_ms - 24 * 3600 * 1000
        log.warning("%s: no stored data, REST-filling last 24h (run binance-history for the full backfill)", symbol)
    else:
        start = int(last.timestamp() * 1000) + MINUTE_MS
        if start < now_ms - MAX_REST_FILL_MS:
            log.warning("%s: last stored bar %s is older than the REST fill window; filling only the last "
                        "%d days (run binance-history for the rest)", symbol, last, MAX_REST_FILL_MS // 86_400_000)
            start = now_ms - MAX_REST_FILL_MS
    added = 0
    backoff = 1
    while start < now_ms - MINUTE_MS:
        try:
            r = requests.get(REST, params={"symbol": symbol, "interval": "1m", "startTime": start, "limit": 1000}, timeout=30)
            if r.status_code in (418, 429) or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}")
            r.raise_for_status()
        except requests.RequestException as e:
            log.warning("%s REST fill error (%s), retry in %ss", symbol, e, backoff)
            time.sleep(backoff)
            backoff = min(backoff * 2, 300)
            continue
        backoff = 1
        rows = [k for k in r.json() if k[6] < now_ms]  # only closed bars
        if not rows:
            break
        added += write_crypto(symbol, klines_to_df(rows))
        start = rows[-1][0] + MINUTE_MS
        if len(rows) < 1000:
            break
        time.sleep(0.2)
    if added:
        log.info("%s: REST gap fill added %d bars", symbol, added)
    return added


class Collector:
    def __init__(self, symbols: list[str]):
        self.symbols = [s.upper() for s in symbols]
        self.buffer: dict[str, list[list]] = {s: [] for s in self.symbols}
        self.stop = asyncio.Event()

    def flush(self) -> None:
        for s, rows in self.buffer.items():
            if rows:
                n = write_crypto(s, klines_to_df(rows))
                log.info("%s: flushed %d bars (%d new)", s, len(rows), n)
                self.buffer[s] = []

    async def flusher(self) -> None:
        while not self.stop.is_set():
            try:
                await asyncio.wait_for(self.stop.wait(), FLUSH_SECONDS)
            except asyncio.TimeoutError:
                pass
            await asyncio.to_thread(self.flush)

    async def stream(self) -> None:
        url = WS + "/".join(f"{s.lower()}@kline_1m" for s in self.symbols)
        backoff = 1
        while not self.stop.is_set():
            try:
                # flush buffer first so the REST fill starts from the latest bar
                await asyncio.to_thread(self.flush)
                for s in self.symbols:
                    await asyncio.to_thread(rest_fill, s)
                async with websockets.connect(url, ping_interval=60, ping_timeout=60, max_queue=4096) as ws:
                    log.info("connected: %s", url)
                    backoff = 1
                    while not self.stop.is_set():
                        try:
                            msg = await asyncio.wait_for(ws.recv(), timeout=5)
                        except asyncio.TimeoutError:
                            continue
                        k = json.loads(msg).get("data", {}).get("k")
                        if k and k.get("x"):
                            self.buffer[k["s"]].append(
                                [k["t"], k["o"], k["h"], k["l"], k["c"], k["v"], k["T"], k["q"], k["n"], k["V"], k["Q"]]
                            )
            except Exception as e:  # network errors, 24h server disconnects, etc.
                if self.stop.is_set():
                    break
                log.warning("websocket disconnected (%s: %s), reconnect in %ss", type(e).__name__, e, backoff)
                try:
                    await asyncio.wait_for(self.stop.wait(), backoff)
                except asyncio.TimeoutError:
                    pass
                backoff = min(backoff * 2, 300)

    async def run(self) -> None:
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, self.stop.set)
        await asyncio.gather(self.stream(), self.flusher())
        self.flush()
        log.info("stopped cleanly")


def main() -> None:
    symbols = load_config()["crypto"]
    log.info("starting live collector for %s", symbols)
    asyncio.run(Collector(symbols).run())


if __name__ == "__main__":
    main()
