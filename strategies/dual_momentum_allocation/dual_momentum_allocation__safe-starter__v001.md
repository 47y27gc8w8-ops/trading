# dual_momentum_allocation: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** EFA, IEF, SPY (etf, 1d)
**Found at:** iteration 3197 of optimization.log (2026-11-27T12:28:31Z); written at the checkpoint in iteration 4838; backtest.py version `164566c210`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 19,172.17)

## Parameters

| parameter | value |
|---|---|
| max_candles | 273 |
| n | 315 |
| stop_loss_pct | 20 |

```json
{
  "max_candles": 273,
  "n": 315,
  "stop_loss_pct": 20
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 31,213.92 | 9,241.37 |
| return % | 312.14 | 92.41 |
| return %/year | 12.5 | 6.2 |
| gross profit | 36,637.98 | 16,785.57 |
| gross loss | 5,424.07 | 7,544.20 |
| trades | 20 | 27 |
| win rate % | 65.0 | 70.4 |
| avg win | 2,818.31 | 883.45 |
| avg loss | -774.87 | -943.03 |
| avg result / trade | 1,560.70 | 342.27 |
| largest single loss | -1,168.01 | -3,075.43 |
| largest loss % of equity | -2.72 | -20.10 |
| max drawdown | -5,600.52 | -4,436.15 |
| max drawdown % | -17.46 | -27.64 |
| profit factor | 6.75 | 2.23 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 7.1 | 9.0 |
| time in market % | 32.0 | 32.5 |
| buy & hold return % | 97.27 | 157.89 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.49 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Dual momentum allocation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end choose the higher ROC(252) asset among SPY/EFA if its ROC(252) exceeds IEF ROC(252); otherwise choose IEF if its ROC(252) > 0, else cash. Assign 100% to selected asset.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell any asset not chosen by this rule.
- **Formal:** Higher ROC(n) of SPY/EFA if it beats IEF's ROC(n); else IEF if its ROC(n) > 0; else cash.
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
| Universe | EFA, IEF, SPY |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2004-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | `--min-trades-is 10` (one asset at a time: about 1-2 full exits a year by construction) |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 252 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 756} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SPY/EFA ties go to EFA (ticker order).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
