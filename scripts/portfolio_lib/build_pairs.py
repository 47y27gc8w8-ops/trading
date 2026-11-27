#!/usr/bin/env python3
"""Build self-contained strategies/<name>/backtest.py files for the library's PAIR specs (long A / short B).

Each file = header + this spec's block (CONFIG, PARAMS, SPACE, valid, signals) + the panel/indicator
half of core.py + pair_core.py (pair simulator, run()) + tail.py without its portfolio run().

    python3 scripts/portfolio_lib/build_pairs.py [name ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

ROOT = build.ROOT
ETF = {**build.ETF, "borrow": 0.25,
       "borrow_note": "ASSUMED (user decision 2026-11-27): easy-to-borrow large caps/ETFs; stress runs 1 % and 3 %"}
CRY = {**build.CRY, "borrow": 3.0,
       "borrow_note": "ASSUMED: crypto margin borrow of the short coin; stress runs 6 % and 10 %"}

COMMON_P = ['"pair_stop_pct": 5.0,   # close-based pair loss, % of entry gross notional',
            '"leg_stop_pct": 8.0,    # per-leg hard stop, % adverse from that leg\'s entry fill',
            '"max_candles": 40,      # held daily bars (entry bar = 1), exit at the next open']
COMMON_S = ['"pair_stop_pct": {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0},',
            '"leg_stop_pct": {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0},',
            '"max_candles": {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252},']

# name -> (title, symbols [A, B, ...], market, start, params, space, valid, body)
SPECS = {
    "ratio_zscore_pairs": (
        "Ratio z-score pairs", ["KO", "PEP"], ETF, "2000-01-01",
        ['"n": 60,     # prior window of the log-ratio mean/std', '"z": 2.0,    # entry deviation (std units)'],
        ['"n": {"min": 20, "max": 120, "step": 10, "hard_min": 5, "hard_max": 504},',
         '"z": {"min": 1.0, "max": 3.0, "step": 0.25, "hard_min": 0.25, "hard_max": 3.75},'],
        'p["n"] >= 5 and 0 < p["z"] < 4',
        '''    """R = log(A/B); Z = (R - mean(R, n)[1]) / std(R, n)[1]; entry Z < -z and 126-day return
    correlation > 0.6; exit Z >= 0 or Z <= -4; equal dollars."""
    C = P["close"]
    R = np.log(C[:, 0] / C[:, 1])
    m, s = prior_stats(R, int(p["n"]))
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = np.where(s > 0, (R - m) / s, np.nan)
    cr = corr_ab(P, 0, 1, 126)
    return {"entry": (Z < -p["z"]) & (cr > 0.6), "exit": (Z >= 0) | (Z <= -4), "ratio": np.ones(len(R))}
'''),
    "cointegration_gated_residual": (
        "Cointegration-gated residual", ["GLD", "IAU"], ETF, "2007-01-01",
        ['"n": 252,    # formation window (daily bars before the month-end)', '"p": 0.05,   # maximum Engle-Granger p-value'],
        ['"n": {"min": 126, "max": 504, "step": 21, "hard_min": 42, "hard_max": 756},',
         '"p": {"min": 0.01, "max": 0.1, "step": 0.01, "hard_min": 0.001, "hard_max": 0.5},'],
        'p["n"] >= 30 and 0 < p["p"] < 1',
        '''    """At each month-end t fit log(A) = alpha + beta log(B) on t-n..t-1; if beta > 0 and the
    Engle-Granger p-value < p, freeze alpha, beta and the residual mean/std for bars t .. next month-end - 1.
    Frozen residual z < -2 -> long A / short B with dollar ratio 1:beta; exit z >= 0 or z <= -4;
    positions are closed at the next month-end (force) before refitting."""
    C = P["close"]
    la, lb = np.log(C[:, 0]), np.log(C[:, 1])
    N = len(la)
    n = int(p["n"])
    Z = np.full(N, np.nan)
    beta = np.full(N, np.nan)
    me = np.flatnonzero(P["month_end"])
    for k, t in enumerate(me):
        if t - n < 0:
            continue
        y, x = la[t - n:t], lb[t - n:t]
        if not (np.isfinite(y).all() and np.isfinite(x).all()):
            continue
        pv, a, b = coint_pvalue(y, x)
        if not (b > 0 and pv < p["p"]):
            continue
        e = y - a - b * x
        mu, sd = e.mean(), e.std()
        if sd <= 0:
            continue
        end = me[k + 1] if k + 1 < len(me) else N
        Z[t:end] = (la[t:end] - a - b * lb[t:end] - mu) / sd
        beta[t:end] = b
    force = P["month_end"].copy()
    return {"entry": Z < -2, "exit": (Z >= 0) | (Z <= -4), "ratio": beta, "force": force}
'''),
    "half_life_filtered_pairs": (
        "Half-life filtered pairs", ["EWA", "EWC"], ETF, "1998-01-01",
        ['"n": 120,    # prior window for the AR(1) fit and the z-score', '"half": 30,  # maximum AR(1) half-life (daily bars)'],
        ['"n": {"min": 60, "max": 250, "step": 10, "hard_min": 20, "hard_max": 504},',
         '"half": {"min": 10, "max": 60, "step": 5, "hard_min": 3, "hard_max": 252},'],
        'p["n"] >= 20 and p["half"] >= 2',
        '''    """R = log(A/B). On t-n..t-1 fit dR = a + b R_lag (OLS); require -1 < b < 0 and
    half-life log(0.5)/log(1+b) in [2, half]. Entry prior-window z(R) < -2; exit z >= 0 or z <= -4; equal dollars."""
    C = P["close"]
    R = np.log(C[:, 0] / C[:, 1])
    n = int(p["n"])
    dR = np.r_[np.nan, np.diff(R)]
    Rlag = np.r_[np.nan, R[:-1]]
    _, b, _ = rolling_ols_prior(dR, Rlag, n)
    with np.errstate(invalid="ignore", divide="ignore"):
        hl = np.where((b > -1) & (b < 0), np.log(0.5) / np.log1p(b), np.nan)
        m, s = prior_stats(R, n)
        Z = np.where(s > 0, (R - m) / s, np.nan)
    ok = (hl >= 2) & (hl <= p["half"])
    return {"entry": ok & (Z < -2), "exit": (Z >= 0) | (Z <= -4), "ratio": np.ones(len(R))}
'''),
    "normalized_distance_pairs": (
        "Normalized distance pairs", ["CL", "KO", "PEP", "PG"], ETF, "2000-01-01",
        ['"formation": 252,  # formation window (daily bars before the six-month boundary)', '"z": 2.0,    # entry deviation (std units)'],
        ['"formation": {"min": 126, "max": 300, "step": 21, "hard_min": 42, "hard_max": 504},',
         '"z": {"min": 1.0, "max": 3.0, "step": 0.25, "hard_min": 0.25, "hard_max": 3.75},'],
        'p["formation"] >= 20 and 0 < p["z"] < 4',
        '''    """At each six-month boundary t (last bar of June / December): on t-f..t-1, normalize every
    candidate's total-return close to 1 at the formation start and pick the pair (alphabetically first
    ticker = A) with the lowest summed squared distance; freeze bases and the spread's mean/std.
    During t+1 .. next boundary: z = (A/baseA - B/baseB - mean) / std; entry z < -z, exit z >= 0 or
    z <= -4; forced exit at the next boundary (end of the trading period). Equal dollars."""
    C = P["close"]
    N, K = C.shape
    f = int(p["formation"])
    months = np.asarray(P["idx"].month)
    bnd = np.flatnonzero(P["month_end"] & np.isin(months, (6, 12)))
    Z = np.full(N, np.nan)
    A = np.full(N, -1)
    B = np.full(N, -1)
    force = np.zeros(N, bool)
    for k, t in enumerate(bnd):
        end = bnd[k + 1] if k + 1 < len(bnd) else N - 1
        force[end] = True
        if t - f < 0:
            continue
        W = C[t - f:t]
        best = None
        for i in range(K):
            for j in range(i + 1, K):
                if not (np.isfinite(W[:, i]).all() and np.isfinite(W[:, j]).all()):
                    continue
                ssd = float((((W[:, i] / W[0, i]) - (W[:, j] / W[0, j])) ** 2).sum())
                if best is None or ssd < best[0]:
                    best = (ssd, i, j)
        if best is None:
            continue
        _, i, j = best
        sp = W[:, i] / W[0, i] - W[:, j] / W[0, j]
        mu, sd = sp.mean(), sp.std()
        if sd <= 0:
            continue
        sl = slice(t + 1, end + 1)
        Z[sl] = (C[sl, i] / W[0, i] - C[sl, j] / W[0, j] - mu) / sd
        A[sl], B[sl] = i, j
    return {"entry": Z < -p["z"], "exit": (Z >= 0) | (Z <= -4), "ratio": np.ones(N), "force": force, "a": A, "b": B}
'''),
    "ols_residual_pairs": (
        "OLS residual pairs", ["XLE", "VDE"], ETF, "2006-01-01",
        ['"n": 120,    # prior OLS window (daily bars, excludes t)', '"z": 2.0,    # entry deviation (residual std units)'],
        ['"n": {"min": 60, "max": 250, "step": 10, "hard_min": 20, "hard_max": 504},',
         '"z": {"min": 1.0, "max": 3.0, "step": 0.25, "hard_min": 0.25, "hard_max": 3.75},'],
        'p["n"] >= 20 and 0 < p["z"] < 4',
        '''    """Daily refit of log(A) = alpha + beta log(B) on t-n..t-1; residual z = (log A - alpha - beta log B)
    / formation residual std. Entry beta > 0 and z < -z (dollar ratio 1:beta, frozen at entry);
    exit refitted z >= 0 or z <= -4."""
    C = P["close"]
    la, lb = np.log(C[:, 0]), np.log(C[:, 1])
    a, b, s = rolling_ols_prior(la, lb, int(p["n"]))
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = np.where(s > 0, (la - a - b * lb) / s, np.nan)
    return {"entry": (b > 0) & (Z < -p["z"]), "exit": (Z >= 0) | (Z <= -4), "ratio": np.where(b > 0, b, np.nan)}
'''),
    "ratio_rsi_recovery": (
        "Ratio RSI recovery", ["ETHUSDT", "BTCUSDT"], CRY, "2018-01-01",
        ['"n": 14,     # RSI length on the price ratio', '"level": 30, # RSI level crossed upward to enter'],
        ['"n": {"min": 7, "max": 28, "step": 1, "hard_min": 2, "hard_max": 50},',
         '"level": {"min": 20, "max": 40, "step": 1, "hard_min": 16, "hard_max": 59},'],
        'p["n"] >= 2 and 15 < p["level"] < 60',
        '''    """R = C_A / C_B; entry RSI(R, n) crosses above level (prev <= level < now) and 126-day return
    correlation > 0.6; exit RSI > 60 or RSI < 15; equal dollars."""
    C = P["close"]
    rsi = wilder_rsi(C[:, 0] / C[:, 1], int(p["n"]))
    prev = np.r_[np.nan, rsi[:-1]]
    cr = corr_ab(P, 0, 1, 126)
    return {"entry": (rsi > p["level"]) & (prev <= p["level"]) & (cr > 0.6),
            "exit": (rsi > 60) | (rsi < 15), "ratio": np.ones(len(rsi))}
'''),
    "relative_momentum_spread_breakout": (
        "Relative momentum spread breakout", ["SPY", "EFA"], ETF, "2002-03-01",
        ['"n": 63,     # entry channel: R above its prior n-bar high', '"exit_n": 21, # exit channel: R below its prior exit_n-bar low'],
        ['"n": {"min": 21, "max": 126, "step": 7, "hard_min": 5, "hard_max": 252},',
         '"exit_n": {"min": 5, "max": 40, "step": 2, "hard_min": 2, "hard_max": 125},'],
        '2 <= p["exit_n"] < p["n"]',
        '''    """R = log(A/B); entry R > HH(R, n)[1]; exit R < LL(R, exit_n)[1]; equal dollars."""
    C = P["close"]
    R = pd.Series(np.log(C[:, 0] / C[:, 1]))
    hi = R.rolling(int(p["n"]), min_periods=int(p["n"])).max().shift(1).to_numpy(float)
    lo = R.rolling(int(p["exit_n"]), min_periods=int(p["exit_n"])).min().shift(1).to_numpy(float)
    r = R.to_numpy(float)
    return {"entry": r > hi, "exit": r < lo, "ratio": np.ones(len(r))}
'''),
    "short_horizon_return_spread": (
        "Short-horizon return spread", ["XLK", "QQQ"], ETF, "2000-01-01",
        ['"n": 5,      # ROC lookback (daily bars)', '"gap": 3.0,  # entry threshold, percentage points'],
        ['"n": {"min": 2, "max": 10, "step": 1, "hard_min": 1, "hard_max": 21},',
         '"gap": {"min": 1.0, "max": 8.0, "step": 0.5, "hard_min": 0.25, "hard_max": 15.0},'],
        'p["n"] >= 1 and p["gap"] > 0',
        '''    """D = ROC_A(n) - ROC_B(n) in percentage points; entry D < -gap and 126-day return correlation > 0.7;
    exit D >= 0 or D < -2 x gap; equal dollars."""
    r = roc(P, int(p["n"]))
    D = (r[:, 0] - r[:, 1]) * 100
    cr = corr_ab(P, 0, 1, 126)
    return {"entry": (D < -p["gap"]) & (cr > 0.7), "exit": (D >= 0) | (D < -2 * p["gap"]), "ratio": np.ones(len(D))}
'''),
}

HEAD_DOC = '''"""{title}: long-A / short-B pair backtest adapted from the generic template.

