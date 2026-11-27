# sector_roc_rotation: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 1344 of optimization.log (2026-11-27T11:49:52Z); written at the checkpoint in iteration 12688; backtest.py version `0771a883af`
**Replaces:** sector_roc_rotation__safe-starter__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 10,865.39)

## Parameters

| parameter | value |
|---|---|
| k | 8 |
| max_candles | 189 |
| n | 357 |
| stop_loss_pct | 2 |

```json
{
  "k": 8,
  "max_candles": 189,
  "n": 357,
  "stop_loss_pct": 2
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 12,204.72 | 8,216.42 |
| return % | 122.05 | 82.16 |
| return %/year | 5.3 | 5.7 |
| gross profit | 22,677.01 | 16,471.25 |
| gross loss | 10,472.30 | 8,254.83 |
| trades | 325 | 310 |
| win rate % | 28.6 | 26.8 |
| avg win | 243.84 | 198.45 |
| avg loss | -45.14 | -36.36 |
| avg result / trade | 37.55 | 26.50 |
| largest single loss | -150.25 | -76.35 |
| largest loss % of equity | -0.64 | -0.42 |
| max drawdown | -2,055.12 | -2,181.78 |
| max drawdown % | -8.50 | -16.56 |
| profit factor | 2.17 | 2.00 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 39.8 | 47.7 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.07 |
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
