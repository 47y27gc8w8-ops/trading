# minimum_variance_trend_basket: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 58 of optimization.log (2026-11-27T11:44:05Z); written at the checkpoint in iteration 179; backtest.py version `7dbf9b5ce0`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 7,903.74)

## Parameters

| parameter | value |
|---|---|
| max_candles | 420 |
| n | 84 |
| stop_loss_pct | 10 |

```json
{
  "max_candles": 420,
  "n": 84,
  "stop_loss_pct": 10
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 9,355.71 | 4,577.91 |
| return % | 93.56 | 45.78 |
| return %/year | 5.7 | 3.5 |
| gross profit | 13,748.66 | 14,859.72 |
| gross loss | 4,392.94 | 10,281.81 |
| trades | 81 | 103 |
| win rate % | 50.6 | 42.7 |
| avg win | 335.33 | 337.72 |
| avg loss | -109.82 | -174.27 |
| avg result / trade | 115.50 | 44.45 |
| largest single loss | -408.15 | -1,594.60 |
| largest loss % of equity | -2.36 | -10.42 |
| max drawdown | -1,320.40 | -4,975.73 |
| max drawdown % | -9.50 | -28.51 |
| profit factor | 3.13 | 1.45 |
| unusually bad trades | 5 | 11 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 34.0 | 37.3 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.62 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Minimum-variance trend basket (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end keep assets above SMA(200); estimate 126-day covariance; choose long-only weights minimizing w.T*cov*w subject to sum(w)=1.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell trend failures and rebalance to newly optimized weights.
- **Formal:** Assets with C > SMA(200); long-only minimum-variance weights (sum 1) from the n-day sample covariance (regularized). Solver failure / no covariance -> cash.
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
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- solver: exact long-only minimum variance by enumerating active sets in numpy (scipy isn't in the backtest image); this is the global optimum of the same objective/constraints INDICATORS.md hands to SLSQP. SMA(200) fixed; n is the covariance window.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
