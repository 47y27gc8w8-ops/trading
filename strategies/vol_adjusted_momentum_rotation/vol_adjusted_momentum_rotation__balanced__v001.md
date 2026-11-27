# vol_adjusted_momentum_rotation: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 99 of optimization.log (2026-11-27T11:43:38Z); written at the checkpoint in iteration 286; backtest.py version `f0b0a8922e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 15,445.84)
**Range warning:** n is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 4 |
| max_candles | 168 |
| n | 252 |
| stop_loss_pct | 24 |

```json
{
  "k": 4,
  "max_candles": 168,
  "n": 252,
  "stop_loss_pct": 24
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 21,891.22 | 7,413.83 |
| return % | 218.91 | 74.14 |
| return %/year | 10.2 | 5.2 |
| gross profit | 31,680.01 | 15,310.53 |
| gross loss | 9,788.79 | 7,896.70 |
| trades | 103 | 90 |
| win rate % | 64.1 | 53.3 |
| avg win | 480.00 | 318.97 |
| avg loss | -264.56 | -188.02 |
| avg result / trade | 212.54 | 82.38 |
| largest single loss | -1,184.66 | -813.89 |
| largest loss % of equity | -6.42 | -6.11 |
| max drawdown | -2,602.56 | -3,334.11 |
| max drawdown % | -16.36 | -26.97 |
| profit factor | 3.24 | 1.94 |
| unusually bad trades | 5 | 8 |
| … threshold (% of equity) | 2.0 | 2.2 |
| time in market % | 45.2 | 43.1 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.52 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Volatility-adjusted momentum rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end score=ROC(126)/Std(daily returns,126); choose top 3 positive-score assets and equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside selected positive-score group.
- **Formal:** score = ROC(n) / Std(daily returns, n) (decimal units, zero volatility skipped); top k positive scores; equal weight.
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
| `n` | 126 |
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504} |
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 8} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- volatility = population std of daily returns over the same n as ROC.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