Built by scripts/portfolio_lib/build_pairs.py (strategy block below + shared panel/indicators from
core.py + pair simulator pair_core.py + the template's generic machinery). CONFIG["symbols"] is ONE
pair strategy (A first), not independent per-symbol trades.

    docker compose run --rm -T backtest python strategies/{name}/backtest.py --period is [--trades]

BORROW COST IS ASSUMED, NOT HISTORICAL: CONFIG["borrow_fee_pct_yr"] (see strategy.md). The spec says
to disable pairs without historical borrow/carry data; the user chose to run them with this labelled
assumption instead (2026-11-27).
"""
'''


def block(name: str) -> str:
    title, syms, mk, start, params, space, valid, body = SPECS[name]
    lines = [
        "# --------------------------------------------------------------------------",
        "# Strategy definition: adapt everything in this block in the copy.",
        "# --------------------------------------------------------------------------",
        "CONFIG = {",
        f'    "name": "{name}",',
        f'    "asset_class": "{mk["asset_class"]}",',
        f'    "symbols": {syms!r},'.replace("'", '"') + "   # A first, then B" + (" (candidates)" if len(syms) > 2 else ""),
        '    "timeframe": "1d",',
        f'    "start": "{start}",',
        f'    "oos_start": "{mk["oos"]}",',
        '    "end": "2026-11-23",             # frozen at setup (last complete daily bar)',
        '    "capital": 10_000.0,',
        '    "position_pct": 1.0,             # gross pair notional = 100 % of sleeve equity',
        f'    "fee_pct": {mk["fee"]:.2f},                # {mk["fee_note"]}',
        f'    "slippage_pct": {mk["slip"]:.2f},           # {mk["slip_note"]}',
        f'    "borrow_fee_pct_yr": {mk["borrow"]},       # {mk["borrow_note"]}',
        '    "big_loss_pct": 2.0,',
        '    "big_loss_mult": 2.0,',
        '    "warmup_bars": 0,',
        "}",
        "",
        "PARAMS = {",
        *[f"    {x}" for x in params + COMMON_P],
        "}",
        "",
        "SPACE = {",
        *[f"    {x}" for x in space + COMMON_S],
        "}",
        "",
        "",
        "def valid(p: dict) -> bool:",
        f'    return ({valid}) and p["pair_stop_pct"] > 0 and p["leg_stop_pct"] > 0 and p["max_candles"] >= 1',
        "",
        "",
        "def signals(P: dict, p: dict) -> dict:",
        body.rstrip("\n"),
        "",
    ]
    return "\n".join(lines) + "\n"


def build_one(name: str) -> Path:
    title = SPECS[name][0]
    core = (HERE / "core.py").read_text()
    panel_part = core.split("\ndef _simulate_portfolio")[0].replace(
        "# Portfolio machinery (shared by the library's month-end allocation specs).",
        "# Panel and indicators (shared with the library's portfolio specs).").replace(
        "# Built from scripts/portfolio_lib/core.py; generalizes breadth_scaled_sector_allocation's\n"
        "# _simulate_portfolio: target_weights() above decides, everything below executes.",
        "# Built from the first half of scripts/portfolio_lib/core.py.")
    tail = (HERE / "tail.py").read_text()
    tail = re.sub(r"\ndef run\(.*?(?=\n\n\ndef metrics)", "", tail, flags=re.S)
    text = (HEAD_DOC.format(title=title, name=name) + build.HEAD_DOC.split('"""', 2)[2].lstrip("\n")
            + block(name) + panel_part.rstrip() + "\n\n" + (HERE / "pair_core.py").read_text() + "\n" + tail)
    out = ROOT / "strategies" / name / "backtest.py"
    out.write_text(text)
    return out


if __name__ == "__main__":
    for n in sys.argv[1:] or SPECS:
        print(build_one(n).relative_to(ROOT))
