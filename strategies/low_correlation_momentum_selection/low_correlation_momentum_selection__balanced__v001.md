# low_correlation_momentum_selection: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 122 of optimization.log (2026-11-27T11:55:57Z); written at the checkpoint in iteration 257; backtest.py version `86f922c15c`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 23,714.94)

## Parameters

| parameter | value |
|---|---|
| corr | 0.65 |
| k | 3 |
| max_candles | 294 |
| stop_loss_pct | 8 |

```json
{
  "corr": 0.65,
  "k": 3,
  "max_candles": 294,
  "stop_loss_pct": 8
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 28,911.92 | 9,100.56 |
| return % | 289.12 | 91.01 |
| return %/year | 12.0 | 6.1 |
| gross profit | 44,841.59 | 22,962.29 |
| gross loss | 15,929.67 | 13,861.73 |
| trades | 84 | 89 |
| win rate % | 61.9 | 47.2 |
| avg win | 862.34 | 546.72 |
| avg loss | -497.80 | -294.93 |
| avg result / trade | 344.19 | 102.25 |
| largest single loss | -2,947.92 | -858.66 |
| largest loss % of equity | -7.03 | -4.06 |
| max drawdown | -6,067.23 | -4,411.25 |
| max drawdown % | -18.57 | -24.66 |
| profit factor | 2.81 | 1.66 |
| unusually bad trades | 3 | 1 |
| … threshold (% of equity) | 3.2 | 4.8 |
| time in market % | 30.9 | 32.6 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.51 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Low-correlation momentum selection (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end sort positive ROC(126) assets descending by ROC(126); greedily select up to 3, admitting each only if its 126-day daily-return correlation with every earlier selected asset is < 0.6; equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets not in the newly selected group.
- **Formal:** Positive ROC(126) assets sorted descending; greedily admit up to k, each only if its 126-day daily-return correlation with every already selected asset is < corr (undefined correlations are skipped, INDICATORS.md); equal weight.
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
| `corr` | 0.6 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 2, "max": 5, "step": 1, "hard_min": 1, "hard_max": 8} |
| `corr` | {"min": 0.3, "max": 0.9, "step": 0.05, "hard_min": 0.0, "hard_max": 1.0} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- correlation pairs with fewer than 3 common returns or zero variance are skipped (not blocking), per INDICATORS.md 'skips undefined correlations'. ROC and correlation windows stay 126.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
