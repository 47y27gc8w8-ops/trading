"""Strategy adapter: runs a library strategy's OWN backtest code on live data and reports which
positions its simulation holds right now.

Every library strategy (strategies/<name>/backtest.py) exposes load_bars(asset_class, symbol,
timeframe) and run(params, period, symbols). Each cycle the adapter
  1. imports a fresh copy of that file (so its module-level caches start empty),
  2. replaces its load_bars with one that returns the project's stored history plus the live
     tail from market.py, including the bar that is still forming,
  3. calls run(params, "live", symbols) and reads the simulated trades still open at the end.
Entries, exits, stops, targets and time limits therefore behave exactly as in the backtest,
with no strategy logic re-implemented here. Position size: portfolio strategies use the simulated
weight (market value / simulated equity); per-symbol strategies use position_pct / N, as at the start
of every backtest period. The bot applies that weight to its own paper equity.
"""
from __future__ import annotations

import importlib.util
import itertools
import logging
import time
from pathlib import Path

import pandas as pd

from src.brokers import market
from src.brokers.market import DataError

log = logging.getLogger("brokers.engine")
ROOT = Path(__file__).resolve().parents[2]
HISTORY_TTL = 6 * 3600          # reload the stored history this often (collectors keep it fresh)
_seq = itertools.count()


