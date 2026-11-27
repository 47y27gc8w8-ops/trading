# three_bar_momentum_thrust__broad: max-income v002

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 283 of optimization.log (2026-11-26T01:51:44Z); written at the checkpoint in iteration 807; backtest.py version `b419c00cd0`
**Replaces:** three_bar_momentum_thrust__broad__max-income__v001.md
**Robustness:** 7/7 one-step neighbours profitable in-sample (worst neighbour net 499.44)

## Parameters

| parameter | value |
|---|---|
| max_candles | 51 |
| roc | 9.5 |
| stop_atr | 4.25 |
| take_profit_atr | 7.0 |

```json
{
  "max_candles": 51,
  "roc": 9.5,
  "stop_atr": 4.25,
  "take_profit_atr": 7.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,710.35 | 770.18 |
| return % | 17.10 | 7.70 |
| return %/year | 2.7 | 2.6 |
| gross profit | 23,219.15 | 7,462.78 |
| gross loss | 21,508.81 | 6,692.60 |
| trades | 1,514 | 707 |
| win rate % | 32.9 | 33.2 |
| avg win | 46.62 | 31.76 |
| avg loss | -21.17 | -14.18 |
| avg result / trade | 1.13 | 1.09 |
| largest single loss | -646.02 | -100.62 |
| largest loss % of equity | -19.24 | -14.27 |
| max drawdown | -6,605.95 | -1,289.78 |
| max drawdown % | -36.92 | -11.30 |
| profit factor | 1.08 | 1.11 |
| unusually bad trades | 106 | 66 |
| … threshold (% of equity) | 8.2 | 6.8 |
| time in market % | 1.9 | 1.7 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.96 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

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
