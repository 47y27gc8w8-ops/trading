# equal_risk_contribution_trend: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 19 of optimization.log (2026-11-27T12:07:56Z); written at the checkpoint in iteration 175; backtest.py version `7bb330d3d9`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 8,863.83)

## Parameters

| parameter | value |
|---|---|
| max_candles | 294 |
| n | 126 |
| stop_loss_pct | 15.0 |

```json
{
  "max_candles": 294,
  "n": 126,
  "stop_loss_pct": 15.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 11,287.05 | 5,914.55 |
| return % | 112.87 | 59.15 |
| return %/year | 6.5 | 4.4 |
| gross profit | 19,867.67 | 15,160.69 |
| gross loss | 8,580.62 | 9,246.14 |
| trades | 102 | 107 |
| win rate % | 44.1 | 41.1 |
| avg win | 441.50 | 344.56 |
| avg loss | -150.54 | -146.76 |
| avg result / trade | 110.66 | 55.28 |
| largest single loss | -483.25 | -2,118.90 |
| largest loss % of equity | -2.34 | -12.91 |
| max drawdown | -2,367.24 | -5,440.93 |
| max drawdown % | -14.28 | -30.14 |
| profit factor | 2.31 | 1.64 |
| unusually bad trades | 6 | 7 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 64.0 | 64.4 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.67 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Equal risk contribution trend (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end keep assets above SMA(200); estimate sample covariance from 126 daily returns. Solve long-only equal-risk-contribution weights under sum(w)=1, then rebalance.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end remove trend failures and resize to new risk-contribution weights.
- **Formal:** Assets with C > SMA(200); long-only equal-risk-contribution weights from the n-day sample covariance (regularized). Solver failure / no covariance -> cash.
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
- solver: the unique long-only ERC point found by cyclical coordinate descent in numpy (scipy, needed for the spec's SLSQP, isn't in the backtest image); same target as INDICATORS.md's objective (= 0 at ERC), validated per decision (finite, sum 1, equal contributions within 1e-6), failure -> cash. SMA(200) fixed; n is the covariance window.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
