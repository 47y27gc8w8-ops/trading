# high_proximity_leader_rotation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 85 of optimization.log (2026-11-27T11:43:21Z); written at the checkpoint in iteration 251; backtest.py version `b629cd4b61`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/5 one-step neighbours profitable in-sample (worst neighbour net 8,796.12)
**Range warning:** n is at the max of its range, k is at the max of its range, stop_loss_pct is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 231 |
| n | 294 |
| stop_loss_pct | 25 |

```json
{
  "k": 5,
  "max_candles": 231,
  "n": 294,
  "stop_loss_pct": 25
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 10,913.67 | 17,600.23 |
| return % | 109.14 | 176.00 |
| return %/year | 4.9 | 9.8 |
| gross profit | 27,171.73 | 34,294.82 |
| gross loss | 16,258.06 | 16,694.59 |
| trades | 205 | 187 |
| win rate % | 59.0 | 57.8 |
| avg win | 224.56 | 317.54 |
| avg loss | -193.55 | -211.32 |
| avg result / trade | 53.24 | 94.12 |
| largest single loss | -1,707.38 | -1,706.60 |
| largest loss % of equity | -13.15 | -11.64 |
| max drawdown | -5,026.19 | -4,926.17 |
| max drawdown % | -38.52 | -30.36 |
| profit factor | 1.67 | 2.05 |
| unusually bad trades | 9 | 7 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 37.2 | 41.6 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.00 |
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
