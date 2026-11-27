# consistent_winner_rotation: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 380 of optimization.log (2026-11-27T11:45:06Z); written at the checkpoint in iteration 910; backtest.py version `ee39969495`
**Replaces:** consistent_winner_rotation__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 8,549.91)

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 315 |
| n | 19 |
| stop_loss_pct | 11 |

```json
{
  "k": 5,
  "max_candles": 315,
  "n": 19,
  "stop_loss_pct": 11
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,353.12 | 17,635.66 |
| return % | 123.53 | 176.36 |
| return %/year | 5.3 | 9.8 |
| gross profit | 27,232.79 | 34,830.39 |
| gross loss | 14,879.67 | 17,194.72 |
| trades | 165 | 152 |
| win rate % | 50.9 | 52.0 |
| avg win | 324.20 | 440.89 |
| avg loss | -183.70 | -235.54 |
| avg result / trade | 74.87 | 116.02 |
| largest single loss | -924.76 | -731.55 |
| largest loss % of equity | -5.67 | -2.78 |
| max drawdown | -4,800.94 | -5,770.99 |
| max drawdown % | -35.57 | -24.31 |
| profit factor | 1.83 | 2.03 |
| unusually bad trades | 17 | 21 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 35.9 | 41.0 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.84 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Consistent winner rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end score=number of positive monthly total returns in the last 12 completed months; select top 3 assets with ROC(126)>0, breaking score ties by ROC(126) then ticker; equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside the selected group.
- **Formal:** score = positive monthly total returns in the last n completed months; eligible ROC(126) > 0; top k by (score, ROC(126), ticker); equal weight.
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
| Universe | XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2000-07-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 12 |
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 6, "max": 24, "step": 1, "hard_min": 1, "hard_max": 60} |
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- n counts completed MONTHS (month-end to month-end total returns), as the spec's '12 completed months' implies; ROC(126) stays fixed at 126 daily bars.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
