"""Final evaluation of the spec and the grid-search picks -> results/report.md + results/final.json.

The holdout (2024-01 .. end) is used here and only here.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

from optimize import HOLD, IS, MIN_IS_TRADES, VAL
from strategy import DEFAULT, HERE, PIP, load_days, metrics, simulate

out = HERE / "results"
d = load_days()
g = pd.read_parquet(out / "grid.parquet")
g = g[g.is_trades >= MIN_IS_TRADES]
KEYS = [k for k in DEFAULT if k != "cost_pips"]


def best(q):
    r = g.query(q).sort_values("is_sharpe", ascending=False).iloc[0]
    return {k: (r[k].item() if hasattr(r[k], "item") else r[k]) for k in KEYS}


variants = {
    "spec (as written)": dict(DEFAULT),
    "best long-only (spec direction)": best("direction == 'long'"),
    "best long-only, close-confirmed": best("direction == 'long' and entry_mode == 'close15'"),
    "best both directions": best("direction == 'both'"),
    "best overall (short-only)": best("direction == 'short'"),
}


def drift_benchmark(sgn: int, start_h: int, exit_h: int) -> pd.DataFrame:
    """Unconditional trade every valid day: enter at start_h, exit at exit_h (no range logic)."""
    e = d.O[:, start_h * 60]
    x = d.C[:, exit_h * 60 - 1]
    pips = (x - e) * sgn / PIP - DEFAULT["cost_pips"]
    hi = np.nanmax(d.H[:, :420], axis=1); lo = np.nanmin(d.L[:, :420], axis=1)
    R = pips / ((hi - lo) / PIP)
    df = pd.DataFrame({"pips": pips, "R": R}, index=d.dates)
    return df[d.valid & ~np.isnan(pips) & (hi > lo)]


periods = {"IS 2010-19": IS, "VAL 2020-23": VAL, "HOLDOUT 2024-26": HOLD, "ALL": (None, None)}
final = {}
lines = ["# EUR/USD London breakout: results", "",
         "Data: HistData.com EURUSD 1-minute bid bars 2010-01 .. 2026-11-13, converted to UTC; "
         "days with <80 % minute coverage in the Asian or London window and US/EU DST-mismatch days excluded. "
         "Costs 1.0 pip per round trip unless stated. Sharpe: daily, annualised, 1 % risk per trade, flat days = 0.", ""]
for name, p in variants.items():
    tr = simulate(d, p)
    final[name] = {"params": p, **{k: metrics(tr, d, *v) for k, v in periods.items()}}
    final[name]["cost_0.5"] = metrics(simulate(d, {**p, "cost_pips": 0.5}), d)
    final[name]["cost_2.0"] = metrics(simulate(d, {**p, "cost_pips": 2.0}), d)
    yr = tr.groupby(tr.index.year).agg(trades=("R", "size"), total_R=("R", "sum"), avg_pips=("pips", "mean"))
    final[name]["per_year"] = {int(y): {"trades": int(r.trades), "total_R": round(float(r.total_R), 1),
                                        "avg_pips": round(float(r.avg_pips), 2)} for y, r in yr.iterrows()}
    lines += [f"## {name}", "", "`" + json.dumps({k: p[k] for k in KEYS}) + "`", "",
              "| period | trades | win % | avg R | avg pips | PF | Sharpe | CAGR % | maxDD % | t |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for k in periods:
        m = final[name][k]
        lines.append(f"| {k} | {m['trades']} | {100 * (m['win_rate'] or 0):.0f} | {m['avg_R']} | {m['avg_pips']} | "
                     f"{m['profit_factor']} | {m['sharpe']} | {m['cagr_pct']} | {m['max_dd_pct']} | {m['t_stat']} |")
    lines += ["", f"Cost sensitivity (ALL): 0.5 pip -> Sharpe {final[name]['cost_0.5']['sharpe']}, "
              f"2.0 pips -> Sharpe {final[name]['cost_2.0']['sharpe']}", "",
              "Per year total R: " + ", ".join(f"{y}: {v['total_R']}" for y, v in final[name]["per_year"].items()), ""]

lines += ["## Drift benchmarks (no breakout logic, trade every valid day)", "",
          "| benchmark | IS Sharpe | VAL Sharpe | HOLDOUT Sharpe |", "|---|---|---|---|"]
for name, (s, a, b) in {"short 08:00 -> 13:00 UTC": (-1, 8, 13), "long 08:00 -> 13:00 UTC": (1, 8, 13),
                        "short 07:00 -> 16:00 UTC": (-1, 7, 16)}.items():
    tr = drift_benchmark(s, a, b)
    ms = [metrics(tr, d, *periods[k])["sharpe"] for k in ("IS 2010-19", "VAL 2020-23", "HOLDOUT 2024-26")]
    final[f"benchmark {name}"] = ms
    lines.append(f"| {name} | {ms[0]} | {ms[1]} | {ms[2]} |")

lines += ["", "## Grid summary (in-sample Sharpe, combos with >= 300 IS trades)", "",
          f"{len(g)} combos. Median IS Sharpe by direction: " +
          ", ".join(f"{k}: {v:.2f}" for k, v in g.groupby("direction").is_sharpe.median().items()) +
          f". Max IS Sharpe overall {g.is_sharpe.max():.2f}; max long-only {g[g.direction == 'long'].is_sharpe.max():.2f}.",
          "With ~7k correlated trials over 10 years, a best-of-grid IS Sharpe around 1 is roughly what noise alone can produce.", ""]
(out / "report.md").write_text("\n".join(lines))
(out / "final.json").write_text(json.dumps(final, indent=1, default=str))
print("\n".join(lines))
