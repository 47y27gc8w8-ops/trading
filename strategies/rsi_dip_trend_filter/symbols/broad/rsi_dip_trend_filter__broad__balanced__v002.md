# rsi_dip_trend_filter__broad: balanced v002

**Profile:** balanced: best net profit / max drawdown with a solid win rate.
**Symbols:** BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, TRXUSDT, ZECUSDT, DOGEUSDT, LINKUSDT, ADAUSDT, XLMUSDT, BCHUSDT, NEARUSDT, LTCUSDT, AVAXUSDT, UNIUSDT, HBARUSDT, SHIBUSDT, AAVEUSDT, JSTUSDT, DOTUSDT, ICPUSDT, ETCUSDT, ALGOUSDT, ATOMUSDT, INJUSDT, CAKEUSDT, STXUSDT, FILUSDT, DASHUSDT, VETUSDT (crypto, 4h)
**Found at:** iteration 719 of optimization.log (2026-11-25T22:40:46Z); written at the checkpoint in iteration 1226; backtest.py version `81be9c69a6`
**Replaces:** rsi_dip_trend_filter__broad__balanced__v001.md
**Robustness:** 10/10 one-step neighbours profitable in-sample (worst neighbour net 918.76)

## Parameters

| parameter | value |
|---|---|
| buy | 16 |
| exit | 55 |
| max_candles | 24 |
| n | 6 |
| stop_atr | 4.0 |
| take_profit_atr | 3.0 |

```json
{
  "buy": 16,
  "exit": 55,
  "max_candles": 24,
  "n": 6,
  "stop_atr": 4.0,
  "take_profit_atr": 3.0
}
```

## Metrics

Capital 10,000 USD, 100% of equity per trade, fee 0.1% per side, slippage 0.1% per fill.

| metric | in-sample | out-of-sample |
|---|---|---|
| net profit | 2,777.83 | 469.73 |
| return % | 27.78 | 4.70 |
| return %/year | 4.2 | 1.6 |
| gross profit | 5,298.87 | 2,333.18 |
| gross loss | 2,521.04 | 1,863.45 |
| trades | 382 | 268 |
| win rate % | 70.7 | 60.1 |
| avg win | 19.63 | 14.49 |
| avg loss | -22.51 | -17.42 |
| avg result / trade | 7.27 | 1.75 |
| largest single loss | -62.35 | -65.64 |
| largest loss % of equity | -16.59 | -17.06 |
| max drawdown | -494.65 | -1,025.99 |
| max drawdown % | -4.05 | -10.05 |
| profit factor | 2.10 | 1.25 |
| unusually bad trades | 15 | 28 |
| … threshold (% of equity) | 11.4 | 8.2 |
| time in market % | 1.0 | 1.4 |
| buy & hold return % | 450.49 | 71.18 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.38 |
| period | 2018-01-31 → 2023-12-31 | 2024-01-01 → 2026-11-23 |

## Rules (strategy.md at the time of saving)

# Rsi Dip Trend Filter

Source: original.md (research-library spec, 2026-11), with ../../EXECUTION.md and ../../INDICATORS.md.
This file is the testable version; backtest.py is generated from scripts/strategy_library/defs/rsi_dip_trend_filter.py.

## Idea
RSI oversold dip above the 200-bar SMA.

## Market
- Base symbol: BTCUSDT (Binance spot, USDT quote = the spec's USD), 4h bars built from 1m data (UTC)
- Screening: the project's 60-coin crypto list; broad basket over every coin the screen marks ok
- Long only, one position at a time per symbol

## Buy trigger
At a bar close: RSI(n) < buy and C > SMA(200). Buy at the next bar open.
Entry veto: no entry if the close-based exit below is already true on the signal bar.

## Sell trigger (first of)
- Signal exit: RSI(n) > exit at a bar close → sell at the next open
- Stop: low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` held bars (entry bar = 1) → sell at the next open
- Stop is assumed before the target when one bar touches both
(E = entry fill, A = ATR(14) of the signal bar, both frozen at entry; entry skipped if A ≤ 0 or the stop ≤ 0)

After an intrabar stop/target exit, one fully flat bar must complete before the next signal.

## Parameters
| name | meaning | spec value | range (step) |
|---|---|---|---|
| n | RSI length | 14 | 7–21 (1) |
| buy | oversold level | 30 | 20–40 (2) |
| exit | exit level | 55 | 45–70 (5) |
| stop_atr | stop distance × ATR(14) | 2 | 1–4 (0.25) |
| take_profit_atr | target distance × ATR(14) | 3 | 1.5–6 (0.5) |
| max_candles | held bars before time exit | 12 | 6–24 (2) |

`risk_fraction` (spec 0.005) is not used: the user chose 100% of equity per trade (2026-11-24).

## Setup
- In-sample 2018-01-01 → 2024-01-01, out-of-sample 2024-01-01 → 2026-11-23 (frozen end)
- Warm-up: 1000 bars of each coin's own history before it may trade (≥ 5× the longest recursive period)
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fee 0.10% per side, slippage 0.10% per fill (spec: 10 bp commission, 5 bp half-spread + 5 bp slippage)

## Assumptions
- Volume = Binance quote volume (USDT), the only volume the loader provides; the spec says base-unit volume. Ratios (RVOL, MFI, VWMA weights) are nearly unaffected.
- Prices from one venue (Binance spot USDT), as the spec requires a single exchange.
- Spec lists BTC and ETH as alternatives: BTC is the base run, ETH and the rest come from screening.
- buy < exit enforced.

---
Backtest results don't guarantee future performance.
