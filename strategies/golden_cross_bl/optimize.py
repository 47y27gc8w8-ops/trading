"""Short grid search for golden_cross_bl (in-sample only decides; OOS only reported).

    docker compose run --rm -T backtest python strategies/golden_cross_bl/optimize.py

Writes results_is.csv (every combo, in-sample) and summary.json (baseline,
picks, their OOS numbers, buy & hold).
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backtest as bt  # noqa: E402


def stats(res: dict) -> dict:
    eq = res["equity"]
    r = eq.pct_change().dropna()
    m = res["metrics"]
    sharpe = float(r.mean() / r.std() * np.sqrt(252)) if r.std() > 0 else 0.0
    cagr, dd = m["yearly_return_pct"], m["max_dd_pct"]
    return {"sharpe": round(sharpe, 3), "cagr_pct": cagr, "max_dd_pct": dd,
            "calmar": round(cagr / abs(dd), 3) if dd else 0.0, "n_trades": m["n_trades"],
            "exposure_pct": m["exposure_pct"], "win_rate": m["win_rate"],
            "return_pct": m["return_pct"], "buy_hold_return_pct": m["buy_hold_return_pct"]}


def buy_hold(period: str) -> dict:
    df = bt.load_bars("etf", "SPY", "1d")
    lo, hi = bt._bounds(df.index, period)
    c = df["close"].iloc[lo:hi]
    r = c.pct_change().dropna()
    yrs = (c.index[-1] - c.index[0]).days / 365.25
    cagr = (c.iloc[-1] / c.iloc[0]) ** (1 / yrs) - 1
    dd = (c / c.cummax() - 1).min()
    return {"sharpe": round(float(r.mean() / r.std() * np.sqrt(252)), 3), "cagr_pct": round(cagr * 100, 2),
            "max_dd_pct": round(dd * 100, 2), "calmar": round(cagr / abs(dd), 3)}


def main() -> None:
    t0 = time.time()
    keys = list(bt.SPACE)
    rows = []
    for combo in itertools.product(*(bt.SPACE[k]["choices"] for k in keys)):
        p = {**bt.PARAMS, **dict(zip(keys, combo))}
        if not bt.valid(p):
            continue
        if p["entry"] == "cross" and p["trailing_stop_pct"] > 0:
            pass  # allowed: after a stop it waits for the next cross (literal reading of the idea)
        rows.append({**p, **stats(bt.run(p, "is"))})
    df = pd.DataFrame(rows)
    # Robustness: average IS Sharpe over the combo and its fast/slow grid neighbours (same other params).
    fl, sl = bt.SPACE["fast"]["choices"], bt.SPACE["slow"]["choices"]
    idx = df.set_index(keys)["sharpe"]
    def neigh(row):
        vals = []
        fi, si = fl.index(row["fast"]), sl.index(row["slow"])
        for df_ in (-1, 0, 1):
            for ds in (-1, 0, 1):
                if 0 <= fi + df_ < len(fl) and 0 <= si + ds < len(sl):
                    k = tuple(row[c] if c not in ("fast", "slow") else (fl[fi + df_] if c == "fast" else sl[si + ds]) for c in keys)
                    if k in idx.index:
                        vals.append(idx[k])
        return round(float(np.mean(vals)), 3)
    df["sharpe_neigh"] = df.apply(neigh, axis=1)
    df = df.sort_values("sharpe_neigh", ascending=False)
    df.to_csv(HERE / "results_is.csv", index=False)

    def pick(row):
        p = {k: (row[k].item() if hasattr(row[k], "item") else row[k]) for k in keys}
        return {"params": p, "is": stats(bt.run(p, "is")), "oos": stats(bt.run(p, "oos")),
                "is_sharpe_neigh": float(row["sharpe_neigh"])}

    base = {k: bt.PARAMS[k] for k in keys}
    out = {
        "n_combos": len(df), "seconds": round(time.time() - t0, 1),
        "baseline_50_200": {"params": base, "is": stats(bt.run(base, "is")), "oos": stats(bt.run(base, "oos"))},
        "buy_hold": {"is": buy_hold("is"), "oos": buy_hold("oos")},
        "robust_best_is": pick(df.iloc[0]),
        "raw_best_is": pick(df.sort_values("sharpe", ascending=False).iloc[0]),
        "best_trailing_stop_only": pick(df[(df.fast == 50) & (df.slow == 200) & (df.ma_type == "sma") & (df.band_pct == 0)]
                                        .sort_values("sharpe", ascending=False).iloc[0]),
        "top10_robust": df.head(10)[keys + ["sharpe", "sharpe_neigh", "cagr_pct", "max_dd_pct", "n_trades"]].to_dict("records"),
    }
    (HERE / "summary.json").write_text(json.dumps(out, indent=2, default=str))
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
