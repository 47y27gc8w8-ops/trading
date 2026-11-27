# rolling_resistance_retest: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** ETHUSDT (crypto, 4h)
**Found at:** iteration 1278 of optimization.log (2026-11-26T01:33:57Z); written at the checkpoint in iteration 12880; backtest.py version `629aa0a90b`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/8 one-step neighbours profitable in-sample (worst neighbour net -1,153.44)

## Parameters

| parameter | value |
|---|---|
| max_candles | 78 |
| n | 45 |
| stop_atr | 2.0 |
| take_profit_atr | 3.0 |

```json
{
  "max_candles": 78,
  "n": 45,
  "stop_atr": 2.0,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 361.95 | 68.36 |
| return % | 3.62 | 0.68 |
| return %/year | 0.6 | 0.2 |
| gross profit | 7,840.70 | 1,517.44 |
| gross loss | 7,478.75 | 1,449.07 |
| trades | 27 | 7 |
| win rate % | 44.4 | 42.9 |
| avg win | 653.39 | 505.81 |
| avg loss | -498.58 | -362.27 |
| avg result / trade | 13.41 | 9.77 |
| largest single loss | -1,036.86 | -444.17 |
| largest loss % of equity | -9.41 | -3.86 |
| max drawdown | -2,220.84 | -1,918.01 |
| max drawdown % | -17.65 | -16.00 |
| profit factor | 1.05 | 1.05 |
| unusually bad trades | 2 | 0 |
| … threshold (% of equity) | 7.7 | 6.7 |
| time in market % | 2.3 | 1.1 |
| buy & hold return % | 110.38 | -25.03 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.40 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Rolling Resistance Retest

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/rolling_resistance_retest.py.

## Idea
Breakout, retest of the broken resistance, then continuation.

## Market
- Base symbol: ETHUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: at t−2 C > B with B = HH(H,n)[3] (frozen); at t−1 L ≤ B and C ≥ B; at t C > H[1]. Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: C < the frozen B at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| n | resistance lookback (bars) | 20 | 10–60 (5) |
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
- B at the signal bar t is HH(H, n) as of t−3, i.e. the level the t−2 close broke; it's frozen at entry (engine entry_level hook).

---
Backtest results don't guarantee future performance.
