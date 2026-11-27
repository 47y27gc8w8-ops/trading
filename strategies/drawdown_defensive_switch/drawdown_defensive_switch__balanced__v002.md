# drawdown_defensive_switch: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** IEF, SPY (etf, 1d)
**Found at:** iteration 659 of optimization.log (2026-11-27T12:17:46Z); written at the checkpoint in iteration 850; backtest.py version `71d2033794`
**Replaces:** drawdown_defensive_switch__balanced__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 13,163.05)

## Parameters

| parameter | value |
|---|---|
| dd | 6 |
| max_candles | 189 |
| n | 105 |
| stop_loss_pct | 7 |

```json
{
  "dd": 6,
  "max_candles": 189,
  "n": 105,
  "stop_loss_pct": 7
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 21,088.13 | 10,954.75 |
| return % | 210.88 | 109.55 |
| return %/year | 9.9 | 7.0 |
| gross profit | 24,884.51 | 15,201.55 |
| gross loss | 3,796.38 | 4,246.81 |
| trades | 25 | 24 |
| win rate % | 76.0 | 62.5 |
| avg win | 1,309.71 | 1,013.44 |
| avg loss | -632.73 | -471.87 |
| avg result / trade | 843.53 | 456.45 |
| largest single loss | -1,485.69 | -1,178.42 |
| largest loss % of equity | -7.12 | -7.12 |
| max drawdown | -2,602.39 | -4,620.84 |
| max drawdown % | -12.46 | -25.41 |
| profit factor | 6.55 | 3.58 |
| unusually bad trades | 2 | 3 |
| … threshold (% of equity) | 4.2 | 3.1 |
| time in market % | 46.9 | 42.1 |
| buy & hold return % | 107.13 | 169.81 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.71 |
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
