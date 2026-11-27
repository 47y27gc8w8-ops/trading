#!/usr/bin/env python3
"""Write strategies/<name>/strategy.md and the setup notes (optimize.py --note) for the portfolio specs.

    python3 scripts/portfolio_lib/docs.py [--notes] [name ...]
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = build.ROOT
TSO = Path("/home/luca/trading/.claude/skills/trading-strategy-optimizer/scripts")

# strategies whose rule holds one asset (or cash) at a time: ~1-2 full exits a year by construction
FEW_TRADES = {"drawdown_defensive_switch", "dual_momentum_allocation", "single_etf_volatility_target"}

COMMON = [
    "point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).",
    "cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.",
    "costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.",
    "Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.",
    "participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.",
    "every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).",
]

SPECIFIC = {
    "consistent_winner_rotation": ["n counts completed MONTHS (month-end to month-end total returns), as the spec's '12 completed months' implies; ROC(126) stays fixed at 126 daily bars."],
    "crypto_equal_weight_rebalance": ["SOL (listed on Binance 2020-08) keeps its 25 % in cash before listing: the rule is a fixed four-coin allocation, so the other coins are not scaled up (EXECUTION.md: 'unless the rule keeps fixed component allocations'). Binance USDT pairs stand in for the spec's BTC/USD etc. (one venue, USD-pegged quote)."],
    "crypto_relative_momentum_basket": ["SMA(200) fixed; n is the ROC lookback. Binance USDT pairs stand in for BTC/USD etc."],
    "downside_risk_weighted_momentum": ["the single parameter n drives both the ROC lookback and the downside-deviation window (both 126 in the spec)."],
    "drawdown_defensive_switch": ["n is the window of SPY's trailing maximum close; IEF's SMA(200) is a fixed constant."],
    "dual_momentum_allocation": ["SPY/EFA ties go to EFA (ticker order)."],
    "equal_risk_contribution_trend": ["solver: the unique long-only ERC point found by cyclical coordinate descent in numpy (scipy, needed for the spec's SLSQP, isn't in the backtest image); same target as INDICATORS.md's objective (= 0 at ERC), validated per decision (finite, sum 1, equal contributions within 1e-6), failure -> cash. SMA(200) fixed; n is the covariance window."],
    "minimum_variance_trend_basket": ["solver: exact long-only minimum variance by enumerating active sets in numpy (scipy isn't in the backtest image); this is the global optimum of the same objective/constraints INDICATORS.md hands to SLSQP. SMA(200) fixed; n is the covariance window."],
    "high_proximity_leader_rotation": ["SMA(200) fixed; n is the HH(C, n) window."],
    "inverse_volatility_trend_basket": ["n is the SMA length; the volatility window stays 63."],
    "low_correlation_momentum_selection": ["correlation pairs with fewer than 3 common returns or zero variance are skipped (not blocking), per INDICATORS.md 'skips undefined correlations'. ROC and correlation windows stay 126."],
    "monthly_loser_rebound_basket": ["ROC(21) and SMA(200) fixed; only k is a signal parameter."],
    "multi_horizon_rank_rotation": ["percentile ranks (average method) are taken across members with all four ROCs defined, before the SMA(200) filter."],
    "sector_roc_rotation": ["SPY is loaded as a signal-only reference series (never traded)."],
    "single_etf_volatility_target": ["volatility annualized with sqrt(252); weight capped at 1 (no leverage)."],
    "stock_bond_paired_switch": ["SPY/TLT ties go to SPY (ticker order)."],
    "trend_equal_weight_global": [],
    "vol_adjusted_momentum_rotation": ["volatility = population std of daily returns over the same n as ROC."],
}


def spec_section(name: str, head: str) -> str:
    txt = (ROOT / "strategies" / name / "original.md").read_text()
    m = re.search(rf"^## {head}\n(.*?)(?=^## )", txt, re.S | re.M)
    return m.group(1).strip() if m else ""


def write_md(name: str) -> None:
    title, syms, mk, start, ref, params, space, _, body = build.SPECS[name]
    rule = re.search(r'"""(.*?)"""', body, re.S).group(1)
    rule = " ".join(x.strip() for x in rule.splitlines())
    buy = spec_section(name, "Buy trigger").split("\n")[0]
    sell = [x for x in spec_section(name, "Sell trigger").splitlines() if x.startswith("- Signal")]
    ptab = "\n".join(f"| `{k}` | {v} |" for k, v in (re.match(r'"(\w+)": ([^,]+),', x).groups() for x in params))
    stab = "\n".join(f"| `{k}` | {r} |" for k, r in (re.match(r'"(\w+)": (\{.*\}),', x).groups() for x in space + [build.SL, build.MC]))
    flags = "`--min-trades-is 10` (one asset at a time: about 1-2 full exits a year by construction)" if name in FEW_TRADES else "defaults"
    md = f"""# {title} (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** {buy}
