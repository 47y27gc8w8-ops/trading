#!/usr/bin/env python3
"""strategy.md + setup notes (optimize.py --note) for the library's pair specs.

    python3 scripts/portfolio_lib/docs_pairs.py [--notes sanity_file] [name ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pairs as bp  # noqa: E402
from docs import note, spec_section  # noqa: E402

ROOT = bp.ROOT

COMMON = [
    "BORROW COST ASSUMED (user decision 2026-11-27): the spec says to disable pairs without historical borrow/carry data; there is none, so the short leg pays a constant labelled fee (CONFIG borrow_fee_pct_yr: 0.25 %/yr for these easy-to-borrow ETFs/large caps, 3 %/yr for crypto margin) on its market value per calendar day; stress runs at higher fees are logged after the optimization. Borrow recalls and margin calls are not modelled.",
    "short proceeds earn 0 % and the long leg is paid from the sleeve (no margin interest): conservative carry; total-return (adjusted) closes on both legs, so the short leg pays the dividends it is short (dividend-in-lieu).",
    "gross notional G = 100 % of sleeve equity at entry (equal dollars: G/2 each; ratio 1:beta: long G/(1+beta), short beta*G/(1+beta)); quantities frozen at entry.",
    "same-bar ambiguity: if a leg's stop is touched intrabar, that leg fills at its stop and the other leg at its worst bar extreme (long: low, short: high); if both legs touch, the long leg is assumed first. Gaps through a stop fill both legs at the open.",
    "no new entry on a bar where a position was closed, and no entry when the exit condition (or a forced window end) is true on the signal bar.",
    "costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), both legs, entry and exit.",
    "IAU, EWA, EWC and VDE were not in the project; their Yahoo daily history was fetched on 2026-11-27 (src.collectors.yahoo_daily.update, full history) without adding them to config/symbols.yaml, so the nightly job doesn't refresh them.",
]
SPECIFIC = {
    "ratio_zscore_pairs": ["z-score prior window (t-n..t-1, population std); the -4 z stop and the 0.6 correlation filter (126 daily returns) are fixed constants."],
    "cointegration_gated_residual": ["Engle-Granger p-value computed in numpy exactly as statsmodels coint(trend='c', maxlag=1, autolag=None) (OLS, ADF on residuals without constant with 1 lag, MacKinnon N=2 'c' p-value constants copied from statsmodels 0.14.4); statsmodels isn't in the backtest image. Formation = the n bars before the month-end bar; the model is frozen from that month-end bar until the next one, where open positions are closed (forced) before refitting. Entry z -2 and stop z -4 are fixed constants."],
    "half_life_filtered_pairs": ["AR(1) fit and z-score both on the prior n bars; half-life lower bound 2 and entry z -2 / stop z -4 are fixed constants."],
    "normalized_distance_pairs": ["six-month boundaries = last bar of June and December; formation = the f bars before the boundary bar; trading window = next bar up to the next boundary, where an open pair is closed. All 6 pairs of CL, KO, PEP, PG compete; alphabetically first ticker is A."],
    "ols_residual_pairs": ["formation residual std = population std of the OLS residuals over t-n..t-1; beta frozen at entry for quantities, no hedge rebalancing; z stop -4 fixed."],
    "ratio_rsi_recovery": ["Binance spot ETHUSDT/BTCUSDT closes stand in for ETH/USD and BTC/USD (one venue, same quote). Crypto margin borrow of BTC assumed at 3 %/yr (stress 6 %, 10 %). RSI warm-up 5 x n bars; exit levels 60/15 fixed."],
    "relative_momentum_spread_breakout": ["channels on the log ratio use prior bars only (HH/LL shifted by one bar); exit_n < n enforced in valid()."],
    "short_horizon_return_spread": ["ROC from adjusted closes; correlation filter 0.7 over 126 daily returns fixed; exit at D >= 0 or D < -2 x gap."],
}


def write_md(name: str) -> None:
    title, syms, mk, start, params, space, _, body = bp.SPECS[name]
    rule = " ".join(x.strip() for x in re.search(r'"""(.*?)"""', body, re.S).group(1).splitlines())
    buy = spec_section(name, "Buy trigger").split("\n")[0]
    sell = [x for x in spec_section(name, "Sell trigger").splitlines() if x.startswith("- Signal")]
    ptab = "\n".join(f"| `{k}` | {v} |" for k, v in (re.match(r'"(\w+)": ([^,]+),', x).groups() for x in params + bp.COMMON_P))
    stab = "\n".join(f"| `{k}` | {r} |" for k, r in (re.match(r'"(\w+)": (\{.*\}),', x).groups() for x in space + bp.COMMON_S))
    md = f"""# {title} (formalized)

