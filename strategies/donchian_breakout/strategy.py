"""Donchian channel breakout (Turtle Traders, Richard Dennis 1983), long-only:
enter when close breaks above the highest high of the previous `entry_n` days,
exit when close falls below the lowest low of the previous `exit_n` days."""
import pandas as pd

from src.backtest.helpers import equal_weight, frame, hold_until


def valid(p):
    return p["exit_n"] < p["entry_n"]


def positions(bars, p):
    c = frame(bars)
    sig = {}
    for s, b in bars.items():
        upper = b["high"].rolling(p["entry_n"]).max().shift(1)
        lower = b["low"].rolling(p["exit_n"]).min().shift(1)
        sig[s] = hold_until(b["close"] > upper, b["close"] < lower)
    return equal_weight(pd.DataFrame(sig).reindex(c.index), c)
