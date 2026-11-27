# rolling_resistance_retest__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 103 of optimization.log (2026-11-26T01:36:58Z); written at the checkpoint in iteration 195; backtest.py version `b2278f94a6`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 430.07)
**Range warning:** n is at the min of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 60 |
| n | 10 |
| stop_atr | 3.75 |
| take_profit_atr | 5.5 |

```json
{
  "max_candles": 60,
  "n": 10,
  "stop_atr": 3.75,
  "take_profit_atr": 5.5
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 959.03 | 123.07 |
| return % | 9.59 | 1.23 |
| return %/year | 1.6 | 0.4 |
| gross profit | 14,523.93 | 7,568.35 |
| gross loss | 13,564.90 | 7,445.28 |
| trades | 1,060 | 796 |
| win rate % | 29.2 | 28.6 |
| avg win | 46.85 | 33.19 |
| avg loss | -18.09 | -13.11 |
| avg result / trade | 0.90 | 0.15 |
| largest single loss | -115.35 | -145.96 |
| largest loss % of equity | -21.05 | -30.96 |
| max drawdown | -1,429.73 | -1,033.27 |
| max drawdown % | -11.92 | -9.72 |
| profit factor | 1.07 | 1.02 |
| unusually bad trades | 91 | 64 |
| … threshold (% of equity) | 9.0 | 6.8 |
| time in market % | 4.2 | 6.1 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.27 |
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
