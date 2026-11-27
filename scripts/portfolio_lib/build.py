#!/usr/bin/env python3
"""Build self-contained strategies/<name>/backtest.py files for the library's month-end portfolio specs.

Each file = template header + this spec's strategy block + core.py (shared portfolio simulator)
+ tail.py (generic machinery). Files are self-contained on purpose: the optimizer fingerprints the
functions of each backtest.py, and the skill wants an adapted copy per strategy.

    python3 scripts/portfolio_lib/build.py [name ...]     # default: all specs below
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

SECT = ["XLB", "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY"]
GLOB = ["DBC", "EEM", "EFA", "GLD", "IEF", "SPY", "TLT", "VNQ"]
CRYPTO = ["BTCUSDT", "ETHUSDT", "LTCUSDT", "SOLUSDT"]

ETF = dict(asset_class="etf", oos="2016-01-01", fee=0.05, slip=0.03,
           fee_note="library convention for US ETFs (spec: 1 bp commission; more conservative)",
           slip_note="spec: half-spread 2 bp + slippage 2 bp per fill")
CRY = dict(asset_class="crypto", oos="2024-01-01", fee=0.10, slip=0.10,
           fee_note="spec: 10 bp commission per side",
           slip_note="spec: 5 bp half-spread + 5 bp adverse slippage per fill")

SL = '"stop_loss_pct": {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0},'
MC = '"max_candles": {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260},'
SLP = '"stop_loss_pct": 15.0,   # hard stop below each holding\'s cost basis (never loosened)'
MCP = '"max_candles": 252,      # held daily bars per holding before a forced exit at the next open'


def k_space(lo, hi, hard_max):
    return f'"k": {{"min": {lo}, "max": {hi}, "step": 1, "hard_min": 1, "hard_max": {hard_max}}},'


# name -> (title, universe, market, start, reference, params lines, space lines, valid expr, body)
SPECS = {
    "consistent_winner_rotation": (
        "Consistent winner rotation", SECT, ETF, "2000-07-01", [],
        ['"n": 12,     # completed months counted for the positive-month score', '"k": 3,      # holdings'],
        ['"n": {"min": 6, "max": 24, "step": 1, "hard_min": 1, "hard_max": 60},', k_space(1, 5, 11)],
        'p["n"] >= 1 and p["k"] >= 1',
        '''    """score = positive monthly total returns in the last n completed months; eligible ROC(126) > 0;
    top k by (score, ROC(126), ticker); equal weight."""
    K = P["close"].shape[1]
    r126 = roc(P, 126)[i]
    cands = []
    for j in range(K):
        if not r126[j] > 0:
            continue
        mc = month_closes(P, j, i, int(p["n"]))
        if mc is None:
            continue
        score = int((mc[1:] / mc[:-1] - 1 > 0).sum())
        cands.append(((-score, -r126[j], j), j))
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "crypto_equal_weight_rebalance": (
        "Crypto equal-weight rebalance", CRYPTO, CRY, "2018-01-01", [],
        [], [], 'True',
        '''    """Fixed 25 % per coin of the four-coin basket (no trend filter). A coin not listed yet keeps
    its 25 % in cash (fixed component allocations, EXECUTION.md: no renormalizing)."""
    K = P["close"].shape[1]
    w = np.zeros(K)
    w[~np.isnan(P["close"][i])] = 1.0 / K
    return w
'''),
    "crypto_relative_momentum_basket": (
        "Crypto relative momentum basket", CRYPTO, CRY, "2018-01-01", [],
        ['"k": 2,      # holdings', '"n": 90,     # ROC lookback (daily bars)'],
        [k_space(1, 3, 4), '"n": {"min": 30, "max": 180, "step": 10, "hard_min": 5, "hard_max": 365},'],
        'p["n"] >= 2 and p["k"] >= 1',
        '''    """Top k by ROC(n), each with C > SMA(200) and ROC(n) > 0; equal weight."""
    K = P["close"].shape[1]
    c, s, r = P["close"][i], sma(P, 200)[i], roc(P, int(p["n"]))[i]
    cands = [((-r[j], j), j) for j in range(K) if c[j] > s[j] and r[j] > 0]
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "downside_risk_weighted_momentum": (
        "Downside-risk weighted momentum", GLOB, ETF, "2004-01-01", [],
        ['"k": 3,      # holdings', '"n": 126,    # ROC lookback and downside-deviation window (daily bars)'],
        [k_space(1, 5, 8), '"n": {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504},'],
        'p["n"] >= 2 and p["k"] >= 1',
        '''    """Top k positive ROC(n); weights proportional to 1/downside deviation over n returns,
    normalized to 100 % after dropping invalid / zero-risk values."""
    K = P["close"].shape[1]
    r, dd = roc(P, int(p["n"]))[i], downside_dev(P, int(p["n"]))[i]
    sel = top_k([((-r[j], j), j) for j in range(K) if r[j] > 0], int(p["k"]))
    sel = [j for j in sel if np.isfinite(dd[j]) and dd[j] > 0]
    w = np.zeros(K)
    if sel:
        inv = np.array([1 / dd[j] for j in sel])
        w[sel] = inv / inv.sum()
    return w
'''),
    "drawdown_defensive_switch": (
        "Drawdown defensive switch", ["IEF", "SPY"], ETF, "2004-01-01", [],
        ['"n": 252,    # trailing window of SPY\'s maximum close (daily bars)', '"dd": 10.0,  # drawdown threshold, percentage points'],
        ['"n": {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 756},',
         '"dd": {"min": 5.0, "max": 20.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0},'],
        'p["n"] >= 2 and p["dd"] > 0',
        '''    """SPY if its drawdown from HH(C, n) is better than -dd %; else IEF if IEF > SMA(200); else cash."""
    K = P["close"].shape[1]
    S, B = P["syms"].index("SPY"), P["syms"].index("IEF")
    c = P["close"][i]
    w = np.zeros(K)
    top = hh(P, int(p["n"]))[i, S]
    if not np.isfinite(top):
        return w
    if c[S] / top - 1 > -p["dd"] / 100:
        w[S] = 1.0
    elif c[B] > sma(P, 200)[i, B]:
        w[B] = 1.0
    return w
'''),
    "dual_momentum_allocation": (
        "Dual momentum allocation", ["EFA", "IEF", "SPY"], ETF, "2004-01-01", [],
        ['"n": 252,    # ROC lookback (daily bars)'],
        ['"n": {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 756},'],
        'p["n"] >= 2',
        '''    """Higher ROC(n) of SPY/EFA if it beats IEF's ROC(n); else IEF if its ROC(n) > 0; else cash."""
    K = P["close"].shape[1]
    r = roc(P, int(p["n"]))[i]
    S, F, B = P["syms"].index("SPY"), P["syms"].index("EFA"), P["syms"].index("IEF")
    w = np.zeros(K)
    risky = [j for j in (F, S) if np.isfinite(r[j])]          # ticker order breaks ties (EFA < SPY)
    if not risky or not np.isfinite(r[B]):
        return w
    best = max(risky, key=lambda j: (r[j], -j))
    if r[best] > r[B]:
        w[best] = 1.0
    elif r[B] > 0:
        w[B] = 1.0
    return w
