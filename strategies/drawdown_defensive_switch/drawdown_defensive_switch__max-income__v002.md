# drawdown_defensive_switch: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** IEF, SPY (etf, 1d)
**Found at:** iteration 339 of optimization.log (2026-11-27T12:16:52Z); written at the checkpoint in iteration 849; backtest.py version `71d2033794`
**Replaces:** drawdown_defensive_switch__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 16,171.87)

## Parameters

| parameter | value |
|---|---|
| dd | 9 |
| max_candles | 252 |
| n | 105 |
| stop_loss_pct | 24 |

```json
{
  "dd": 9,
  "max_candles": 252,
  "n": 105,
  "stop_loss_pct": 24
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 22,666.96 | 28,493.38 |
| return % | 226.67 | 284.93 |
| return %/year | 10.4 | 13.2 |
| gross profit | 26,337.66 | 34,129.84 |
| gross loss | 3,670.69 | 5,636.46 |
| trades | 17 | 15 |
| win rate % | 64.7 | 66.7 |
| avg win | 2,394.33 | 3,412.98 |
| avg loss | -611.78 | -1,127.29 |
| avg result / trade | 1,333.35 | 1,899.56 |
| largest single loss | -999.34 | -1,397.76 |
| largest loss % of equity | -8.25 | -5.65 |
| max drawdown | -4,986.85 | -6,080.13 |
| max drawdown % | -19.80 | -22.52 |
| profit factor | 7.17 | 6.05 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 4.5 | 11.3 |
| time in market % | 47.3 | 44.4 |
| buy & hold return % | 107.13 | 169.81 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 1.27 |
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
