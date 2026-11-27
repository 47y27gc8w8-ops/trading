#!/usr/bin/env python3
"""strategy.md + setup notes for the library's US 5-minute specs.

    python3 scripts/portfolio_lib/docs_intraday.py [--notes] [name ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_intraday as bi  # noqa: E402
from docs import note, spec_section  # noqa: E402

ROOT = bi.ROOT
COMMON = [
    "data: Alpaca SIP 5-minute bars (free plan, history from 2016), split + dividend adjusted (adjustment=all) and used for signals and fills; regular session 09:30-16:00 America/New_York only. Early closes come from the data itself (the session's last bar), so the scheduled liquidation and the 'earlier of 15:00 and 60 minutes before the close' entry cutoff follow the real calendar.",
    "sizing: 100 % of equity per trade instead of the spec's risk_fraction sizing (user's choice for all library specs with risk_fraction, so results compare across the leaderboard); risk_fraction is therefore not optimized.",
    "time windows refer to the signal bar's CLOSE time (bars are labelled by close, EXECUTION.md); crosses need both bars in the same session; frozen levels (opening ranges, lunch range, prior-session levels) only exist once complete.",
    "fills: market/stop fills pay slippage 0.03 % and every fill pays fee 0.05 % (library convention for US stocks/ETFs); the resting target limit fills at its price without slippage; a gap above the target fills at the target (never better than the limit); stop first when one bar touches both.",
    "ATR(14), ADX(14) and EMA run continuously across sessions (overnight gaps count in the true range); warm-up 5 x period bars. Session VWAP anchors at 09:30 with TP = (H+L+C)/3.",
    "participation cap not modelled (10k sleeve in the most liquid US names).",
    "IS 2016-03-01 -> 2023-01-01, OOS 2023-01-01 -> 2026-11-25: Alpaca's free history starts in 2016, so the library's usual 2016 split for Yahoo daily data can't apply.",
]
SPECIFIC = {
    "afternoon_momentum_continuation": ["first-hour high = high of 09:30-10:30, frozen at 10:30; HH(H,6)[1] uses the six prior bars of the same session."],
    "full_gap_up_continuation": ["the spec's 10:00-12:00 entry window and one entry per session applied."],
    "gap_down_reversal_strength": ["no entry limit per session (spec sets none); prior-session levels are regular-session high/low/close."],
    "intraday_lunch_compression_break": ["lunch range = bars starting 11:30 to 12:55 (closing 11:35-13:00), frozen with the ATR(14) of the bar closing 13:00; entries on bars closing 13:05-15:00."],
    "opening_range_breakout": ["base symbol SPY (spec lists SPY and QQQ as separate alternatives; QQQ can be a follow-up run); entries 10:30-15:00 regardless of range length."],
    "opening_range_failed_breakdown": [],
    "partial_gap_down_fill": ["gap band: open between prior close x (1 - gap/100) and prior close x (1 - 0.002); the 0.2 % lower edge is a fixed constant."],
    "previous_day_high_intraday_break": ["relative volume = V / median volume of the same time slot over the 20 preceding sessions (same-slot rule, INDICATORS.md)."],
    "session_vwap_deviation_reversion": ["level condition (can recur while flat); no entry limit per session."],
    "session_vwap_reclaim": [],
    "session_vwap_trend_pullback": ["VWAP[3] and H[1] must come from the same session."],
}


def write_md(name: str) -> None:
    title, sym, max_e, params, space, _, body = bi.SPECS[name]
    rule = " ".join(x.strip() for x in re.search(r'"""(.*?)"""', body, re.S).group(1).splitlines())
    buy = spec_section(name, "Buy trigger").split("\n")[0]
    sell = [x for x in spec_section(name, "Sell trigger").splitlines() if x.startswith("- Signal")]
    ptab = "\n".join(f"| `{k}` | {v} |" for k, v in (re.match(r'"(\w+)": ([^,]+),', x).groups() for x in params + bi.COMMON_P))
    stab = "\n".join(f"| `{k}` | {r} |" for k, r in (re.match(r'"(\w+)": (\{.*\}),', x).groups() for x in space + bi.COMMON_S))
    md = f"""# {title} (formalized)

Source: `original.md` (library spec), EXECUTION.md (US 5-minute rules) / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_intraday.py`; rule = `signals()`, execution = `_simulate_intraday()`).

## Rule
- **Spec buy trigger:** {buy}
- **Spec exit:** {sell[0][2:] if sell else "-"}
- **Formal:** {rule}
- **Fill:** next 5-minute bar's open; no fill at/after the earlier of 15:00 and 60 minutes before the
  session close, none on the session's last bar{"; max one entry per session" if max_e else ""}.
- **Exits (OR, earliest wins):** stop at fill - stop_atr x ATR(14) of the signal bar; target at
  fill + take_profit_atr x the same ATR; signal exit at the next open; time exit after max_candles
  held bars (entry bar = 1); scheduled liquidation at the open of the session's last bar.

## Setup
| | |
|---|---|
| Symbol | {sym} |
| Data | Alpaca SIP 5-minute bars, regular session, split + dividend adjusted |
| In-sample | 2016-03-01 -> 2023-01-01 |
| Out-of-sample | 2023-01-01 -> 2026-11-25 (frozen) |
| Capital / sizing | 10,000 USD, 100 % of equity per trade |
| Costs | fee 0.05 % per fill, slippage 0.03 % on market/stop fills |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
{ptab}

## Search space
| Parameter | Range |
|---|---|
{stab}

## Assumptions
""" + "\n".join(f"- {a}" for a in SPECIFIC[name] + COMMON) + "\n"
    (ROOT / "strategies" / name / "strategy.md").write_text(md)


def write_notes(name: str) -> None:
    title, sym, *_ = bi.SPECS[name]
    note(name, f"setup: {sym} 5-minute regular-session bars from Alpaca (SIP, adjusted); IS 2016-03-01 -> 2023-01-01, OOS -> 2026-11-25 (frozen); "
               "10,000 USD, 100 % of equity per trade; fee 0.05 % per fill, slippage 0.03 % on market/stop fills.")
    note(name, "answers: user chose (2026-11-27) to get 5-minute history from a free Alpaca key (Yahoo has only 60 days of 5-minute bars).")
    note(name, "assumptions: " + " | ".join(SPECIFIC[name] + COMMON))
    note(name, "backtest.py adapted from template: built by scripts/portfolio_lib/build_intraday.py = this spec's signals() + shared "
               "intraday_core.py (5-minute session features: session open, prior-session H/L/C, session VWAP, frozen ranges, ATR/ADX/EMA, "
               "same-slot volume median; single-position simulator with frozen ATR stop/target, time exit, scheduled session liquidation, "
               "entry cutoff, entries per session) + the template's generic machinery.")


if __name__ == "__main__":
    args = sys.argv[1:]
    notes = "--notes" in args
    names = [a for a in args if not a.startswith("--")] or list(bi.SPECS)
    for n in names:
        write_md(n)
        if notes:
            write_notes(n)
    print(len(names), "intraday specs documented", "(+ notes)" if notes else "")