- **Spec rebalance exit:** {sell[0][2:] if sell else "-"}
- **Formal:** {rule}
- **Decision / fill:** at the close of the last daily bar of each complete month; orders fill at the
  next daily open. Sells and trims first, then buys to target; buys scale down if cash is short.
  Weights sum to at most 100 %; the rest is cash (0 %).
- **Protective stop:** every holding, stop_loss_pct below its average cost; gap below -> open,
  otherwise intrabar at the stop. On additions the stop never loosens:
  new stop = max(old, E_new x (1 - stop_loss_pct/100)).
- **Time exit:** after max_candles held daily bars, sell at the next open (age survives trims/additions).
- A stopped or timed-out holding can only return at a later month-end decision.

## Setup
| | |
|---|---|
| Universe | {", ".join(syms)}{"  (reference, not traded: " + ", ".join(ref) + ")" if ref else ""} |
| Data | {"Binance 1m -> UTC daily bars" if mk["asset_class"] == "crypto" else "Yahoo daily, dividend/split adjusted"} |
| In-sample | {start} -> {mk["oos"]} |
| Out-of-sample | {mk["oos"]} -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee {mk["fee"]:.2f} % + slippage {mk["slip"]:.2f} % per fill |
| Optimizer settings | {flags} |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
{ptab}
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
{stab}

## Assumptions
""" + "\n".join(f"- {a}" for a in SPECIFIC[name] + COMMON) + "\n"
    (ROOT / "strategies" / name / "strategy.md").write_text(md)


def note(name: str, text: str) -> None:
    subprocess.run(["python3", str(TSO / "optimize.py"), f"strategies/{name}", "--note", text], cwd=ROOT, check=True,
                   stdout=subprocess.DEVNULL)


def write_notes(name: str, sanity: str) -> None:
    title, syms, mk, start, ref, *_ = build.SPECS[name]
    note(name, f"setup: universe {','.join(syms)} as ONE month-end portfolio{' (reference ' + ','.join(ref) + ')' if ref else ''}; "
               f"{'Binance 1m -> UTC daily' if mk['asset_class'] == 'crypto' else 'Yahoo daily adjusted'}; IS {start} -> {mk['oos']}, OOS -> 2026-11-23 (frozen); "
               f"10,000 USD sleeve, 100 % split by target weights; fee {mk['fee']:.2f} % + slippage {mk['slip']:.2f} % per fill.")
    note(name, "assumptions: " + " | ".join(SPECIFIC[name] + COMMON))
    note(name, "backtest.py adapted from template: built by scripts/portfolio_lib/build.py = this spec's target_weights() "
               "+ shared month-end portfolio simulator (generalized from breadth_scaled_sector_allocation's _simulate_portfolio: "
               "EXECUTION.md sells-first rebalance, no-loosen hard stop, max_candles age, skip rebalance on a missing member bar) "
               "+ the template's generic machinery. run() simulates the symbol list as one portfolio.")
    if name in FEW_TRADES:
        note(name, "settings: --min-trades-is 10 because the rule holds a single asset (or cash) at a time, so it has about 1-2 full exits "
                   "a year by construction (default 20 would reject the spec's own design; precedent: trix_zero_trend).")
    note(name, f"sanity check: {sanity}")


if __name__ == "__main__":
    args = sys.argv[1:]
    notes = "--notes" in args
    names = [a for a in args if not a.startswith("--")] or list(build.SPECS)
    for n in names:
        write_md(n)
        print("strategy.md", n)
