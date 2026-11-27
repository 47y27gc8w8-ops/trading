# inverse_volatility_trend_basket: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** DBC, EEM, EFA, GLD, IEF, SPY, TLT, VNQ (etf, 1d)
**Found at:** iteration 333 of optimization.log (2026-11-27T11:51:52Z); written at the checkpoint in iteration 844; backtest.py version `aa09d6f490`
**Replaces:** inverse_volatility_trend_basket__max-income__v001.md
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 12,930.17)

## Parameters

| parameter | value |
|---|---|
| max_candles | 399 |
| n | 170 |
| stop_loss_pct | 16 |

```json
{
  "max_candles": 399,
  "n": 170,
  "stop_loss_pct": 16
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.05% per side, slippage 0.03% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 15,275.68 | 10,996.85 |
| return % | 152.76 | 109.97 |
| return %/year | 8.0 | 7.0 |
| gross profit | 24,137.29 | 19,909.57 |
| gross loss | 8,861.62 | 8,912.72 |
| trades | 96 | 101 |
| win rate % | 44.8 | 45.5 |
| avg win | 561.33 | 432.82 |
| avg loss | -167.20 | -162.05 |
| avg result / trade | 159.12 | 108.88 |
| largest single loss | -637.30 | -2,020.85 |
| largest loss % of equity | -2.48 | -10.92 |
| max drawdown | -3,058.94 | -5,400.74 |
| max drawdown % | -13.32 | -26.01 |
| profit factor | 2.72 | 2.23 |
| unusually bad trades | 3 | 3 |
| … threshold (% of equity) | 2.0 | 2.0 |
| time in market % | 63.2 | 65.5 |
| buy & hold return % | 98.52 | 132.14 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.88 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Inverse-volatility trend basket (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At month-end retain all assets above SMA(200); assign weights proportional to 1/Std(daily returns,63), normalized to sum to 100%.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end remove assets below SMA(200) and resize remaining positions.
- **Formal:** All assets with C > SMA(n); weights proportional to 1/Std(daily returns, 63), normalized.
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
| `n` | 200 |
| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 100, "max": 300, "step": 10, "hard_min": 20, "hard_max": 500} |
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- n is the SMA length; the volatility window stays 63.
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
