#!/usr/bin/env python3
"""Build self-contained strategies/<name>/backtest.py files for the library's US 5-minute specs.

Each file = header + this spec's block (CONFIG, PARAMS, SPACE, valid, signals) + intraday_core.py
(5-minute session features, single-position simulator, run()) + tail.py without its portfolio run().

    python3 scripts/portfolio_lib/build_intraday.py [name ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

ROOT = build.ROOT
COMMON_P = ['"stop_atr": 2.0,         # initial stop, x ATR(14) of the signal bar below the fill',
            '"take_profit_atr": 3.0,  # resting target, x the same ATR above the fill',
            '"max_candles": 24,       # held 5-minute bars (entry bar = 1), exit at the next open']
COMMON_S = ['"stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25, "hard_max": 10.0},',
            '"take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.25, "hard_min": 0.25, "hard_max": 15.0},',
            '"max_candles": {"min": 12, "max": 48, "step": 2, "hard_min": 2, "hard_max": 78},']

# name -> (title, symbol, max entries per session (0 = no limit), params, space, valid, body)
SPECS = {
    "afternoon_momentum_continuation": (
        "Afternoon momentum continuation", "QQQ", 0,
        ['"roc": 0.7,   # minimum return since the 09:30 open, percentage points'],
        ['"roc": {"min": 0.3, "max": 1.5, "step": 0.1, "hard_min": 0.0, "hard_max": 5.0},'],
        'p["roc"] >= 0',
        '''    """Bar closing 14:00-15:00: C / session open - 1 > roc %, C > first-hour high (frozen at 10:30),
    C crosses above HH(H, 6)[1] (prior 6 bars, same session). Exit C < EMA(20)."""
    c = F["c"]
    fh, _ = range_frozen(F, 570, 630)
    hh6 = np.array(pd.Series(F["h"]).rolling(6, min_periods=6).max().shift(1), dtype=float)
    hh6[~same_prev(F, 6)] = np.nan
    with np.errstate(invalid="ignore"):
        e = in_window(F, "14:00", "15:00") & (c / F["sess_open"] - 1 > p["roc"] / 100) & (c > fh) & cross_above(F, c, hh6)
        x = c < ema(F, 20)
    return {"entry": e, "exit": x}
'''),
    "full_gap_up_continuation": (
        "Full gap-up continuation", "MSFT", 1,
        ['"gap": 0.5,   # session open above prior-session high by more than gap %'],
        ['"gap": {"min": 0.1, "max": 2.0, "step": 0.1, "hard_min": 0.0, "hard_max": 10.0},'],
        'p["gap"] >= 0',
        '''    """Session open > prior-session high x (1 + gap/100); bar closing 10:00-12:00: C crosses above the
    first-30-minute high and C > VWAP. Exit C < first-30-minute low. One entry per session."""
    c = F["c"]
    orh, orl = range_frozen(F, 570, 600)
    with np.errstate(invalid="ignore"):
        e = (F["sess_open"] > F["prev_h"] * (1 + p["gap"] / 100)) & in_window(F, "10:00", "12:00") \\
            & cross_above(F, c, orh) & (c > F["vwap"])
        x = c < orl
    return {"entry": e, "exit": x}
'''),
    "gap_down_reversal_strength": (
        "Gap-down reversal strength", "QQQ", 0,
        [], [], 'True',
        '''    """Session open < prior-session low; bar closing 10:00-12:00: C crosses above the prior-session low
    and C > VWAP. Exit C >= prior-session midpoint."""
    c = F["c"]
    pl = F["prev_l"]
    with np.errstate(invalid="ignore"):
        e = (F["sess_open"] < pl) & in_window(F, "10:00", "12:00") & cross_above(F, c, pl) & (c > F["vwap"])
        x = c >= (F["prev_h"] + pl) / 2
    return {"entry": e, "exit": x}
'''),
    "intraday_lunch_compression_break": (
        "Intraday lunch compression break", "SPY", 1,
        ['"k": 3.0,     # lunch range width must be < k x ATR(14) at 13:00'],
        ['"k": {"min": 1.5, "max": 5.0, "step": 0.25, "hard_min": 0.25, "hard_max": 20.0},'],
        'p["k"] > 0',
        '''    """Lunch range = bars 11:30-13:00, frozen with ATR(14) at the bar closing 13:00; width < k x that ATR.
    Bar closing after 13:00 up to 15:00: C crosses above the lunch high and C > VWAP.
    Exit C < lunch-range midpoint. One entry per session."""
    c = F["c"]
    lh, ll = range_frozen(F, 690, 780)
    atr13 = pd.Series(np.where(F["close_min"] == 780, F["atr"], np.nan)).groupby(F["sid"]).transform("max").to_numpy()
    with np.errstate(invalid="ignore"):
        ok = (lh - ll) < p["k"] * atr13
        e = ok & in_window(F, "13:05", "15:00") & cross_above(F, c, lh) & (c > F["vwap"])
        x = c < (lh + ll) / 2
    return {"entry": e, "exit": x}
'''),
    "opening_range_breakout": (
        "Opening range breakout", "SPY", 1,
        ['"minutes": 15,  # opening-range length (regular-session minutes)'],
        ['"minutes": {"min": 5, "max": 60, "step": 5, "hard_min": 5, "hard_max": 120},'],
        'p["minutes"] >= 5 and int(p["minutes"]) % 5 == 0',
        '''    """Opening range = first `minutes` from 09:30, frozen when complete. Bar closing 10:30-15:00:
    C crosses above the range high and C > VWAP. Exit C < range midpoint. One entry per session."""
    c = F["c"]
    orh, orl = range_frozen(F, 570, 570 + int(p["minutes"]))
    with np.errstate(invalid="ignore"):
        e = in_window(F, "10:30", "15:00") & cross_above(F, c, orh) & (c > F["vwap"])
        x = c < (orh + orl) / 2
    return {"entry": e, "exit": x}
'''),
    "opening_range_failed_breakdown": (
        "Opening range failed breakdown", "IWM", 1,
        ['"minutes": 30,  # opening-range length (regular-session minutes)'],
        ['"minutes": {"min": 5, "max": 60, "step": 5, "hard_min": 5, "hard_max": 120},'],
        'p["minutes"] >= 5 and int(p["minutes"]) % 5 == 0',
        '''    """Opening range = first `minutes` from 09:30, frozen when complete. Bar closing 10:30-15:00:
    L < range low, C > range low and C > O. Exit C >= range midpoint. One entry per session."""
    c = F["c"]
    orh, orl = range_frozen(F, 570, 570 + int(p["minutes"]))
    with np.errstate(invalid="ignore"):
        e = in_window(F, "10:30", "15:00") & (F["l"] < orl) & (c > orl) & (c > F["o"])
        x = c >= (orh + orl) / 2
    return {"entry": e, "exit": x}
'''),
    "partial_gap_down_fill": (
        "Partial gap-down fill", "SPY", 1,
        ['"gap": 1.0,   # largest accepted gap below the prior close, % (smallest fixed at 0.2 %)'],
        ['"gap": {"min": 0.5, "max": 2.0, "step": 0.1, "hard_min": 0.3, "hard_max": 5.0},'],
        'p["gap"] > 0.2',
        '''    """Session open below the prior close by 0.2 %-gap % and above the prior-session low; bar closing
    10:00-12:00: C crosses above the first-30-minute high. Exit C >= prior-session close. One entry per session."""
    c = F["c"]
    so, pc = F["sess_open"], F["prev_c"]
    orh, _ = range_frozen(F, 570, 600)
    with np.errstate(invalid="ignore"):
        g = so / pc - 1
        e = (g <= -0.002) & (g >= -p["gap"] / 100) & (so > F["prev_l"]) & in_window(F, "10:00", "12:00") & cross_above(F, c, orh)
        x = c >= pc
    return {"entry": e, "exit": x}
'''),
    "previous_day_high_intraday_break": (
        "Previous-day high intraday break", "AAPL", 0,
        ['"rvol": 1.5,  # volume multiple of the same-slot median of the 20 preceding sessions'],
        ['"rvol": {"min": 1.0, "max": 3.0, "step": 0.1, "hard_min": 0.5, "hard_max": 10.0},'],
        'p["rvol"] > 0',
        '''    """Bar closing 10:30-15:00: C crosses above the prior-session high and V > rvol x median same-slot
    volume of the 20 preceding sessions. Exit C < VWAP."""
    c = F["c"]
    with np.errstate(invalid="ignore"):
        e = in_window(F, "10:30", "15:00") & cross_above(F, c, F["prev_h"]) & (F["v"] > p["rvol"] * F["slot_med_vol"])
        x = c < F["vwap"]
    return {"entry": e, "exit": x}
'''),
    "session_vwap_deviation_reversion": (
        "Session VWAP deviation reversion", "SPY", 0,
        ['"k": 2.0,     # entry when (C - VWAP) / ATR(14) < -k'],
        ['"k": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25, "hard_max": 10.0},'],
        'p["k"] > 0',
        '''    """Bar closing 10:30-15:00: (C - VWAP) / ATR(14) < -k and ADX(14) < 20. Exit C >= VWAP."""
    c = F["c"]
    with np.errstate(invalid="ignore", divide="ignore"):
        z = np.where(F["atr"] > 0, (c - F["vwap"]) / F["atr"], np.nan)
        e = in_window(F, "10:30", "15:00") & (z < -p["k"]) & (F["adx"] < 20)
        x = c >= F["vwap"]
    return {"entry": e, "exit": x}
'''),
    "session_vwap_reclaim": (
        "Session VWAP reclaim", "AAPL", 0,
        ['"n": 20,      # EMA length for the slope filter EMA(n) > EMA(n)[3]'],
        ['"n": {"min": 10, "max": 50, "step": 5, "hard_min": 2, "hard_max": 200},'],
        'p["n"] >= 2',
        '''    """Bar closing 10:30-15:00: C crosses above VWAP and EMA(n) > EMA(n)[3]. Exit C < VWAP."""
    c, vw = F["c"], F["vwap"]
    em = ema(F, int(p["n"]))
    with np.errstate(invalid="ignore"):
        e = in_window(F, "10:30", "15:00") & cross_above(F, c, vw) & (em > lag(em, 3))
        x = c < vw
    return {"entry": e, "exit": x}
'''),
    "session_vwap_trend_pullback": (
        "Session VWAP trend pullback", "NVDA", 0,
        [], [], 'True',
        '''    """Bar closing 10:30-15:00: VWAP > VWAP[3] (same session), L <= VWAP, C > VWAP and C > H[1]
    (same session). Exit C < VWAP."""
    c, vw = F["c"], F["vwap"]
    with np.errstate(invalid="ignore"):
        e = in_window(F, "10:30", "15:00") & same_prev(F, 3) & (vw > lag(vw, 3)) & (F["l"] <= vw) & (c > vw) \\
            & same_prev(F) & (c > lag(F["h"]))
        x = c < vw
    return {"entry": e, "exit": x}
'''),
}

HEAD_DOC = '''"""{title}: US 5-minute single-position backtest adapted from the generic template.

