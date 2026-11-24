"""Does picking coins by their past breakout results actually pick next year's winners?

For each test year Y (2021 .. 2026 YTD) coins are chosen using ONLY the 3 years before Y, then the chosen
coins' strategy result in year Y is compared with the coins that were not chosen. Selectors:
  perf   trailing 3y strategy Sharpe >= 0.8 and profit factor proxy (sum gains / sum losses of daily P&L) >= 1.3
  trend  top third by trailing 3y efficiency ratio (how cleanly the coin trended), no strategy results used
  all    every coin with 3y of history (the baseline)

    docker compose run --rm -T backtest python strategies/breakout_bl/walkforward.py [--params '{...}']
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backtest as bt  # noqa: E402
from optimize import all_coins  # noqa: E402


def stats(r: pd.Series) -> tuple[float, float]:
    r = r.dropna()
    if len(r) < 30 or r.std() == 0:
        return np.nan, np.nan
    return float(r.mean() / r.std() * np.sqrt(365)), float(r[r > 0].sum() / max(1e-12, -r[r < 0].sum()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default="{}")
    ap.add_argument("--tag", default="original")
    a = ap.parse_args()
    p = {**bt.PARAMS, **json.loads(a.params)}
    rets, er = {}, {}
    for c in all_coins():
        try:
            res = bt.run(p, "all", [c])
        except ValueError:
            continue
        rets[c] = res["equity"].pct_change()
        cl = bt.load_bars("crypto", c, "1d")["close"]
        er[c] = ((cl - cl.shift(20)).abs() / cl.diff().abs().rolling(20).sum())
    R, E = pd.DataFrame(rets), pd.DataFrame(er)
    rows = []
    for y in range(2021, 2027):
        tr = (R.index >= pd.Timestamp(f"{y-3}-01-01", tz="UTC")) & (R.index < pd.Timestamp(f"{y}-01-01", tz="UTC"))
        te = (R.index >= pd.Timestamp(f"{y}-01-01", tz="UTC")) & (R.index < pd.Timestamp(f"{y+1}-01-01", tz="UTC"))
        hist = [c for c in R if R.loc[tr, c].notna().sum() >= 365 * 2.5 and R.loc[te, c].notna().sum() >= 30]
        past = {c: stats(R.loc[tr, c]) for c in hist}
        perf = [c for c in hist if past[c][0] >= 0.8 and past[c][1] >= 1.3]
        er_tr = E.loc[E.index.isin(R.index[tr]), hist].mean()
        trend = list(er_tr.sort_values(ascending=False).index[: max(1, len(hist) // 3)])
        nxt = lambda cs: R.loc[te, cs].mean(axis=1) if cs else pd.Series(dtype=float)  # equal-weight basket, daily rebalanced  # noqa: E731
        row = {"year": y, "n_all": len(hist)}
        for name, cs in (("all", hist), ("perf", perf), ("not_perf", [c for c in hist if c not in perf]),
                         ("trend", trend), ("not_trend", [c for c in hist if c not in trend])):
            b = nxt(cs)
            row[f"{name}_n"] = len(cs)
            row[f"{name}_ret"] = round(float((1 + b.fillna(0)).prod() - 1) * 100, 1) if len(b) else np.nan
            row[f"{name}_sharpe"] = round(stats(b)[0], 2) if len(b) else np.nan
        row["perf_coins"] = ",".join(perf)
        rows.append(row)
    df = pd.DataFrame(rows)
    out = HERE / "results" / f"walkforward_{a.tag}.csv"
    df.to_csv(out, index=False)
    with pd.option_context("display.width", 250, "display.max_columns", 30):
        print(df.drop(columns=["perf_coins"]).to_string(index=False))
    for k in ("perf", "trend"):
        d = df[f"{k}_sharpe"] - df[f"not_{k}_sharpe"]
        print(f"{k}: chosen beat not-chosen (Sharpe) in {int((d > 0).sum())}/{d.notna().sum()} years, mean diff {d.mean():.2f}")


if __name__ == "__main__":
    main()