'''),
    "equal_risk_contribution_trend": (
        "Equal risk contribution trend", GLOB, ETF, "2004-01-01", [],
        ['"n": 126,    # covariance window (daily returns)'],
        ['"n": {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504},'],
        'p["n"] >= 10',
        '''    """Assets with C > SMA(200); long-only equal-risk-contribution weights from the n-day sample
    covariance (regularized). Solver failure / no covariance -> cash."""
    K = P["close"].shape[1]
    c, s = P["close"][i], sma(P, 200)[i]
    elig = [j for j in range(K) if c[j] > s[j]]
    w = np.zeros(K)
    if not elig:
        return w
    C = cov_window(P, i, elig, int(p["n"]))
    x = erc(C) if C is not None else None
    if x is not None:
        w[elig] = x
    return w
'''),
    "high_proximity_leader_rotation": (
        "High-proximity leader rotation", SECT, ETF, "2000-07-01", [],
        ['"n": 252,    # HH(C, n) window (daily bars)', '"k": 3,      # holdings'],
        ['"n": {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 380},', k_space(1, 5, 11)],
        'p["n"] >= 2 and p["k"] >= 1',
        '''    """score = C / HH(C, n); top k among C > SMA(200); equal weight."""
    K = P["close"].shape[1]
    c, s, top = P["close"][i], sma(P, 200)[i], hh(P, int(p["n"]))[i]
    cands = [((-(c[j] / top[j]), j), j) for j in range(K) if c[j] > s[j] and top[j] > 0]
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "inverse_volatility_trend_basket": (
        "Inverse-volatility trend basket", GLOB, ETF, "2004-01-01", [],
        ['"n": 200,    # SMA length of the trend filter (daily bars)'],
        ['"n": {"min": 100, "max": 300, "step": 10, "hard_min": 20, "hard_max": 500},'],
        'p["n"] >= 2',
        '''    """All assets with C > SMA(n); weights proportional to 1/Std(daily returns, 63), normalized."""
    K = P["close"].shape[1]
    c, s, v = P["close"][i], sma(P, int(p["n"]))[i], vol(P, 63)[i]
    elig = [j for j in range(K) if c[j] > s[j] and np.isfinite(v[j]) and v[j] > 0]
    w = np.zeros(K)
    if elig:
        inv = np.array([1 / v[j] for j in elig])
        w[elig] = inv / inv.sum()
    return w
'''),
    "low_correlation_momentum_selection": (
        "Low-correlation momentum selection", GLOB, ETF, "2004-01-01", [],
        ['"k": 3,      # holdings', '"corr": 0.6, # maximum admitted pairwise correlation (126 daily returns)'],
        [k_space(2, 5, 8), '"corr": {"min": 0.3, "max": 0.9, "step": 0.05, "hard_min": 0.0, "hard_max": 1.0},'],
        'p["k"] >= 1 and 0 < p["corr"] <= 1',
        '''    """Positive ROC(126) assets sorted descending; greedily admit up to k, each only if its 126-day
    daily-return correlation with every already selected asset is < corr (undefined correlations
    are skipped, INDICATORS.md); equal weight."""
    K = P["close"].shape[1]
    r = roc(P, 126)[i]
    R = rets(P)[max(0, i - 125): i + 1]
    sel: list = []
    for _, j in sorted(((-r[j], j), j) for j in range(K) if r[j] > 0):
        if len(sel) >= int(p["k"]):
            break
        ok = True
        for q in sel:
            m = ~np.isnan(R[:, j]) & ~np.isnan(R[:, q])
            if m.sum() < 3:
                continue
            a, b = R[m, j], R[m, q]
            if a.std() == 0 or b.std() == 0:
                continue
            if np.corrcoef(a, b)[0, 1] >= p["corr"]:
                ok = False
                break
        if ok:
            sel.append(j)
    return equal(K, sel)
'''),
    "minimum_variance_trend_basket": (
        "Minimum-variance trend basket", GLOB, ETF, "2004-01-01", [],
        ['"n": 126,    # covariance window (daily returns)'],
        ['"n": {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504},'],
        'p["n"] >= 10',
        '''    """Assets with C > SMA(200); long-only minimum-variance weights (sum 1) from the n-day sample
    covariance (regularized). Solver failure / no covariance -> cash."""
    K = P["close"].shape[1]
    c, s = P["close"][i], sma(P, 200)[i]
    elig = [j for j in range(K) if c[j] > s[j]]
    w = np.zeros(K)
    if not elig:
        return w
    C = cov_window(P, i, elig, int(p["n"]))
    x = min_variance(C) if C is not None else None
    if x is not None:
        w[elig] = x
    return w
'''),
    "monthly_loser_rebound_basket": (
        "Monthly loser rebound basket", SECT, ETF, "2000-07-01", [],
        ['"k": 3,      # holdings'],
        [k_space(1, 5, 11)],
        'p["k"] >= 1',
        '''    """The k lowest ROC(21) sectors among those with C > SMA(200); equal weight."""
    K = P["close"].shape[1]
    c, s, r = P["close"][i], sma(P, 200)[i], roc(P, 21)[i]
    cands = [((r[j], j), j) for j in range(K) if c[j] > s[j] and np.isfinite(r[j])]
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "multi_horizon_rank_rotation": (
        "Multi-horizon rank rotation", GLOB, ETF, "2004-01-01", [],
        ['"k": 3,      # holdings'],
        [k_space(1, 5, 8)],
        'p["k"] >= 1',
        '''    """score = mean cross-sectional percentile rank of ROC(21/63/126/252) among assets with all four
    defined; top k with C > SMA(200); equal weight."""
    K = P["close"].shape[1]
    R = np.column_stack([roc(P, n)[i] for n in (21, 63, 126, 252)])
    ok = np.isfinite(R).all(axis=1)
    cols = np.flatnonzero(ok)
    if cols.size == 0:
        return np.zeros(K)
    ranks = pd.DataFrame(R[cols]).rank(pct=True, method="average").to_numpy()
    score = dict(zip(cols.tolist(), ranks.mean(axis=1)))
    c, s = P["close"][i], sma(P, 200)[i]
    cands = [((-score[j], j), j) for j in score if c[j] > s[j]]
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "sector_roc_rotation": (
        "Sector ROC rotation", SECT, ETF, "2000-07-01", ["SPY"],
        ['"k": 3,      # holdings', '"n": 63,     # ROC lookback (daily bars)'],
        [k_space(1, 5, 11), '"n": {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 380},'],
        'p["k"] >= 1 and p["n"] >= 2',
        '''    """Top k sectors by ROC(n), only while SPY > SMA(200) (SPY is a reference, not traded); equal weight."""
    K = P["close"].shape[1]
    spy = ref_close(P, "SPY")
    if not spy[i] > sma(P, 200, spy)[i]:
        return np.zeros(K)
    r = roc(P, int(p["n"]))[i]
    cands = [((-r[j], j), j) for j in range(K) if np.isfinite(r[j])]
    return equal(K, top_k(cands, int(p["k"])))
'''),
    "single_etf_volatility_target": (
        "Single ETF volatility target", ["SPY"], ETF, "1994-01-01", [],
        ['"target": 0.1,  # target annual volatility (decimal)'],
        ['"target": {"min": 0.05, "max": 0.2, "step": 0.01, "hard_min": 0.01, "hard_max": 1.0},'],
        'p["target"] > 0',
        '''    """If SPY > SMA(200): weight = min(1, target / (Std(daily returns, 63) * sqrt(252))); rest cash."""
    v = vol(P, 63)[i, 0]
    w = np.zeros(1)
    if P["close"][i, 0] > sma(P, 200)[i, 0] and np.isfinite(v) and v > 0:
        w[0] = min(1.0, p["target"] / (v * np.sqrt(252)))
    return w
'''),
    "stock_bond_paired_switch": (
        "Stock-bond paired switch", ["SPY", "TLT"], ETF, "2004-01-01", [],
        ['"n": 126,    # ROC lookback (daily bars)'],
        ['"n": {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 504},'],
        'p["n"] >= 2',
        '''    """100 % in the higher ROC(n) of SPY/TLT if that ROC(n) > 0; else cash."""
    K = P["close"].shape[1]
    r = roc(P, int(p["n"]))[i]
    w = np.zeros(K)
    fin = [j for j in range(K) if np.isfinite(r[j])]
    if len(fin) == K:
        best = max(fin, key=lambda j: (r[j], -j))
        if r[best] > 0:
            w[best] = 1.0
    return w
'''),
    "trend_equal_weight_global": (
        "Trend equal-weight global", GLOB, ETF, "2004-01-01", [],
        ['"n": 200,    # SMA length of the trend filter (daily bars)'],
        ['"n": {"min": 100, "max": 300, "step": 10, "hard_min": 20, "hard_max": 500},'],
        'p["n"] >= 2',
        '''    """Every asset with C > SMA(n), equal weight; cash if none."""
    K = P["close"].shape[1]
    c, s = P["close"][i], sma(P, int(p["n"]))[i]
    return equal(K, [j for j in range(K) if c[j] > s[j]])
'''),
    "vol_adjusted_momentum_rotation": (
        "Volatility-adjusted momentum rotation", GLOB, ETF, "2004-01-01", [],
        ['"n": 126,    # ROC and volatility window (daily bars)', '"k": 3,      # holdings'],
        ['"n": {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504},', k_space(1, 5, 8)],
        'p["n"] >= 2 and p["k"] >= 1',
        '''    """score = ROC(n) / Std(daily returns, n) (decimal units, zero volatility skipped);
    top k positive scores; equal weight."""
    K = P["close"].shape[1]
    r, v = roc(P, int(p["n"]))[i], vol(P, int(p["n"]))[i]
    cands = [((-(r[j] / v[j]), j), j) for j in range(K) if np.isfinite(v[j]) and v[j] > 0 and r[j] / v[j] > 0]
    return equal(K, top_k(cands, int(p["k"])))
'''),
}

