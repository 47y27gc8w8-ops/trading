# crypto_equal_weight_rebalance: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, LTCUSDT, SOLUSDT (crypto, 1d)
**Found at:** iteration 379 of optimization.log (2026-11-27T12:07:35Z); written at the checkpoint in iteration 435; backtest.py version `7d4096a16d`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 4/4 one-step neighbours profitable in-sample (worst neighbour net 58,294.78)

## Parameters

| parameter | value |
|---|---|
| max_candles | 84 |
| stop_loss_pct | 13 |

```json
{
  "max_candles": 84,
  "stop_loss_pct": 13
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 87,619.78 | 4,693.99 |
| return % | 876.20 | 46.94 |
| return %/year | 46.2 | 14.2 |
| gross profit | 216,450.17 | 29,491.80 |
| gross loss | 128,830.38 | 24,797.81 |
| trades | 139 | 70 |
| win rate % | 32.4 | 34.3 |
| avg win | 4,810.00 | 1,228.83 |
| avg loss | -1,370.54 | -539.08 |
| avg result / trade | 630.36 | 67.06 |
| largest single loss | -3,756.43 | -731.26 |
| largest loss % of equity | -3.31 | -3.31 |
| max drawdown | -94,613.00 | -12,622.63 |
| max drawdown % | -70.90 | -51.54 |
| profit factor | 1.68 | 1.19 |
| unusually bad trades | 0 | 0 |
| … threshold (% of equity) | 6.6 | 6.6 |
| time in market % | 63.0 | 71.0 |
| buy & hold return % | 955.32 | -13.09 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.31 |
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
