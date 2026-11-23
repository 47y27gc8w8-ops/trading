"""Time-series momentum with volatility targeting (Moskowitz, Ooi, Pedersen 2012),
long-only spot version: hold an asset when its own trailing `lookback` return
is positive, sized to `target_vol` / realised vol (capped at 1), 1/N per asset."""
import numpy as np

from src.backtest.helpers import equal_weight, frame


def positions(bars, p):
    c = frame(bars)
    mom = c / c.shift(p["lookback"]) - 1
    vol = c.pct_change(fill_method=None).rolling(p["vol_window"]).std() * np.sqrt(365)
    size = (p["target_vol"] / vol).clip(upper=1.0)
    sig = (mom > 0).astype(float) * size
    return equal_weight(sig, c)