Built by scripts/portfolio_lib/build_intraday.py (strategy block below + intraday_core.py: session
features, EXECUTION.md 5-minute execution rules, run() + the template's generic machinery).
Data: data/etf/5m/<SYMBOL>.parquet from Alpaca (scripts/fetch_alpaca_5m.py), regular session.

    docker compose run --rm -T backtest python strategies/{name}/backtest.py --period is [--trades]
"""
'''


def block(name: str) -> str:
    title, sym, max_e, params, space, valid, body = SPECS[name]
    lines = [
        "# --------------------------------------------------------------------------",
        "# Strategy definition: adapt everything in this block in the copy.",
        "# --------------------------------------------------------------------------",
        "CONFIG = {",
        f'    "name": "{name}",',
        '    "asset_class": "etf",            # Alpaca SIP 5-minute bars, split + dividend adjusted',
        f'    "symbols": ["{sym}"],',
        '    "timeframe": "5min",             # regular session 09:30-16:00 America/New_York',
        '    "start": "2016-03-01",           # Alpaca free history starts 2016; 2 months of warm-up',
        '    "oos_start": "2023-01-01",       # last ~4 years held out',
        '    "end": "2026-11-25",             # frozen at setup (last complete session)',
        '    "capital": 10_000.0,',
        '    "position_pct": 1.0,             # 100 % of equity per trade (user choice for risk_fraction specs)',
        '    "fee_pct": 0.05,                 # library convention for US stocks/ETFs (spec: 1 bp commission; more conservative)',
        '    "slippage_pct": 0.03,            # market/stop fills (spec: half-spread 2 bp + slippage 2 bp); target limits: none',
        f'    "max_entries_per_session": {max_e},   # {"spec: max one entry per session" if max_e else "0 = no limit (spec sets none)"}',
        '    "big_loss_pct": 2.0,',
        '    "big_loss_mult": 2.0,',
        '    "warmup_bars": 0,                # indicators carry their own warm-up (NaN until ready)',
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
        f'    return ({valid}) and p["stop_atr"] > 0 and p["take_profit_atr"] > 0 and p["max_candles"] >= 1',
        "",
        "",
        "def signals(F: dict, p: dict) -> dict:",
        body.rstrip("\n"),
        "",
    ]
    return "\n".join(lines) + "\n"


def build_one(name: str) -> Path:
    title = SPECS[name][0]
    tail = (HERE / "tail.py").read_text()
    tail = re.sub(r"\ndef run\(.*?(?=\n\n\ndef metrics)", "", tail, flags=re.S)
    text = (HEAD_DOC.format(title=title, name=name) + build.HEAD_DOC.split('"""', 2)[2].lstrip("\n")
            + block(name) + (HERE / "intraday_core.py").read_text() + "\n" + tail)
    out = ROOT / "strategies" / name / "backtest.py"
    out.write_text(text)
    return out


if __name__ == "__main__":
    for n in sys.argv[1:] or SPECS:
        print(build_one(n).relative_to(ROOT))
