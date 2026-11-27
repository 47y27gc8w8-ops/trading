# ratio_zscore_pairs: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** KO, PEP (etf, 1d)
**Found at:** iteration 5675 of optimization.log (2026-11-27T12:06:01Z); written at the checkpoint in iteration 6188; backtest.py version `c920f7da44`
**Replaces:** ratio_zscore_pairs__max-income__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 696.92)

## Parameters

| parameter | value |
|---|---|
| leg_stop_pct | 13 |
| max_candles | 40 |
| n | 100 |
| pair_stop_pct | 4.0 |
| z | 1.0 |

```json
{
  "leg_stop_pct": 13,
  "max_candles": 40,
  "n": 100,
  "pair_stop_pct": 4.0,
  "z": 1.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,156.83 | 200.49 |
| return % | 11.57 | 2.00 |
| return %/year | 0.7 | 0.2 |
| gross profit | 2,430.93 | 3,514.31 |
| gross loss | 1,274.10 | 3,313.82 |
| trades | 23 | 33 |
| win rate % | 69.6 | 57.6 |
| avg win | 151.93 | 184.96 |
| avg loss | -182.01 | -236.70 |
| avg result / trade | 50.30 | 6.08 |
| largest single loss | -346.39 | -475.96 |
| largest loss % of equity | -3.33 | -4.85 |
| max drawdown | -959.66 | -1,166.49 |
| max drawdown % | -9.19 | -11.07 |
| profit factor | 1.91 | 1.06 |
| unusually bad trades | 3 | 3 |
| … threshold (% of equity) | 2.5 | 4.2 |
| time in market % | 11.4 | 29.9 |
| buy & hold return % | 0.00 | 0.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.26 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Ratio z-score pairs (formalized)

Source: `original.md` (library spec), EXECUTION.md "Pair execution" / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_pairs.py`; rule = `signals()`, execution = `_simulate_pair()`).

> **Borrow cost is an assumption (0.25 %/yr), not historical data.** The spec says to disable
> this strategy without borrow/carry history; the user chose to run it with a labelled assumption.

## Rule
- **Spec buy trigger:** Compute R=log(C_A/C_B), Z=(R-mean(R,60)[1])/std(R,60)[1]. If Z < -2 and 126-day daily-return correlation >0.6, buy A and short B with equal dollar notionals.
- **Spec exit:** Signal/rebalance exit: Z >= 0 or Z <= -4.
- **Formal:** R = log(A/B); Z = (R - mean(R, n)[1]) / std(R, n)[1]; entry Z < -z and 126-day return correlation > 0.6; exit Z >= 0 or Z <= -4; equal dollars.
- **Fills:** decided at bar t's close, both legs filled at the next synchronized open (both need a bar).
- **Protective exits (OR):** per-leg hard stop leg_stop_pct (long below, short above its entry fill;
  a stop forces the other leg out); net pair P&L incl. fees and borrow <= -pair_stop_pct % of entry
  gross at a close -> next open; time exit after max_candles held bars (entry bar = 1) -> next open.

## Setup
| | |
|---|---|
| Legs | KO / PEP |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2000-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, gross pair notional 100 % of equity |
| Costs | fee 0.05 % + slippage 0.03 % per fill, both legs |
| Borrow (short leg) | **0.25 %/yr, assumed** |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 60 |
| `z` | 2.0 |
| `pair_stop_pct` | 5.0 |
| `leg_stop_pct` | 8.0 |
| `max_candles` | 40 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 20, "max": 120, "step": 10, "hard_min": 5, "hard_max": 504} |
| `z` | {"min": 1.0, "max": 3.0, "step": 0.25, "hard_min": 0.25, "hard_max": 3.75} |
| `pair_stop_pct` | {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0} |
| `leg_stop_pct` | {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0} |
| `max_candles` | {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252} |

## Assumptions
- z-score prior window (t-n..t-1, population std); the -4 z stop and the 0.6 correlation filter (126 daily returns) are fixed constants.
- BORROW COST ASSUMED (user decision 2026-11-27): the spec says to disable pairs without historical borrow/carry data; there is none, so the short leg pays a constant labelled fee (CONFIG borrow_fee_pct_yr: 0.25 %/yr for these easy-to-borrow ETFs/large caps, 3 %/yr for crypto margin) on its market value per calendar day; stress runs at higher fees are logged after the optimization. Borrow recalls and margin calls are not modelled.
- short proceeds earn 0 % and the long leg is paid from the sleeve (no margin interest): conservative carry; total-return (adjusted) closes on both legs, so the short leg pays the dividends it is short (dividend-in-lieu).
- gross notional G = 100 % of sleeve equity at entry (equal dollars: G/2 each; ratio 1:beta: long G/(1+beta), short beta*G/(1+beta)); quantities frozen at entry.
- same-bar ambiguity: if a leg's stop is touched intrabar, that leg fills at its stop and the other leg at its worst bar extreme (long: low, short: high); if both legs touch, the long leg is assumed first. Gaps through a stop fill both legs at the open.
- no new entry on a bar where a position was closed, and no entry when the exit condition (or a forced window end) is true on the signal bar.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), both legs, entry and exit.
- IAU, EWA, EWC and VDE were not in the project; their Yahoo daily history was fetched on 2026-11-27 (src.collectors.yahoo_daily.update, full history) without adding them to config/symbols.yaml, so the nightly job doesn't refresh them.

---
Backtest results don't guarantee future performance.
