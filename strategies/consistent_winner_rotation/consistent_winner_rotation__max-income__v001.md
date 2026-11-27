# consistent_winner_rotation: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d)
**Found at:** iteration 35 of optimization.log (2026-11-27T11:43:09Z); written at the checkpoint in iteration 214; backtest.py version `ee39969495`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 5,622.49)

## Parameters

| parameter | value |
|---|---|
| k | 3 |
| max_candles | 231 |
| n | 11 |
| stop_loss_pct | 15.0 |

```json
{
  "k": 3,
  "max_candles": 231,
  "n": 11,
  "stop_loss_pct": 15.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 9,967.65 | 15,979.89 |
| return % | 99.68 | 159.80 |
| return %/year | 4.6 | 9.2 |
| gross profit | 26,419.33 | 36,057.73 |
| gross loss | 16,451.68 | 20,077.84 |
| trades | 143 | 103 |
| win rate % | 55.9 | 50.5 |
| avg win | 330.24 | 693.42 |
| avg loss | -261.14 | -393.68 |
| avg result / trade | 69.70 | 155.14 |
| largest single loss | -1,126.73 | -1,219.34 |
| largest loss % of equity | -5.04 | -5.49 |
| max drawdown | -4,849.49 | -6,705.35 |
| max drawdown % | -43.24 | -27.90 |
| profit factor | 1.61 | 1.80 |
| unusually bad trades | 12 | 11 |
| … threshold (% of equity) | 2.9 | 3.0 |
| time in market % | 23.1 | 25.8 |
| buy & hold return % | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 2.01 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Consistent winner rotation (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end score=number of positive monthly total returns in the last 12 completed months; select top 3 assets with ROC(126)>0, breaking score ties by ROC(126) then ticker; equal-weight.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside the selected group.
- **Formal:** score = positive monthly total returns in the last n completed months; eligible ROC(126) > 0; top k by (score, ROC(126), ticker); equal weight.
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
| `n` | 12 |
| `k` | 3 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 6, "max": 24, "step": 1, "hard_min": 1, "hard_max": 60} |
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 11} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- n counts completed MONTHS (month-end to month-end total returns), as the spec's '12 completed months' implies; ROC(126) stays fixed at 126 daily bars.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
