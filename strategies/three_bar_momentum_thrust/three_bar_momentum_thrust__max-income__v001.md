# three_bar_momentum_thrust: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** SOLUSDT (crypto, 4h)
**Found at:** iteration 702 of optimization.log (2026-11-26T01:41:55Z); written at the checkpoint in iteration 24669; backtest.py version `ee689764b5`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 5/7 one-step neighbours profitable in-sample (worst neighbour net -697.31)

## Parameters

| parameter | value |
|---|---|
| max_candles | 42 |
| roc | 10.0 |
| stop_atr | 3.5 |
| take_profit_atr | 2.5 |

```json
{
  "max_candles": 42,
  "roc": 10.0,
  "stop_atr": 3.5,
  "take_profit_atr": 2.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,038.62 | 530.48 |
| return % | 20.39 | 5.30 |
| return %/year | 6.5 | 1.8 |
| gross profit | 14,765.82 | 2,092.51 |
| gross loss | 12,727.20 | 1,562.04 |
| trades | 51 | 11 |
| win rate % | 43.1 | 54.5 |
| avg win | 671.17 | 348.75 |
| avg loss | -438.87 | -312.41 |
| avg result / trade | 39.97 | 48.23 |
| largest single loss | -992.49 | -576.99 |
| largest loss % of equity | -9.20 | -5.32 |
| max drawdown | -5,032.03 | -1,510.00 |
| max drawdown % | -45.24 | -13.36 |
| profit factor | 1.16 | 1.34 |
| unusually bad trades | 3 | 1 |
| … threshold (% of equity) | 9.1 | 5.2 |
| time in market % | 2.6 | 0.8 |
| buy & hold return % | 2,768.91 | -29.19 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.28 |
| period | 2021-01-24 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Three Bar Momentum Thrust

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/three_bar_momentum_thrust.py.

## Idea
Momentum: three rising bullish bars with a strong 3-bar return in a trending market.

## Market
- Base symbol: SOLUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: C > O on t, t−1, t−2; C > C[1] > C[2]; ROC(3) > roc %; ADX(14) > 20. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C < L[1] at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| roc | min 3-bar return, % | 4 | 2–10 (0.5) |
| stop_atr | stop distance × ATR(14) | 2 | 1–4 (0.25) |
| take_profit_atr | target distance × ATR(14) | 3 | 1.5–6 (0.5) |
| max_candles | held bars before time exit | 48 | 24–96 (9) |

`risk_fraction` (spec 0.005) is not used: the user chose 100% of equity per trade (2026-11-24).

## Setup
- In-sample 2018-01-01 → 2024-01-01, out-of-sample 2024-01-01 → 2026-11-23 (frozen end)
- Warm-up: 1000 bars of each coin's own history before it may trade (≥ 5× the longest recursive period)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fee 0.10% per side, slippage 0.10% per fill (spec: 10 bp commission, 5 bp half-spread + 5 bp slippage)

## Assumptions
- Volume = Binance quote volume (USDT), the only volume the loader provides; the spec says base-unit volume. Ratios (RVOL, MFI, VWMA weights) are nearly unaffected.
- Prices from one venue (Binance spot USDT), as the spec requires a single exchange.
- 'Increasing closes' = C[2] < C[1] < C (the three bars themselves).

---
Backtest results don't guarantee future performance.
