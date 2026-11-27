# sector_roc_rotation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 103 of optimization.log (2026-11-27T11:43:30Z); written at the checkpoint in iteration 273; backtest.py version `0771a883af`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 25,094.88)

## Parameters

| parameter | value |
|---|---|
| k | 1 |
| max_candles | 462 |
| n | 189 |
| stop_loss_pct | 24 |

```json
{
  "k": 1,
  "max_candles": 462,
  "n": 189,
  "stop_loss_pct": 24
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 39,647.98 | 6,100.15 |
| return % | 396.48 | 61.00 |
| return %/year | 10.9 | 4.5 |
| gross profit | 68,385.62 | 24,698.45 |
| gross loss | 28,737.63 | 18,598.30 |
| trades | 57 | 49 |
| win rate % | 61.4 | 49.0 |
| avg win | 1,953.87 | 1,029.10 |
| avg loss | -1,306.26 | -743.93 |
| avg result / trade | 695.58 | 124.49 |
| largest single loss | -4,807.63 | -2,515.23 |
| largest loss % of equity | -8.53 | -12.38 |
| max drawdown | -11,631.18 | -6,199.64 |
| max drawdown % | -25.88 | -29.17 |
| profit factor | 2.38 | 1.33 |
| unusually bad trades | 2 | 5 |
| … threshold (% of equity) | 7.3 | 7.2 |
| time in market % | 6.3 | 7.5 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.41 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Sector ROC rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** On each month-end select the top 3 sectors by ROC(63), only if SPY > its SMA(200); equal-weight selected assets.
- **Spec rebalance exit:** Signal/rebalance exit: At each month-end sell assets no longer selected or if SPY <= SMA(200).
- **Formal:** Top k sectors by ROC(n), only while SPY > SMA(200) (SPY is a reference, not traded); equal weight.
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
| Universe | XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY  (reference, not traded: SPY) |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2000-07-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `k` | 3 |
| `n` | 63 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `n` | {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 380} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SPY is loaded as a signal-only reference series (never traded).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
