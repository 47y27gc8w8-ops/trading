# multi_horizon_rank_rotation: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 294 of optimization.log (2026-11-27T11:48:35Z); written at the checkpoint in iteration 2086; backtest.py version `01c28d73a1`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 19,026.68)

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 441 |
| stop_loss_pct | 14 |

```json
{
  "k": 5,
  "max_candles": 441,
  "stop_loss_pct": 14
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 20,209.67 | 15,176.61 |
| return % | 202.10 | 151.77 |
| return %/year | 9.7 | 8.8 |
| gross profit | 33,705.10 | 22,223.07 |
| gross loss | 13,495.43 | 7,046.46 |
| trades | 109 | 111 |
| win rate % | 55.0 | 45.0 |
| avg win | 561.75 | 444.46 |
| avg loss | -275.42 | -115.52 |
| avg result / trade | 185.41 | 136.73 |
| largest single loss | -1,034.92 | -583.29 |
| largest loss % of equity | -3.49 | -4.78 |
| max drawdown | -3,580.02 | -4,672.24 |
| max drawdown % | -18.42 | -23.53 |
| profit factor | 2.50 | 3.15 |
| unusually bad trades | 9 | 4 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 53.8 | 53.5 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.92 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Multi-horizon rank rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end rank each asset by mean cross-sectional percentile rank of ROC(21), ROC(63), ROC(126), ROC(252); select top 3 with C > SMA(200); equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside the selected group or below SMA(200).
- **Formal:** score = mean cross-sectional percentile rank of ROC(21/63/126/252) among assets with all four defined; top k with C > SMA(200); equal weight.
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
| Universe | DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2004-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 8} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- percentile ranks (average method) are taken across members with all four ROCs defined, before the SMA(200) filter.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
