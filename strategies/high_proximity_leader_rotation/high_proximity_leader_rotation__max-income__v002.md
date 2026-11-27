# high_proximity_leader_rotation: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 338 of optimization.log (2026-11-27T11:44:45Z); written at the checkpoint in iteration 1059; backtest.py version `b629cd4b61`
**Replaces:** high_proximity_leader_rotation__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 8,718.35)

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 273 |
| n | 294 |
| stop_loss_pct | 27 |

```json
{
  "k": 5,
  "max_candles": 273,
  "n": 294,
  "stop_loss_pct": 27
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,558.84 | 16,823.88 |
| return % | 125.59 | 168.24 |
| return %/year | 5.4 | 9.5 |
| gross profit | 27,399.79 | 32,978.02 |
| gross loss | 14,840.96 | 16,154.14 |
| trades | 202 | 185 |
| win rate % | 59.4 | 57.3 |
| avg win | 228.33 | 311.11 |
| avg loss | -180.99 | -204.48 |
| avg result / trade | 62.17 | 90.94 |
| largest single loss | -1,712.17 | -1,670.49 |
| largest loss % of equity | -13.15 | -11.66 |
| max drawdown | -5,040.28 | -4,820.52 |
| max drawdown % | -38.52 | -30.36 |
| profit factor | 1.85 | 2.04 |
| unusually bad trades | 7 | 7 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 37.3 | 41.7 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.76 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# High-proximity leader rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end score=C/HH(C,252); choose top 3 assets with C>SMA(200); equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside selected group or below SMA(200).
- **Formal:** score = C / HH(C, n); top k among C > SMA(200); equal weight.
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
| `n` | 252 |
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 380} |
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SMA(200) fixed; n is the HH(C, n) window.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
