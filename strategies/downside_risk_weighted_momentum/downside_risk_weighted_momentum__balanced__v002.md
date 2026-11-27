# downside_risk_weighted_momentum: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 342 of optimization.log (2026-11-27T11:44:45Z); written at the checkpoint in iteration 843; backtest.py version `fa213e948c`
**Replaces:** downside_risk_weighted_momentum__balanced__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 11,328.80)

## Parameters

| parameter | value |
|---|---|
| k | 6 |
| max_candles | 462 |
| n | 252 |
| stop_loss_pct | 14 |

```json
{
  "k": 6,
  "max_candles": 462,
  "n": 252,
  "stop_loss_pct": 14
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 14,626.17 | 3,848.16 |
| return % | 146.26 | 38.48 |
| return %/year | 7.8 | 3.0 |
| gross profit | 20,031.38 | 9,597.20 |
| gross loss | 5,405.21 | 5,749.04 |
| trades | 77 | 68 |
| win rate % | 57.1 | 44.1 |
| avg win | 455.26 | 319.91 |
| avg loss | -163.79 | -151.29 |
| avg result / trade | 189.95 | 56.59 |
| largest single loss | -566.76 | -712.74 |
| largest loss % of equity | -2.58 | -5.94 |
| max drawdown | -2,168.08 | -3,491.07 |
| max drawdown % | -12.52 | -27.96 |
| profit factor | 3.71 | 1.67 |
| unusually bad trades | 4 | 7 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 60.5 | 58.9 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.39 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Downside-risk weighted momentum (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end select top 3 positive ROC(126) assets; set weights proportional to inverse downside deviation over 126 daily returns, normalized to 100%.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell assets outside the selected group and rebalance weights.
- **Formal:** Top k positive ROC(n); weights proportional to 1/downside deviation over n returns, normalized to 100 % after dropping invalid / zero-risk values.
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
| `n` | 126 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1, "max": 5, "step": 1, "hard_min": 1, "hard_max": 8} |
| `n` | {"min": 63, "max": 252, "step": 21, "hard_min": 21, "hard_max": 504} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- the single parameter n drives both the ROC lookback and the downside-deviation window (both 126 in the spec).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
