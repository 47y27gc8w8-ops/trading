# crypto_equal_weight_rebalance: safe-starter v001

**Profile:** safe-starter: smallest max drawdown plus largest single loss, few or no unusually bad trades, still a minimum yearly return. A low-risk starting point.
**Symbols:** BTCUSDT, ETHUSDT, LTCUSDT, SOLUSDT (crypto, 1d)
**Found at:** iteration 352 of optimization.log (2026-11-27T12:07:31Z); written at the checkpoint in iteration 436; backtest.py version `7d4096a16d`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 3/3 one-step neighbours profitable in-sample (worst neighbour net 42,823.05)

## Parameters

| parameter | value |
|---|---|
| max_candles | 42 |
| stop_loss_pct | 11 |

```json
{
  "max_candles": 42,
  "stop_loss_pct": 11
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 59,176.73 | 3,036.62 |
| return % | 591.77 | 30.37 |
| return %/year | 38.1 | 9.6 |
| gross profit | 176,256.82 | 26,099.71 |
| gross loss | 117,080.08 | 23,063.08 |
| trades | 180 | 90 |
| win rate % | 30.0 | 41.1 |
| avg win | 3,264.02 | 705.40 |
| avg loss | -929.21 | -435.15 |
| avg result / trade | 328.76 | 33.74 |
| largest single loss | -2,369.07 | -601.38 |
| largest loss % of equity | -2.82 | -2.84 |
| max drawdown | -51,081.10 | -11,053.51 |
| max drawdown % | -58.23 | -47.05 |
| profit factor | 1.50 | 1.13 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 5.6 | 5.6 |
| time in market % | 46.2 | 51.4 |
| buy & hold return % | 955.32 | -13.09 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.25 |
| period | 2018-01-01 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Crypto equal-weight rebalance (formalized)

Source: `original.md` (library spec), EXECUTION.md / INDICATORS.md conventions. Code: `backtest.py`
(built by `scripts/portfolio_lib/build.py`; rule = `target_weights()`).

## Rule
- **Spec buy trigger:** At each month-end buy underweight components to restore 25% weights across the fixed four-coin basket.
- **Spec rebalance exit:** Signal/rebalance exit: At month-end sell overweight components back to 25%; otherwise only stop/time exits.
- **Formal:** Fixed 25 % per coin of the four-coin basket (no trend filter). A coin not listed yet keeps its 25 % in cash (fixed component allocations, EXECUTION.md: no renormalizing).
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
| Universe | BTCUSDT, ETHUSDT, LTCUSDT, SOLUSDT |
| Data | Binance 1m -> UTC daily bars |
| In-sample | 2018-01-01 -> 2024-01-01 |
| Out-of-sample | 2024-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, 100 % split by the rule's weights |
| Costs | fee 0.10 % + slippage 0.10 % per fill |
| Optimizer settings | defaults |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|

| `stop_loss_pct` | 15.0 |
| `max_candles` | 252 |

## Search space
| Parameter | Range |
|---|---|
| `stop_loss_pct` | {"min": 8.0, "max": 25.0, "step": 1.0, "hard_min": 2.0, "hard_max": 50.0} |
| `max_candles` | {"min": 126, "max": 504, "step": 21, "hard_min": 21, "hard_max": 1260} |

## Assumptions
- SOL (listed on Binance 2020-08) keeps its 25 % in cash before listing: the rule is a fixed four-coin allocation, so the other coins are not scaled up (EXECUTION.md: 'unless the rule keeps fixed component allocations'). Binance USDT pairs stand in for the spec's BTC/USD etc. (one venue, USD-pegged quote).
- point-in-time universe: a member joins once it is listed and its indicators exist; before that it is not part of the ranking (same as breadth_scaled_sector_allocation). EXECUTION.md's 'skip the rebalance if a member lacks history' would otherwise move the start to the youngest ETF's listing (XLC 2018, DBC 2006).
- cash earns 0 %: EXECUTION.md allows this only as the labelled conservative scenario; none of these rules needs a cash yield (no excess-cash momentum), so ^IRX isn't used.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), same as the other library runs, so leaderboard entries compare.
- Yahoo adjusted closes (dividends reinvested) serve as both the signal (total-return) and the fill series, like every other library run; EXECUTION.md's separate raw execution series isn't available.
- participation cap (1 % of volume) not modelled: a 10k sleeve in liquid ETFs/coins never reaches it.
- every month-end decision restores the target weights, trimming drift too; trims keep the holding's cost basis, stop and age, and don't close a trade (a trade = first buy to full exit).

---
Backtest results don't guarantee future performance.
