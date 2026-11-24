"""Screen coins for the breakout idea, then tune it on the coins that pass.

Run inside the backtest container (repo root is /app):

    docker compose run --rm -T backtest python strategies/breakout_bl/optimize.py [--budget-min 10] [--workers 6]

Stages (decisions use ONLY the in-sample window 2018-01-01 .. 2024-12-31; out-of-sample 2025-01-01 -> now is
only reported, never used to select coins or parameters):

1. screen    original rules (20/10) on every coin with a daily bar cache, one coin at a time.
2. select    coins that pass fixed in-sample rules (below).
3. tune      one shared parameter set for the selected basket (grid over SPACE), fitness = basket IS Sharpe,
             chosen on a smoothed (neighbour-averaged) score so a lone spike can't win.
4. per-coin  best grid point per selected coin, reported next to the shared set to show whether per-coin tuning
             actually holds up out of sample.

Writes results/*.csv, results/summary.json and appends to log.md.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backtest as bt  # noqa: E402

RES = HERE / "results"
MIN_IS_YEARS = 1.5        # coin needs this much in-sample history to be judged at all
MIN_TRADES = 8            # in-sample trades for a coin to count
SEL = {"sharpe": 0.8, "profit_factor": 1.3}   # in-sample pass marks (plus: drawdown smaller than buy & hold)


def all_coins() -> list[str]:
    from src.common.storage import DATA
    return sorted(p.name[5:-len("_1D.parquet")] for p in (DATA / "cache").glob("bars_*USDT_1D.parquet"))


def sharpe(eq: pd.Series) -> float:
    r = eq.pct_change().dropna()
    return float(r.mean() / r.std() * np.sqrt(365)) if len(r) > 2 and r.std() > 0 else 0.0


def bh_dd(sym: str, period: str) -> float:
    df = bt.load_bars("crypto", sym, "1d")
    lo, hi = bt._bounds(df.index, period)
    c = df["close"].iloc[lo:hi]
    return float((c / c.cummax() - 1).min() * 100) if len(c) else 0.0


def evaluate(args):
    """(params, symbols, period) -> flat result row. Never raises (bad rows get an 'error')."""
    p, syms, period = args
    try:
        r = bt.run(p, period, syms)
        m = r["metrics"]
        eq = r["equity"]
        # half-period sharpe for in-sample stability
        halves = {}
        if period == "is":
            mid = pd.Timestamp("2021-07-01", tz="UTC")
            halves = {"sharpe_h1": round(sharpe(eq[eq.index < mid]), 3), "sharpe_h2": round(sharpe(eq[eq.index >= mid]), 3)}
        return {**p, "symbols": ",".join(syms), "period": period, "sharpe": round(sharpe(eq), 3), **halves,
                **{k: m[k] for k in ("yearly_return_pct", "return_pct", "max_dd_pct", "profit_factor", "n_trades",
                                     "win_rate", "exposure_pct", "buy_hold_return_pct", "years", "n_big_losses")}}
    except Exception as e:  # noqa: BLE001
        return {**p, "symbols": ",".join(syms), "period": period, "error": str(e)}


def efficiency_ratio(sym: str) -> float:
    """Kaufman efficiency ratio of 20-day moves, mean over in-sample: 1 = straight line, 0 = pure noise.
    A cheap 'how much does this coin trend' number, to check the hypothesis in breakout.md."""
    df = bt.load_bars("crypto", sym, "1d")
    lo, hi = bt._bounds(df.index, "is")
    c = df["close"].iloc[max(0, lo - 20):hi]
    er = (c - c.shift(20)).abs() / c.diff().abs().rolling(20).sum()
    return round(float(er.mean()), 3)


def grid() -> list[dict]:
    keys = list(bt.LEGACY_SPACE)
    out = []
    for vals in itertools.product(*(bt.LEGACY_SPACE[k]["choices"] for k in keys)):
        p = {**bt.PARAMS, **dict(zip(keys, vals))}
        if bt.valid(p):
            out.append(p)
    return out


def smooth(df: pd.DataFrame, col: str) -> pd.Series:
    """Mean of col over each grid point and its immediate neighbours in entry_n / exit_n (same filters)."""
    e_ch, x_ch = bt.LEGACY_SPACE["entry_n"]["choices"], bt.LEGACY_SPACE["exit_n"]["choices"]
    idx = {(r.entry_n, r.exit_n, r.trend_sma, r.trailing_stop_pct): r[col] for _, r in df.iterrows()}
    out = []
    for _, r in df.iterrows():
        ei, xi = e_ch.index(r.entry_n), x_ch.index(r.exit_n)
        vals = [idx.get((e_ch[a], x_ch[b], r.trend_sma, r.trailing_stop_pct))
                for a in range(max(0, ei - 1), min(len(e_ch), ei + 2))
                for b in range(max(0, xi - 1), min(len(x_ch), xi + 2))]
        vals = [v for v in vals if v is not None and not pd.isna(v)]
        out.append(float(np.mean(vals)))
    return pd.Series(out, index=df.index)


def log(msg: str) -> None:
    line = f"- {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(HERE / "log.md", "a") as f:
        f.write(line + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget-min", type=float, default=10.0)
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    RES.mkdir(exist_ok=True)
    t0 = time.time()
    left = lambda: a.budget_min * 60 - (time.time() - t0)  # noqa: E731
    base = dict(bt.PARAMS)
    pool = Pool(a.workers)

    # ---- 1. screen --------------------------------------------------------------------------------------
    coins = all_coins()
    log(f"screen: {len(coins)} coins with daily bars, original rules {base}")
    rows = pool.map(evaluate, [(base, [s], per) for s in coins for per in ("is", "oos")])
    scr = pd.DataFrame(rows)
    is_ = scr[scr.period == "is"].set_index("symbols")
    oos = scr[scr.period == "oos"].set_index("symbols")
    s = is_[["sharpe", "sharpe_h1", "sharpe_h2", "yearly_return_pct", "max_dd_pct", "profit_factor", "n_trades",
             "win_rate", "exposure_pct", "buy_hold_return_pct", "years"]].copy()
    s["bh_max_dd_pct"] = [bh_dd(c, "is") if not pd.isna(s.loc[c, "years"]) else np.nan for c in s.index]
    s["trend_er"] = [efficiency_ratio(c) if not pd.isna(s.loc[c, "years"]) else np.nan for c in s.index]
    for k in ("sharpe", "yearly_return_pct", "max_dd_pct", "profit_factor", "n_trades", "buy_hold_return_pct"):
        s["oos_" + k] = oos[k].reindex(s.index)
    s["eligible"] = (s["years"] >= MIN_IS_YEARS) & (s["n_trades"] >= MIN_TRADES)
    s["selected"] = (s["eligible"] & (s["sharpe"] >= SEL["sharpe"]) & (s["profit_factor"] >= SEL["profit_factor"])
                     & (s["max_dd_pct"] > s["bh_max_dd_pct"]))
    s = s.sort_values(["selected", "eligible", "sharpe"], ascending=False)
    s.index.name = "symbol"
    s.to_csv(RES / "screen.csv")
    sel = list(s.index[s.selected])
    rej = list(s.index[s.eligible & ~s.selected])
    el = s[s.eligible]
    corr = float(el["trend_er"].rank().corr(el["sharpe"].rank()))
    log(f"screen done in {time.time() - t0:.0f}s: {int(s.eligible.sum())} eligible, {len(sel)} selected: {', '.join(sel)}")
    log(f"trendiness check: Spearman(efficiency ratio, IS Sharpe) over eligible coins = {corr:.2f}")

    # basket comparison at original params: does the screen pick coins that keep working out of sample?
    basket = {}
    for name, syms in (("selected", sel), ("rejected", rej), ("all_eligible", sel + rej)):
        if syms:
            basket[name] = {per: evaluate((base, syms, per)) for per in ("is", "oos")}
    for name, d in basket.items():
        log(f"original rules, {name} basket ({len(d['is']['symbols'].split(','))} coins): IS Sharpe {d['is']['sharpe']}, "
            f"OOS Sharpe {d['oos']['sharpe']}, OOS return {d['oos']['return_pct']}% (B&H {d['oos']['buy_hold_return_pct']}%), "
            f"OOS maxDD {d['oos']['max_dd_pct']}%")

    # ---- 2. tune one shared parameter set on the selected basket --------------------------------------
    g = grid()
    log(f"tune: {len(g)} grid points on the {len(sel)}-coin basket, budget left {left():.0f}s")
    rows = pool.map(evaluate, [(p, sel, "is") for p in g])
    tg = pd.DataFrame(rows).dropna(subset=["sharpe"])
    tg = tg[tg.n_trades >= MIN_TRADES * len(sel) / 2]
    tg["sharpe_smooth"] = smooth(tg, "sharpe")
    tg["min_half"] = tg[["sharpe_h1", "sharpe_h2"]].min(axis=1)
    tg = tg.sort_values("sharpe_smooth", ascending=False)
    top = tg.head(5)
    keys = list(bt.LEGACY_SPACE)
    # OOS of the top 5 only for the report (choice is already made: the first row)
    tops = []
    for _, r in top.iterrows():
        p = {k: r[k] for k in keys}
        p = {k: (int(v) if k != "trailing_stop_pct" else float(v)) for k, v in p.items()}
        o = evaluate((p, sel, "oos"))
        tops.append({"params": p, "is_sharpe": r.sharpe, "is_sharpe_smooth": round(r.sharpe_smooth, 3),
                     "is_sharpe_halves": [r.sharpe_h1, r.sharpe_h2], "is_yearly": r.yearly_return_pct,
                     "is_max_dd": r.max_dd_pct, "oos_sharpe": o["sharpe"], "oos_return_pct": o["return_pct"],
                     "oos_max_dd": o["max_dd_pct"], "oos_trades": o["n_trades"]})
    tg.to_csv(RES / "tune_grid.csv", index=False)
    champ = tops[0]["params"]
    log(f"tune done ({time.time() - t0:.0f}s): shared champion {champ} IS Sharpe {tops[0]['is_sharpe']} "
        f"(smoothed {tops[0]['is_sharpe_smooth']}) vs original {basket['selected']['is']['sharpe']}; "
        f"OOS Sharpe {tops[0]['oos_sharpe']} vs original {basket['selected']['oos']['sharpe']}")

    # ---- 3. per-coin best (info only) --------------------------------------------------------------------
    per_coin = []
    if left() > 60:
        rows = pool.map(evaluate, [(p, [c], "is") for c in sel for p in g])
        pc = pd.DataFrame(rows).dropna(subset=["sharpe"])
        pc = pc[pc.n_trades >= MIN_TRADES]
        for c in sel:
            d = pc[pc.symbols == c].copy()
            d["sharpe_smooth"] = smooth(d, "sharpe")
            b = d.sort_values("sharpe_smooth", ascending=False).iloc[0]
            p = {k: (int(b[k]) if k != "trailing_stop_pct" else float(b[k])) for k in keys}
            o_best, o_sh, o_base = (evaluate((p, [c], "oos")), evaluate((champ, [c], "oos")), evaluate((base, [c], "oos")))
            i_sh = evaluate((champ, [c], "is"))
            per_coin.append({"symbol": c, **{f"best_{k}": v for k, v in p.items()},
                             "is_sharpe_best": b.sharpe, "is_sharpe_shared": i_sh["sharpe"], "is_sharpe_original": s.loc[c, "sharpe"],
                             "oos_sharpe_best": o_best["sharpe"], "oos_sharpe_shared": o_sh["sharpe"], "oos_sharpe_original": o_base["sharpe"],
                             "oos_return_best": o_best["return_pct"], "oos_return_shared": o_sh["return_pct"],
                             "oos_return_original": o_base["return_pct"], "oos_bh_return": o_base["buy_hold_return_pct"],
                             "oos_maxdd_shared": o_sh["max_dd_pct"], "oos_trades_shared": o_sh["n_trades"]})
        pd.DataFrame(per_coin).to_csv(RES / "per_coin.csv", index=False)
        log(f"per-coin tuning done ({time.time() - t0:.0f}s) for {len(sel)} coins")
    else:
        log("per-coin tuning skipped: budget used up")

    # ---- final basket numbers --------------------------------------------------------------------------
    final = {per: evaluate((champ, sel, per)) for per in ("is", "oos", "live")}
    summary = {
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"), "elapsed_s": round(time.time() - t0, 1),
        "split": {"is": f"{bt.CONFIG['start']} .. {bt.CONFIG['oos_start']} (excl.)", "oos": f"{bt.CONFIG['oos_start']} -> latest"},
        "costs": {"fee_pct": bt.CONFIG["fee_pct"], "slippage_pct": bt.CONFIG["slippage_pct"]},
        "selection_rules": {"min_is_years": MIN_IS_YEARS, "min_trades": MIN_TRADES, **SEL, "max_dd_better_than_bh": True},
        "n_coins_screened": len(coins), "n_eligible": int(s.eligible.sum()), "selected": sel,
        "trend_er_vs_is_sharpe_spearman": round(corr, 3),
        "original_rules_baskets": basket, "shared_champion": champ, "top5_shared": tops,
        "final_selected_basket": final, "per_coin": per_coin,
    }
    (RES / "summary.json").write_text(json.dumps(summary, indent=2, default=str))
    log(f"finished in {time.time() - t0:.0f}s; results in results/")


if __name__ == "__main__":
    main()
