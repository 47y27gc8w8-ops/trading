"""Moving-average crossover trend following ("golden cross").
Long when SMA(fast) > SMA(slow), otherwise cash. Long-only."""
from src.backtest.helpers import equal_weight, frame


def valid(p):
    return p["fast"] < p["slow"]


def positions(bars, p):
    c = frame(bars)
    sig = (c.rolling(p["fast"]).mean() > c.rolling(p["slow"]).mean()).astype(float)
    return equal_weight(sig, c)
