"""Vectorised daily backtester.

A strategy module exposes `positions(bars: dict[str, DataFrame], params) -> DataFrame`
returning target weights per symbol (columns) per date (index), decided with
information up to and including that day's close. The engine applies them to
the NEXT day's close-to-close return (no look-ahead) and charges costs on
every change in weight (turnover * cost_bps).

Gross exposure is the strategy's responsibility: single-asset strategies should
return weights in [0, 1/N] per symbol so the sum stays <= 1 (fully cash-funded,
no leverage).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import data


def run(strategy, cfg: dict, params: dict) -> dict:
    ac = cfg["asset_class"]
    bars = {s: data.load(ac, s) for s in cfg["universe"]}
    if cfg.get("start"):
        bars = {s: b[b.index >= pd.Timestamp(cfg["start"], tz="UTC")] for s, b in bars.items()}
    closes = pd.DataFrame({s: b["close"] for s, b in bars.items()}).sort_index()
    rets = closes.pct_change(fill_method=None).fillna(0.0)

    w = strategy.positions(bars, params).reindex(closes.index).fillna(0.0)
    w = w.reindex(columns=closes.columns).fillna(0.0)
    held = w.shift(1).fillna(0.0)                       # trade at close t, earn t+1
    turnover = w.diff().abs().sum(axis=1).fillna(w.abs().sum(axis=1))
    cost = turnover.shift(1).fillna(0.0) * cfg.get("cost_bps", 10) / 1e4
    pnl = (held * rets).sum(axis=1) - cost

    # benchmark: equal-weight buy & hold of the universe (assets as they appear)
    avail = closes.notna().astype(float)
    bench = (rets * avail).sum(axis=1) / avail.sum(axis=1).replace(0, np.nan)
    first = closes.dropna(how="all").index[0]
    pnl, bench, held, turnover = (x[x.index >= first] for x in (pnl, bench.fillna(0.0), held, turnover))
    return {"returns": pnl, "benchmark": bench, "exposure": held.abs().sum(axis=1), "turnover": turnover}
