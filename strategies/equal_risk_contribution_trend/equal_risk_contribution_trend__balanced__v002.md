# equal_risk_contribution_trend: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 277 of optimization.log (2026-11-27T12:10:24Z); written at the checkpoint in iteration 788; backtest.py version `7bb330d3d9`
**Replaces:** equal_risk_contribution_trend__balanced__v001.md
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 8,149.84)

## Parameters

| parameter | value |
|---|---|
| max_candles | 189 |
| n | 63 |
| stop_loss_pct | 13 |

```json
{
  "max_candles": 189,
  "n": 63,
  "stop_loss_pct": 13
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 10,698.13 | 6,654.79 |
| return % | 106.98 | 66.55 |
| return %/year | 6.2 | 4.8 |
| gross profit | 20,375.00 | 17,063.60 |
| gross loss | 9,676.87 | 10,408.80 |
| trades | 126 | 128 |
| win rate % | 48.4 | 40.6 |
| avg win | 334.02 | 328.15 |
| avg loss | -148.87 | -136.96 |
| avg result / trade | 84.91 | 51.99 |
| largest single loss | -526.13 | -783.50 |
| largest loss % of equity | -2.55 | -4.37 |
| max drawdown | -1,909.91 | -4,728.61 |
| max drawdown % | -11.84 | -25.99 |
| profit factor | 2.11 | 1.64 |
| unusually bad trades | 6 | 9 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 61.0 | 62.8 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.77 |
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
