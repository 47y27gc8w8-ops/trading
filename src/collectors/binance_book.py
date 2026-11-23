"""Record every best bid/ask change (Binance `bookTicker` websocket) for all coins in
config `crypto`. ~1000 updates/s for 60 coins (~1 GB/day as Parquet).

Layout: data/crypto/book/date=<YYYY-MM-DD>/<HHMMSS>.parquet  (one file per flush, all symbols)
Columns: recv_time (UTC, µs: local receive time - Binance spot bookTicker carries no
         exchange timestamp), symbol, update_id, bid, bid_qty, ask, ask_qty

Flushes every FLUSH_SECONDS and on shutdown; reconnects with backoff; a gap in
recording is visible as a gap in recv_time. Retention: src.common.budget.prune_book
(oldest days first) runs after every flush hour.
"""
from __future__ import annotations

import asyncio
import json
import signal
import time
from datetime import datetime, timezone

import pyarrow as pa
import pyarrow.parquet as pq
import websockets

from src.common.budget import BOOK, prune_book
from src.common.storage import load_config, setup_logging

log = setup_logging("binance_book")
WS = "wss://data-stream.binance.vision:443/stream?streams="
FLUSH_SECONDS = 300
SCHEMA = pa.schema([("recv_time", pa.timestamp("us", tz="UTC")), ("symbol", pa.dictionary(pa.int16(), pa.string())),
                    ("update_id", pa.int64()), ("bid", pa.float64()), ("bid_qty", pa.float64()),
                    ("ask", pa.float64()), ("ask_qty", pa.float64())])


class Recorder:
    def __init__(self, symbols: list[str]):
        self.symbols = symbols
        self.stop = asyncio.Event()
        self._new()
        self.total = 0

    def _new(self):
        self.cols = {k: [] for k in ("recv_time", "symbol", "update_id", "bid", "bid_qty", "ask", "ask_qty")}

    def flush(self) -> None:
        cols, n = self.cols, len(self.cols["recv_time"])
        self._new()
        if not n:
            return
        tbl = pa.table({
            "recv_time": pa.array(cols["recv_time"], pa.int64()).cast(pa.timestamp("us", tz="UTC")),
            "symbol": pa.array(cols["symbol"], pa.string()),
            "update_id": pa.array(cols["update_id"], pa.int64()),
            **{k: pa.array(cols[k], pa.float64()) for k in ("bid", "bid_qty", "ask", "ask_qty")},
        })
        # sort on the plain strings (Arrow can't sort dictionary columns), then dictionary-encode
        tbl = tbl.sort_by([("symbol", "ascending"), ("recv_time", "ascending")]).cast(SCHEMA)
        first = datetime.fromtimestamp(cols["recv_time"][0] / 1e6, timezone.utc)
        d = BOOK / f"date={first:%Y-%m-%d}"
        d.mkdir(parents=True, exist_ok=True)
        path = d / f"{first:%H%M%S}.parquet"
        tmp = d / ("." + path.name + ".tmp")
        pq.write_table(tbl, tmp, compression="zstd", compression_level=6, row_group_size=500_000)
        tmp.replace(path)
        self.total += n
        log.info("flushed %s updates (%.1f MB) -> %s", f"{n:,}", path.stat().st_size / 1e6, path.relative_to(BOOK))

    async def flusher(self) -> None:
        last_prune = 0.0
        while not self.stop.is_set():
            try:
                await asyncio.wait_for(self.stop.wait(), FLUSH_SECONDS)
            except asyncio.TimeoutError:
                pass
            try:
                await asyncio.to_thread(self.flush)
                if time.time() - last_prune > 3600:
                    last_prune = time.time()
                    await asyncio.to_thread(prune_book)
            except Exception:
                log.exception("flush/prune failed (recording continues)")

    async def stream(self) -> None:
        url = WS + "/".join(f"{s.lower()}@bookTicker" for s in self.symbols)
        backoff = 1
        c = self.cols
        while not self.stop.is_set():
            try:
                async with websockets.connect(url, ping_interval=60, ping_timeout=60, max_queue=None) as ws:
                    log.info("connected: %d bookTicker streams", len(self.symbols))
                    backoff = 1
                    while not self.stop.is_set():
                        try:
                            msg = await asyncio.wait_for(ws.recv(), timeout=5)
                        except asyncio.TimeoutError:
                            continue
                        now = time.time_ns() // 1000
                        d = json.loads(msg).get("data")
                        if not d or "b" not in d:
                            continue
                        c = self.cols
                        c["recv_time"].append(now)
                        c["symbol"].append(d["s"])
                        c["update_id"].append(d["u"])
                        c["bid"].append(float(d["b"]))
                        c["bid_qty"].append(float(d["B"]))
                        c["ask"].append(float(d["a"]))
                        c["ask_qty"].append(float(d["A"]))
            except Exception as e:  # network errors, 24h server disconnects, ...
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
        log.info("stopped cleanly, %s updates recorded this run", f"{self.total:,}")


def main() -> None:
    cfg = load_config()
    if not cfg.get("book_ticker", True):
        log.info("book_ticker disabled in config; idling")
        signal.sigwait({signal.SIGTERM, signal.SIGINT})
        return
    symbols = [str(s) for s in cfg["crypto"]]
    log.info("recording bookTicker for %d symbols", len(symbols))
    asyncio.run(Recorder(symbols).run())


if __name__ == "__main__":
    main()
