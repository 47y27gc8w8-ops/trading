"""Cross-sectional momentum / rotation (Jegadeesh & Titman 1993; for crypto see
Liu, Tsyvinski & Wu 2022): every `rebalance` days hold the `top_k` coins with the
highest `lookback` return, equal weight. Regime filter: go to cash when BTC is
below its SMA(`regime_sma`). Coins need `min_history` days of data to qualify."""
import numpy as np
import pandas as pd

from src.backtest.helpers import frame


def positions(bars, p):
    c = frame(bars)
    mom = c / c.shift(p["lookback"]) - 1
    age = c.notna().cumsum()
    mom = mom.where(age >= p["min_history"])
    rank = mom.rank(axis=1, ascending=False)
    w = (rank <= p["top_k"]).astype(float)
    w = w.div(w.sum(axis=1).replace(0, np.nan), axis=0).fillna(0.0)
    if p["regime_sma"] > 0:
        btc = c["BTCUSDT"]
        w = w.mul((btc > btc.rolling(p["regime_sma"]).mean()).astype(float), axis=0)
    # only change weights on rebalance days
    days = np.arange(len(w)) % p["rebalance"] == 0
    return w.where(pd.Series(days, index=w.index), np.nan).ffill().fillna(0.0)
