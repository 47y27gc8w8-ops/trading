"""Grid search for the EUR/USD London breakout.

Split (decisions use in-sample only):
  in-sample   2010-01-01 .. 2019-12-31   ranking
  validation  2020-01-01 .. 2023-12-31   checked for the IS top-N, used to pick the final variant
  holdout     2024-01-01 .. end           looked at once, for the final picks only

Usage: python optimize.py            -> results/grid.parquet, results/top.json, results/report.md
"""
from __future__ import annotations

import itertools
import json
import time

import numpy as np
import pandas as pd

from strategy import DEFAULT, HERE, load_days, metrics, simulate

IS = (None, "2020-01-01")
VAL = ("2020-01-01", "2024-01-01")
HOLD = ("2024-01-01", None)
MIN_IS_TRADES = 300

GRID = dict(
    entry_mode=["touch", "close15"],
    entry_start=[7, 8],
    entry_end=[9, 11, 13, 16],
    buffer_pips=[0.0, 3.0],
    stop_frac=[1.0, 0.5],
    tp_mult=[0.0, 1.0, 2.0, 3.0],
    exit_hour=[11, 13, 16],
    direction=["long", "short", "both"],
    min_range_pips=[0.0, 15.0],
    max_range_pips=[1e9, 50.0],
)
SPEC = dict(DEFAULT)


def combos():
    keys = list(GRID)
    for vals in itertools.product(*GRID.values()):
        p = dict(zip(keys, vals))
        if p["exit_hour"] < p["entry_end"]:
            continue
        yield p


def fast_is(tr: pd.DataFrame, is_days: pd.DatetimeIndex) -> tuple[float, int, float]:
    t = tr[tr.index.isin(is_days)]
    r = np.zeros(len(is_days))
    r[is_days.get_indexer(t.index)] = t.R.to_numpy()
    sd = r.std()
    return (float(r.mean() / sd * np.sqrt(252)) if sd > 0 else 0.0), len(t), float(t.R.sum())


def neighbours(p: dict) -> list[dict]:
    out = []
    for k, vals in GRID.items():
        i = vals.index(p[k])
        for j in (i - 1, i + 1):
            if 0 <= j < len(vals) and k not in ("direction", "entry_mode"):
                q = dict(p, **{k: vals[j]})
                if q["exit_hour"] >= q["entry_end"]:
                    out.append(q)
    return out


def main() -> None:
    out = HERE / "results"
    out.mkdir(exist_ok=True)
    d = load_days()
    is_days = d.dates[d.valid & (d.dates < pd.Timestamp(IS[1], tz="UTC"))]
    rows, t0 = [], time.time()
    allp = list(combos())
    for i, p in enumerate(allp):
        tr = simulate(d, p)
        s, n, tot = fast_is(tr, is_days)
        rows.append({**p, "is_sharpe": s, "is_trades": n, "is_total_R": tot})
        if i % 500 == 0:
            print(f"{i}/{len(allp)} {time.time() - t0:.0f}s", flush=True)
    g = pd.DataFrame(rows)
    key = list(GRID)
    g["key"] = g[key].astype(str).agg("|".join, axis=1)
    lookup = dict(zip(g.key, g.is_sharpe))

    def nb_score(p):
        v = [lookup.get("|".join(map(str, (q[k] for k in key)))) for q in neighbours(p)]
        v = [x for x in v if x is not None]
        return float(np.mean(v)) if v else np.nan, float(np.min(v)) if v else np.nan

    elig = g[g.is_trades >= MIN_IS_TRADES].sort_values("is_sharpe", ascending=False)
    top = elig.head(40).copy()
    recs = []
    for _, r in top.iterrows():
        p = {k: r[k] for k in key}
        p = {k: (v.item() if hasattr(v, "item") else v) for k, v in p.items()}
        tr = simulate(d, p)
        nm, nmin = nb_score(p)
        recs.append({"params": p, "nb_mean_is_sharpe": round(nm, 2), "nb_min_is_sharpe": round(nmin, 2),
                     "is": metrics(tr, d, *IS), "val": metrics(tr, d, *VAL)})
    g.drop(columns="key").to_parquet(out / "grid.parquet")
    (out / "top.json").write_text(json.dumps(recs, indent=1))
    print(f"done {len(g)} combos in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
