# half_life_filtered_pairs: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** EWA, EWC (etf, 1d)
**Found at:** iteration 289 of optimization.log (2026-11-27T12:07:12Z); written at the checkpoint in iteration 790; backtest.py version `31c5e452a7`
**Replaces:** half_life_filtered_pairs__max-income__v001.md
**Robustness:** 7/9 one-step neighbours profitable in-sample (worst neighbour net -659.46)

## Parameters

| parameter | value |
|---|---|
| half | 70 |
| leg_stop_pct | 13 |
| max_candles | 25 |
| n | 70 |
| pair_stop_pct | 3.5 |

```json
{
  "half": 70,
  "leg_stop_pct": 13,
  "max_candles": 25,
  "n": 70,
  "pair_stop_pct": 3.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,509.94 | 246.36 |
| return % | 15.10 | 2.46 |
| return %/year | 0.8 | 0.2 |
| gross profit | 6,046.67 | 2,325.70 |
| gross loss | 4,536.72 | 2,079.35 |
| trades | 57 | 36 |
| win rate % | 61.4 | 58.3 |
| avg win | 172.76 | 110.75 |
| avg loss | -206.21 | -138.62 |
| avg result / trade | 26.49 | 6.84 |
| largest single loss | -556.91 | -227.59 |
| largest loss % of equity | -4.85 | -2.20 |
| max drawdown | -1,463.30 | -1,100.77 |
| max drawdown % | -14.09 | -9.92 |
| profit factor | 1.33 | 1.12 |
| unusually bad trades | 5 | 0 |
| … threshold (% of equity) | 3.0 | 2.4 |
| time in market % | 21.4 | 21.6 |
| buy & hold return % | 0.00 | 0.00 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |
| period | 1998-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Half-life filtered pairs (formalized)

Source: `original.md` (library spec), EXECUTION.md "Pair execution" / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_pairs.py`; rule = `signals()`, execution = `_simulate_pair()`).

> **Borrow cost is an assumption (0.25 %/yr), not historical data.** The spec says to disable
> this strategy without borrow/carry history; the user chose to run it with a labelled assumption.

## Rule
- **Spec buy trigger:** R=log(A/B). On preceding 120 bars fit delta_R=a+b*R_lag. Require -1<b<0 and half_life=log(0.5)/log(1+b) between 2 and 30 bars. If current prior-window R z-score<-2, buy A/short B equal dollars.
- **Spec exit:** Signal/rebalance exit: Prior-window R z-score >=0 or <=-4.
- **Formal:** R = log(A/B). On t-n..t-1 fit dR = a + b R_lag (OLS); require -1 < b < 0 and half-life log(0.5)/log(1+b) in [2, half]. Entry prior-window z(R) < -2; exit z >= 0 or z <= -4; equal dollars.
- **Fills:** decided at bar t's close, both legs filled at the next synchronized open (both need a bar).
- **Protective exits (OR):** per-leg hard stop leg_stop_pct (long below, short above its entry fill;
  a stop forces the other leg out); net pair P&L incl. fees and borrow <= -pair_stop_pct % of entry
  gross at a close -> next open; time exit after max_candles held bars (entry bar = 1) -> next open.

## Setup
| | |
|---|---|
| Legs | EWA / EWC |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 1998-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, gross pair notional 100 % of equity |
| Costs | fee 0.05 % + slippage 0.03 % per fill, both legs |
| Borrow (short leg) | **0.25 %/yr, assumed** |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 120 |
| `half` | 30 |
| `pair_stop_pct` | 5.0 |
| `leg_stop_pct` | 8.0 |
| `max_candles` | 40 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 60, "max": 250, "step": 10, "hard_min": 20, "hard_max": 504} |
| `half` | {"min": 10, "max": 60, "step": 5, "hard_min": 3, "hard_max": 252} |
| `pair_stop_pct` | {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0} |
| `leg_stop_pct` | {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0} |
| `max_candles` | {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252} |

## Assumptions
- AR(1) fit and z-score both on the prior n bars; half-life lower bound 2 and entry z -2 / stop z -4 are fixed constants.
- BORROW COST ASSUMED (user decision 2026-11-27): the spec says to disable pairs without historical borrow/carry data; there is none, so the short leg pays a constant labelled fee (CONFIG borrow_fee_pct_yr: 0.25 %/yr for these easy-to-borrow ETFs/large caps, 3 %/yr for crypto margin) on its market value per calendar day; stress runs at higher fees are logged after the optimization. Borrow recalls and margin calls are not modelled.
- short proceeds earn 0 % and the long leg is paid from the sleeve (no margin interest): conservative carry; total-return (adjusted) closes on both legs, so the short leg pays the dividends it is short (dividend-in-lieu).
- gross notional G = 100 % of sleeve equity at entry (equal dollars: G/2 each; ratio 1:beta: long G/(1+beta), short beta*G/(1+beta)); quantities frozen at entry.
- same-bar ambiguity: if a leg's stop is touched intrabar, that leg fills at its stop and the other leg at its worst bar extreme (long: low, short: high); if both legs touch, the long leg is assumed first. Gaps through a stop fill both legs at the open.
- no new entry on a bar where a position was closed, and no entry when the exit condition (or a forced window end) is true on the signal bar.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), both legs, entry and exit.
- IAU, EWA, EWC and VDE were not in the project; their Yahoo daily history was fetched on 2026-11-27 (src.collectors.yahoo_daily.update, full history) without adding them to config/symbols.yaml, so the nightly job doesn't refresh them.

---
Backtest results don't guarantee future performance.
