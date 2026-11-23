from __future__ import annotations

import numpy as np
import pandas as pd


def stats(r: pd.Series, ppy: int, exposure: pd.Series | None = None, turnover: pd.Series | None = None) -> dict:
    r = r.dropna()
    if len(r) < 20:
        return {"sharpe": float("nan")}
    eq = (1 + r).cumprod()
    years = len(r) / ppy
    cagr = eq.iloc[-1] ** (1 / years) - 1 if eq.iloc[-1] > 0 else -1.0
    vol = r.std() * np.sqrt(ppy)
    sharpe = r.mean() / r.std() * np.sqrt(ppy) if r.std() > 0 else 0.0
    downside = r[r < 0].std() * np.sqrt(ppy)
    dd = (eq / eq.cummax() - 1).min()
    out = {
        "start": str(r.index[0].date()), "end": str(r.index[-1].date()), "days": len(r),
        "cagr": cagr, "vol": vol, "sharpe": sharpe,
        "sortino": r.mean() * ppy / downside if downside > 0 else 0.0,
        "max_dd": dd, "calmar": cagr / abs(dd) if dd < 0 else 0.0,
        "total_return": eq.iloc[-1] - 1,
    }
    if exposure is not None:
        out["avg_exposure"] = exposure.loc[r.index].mean()
    if turnover is not None:
        out["turnover_per_year"] = turnover.loc[r.index].sum() / years
    return {k: (round(float(v), 4) if isinstance(v, (float, np.floating)) else v) for k, v in out.items()}
