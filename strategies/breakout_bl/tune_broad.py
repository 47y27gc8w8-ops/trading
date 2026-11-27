"""Tune one shared parameter set on ALL eligible coins (broad basket) instead of the screened subset.
Same grid, fitness (IS Sharpe, neighbour-smoothed) and split as optimize.py.

    docker compose run --rm -T backtest python strategies/breakout_bl/tune_broad.py
"""
import json, sys, time
from multiprocessing import Pool
from pathlib import Path
import pandas as pd
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backtest as bt  # noqa: E402
from optimize import evaluate, grid, smooth, log, MIN_TRADES  # noqa: E402

t0 = time.time()
scr = pd.read_csv(HERE / "results" / "screen.csv")
coins = list(scr.loc[scr.eligible, "symbol"])
g = grid()
log(f"tune_broad: {len(g)} grid points on all {len(coins)} eligible coins")
with Pool(6) as pool:
    tg = pd.DataFrame(pool.map(evaluate, [(p, coins, "is") for p in g])).dropna(subset=["sharpe"])
tg = tg[tg.n_trades >= MIN_TRADES * len(coins) / 2]
tg["sharpe_smooth"] = smooth(tg, "sharpe")
tg = tg.sort_values("sharpe_smooth", ascending=False)
tg.to_csv(HERE / "results" / "tune_grid_broad.csv", index=False)
keys = list(bt.LEGACY_SPACE)
out = []
cands = [{k: (float(r[k]) if k == "trailing_stop_pct" else int(r[k])) for k in keys} for _, r in tg.head(5).iterrows()]
cands.append(dict(bt.PARAMS))
for p in cands:
    i, o, l = (evaluate((p, coins, per)) for per in ("is", "oos", "live"))
    out.append({"params": p, "is": {k: i[k] for k in ("sharpe", "sharpe_h1", "sharpe_h2", "yearly_return_pct", "max_dd_pct", "profit_factor", "n_trades", "buy_hold_return_pct")},
                "oos": {k: o[k] for k in ("sharpe", "return_pct", "yearly_return_pct", "max_dd_pct", "profit_factor", "n_trades", "buy_hold_return_pct")},
                "live_since_2018": {k: l[k] for k in ("sharpe", "yearly_return_pct", "max_dd_pct")}})
    print(json.dumps(out[-1]))
(HERE / "results" / "tune_broad.json").write_text(json.dumps({"coins": coins, "candidates": out}, indent=2))
log(f"tune_broad done in {time.time()-t0:.0f}s: champion {cands[0]} IS Sharpe {out[0]['is']['sharpe']} OOS Sharpe {out[0]['oos']['sharpe']} "
    f"(original 20/10: IS {out[-1]['is']['sharpe']}, OOS {out[-1]['oos']['sharpe']})")