HEAD_DOC = '''"""{title}: month-end portfolio backtest adapted from the generic template.

Built by scripts/portfolio_lib/build.py (strategy block below + shared portfolio simulator
core.py + the template's generic machinery). The symbol list is ONE portfolio, not independent
per-symbol trades, so run() uses _simulate_portfolio instead of the template's per-symbol _simulate.

    docker compose run --rm -T backtest python strategies/{name}/backtest.py --period is [--trades]
    ... --period oos | all | live    --params '{{"stop_loss_pct": 12}}'

Rules (EXECUTION.md "Sizing and portfolio sleeves", see strategy.md):
- Decide at the close of the last bar of each complete month; fill at the next bar's open.
- Sells/trims first, then buys to target; buys scaled down if cash is short. Rest is cash (0 %).
- Each holding: hard stop stop_loss_pct below its cost basis (gap -> open, else intrabar at the
  stop; never loosened on additions), time exit after max_candles held bars at the next open.
  A stopped holding can only come back at a later month-end decision.
- Fees CONFIG["fee_pct"] per side on traded value, slippage CONFIG["slippage_pct"] against every fill.
- A trade = one holding from first buy to full exit; partial trims don't close it.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name != "strategies" else Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

'''


def block(name: str) -> str:
    title, syms, mk, start, ref, params, space, valid, body = SPECS[name]
    lines = [
        "# --------------------------------------------------------------------------",
        "# Strategy definition: adapt everything in this block in the copy.",
        "# --------------------------------------------------------------------------",
        "CONFIG = {",
        f'    "name": "{name}",',
        f'    "asset_class": "{mk["asset_class"]}",' + ("            # Binance 1m -> UTC daily bars" if mk["asset_class"] == "crypto" else "               # Yahoo daily, dividend/split adjusted (= total return)"),
        f'    "symbols": {syms!r},'.replace("'", '"'),
    ]
    if ref:
        lines.append(f'    "reference": {ref!r},'.replace("'", '"') + "   # signal-only series, never traded")
    lines += [
        '    "timeframe": "1d",               # daily bars for fills and stop monitoring; decisions at month-end',
        f'    "start": "{start}",           # first simulated bar; members join once listed and warmed up',
        f'    "oos_start": "{mk["oos"]}",',
        '    "end": "2026-11-23",             # frozen at setup (last complete daily bar)',
        '    "capital": 10_000.0,',
        '    "position_pct": 1.0,             # whole sleeve, split by target_weights()',
        f'    "fee_pct": {mk["fee"]:.2f},                # {mk["fee_note"]}',
        f'    "slippage_pct": {mk["slip"]:.2f},           # {mk["slip_note"]}',
        '    "big_loss_pct": 2.0,',
        '    "big_loss_mult": 2.0,',
        '    "warmup_bars": 0,                # not used: a member is eligible once its indicators exist',
        "}",
        "",
        "PARAMS = {",
        *[f"    {x}" for x in params],
        f"    {SLP}",
        f"    {MCP}",
        "}",
        "",
        "SPACE = {",
        *[f"    {x}" for x in space],
        f"    {SL}",
        f"    {MC}",
        "}",
        "",
        "",
        "def valid(p: dict) -> bool:",
        f'    return ({valid}) and p["stop_loss_pct"] > 0 and p["max_candles"] >= 1',
        "",
        "",
        "def target_weights(P: dict, i: int, p: dict) -> np.ndarray:",
        body.rstrip("\n"),
        "",
    ]
    return "\n".join(lines) + "\n"


def build(name: str) -> Path:
    title = SPECS[name][0]
    text = (HEAD_DOC.format(title=title, name=name) + block(name)
            + (HERE / "core.py").read_text() + "\n" + (HERE / "tail.py").read_text())
    out = ROOT / "strategies" / name / "backtest.py"
    out.write_text(text)
    return out


if __name__ == "__main__":
    for n in sys.argv[1:] or SPECS:
        print(build(n).relative_to(ROOT))
