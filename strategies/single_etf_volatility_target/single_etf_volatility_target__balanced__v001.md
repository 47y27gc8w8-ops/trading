# single_etf_volatility_target: balanced v001

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 187 of optimization.log (2026-11-27T11:51:58Z); written at the checkpoint in iteration 5588; backtest.py version `e2f6a72d5f`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 12,192.32)

## Parameters

| parameter | value |
|---|---|
| max_candles | 210 |
| stop_loss_pct | 13 |
| target | 0.06 |

```json
{
  "max_candles": 210,
  "stop_loss_pct": 13,
  "target": 0.06
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 15,922.34 | 5,374.30 |
| return % | 159.22 | 53.74 |
| return %/year | 4.4 | 4.0 |
| gross profit | 19,150.47 | 7,389.77 |
| gross loss | 3,228.13 | 2,015.47 |
| trades | 25 | 16 |
| win rate % | 72.0 | 50.0 |
| avg win | 1,063.92 | 923.72 |
| avg loss | -461.16 | -251.93 |
| avg result / trade | 636.89 | 335.89 |
| largest single loss | -723.29 | -598.83 |
| largest loss % of equity | -3.64 | -4.55 |
| max drawdown | -1,096.91 | -1,405.13 |
| max drawdown % | -8.00 | -9.80 |
| profit factor | 5.93 | 3.67 |
| unusually bad trades | 1 | 1 |
| … threshold (% of equity) | 4.9 | 2.6 |
| time in market % | 70.5 | 80.5 |
| buy & hold return % | 555.68 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.91 |
| period | 1994-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Single ETF volatility target (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end if SPY>SMA(200), target weight=min(1, 0.1/annualized daily volatility over 63 bars); residual stays cash.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end reduce to the recomputed weight or sell fully if SPY<=SMA(200).
- **Formal:** If SPY > SMA(200): weight = min(1, target / (Std(daily returns, 63) * sqrt(252))); rest cash.
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
| Universe | SPY |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 1994-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | `--min-trades-is 10` (one asset at a time: about 1-2 full exits a year by construction) |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `target` | 0.1 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `target` | {"min": 0.05, "max": 0.2, "step": 0.01, "hard_min": 0.01, "hard_max": 1.0} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- volatility annualized with sqrt(252); weight capped at 1 (no leverage).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
