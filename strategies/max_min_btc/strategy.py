"""Quantpedia "Trend-following and Mean-reversion in Bitcoin" (Padysak & Vojtko, 2022):
hold BTC for the next day when today's close is at its `lookback`-day maximum
(trend) and/or at its `lookback`-day minimum (reversion). The paper found the
combination (MAX or MIN) worked best; `mode` lets evolution pick max/min/both."""
from src.backtest.helpers import equal_weight, frame


def positions(bars, p):
    c = frame(bars)
    n = p["lookback"]
    at_max = c >= c.rolling(n).max()
    at_min = c <= c.rolling(n).min()
    sig = {"max": at_max, "min": at_min, "both": at_max | at_min}[p["mode"]].astype(float)
    if p["hold_days"] > 1:  # keep the position for hold_days after each signal
        sig = sig.rolling(p["hold_days"], min_periods=1).max()
    return equal_weight(sig, c)
