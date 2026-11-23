"""Small building blocks shared by strategies."""
from __future__ import annotations

import numpy as np
import pandas as pd


def frame(bars: dict[str, pd.DataFrame], col: str = "close") -> pd.DataFrame:
    return pd.DataFrame({s: b[col] for s, b in bars.items()}).sort_index()


def equal_weight(signal: pd.DataFrame, closes: pd.DataFrame) -> pd.DataFrame:
    """Turn per-asset 0..1 signals into portfolio weights: 1/N of capital per
    asset that has data on that day (N = assets listed so far)."""
    n = closes.notna().sum(axis=1).replace(0, np.nan)
    return signal.fillna(0.0).div(n, axis=0).fillna(0.0)


def rsi(close: pd.Series | pd.DataFrame, n: int):
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def hold_until(entry: pd.Series, exit_: pd.Series) -> pd.Series:
    """1 from an entry signal until (and excluding the day after) an exit signal."""
    pos, out = 0.0, []
    for e, x in zip(entry.to_numpy(), exit_.to_numpy()):
        if pos and x:
            pos = 0.0
        elif not pos and e:
            pos = 1.0
        out.append(pos)
    return pd.Series(out, index=entry.index)