class Strategy:
    def __init__(self, name: str, params: dict, symbols: list[str]):
        self.name, self.params, self.symbols = name, dict(params), list(symbols)
        self.path = ROOT / "strategies" / name / "backtest.py"
        if not self.path.exists():
            raise FileNotFoundError(self.path)
        mod = self._fresh()
        self.asset_class = mod.CONFIG["asset_class"]
        self.timeframe = mod.CONFIG["timeframe"]
        # Two kinds of library strategy: a portfolio panel (_simulate_portfolio: real portfolio weights)
        # or independent per-symbol sub-accounts of capital/N each. A per-symbol simulation that has run
        # since 1995 lets those sub-accounts compound apart (one winner ends up as most of the equity),
        # so for those the bot sizes like each backtest period starts: position_pct / N per position.
        self.per_symbol = not hasattr(mod, "_simulate_portfolio")
        self.slot = float(mod.CONFIG.get("position_pct", 1.0)) / len(self.symbols)
        if self.timeframe not in ("1d", "4h", "1h"):
            raise ValueError(f"{name}: timeframe {self.timeframe} not supported by the live bots")
        self.hist: dict[str, pd.DataFrame] = {}
        self.extra: dict[str, pd.DataFrame] = {}   # symbols the strategy loads besides its own (e.g. ^IRX)
        self.hist_at = 0.0
        self.bars: dict[str, pd.DataFrame] = {}

    # -------------------------------------------------------------- loading ---
    def _fresh(self):
        spec = importlib.util.spec_from_file_location(f"_broker_{self.name}_{next(_seq)}", self.path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def _refresh_history(self) -> None:
        mod = self._fresh()
        try:  # the project loader caches crypto daily bars for the process lifetime
            from src.backtest import data
            for fn in vars(data).values():
                if hasattr(fn, "cache_clear"):
                    fn.cache_clear()
        except Exception:  # noqa: BLE001
            pass
        hist = {s: mod.load_bars(self.asset_class, s, self.timeframe) for s in self.symbols}
        self.hist, self.extra, self.hist_at = hist, {}, time.time()
        log.info("%s: history loaded, %s", self.name,
                 ", ".join(f"{s} to {df.index[-1]:%Y-%m-%d %H:%M}" for s, df in list(hist.items())[:4]))

    def _extra_bars(self, asset_class: str, symbol: str, timeframe: str) -> pd.DataFrame:
        key = f"{asset_class}:{symbol}:{timeframe}"
        if key not in self.extra:
            self.extra[key] = self._fresh().load_bars(asset_class, symbol, timeframe)
        return self.extra[key]

    def update_bars(self) -> dict[str, pd.DataFrame]:
        """Stored history + live tail for every symbol. Raises DataError if a gap can't be closed."""
        if time.time() - self.hist_at > HISTORY_TTL or not self.hist:
            self._refresh_history()
        bars = {}
        if self.asset_class == "crypto":
            for s in self.symbols:
                h = self.hist[s]
                tail = market.crypto_bars(s, self.timeframe, 60)
                if h.index[-1] < tail.index[0]:
                    tail = market.crypto_bars(s, self.timeframe, 1000)
                    if h.index[-1] < tail.index[0]:
                        raise DataError(f"{s}: stored history ends {h.index[-1]}, live klines start {tail.index[0]}")
                bars[s] = pd.concat([h[h.index < tail.index[0]], tail])
        else:
            tails = market.yahoo_daily(self.symbols)
            for s in self.symbols:
                h, tail = self.hist[s], tails[s]
                ov = h.index.intersection(tail.index)
                if len(ov) == 0:
                    raise DataError(f"{s}: stored daily history ends {h.index[-1]}, Yahoo tail starts {tail.index[0]}")
                # Yahoo adjusts the whole series after each dividend: rescale the stored history
                # onto the fresh adjustment so the join has no artificial jump.
                ratio = float((tail.loc[ov, "close"] / h.loc[ov, "close"]).median())
                h = h.copy()
                h[["open", "high", "low", "close"]] *= ratio
                bars[s] = pd.concat([h[h.index < tail.index[0]], tail])
        self.bars = bars
        return bars

    # ------------------------------------------------------------- signals ---
    def targets(self) -> tuple[dict[str, dict], dict[str, dict]]:
        """({symbol: {weight, sim_entry, sim_entry_price}}, {symbol: its last closed simulated trade}).
        Also keeps self.sim_closed (every closed simulated trade, for the journal's shadow record)."""
        mod = self._fresh()
        bars = self.bars
        given: dict = {}   # one persistent frame per symbol: strategies memoize on id(df)

        def load_bars(asset_class, symbol, timeframe):
            key = (asset_class, symbol, timeframe)
            if key not in given:
                src = bars[symbol] if symbol in bars else self._extra_bars(asset_class, symbol, timeframe)
                given[key] = src.copy()
            return given[key]

        mod.load_bars = load_bars
        res = mod.run(self.params, "live", self.symbols)
        eq = float(res["equity"].iloc[-1])
        out, last_exit, closed = {}, {}, []
        for t in res["trades"]:
            if t["exit_reason"] == "end":
                px = float(bars[t["symbol"]]["close"].iloc[-1])
                w = self.slot if self.per_symbol else max(0.0, t["qty"] * px / eq)
                out[t["symbol"]] = {"weight": min(1.0, w), "sim_entry": str(t["entry_time"]),
                                    "sim_entry_price": float(t["entry_price"])}
            else:
                c = {"symbol": t["symbol"], "entry_time": str(t["entry_time"]), "exit_time": str(t["exit_time"]),
                     "entry_price": float(t["entry_price"]), "exit_price": float(t["exit_price"]),
                     "reason": t["exit_reason"], "pnl_pct": (float(t["exit_price"]) / float(t["entry_price"]) - 1) * 100}
                last_exit[t["symbol"]] = c
                closed.append(c)
        self.sim_closed = closed
        self._last_run = (mod, given)
        return out, last_exit

    def closed_bar_signals(self) -> dict[str, dict]:
        """Buy/sell flags of each symbol's last COMPLETED bar, from the strategy's own buy_signal /
        sell_signal (per-symbol strategies only; portfolio strategies decide inside their simulation)."""
        mod, given = getattr(self, "_last_run", (None, None))
        if mod is None or not (hasattr(mod, "buy_signal") and hasattr(mod, "sell_signal")) or not self.per_symbol:
            return {}
        out = {}
        for (_, sym, _), df in given.items():
            if sym not in self.symbols or len(df) < 2:
                continue
            try:
                b = mod.buy_signal(df, self.params).fillna(False)
                s = mod.sell_signal(df, self.params).fillna(False)
                out[sym] = {"buy": bool(b.iloc[-2]), "sell": bool(s.iloc[-2])}
            except Exception as ex:  # noqa: BLE001 - diagnostics only
                out[sym] = {"error": f"{type(ex).__name__}: {ex}"[:200]}
        return out

    def closed_bars(self) -> dict[str, dict]:
        """Last completed bar per symbol (the last row of each frame is still forming)."""
        out = {}
        for s, df in self.bars.items():
            if len(df) >= 2:
                r = df.iloc[-2]
                out[s] = {"t": str(df.index[-2]), "o": float(r["open"]), "h": float(r["high"]), "l": float(r["low"]),
                          "c": float(r["close"]), "v": float(r["volume"])}
        return out

    def prices(self) -> dict[str, float]:
        return {s: float(df["close"].iloc[-1]) for s, df in self.bars.items()}
