# sector_roc_rotation: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 51 of optimization.log (2026-11-27T11:43:19Z); written at the checkpoint in iteration 274; backtest.py version `0771a883af`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 27,691.63)
**Range warning:** k is at the max of its range, n is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| k | 5 |
| max_candles | 441 |
| n | 252 |
| stop_loss_pct | 18 |

```json
{
  "k": 5,
  "max_candles": 441,
  "n": 252,
  "stop_loss_pct": 18
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 29,505.76 | 11,698.21 |
| return % | 295.06 | 116.98 |
| return %/year | 9.3 | 7.4 |
| gross profit | 36,343.39 | 20,647.61 |
| gross loss | 6,837.62 | 8,949.40 |
| trades | 117 | 127 |
| win rate % | 68.4 | 54.3 |
| avg win | 454.29 | 299.24 |
| avg loss | -184.80 | -154.30 |
| avg result / trade | 252.19 | 92.11 |
| largest single loss | -1,517.02 | -590.59 |
| largest loss % of equity | -3.61 | -3.78 |
| max drawdown | -5,449.34 | -3,190.50 |
| max drawdown % | -18.91 | -23.04 |
| profit factor | 5.32 | 2.31 |
| unusually bad trades | 1 | 12 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 31.1 | 37.4 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.80 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Sector ROC rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** On each month-end select the top 3 sectors by ROC(63), only if SPY > its SMA(200); equal-weight selected assets.
- **Spec rebalance exit:** Signal/rebalance exit: At each month-end sell assets no longer selected or if SPY <= SMA(200).
- **Formal:** Top k sectors by ROC(n), only while SPY > SMA(200) (SPY is a reference, not traded); equal weight.
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
| Universe | XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY  (reference, not traded: SPY) |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2000-07-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `k` | 3 |
| `n` | 63 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `n` | {"min": 21, "max": 252, "step": 21, "hard_min": 5, "hard_max": 380} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SPY is loaded as a signal-only reference series (never traded).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
