# monthly_loser_rebound_basket: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 1751 of optimization.log (2026-11-27T12:15:50Z); written at the checkpoint in iteration 2545; backtest.py version `8b81321b31`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 10,371.44)

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 315 |
| stop_loss_pct | 28 |

```json
{
  "k": 5,
  "max_candles": 315,
  "stop_loss_pct": 28
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 11,334.05 | 14,686.85 |
| return % | 113.34 | 146.87 |
| return %/year | 5.0 | 8.7 |
| gross profit | 30,640.99 | 39,797.74 |
| gross loss | 19,306.94 | 25,110.89 |
| trades | 313 | 292 |
| win rate % | 64.9 | 62.3 |
| avg win | 150.94 | 218.67 |
| avg loss | -175.52 | -228.28 |
| avg result / trade | 36.21 | 50.30 |
| largest single loss | -1,659.56 | -2,099.02 |
| largest loss % of equity | -13.15 | -13.43 |
| max drawdown | -4,968.70 | -5,620.11 |
| max drawdown % | -38.86 | -31.40 |
| profit factor | 1.59 | 1.58 |
| unusually bad trades | 14 | 15 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 37.5 | 41.8 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.73 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Monthly loser rebound basket (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end select the 3 lowest ROC(21) sectors among those above SMA(200); equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At next month-end sell assets no longer in the lowest-ROC eligible group.
- **Formal:** The k lowest ROC(21) sectors among those with C > SMA(200); equal weight.
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
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- ROC(21) and SMA(200) fixed; only k is a signal parameter.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
