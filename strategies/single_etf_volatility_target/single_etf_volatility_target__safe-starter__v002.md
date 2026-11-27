# single_etf_volatility_target: safe-starter v002

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** SPY (etf, 1d)
**Found at:** iteration 6318 of optimization.log (2026-11-27T12:13:14Z); written at the checkpoint in iteration 12688; backtest.py version `e2f6a72d5f`
**Replaces:** single_etf_volatility_target__safe-starter__v001.md
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 3,551.83)

## Parameters

| parameter | value |
|---|---|
| max_candles | 315 |
| stop_loss_pct | 7 |
| target | 0.03 |

```json
{
  "max_candles": 315,
  "stop_loss_pct": 7,
  "target": 0.03
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 5,739.27 | 2,660.42 |
| return % | 57.39 | 26.60 |
| return %/year | 2.1 | 2.2 |
| gross profit | 6,397.13 | 3,437.87 |
| gross loss | 657.86 | 777.45 |
| trades | 19 | 13 |
| win rate % | 79.0 | 46.1 |
| avg win | 426.48 | 572.98 |
| avg loss | -164.46 | -111.06 |
| avg result / trade | 302.07 | 204.65 |
| largest single loss | -270.16 | -185.09 |
| largest loss % of equity | -2.70 | -1.54 |
| max drawdown | -558.89 | -653.39 |
| max drawdown % | -3.87 | -5.36 |
| profit factor | 9.72 | 4.42 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 2.9 | 2.0 |
| time in market % | 73.3 | 79.7 |
| buy & hold return % | 555.68 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.05 |
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
