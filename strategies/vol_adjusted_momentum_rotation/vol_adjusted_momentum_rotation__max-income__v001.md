# vol_adjusted_momentum_rotation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 138 of optimization.log (2026-11-27T11:43:43Z); written at the checkpoint in iteration 285; backtest.py version `f0b0a8922e`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 17,477.62)
**Range warning:** n is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 3 |
| max_candles | 378 |
| n | 63 |
| stop_loss_pct | 22 |

```json
{
  "k": 3,
  "max_candles": 378,
  "n": 63,
  "stop_loss_pct": 22
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 25,648.87 | 13,754.89 |
| return % | 256.49 | 137.55 |
| return %/year | 11.2 | 8.3 |
| gross profit | 49,424.35 | 26,280.30 |
| gross loss | 23,775.49 | 12,525.40 |
| trades | 129 | 127 |
| win rate % | 58.9 | 53.5 |
| avg win | 650.32 | 386.47 |
| avg loss | -448.59 | -212.29 |
| avg result / trade | 198.83 | 108.31 |
| largest single loss | -3,293.62 | -1,100.90 |
| largest loss % of equity | -7.99 | -4.18 |
| max drawdown | -9,531.64 | -5,195.72 |
| max drawdown % | -25.81 | -23.71 |
| profit factor | 2.08 | 2.10 |
| unusually bad trades | 11 | 11 |
| … threshold (% of equity) | 2.5 | 2.0 |
| time in market % | 35.2 | 33.8 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.74 |
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
