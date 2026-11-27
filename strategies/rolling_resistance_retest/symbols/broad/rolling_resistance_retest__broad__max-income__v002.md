# rolling_resistance_retest__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 427 of optimization.log (2026-11-26T01:38:28Z); written at the checkpoint in iteration 916; backtest.py version `b2278f94a6`
**Replaces:** rolling_resistance_retest__broad__max-income__v001.md
**Robustness:** 8/8 one-step neighbours profitable in-sample (worst neighbour net 1,568.02)

## Parameters

| parameter | value |
|---|---|
| max_candles | 42 |
| n | 7 |
| stop_atr | 3.75 |
| take_profit_atr | 9.5 |

```json
{
  "max_candles": 42,
  "n": 7,
  "stop_atr": 3.75,
  "take_profit_atr": 9.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 6,690.34 | 881.01 |
| return % | 66.90 | 8.81 |
| return %/year | 9.1 | 3.0 |
| gross profit | 25,407.78 | 9,980.51 |
| gross loss | 18,717.43 | 9,099.50 |
| trades | 1,222 | 941 |
| win rate % | 29.8 | 27.9 |
| avg win | 69.80 | 37.95 |
| avg loss | -21.82 | -13.42 |
| avg result / trade | 5.47 | 0.94 |
| largest single loss | -439.61 | -128.80 |
| largest loss % of equity | -10.64 | -30.96 |
| max drawdown | -1,608.35 | -1,265.14 |
| max drawdown % | -10.28 | -11.09 |
| profit factor | 1.36 | 1.10 |
| unusually bad trades | 103 | 64 |
| … threshold (% of equity) | 8.8 | 6.9 |
| time in market % | 5.5 | 8.6 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.33 |
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
