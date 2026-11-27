# drawdown_defensive_switch: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** IEF, SPY (etf, 1d)
**Found at:** iteration 176 of optimization.log (2026-11-27T12:16:27Z); written at the checkpoint in iteration 291; backtest.py version `71d2033794`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 13,359.82)
**Range warning:** dd is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| dd | 5 |
| max_candles | 189 |
| n | 210 |
| stop_loss_pct | 22 |

```json
{
  "dd": 5,
  "max_candles": 189,
  "n": 210,
  "stop_loss_pct": 22
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 15,800.26 | 15,655.96 |
| return % | 158.00 | 156.56 |
| return %/year | 8.2 | 9.0 |
| gross profit | 17,494.63 | 17,952.61 |
| gross loss | 1,694.37 | 2,296.65 |
| trades | 26 | 22 |
| win rate % | 76.9 | 68.2 |
| avg win | 874.73 | 1,196.84 |
| avg loss | -282.39 | -328.09 |
| avg result / trade | 607.70 | 711.63 |
| largest single loss | -449.15 | -747.18 |
| largest loss % of equity | -1.71 | -4.05 |
| max drawdown | -2,159.74 | -3,173.79 |
| max drawdown % | -12.02 | -13.31 |
| profit factor | 10.32 | 7.82 |
| unusually bad trades | 0 | 1 |
| … threshold (% of equity) | 3.6 | 3.1 |
| time in market % | 46.1 | 40.0 |
| buy & hold return % | 107.13 | 169.81 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.10 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Drawdown defensive switch (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end if SPY drawdown from its trailing 252-bar maximum close is better than -10% select SPY; else choose IEF only if IEF>SMA(200), otherwise cash. Allocate 100% to chosen asset.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell the previous asset when selection changes.
- **Formal:** SPY if its drawdown from HH(C, n) is better than -dd %; else IEF if IEF > SMA(200); else cash.
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
| Universe | IEF, SPY |
| Data | Yahoo daily, dividend/split adjusted |
| In-sample | 2004-01-01 -> 2016-01-01 |
| Out-of-sample | 2016-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.05 % + slippage 0.03 % per fill |
| Optimizer settings | `--min-trades-is 10` (one asset at a time: about 1-2 full exits a year by construction) |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 252 |
| `dd` | 10.0 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 126, "max": 300, "step": 21, "hard_min": 21, "hard_max": 756} |
| `dd` | {"min": 5.0, "max": 20.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- n is the window of SPY's trailing maximum close; IEF's SMA(200) is a fixed constant.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
