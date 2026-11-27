# stock_bond_paired_switch: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY, TLT (etf, 1d)
**Found at:** iteration 35 of optimization.log (2026-11-27T11:49:14Z); written at the checkpoint in iteration 6305; backtest.py version `c52945f714`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 9,387.61)

## Parameters

| parameter | value |
|---|---|
| max_candles | 252 |
| n | 42 |
| stop_loss_pct | 20 |

```json
{
  "max_candles": 252,
  "n": 42,
  "stop_loss_pct": 20
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 10,505.52 | 7,985.07 |
| return % | 105.06 | 79.85 |
| return %/year | 6.2 | 5.5 |
| gross profit | 17,481.46 | 16,008.02 |
| gross loss | 6,975.94 | 8,022.95 |
| trades | 46 | 42 |
| win rate % | 56.5 | 47.6 |
| avg win | 672.36 | 800.40 |
| avg loss | -348.80 | -364.68 |
| avg result / trade | 228.38 | 190.12 |
| largest single loss | -821.09 | -1,417.15 |
| largest loss % of equity | -8.16 | -9.24 |
| max drawdown | -2,420.35 | -4,943.08 |
| max drawdown % | -22.66 | -29.78 |
| profit factor | 2.51 | 2.00 |
| unusually bad trades | 4 | 6 |
| … threshold (% of equity) | 4.6 | 3.7 |
| time in market % | 45.5 | 42.0 |
| buy & hold return % | 127.89 | 159.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.90 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Stock-bond paired switch (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end choose the higher ROC(126) asset among SPY/TLT; allocate 100% if winner ROC(126) > 0, otherwise cash.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell when the chosen asset changes or fails positive momentum.
- **Formal:** 100 % in the higher ROC(n) of SPY/TLT if that ROC(n) > 0; else cash.
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
| Universe | SPY, TLT |
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
| `n` | {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 504} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SPY/TLT ties go to SPY (ticker order).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
