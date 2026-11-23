"""Larry Connors' RSI(2) mean reversion ("Short Term Trading Strategies That Work", 2008):
buy when price is above its long-term SMA (uptrend) and RSI(rsi_n) < entry;
sell when close > SMA(exit_sma)."""
import pandas as pd

from src.backtest.helpers import equal_weight, frame, hold_until, rsi


def positions(bars, p):
    c = frame(bars)
    sig = {}
    for s in c:
        x = c[s].dropna()
        entry = (x > x.rolling(p["trend_sma"]).mean()) & (rsi(x, p["rsi_n"]) < p["entry"])
        sig[s] = hold_until(entry, x > x.rolling(p["exit_sma"]).mean())
    return equal_weight(pd.DataFrame(sig).reindex(c.index), c)
