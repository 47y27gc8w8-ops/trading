# three_bar_momentum_thrust__broad: max-income v001

**Profile:** max-income: highest in-sample net profit among variants that are also profitable out-of-sample. May be risky.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 143 of optimization.log (2026-11-26T01:50:52Z); written at the checkpoint in iteration 188; backtest.py version `b419c00cd0`
**Replaces:** nothing (first variant for this profile)
**Robustness:** 6/6 one-step neighbours profitable in-sample (worst neighbour net 93.42)
**Range warning:** stop_atr is at the max of its range, take_profit_atr is at the max of its range; the optimum may lie outside the searched range.

## Parameters

| parameter | value |
|---|---|
| max_candles | 60 |
| roc | 9.5 |
| stop_atr | 4.0 |
| take_profit_atr | 6.0 |

```json
{
  "max_candles": 60,
  "roc": 9.5,
  "stop_atr": 4.0,
  "take_profit_atr": 6.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 1,498.10 | 565.67 |
| return % | 14.98 | 5.66 |
| return %/year | 2.4 | 1.9 |
| gross profit | 22,305.91 | 7,309.95 |
| gross loss | 20,807.81 | 6,744.28 |
| trades | 1,524 | 715 |
| win rate % | 33.1 | 33.3 |
| avg win | 44.17 | 30.71 |
| avg loss | -20.42 | -14.14 |
| avg result / trade | 0.98 | 0.79 |
| largest single loss | -542.28 | -86.66 |
| largest loss % of equity | -15.15 | -14.27 |
| max drawdown | -6,308.81 | -1,322.92 |
| max drawdown % | -36.14 | -11.77 |
| profit factor | 1.07 | 1.08 |
| unusually bad trades | 106 | 67 |
| … threshold (% of equity) | 8.2 | 6.8 |
| time in market % | 1.9 | 1.6 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.80 |
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