Source: `original.md` (library spec), EXECUTION.md "Pair execution" / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_pairs.py`; rule = `signals()`, execution = `_simulate_pair()`).

> **Borrow cost is an assumption ({mk["borrow"]} %/yr), not historical data.** The spec says to disable
> this strategy without borrow/carry history; the user chose to run it with a labelled assumption.

## Rule
- **Spec buy trigger:** {buy}
- **Spec exit:** {sell[0][2:] if sell else "-"}
- **Formal:** {rule}
- **Fills:** decided at bar t's close, both legs filled at the next synchronized open (both need a bar).
- **Protective exits (OR):** per-leg hard stop leg_stop_pct (long below, short above its entry fill;
  a stop forces the other leg out); net pair P&L incl. fees and borrow <= -pair_stop_pct % of entry
  gross at a close -> next open; time exit after max_candles held bars (entry bar = 1) -> next open.

## Setup
| | |
|---|---|
| Legs | {" / ".join(syms) if len(syms) == 2 else "candidates " + ", ".join(syms)} |
| Data | {"Binance 1m -> UTC daily bars" if mk["asset_class"] == "crypto" else "Yahoo daily, dividend/split adjusted"} |
| In-sample | {start} -> {mk["oos"]} |
| Out-of-sample | {mk["oos"]} -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, gross pair notional 100 % of equity |
| Costs | fee {mk["fee"]:.2f} % + slippage {mk["slip"]:.2f} % per fill, both legs |
| Borrow (short leg) | **{mk["borrow"]} %/yr, assumed** |

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


def write_notes(name: str, sanity: str) -> None:
    title, syms, mk, start, *_ = bp.SPECS[name]
    note(name, f"setup: pair {'/'.join(syms) if len(syms) == 2 else 'chosen among ' + ','.join(syms)} long A / short B; "
               f"{'Binance 1m -> UTC daily' if mk['asset_class'] == 'crypto' else 'Yahoo daily adjusted'}; IS {start} -> {mk['oos']}, OOS -> 2026-11-23 (frozen); "
               f"10,000 USD sleeve, gross 100 %; fee {mk['fee']:.2f} % + slippage {mk['slip']:.2f} % per fill per leg; borrow {mk['borrow']} %/yr ASSUMED.")
    note(name, "answers: user chose (2026-11-27) to run the pair specs with a labelled assumed borrow fee on the short leg "
               "(0.25 %/yr base for easy-to-borrow ETFs/large caps, stress 1 % and 3 %) instead of disabling them as the spec requires without borrow data.")
    note(name, "assumptions: " + " | ".join(SPECIFIC[name] + COMMON))
    note(name, "backtest.py adapted from template: built by scripts/portfolio_lib/build_pairs.py = this spec's signals() + shared pair "
               "simulator pair_core.py (EXECUTION.md pair execution: synchronized next-open fills, per-leg hard stops, close-based pair stop, "
               "max_candles, entry veto, borrow accrual) + panel/indicators from core.py + the template's generic machinery; run() simulates one pair.")
    note(name, f"sanity check: {sanity}")


if __name__ == "__main__":
    args = sys.argv[1:]
    sanity_file = None
    if "--notes" in args:
        k = args.index("--notes")
        sanity_file = args[k + 1]
        del args[k:k + 2]
    names = args or list(bp.SPECS)
    for n in names:
        write_md(n)
    if sanity_file:
        for line in open(sanity_file):
            m = re.match(r"(\w+)\s+IS trades/%yr/dd/s \((\d+), ([-\d.]+), ([-\d.]+), [\d.]+\)\s+OOS \((\d+), ([-\d.]+), ([-\d.]+)", line)
            if m and m.group(1) in names:
                n, it, iy, idd, ot, oy, od = m.groups()
                write_notes(n, f"spec defaults IS: {it} trades, {iy} %/yr, max DD {idd} % (OOS {ot} trades, {oy} %/yr, DD {od} %). "
                               "Verified on generated trades (ratio_zscore, normalized_distance, ratio_rsi): every entry follows an entry signal "
                               "on the previous bar with no exit signal; signal exits follow an exit signal; after an exit no fill on the same bar "
                               "(e.g. KO/PEP stopped 2008-07-01, next entry 2008-07-03); sum of trade P&L = equity change (-769.93 over 'all'); "
                               "borrow fee lowers results monotonically (0 / 0.25 / 3 %/yr -> IS net 466 / 450 / 282). "
                               "Engle-Granger p at MacKinnon's 5 % critical value (-3.34, N=2) = 0.0495.")
                print("notes", n)
