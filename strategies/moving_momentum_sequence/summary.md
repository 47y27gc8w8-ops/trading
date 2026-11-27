# moving_momentum_sequence: optimization summary

Updated 2026-11-25T23:54:44Z · backtest.py version `0abd94298e` · 18,616 parameter sets tested with this version (18,616 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: SPY (etf, 1d bars)
- In-sample (tuning): 1995-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [moving_momentum_sequence__max-income__v001.md](moving_momentum_sequence__max-income__v001.md) | 18616 | `{"max_candles": 108, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |
| balanced | [moving_momentum_sequence__balanced__v001.md](moving_momentum_sequence__balanced__v001.md) | 18616 | `{"max_candles": 108, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 4.5}` | flat (data up to 2026-11-25 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 668.26 | 1,177.09 | 668.26 | 1,177.09 |
| return % | 6.68 | 11.77 | 6.68 | 11.77 |
| return %/year | 0.3 | 1.0 | 0.3 | 1.0 |
| gross profit | 1,478.48 | 1,212.95 | 1,478.48 | 1,212.95 |
| gross loss | 810.22 | 35.86 | 810.22 | 35.86 |
| trades | 23 | 7 | 23 | 7 |
| win rate % | 60.9 | 85.7 | 60.9 | 85.7 |
| avg win | 105.61 | 202.16 | 105.61 | 202.16 |
| avg loss | -90.02 | -35.86 | -90.02 | -35.86 |
| avg result / trade | 29.05 | 168.16 | 29.05 | 168.16 |
| largest single loss | -308.22 | -35.86 | -308.22 | -35.86 |
| largest loss % of equity | -2.81 | -0.32 | -2.81 | -0.32 |
| max drawdown | -386.05 | -151.02 | -386.05 | -151.02 |
| max drawdown % | -3.77 | -1.42 | -3.77 | -1.42 |
| profit factor | 1.82 | 33.82 | 1.82 | 33.82 |
| unusually bad trades | 2 | 0 | 2 | 0 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 1.4 | 0.5 | 1.4 | 0.5 |
| buy & hold return % | 551.07 | 328.39 | 551.07 | 328.39 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 3.32 |  | 3.32 |
| period | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 1995-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 1995 | 0.0 | 0.0 |
| 1996 | 0.0 | 0.0 |
| 1997 | 1.3 | 1.3 |
| 1998 | 0.0 | 0.0 |
| 1999 | -0.1 | -0.1 |
| 2000 | 4.7 | 4.7 |
| 2001 | 0.0 | 0.0 |
| 2002 | 0.0 | 0.0 |
| 2003 | 1.2 | 1.2 |
| 2004 | -0.1 | -0.1 |
| 2005 | -0.2 | -0.2 |
| 2006 | -2.5 | -2.5 |
| 2007 | 0.0 | 0.0 |
| 2008 | 0.0 | 0.0 |
| 2009 | 2.4 | 2.4 |
| 2010 | 0.2 | 0.2 |
| 2011 | -0.6 | -0.6 |
| 2012 | 1.1 | 1.1 |
| 2013 | 1.2 | 1.2 |
| 2014 | -0.4 | -0.4 |
| 2015 | -1.5 | -1.5 |
| 2016 (OOS) | 2.2 | 2.2 |
| 2017 (OOS) | 0.0 | 0.0 |
| 2018 (OOS) | 0.0 | 0.0 |
| 2019 (OOS) | 1.6 | 1.6 |
| 2020 (OOS) | 7.2 | 7.2 |
| 2021 (OOS) | 0.0 | 0.0 |
| 2022 (OOS) | 0.0 | 0.0 |
| 2023 (OOS) | 0.4 | 0.4 |
| 2024 (OOS) | 0.4 | 0.4 |
| 2025 (OOS) | 0.0 | 0.0 |
| 2026 (OOS) | -0.3 | -0.3 |

### Risk in plain language

- **max-income**: Risk looks low: the account fell up to 3.8% from a peak in-sample and 1.4% out-of-sample, and the worst single trade cost 0.3% of the account out-of-sample. About 61 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).
- **balanced**: Risk looks low: the account fell up to 3.8% from a peak in-sample and 1.4% out-of-sample, and the worst single trade cost 0.3% of the account out-of-sample. About 61 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 86 | `{"max_candles": 96, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 242 | `{"max_candles": 48, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 1171 | `{"max_candles": 168, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 1204 | `{"max_candles": 192, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 6395 | `{"max_candles": 144, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 6955 | `{"max_candles": 60, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 8169 | `{"max_candles": 156, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 12902 | `{"max_candles": 72, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 13228 | `{"max_candles": 132, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 13324 | `{"max_candles": 180, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 13858 | `{"max_candles": 120, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 14004 | `{"max_candles": 84, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |
| 17277 | `{"max_candles": 108, "oversold": 16, "stop_atr": 2.0, "take_profit_atr": 2.5}` | 680.45 | 0.3 | -3.8 | 60.9 | 1,177.09 | 1.0 | -1.4 | 3.32 | 23/7 | not checked |

## Screening: where does the strategy work? (in-sample ranking)

53 of 64 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | QQQ | 68% | 0.7 | 1.5 | 0.6 | 0.9 | -0.1 | 1 |
| 2 | XLE | 66% | 1.4 | 2.3 | 7.0 | 2.0 | -0.8 | 0 |
| 3 | XLP | 66% | 0.4 | 0.8 | 7.5 | 0.4 | 0.1 | 0 |
| 4 | XLI | 66% | 0.4 | 0.8 | 5.9 | 0.2 | 2.1 | 41 |
| 5 | XLF | 60% | 0.4 | 0.7 | 2.2 | 0.6 | 0.9 | 35 |
| 6 | DIA | 58% | 0.2 | 0.4 | 6.1 | 0.1 | 1.1 | 36 |
| 7 | XLV | 55% | 0.2 | 0.4 | 7.1 | 0.3 | 1.0 | 34 |
| 8 | XLB | 52% | 0.2 | 0.6 | 5.7 | 0.5 | 0.9 | 32 |
| 9 | TIP | 39% | 0.1 | 0.3 | 3.8 | 0.2 | -0.6 | 0 |
| 10 | VTV | 27% | -0.1 | 0.4 | 6.9 | -0.1 | 1.2 | 17 |
| 11 | VTI | 16% | -0.0 | 0.2 | 7.9 | 0.2 | 0.9 | 10 |
| 12 | IVV | 15% | -0.0 | 0.3 | 5.2 | -0.0 | 1.5 | 9 |
| 13 | BND | 11% | 0.1 | 0.2 | 3.9 | 0.1 | -0.2 | 0 |
| 14 | SPY | 11% | -0.3 | 0.3 | 9.3 | -0.3 | 1.5 | 7 |
| 15 | VNQ | 10% | 0.5 | 1.0 | 7.8 | 0.4 | 0.4 | 2 |
| 16 | XLY | 10% | -0.3 | 0.2 | 7.4 | -0.5 | -0.8 | 0 |
| 17 | EFA | 8% | -0.4 | 0.2 | 6.7 | 0.0 | -0.9 | 0 |
| 18 | RSP | 6% | -0.3 | 0.2 | 8.5 | -0.3 | 0.5 | 4 |
| 19 | CSSPX.SW | 5% | 1.0 | 0.5 | 11.3 | 1.3 | 0.4 | 3 |
| 20 | TLT | 3% | -0.6 | 0.1 | 6.9 | -0.8 | -0.9 | 0 |
| 21 | CSSMI.SW | 2% | 0.2 | 0.3 | 8.7 | -0.2 | 0.1 | 1 |
| 22 | XLK | 2% | -0.5 | 0.2 | -0.1 | -0.8 | 1.2 | 1 |
| 23 | SLV | 0% | 1.6 | n/a | -0.1 | -0.1 | 2.1 | 0 |
| 24 | GDX | 0% | 1.5 | n/a | -10.7 | 1.7 | -1.4 | 0 |
| 25 | CSPX.L | 0% | 1.3 | n/a | 16.2 | 1.6 | 7.0 | 0 |
| 26 | DBC | 0% | 1.3 | n/a | -6.1 | 1.4 | 0.0 | 0 |
| 27 | SQQQ | 0% | 1.2 | n/a | -47.0 | 1.2 | -0.8 | 0 |
| 28 | SCHD | 0% | 1.1 | n/a | 12.3 | 1.2 | 0.3 | 0 |
| 29 | USMV | 0% | 1.1 | n/a | 13.4 | 1.9 | 0.8 | 0 |
| 30 | VWRL.SW | 0% | 0.9 | n/a | 5.5 | 1.1 | 0.1 | 0 |
| 31 | VXUS | 0% | 0.8 | n/a | 3.5 | 0.8 | 0.2 | 0 |
| 32 | VOO | 0% | 0.6 | n/a | 16.7 | 0.5 | 1.5 | 0 |
| 33 | VT | 0% | 0.1 | n/a | 10.5 | 0.6 | 0.7 | 0 |
| 34 | ACWI | 0% | -0.0 | n/a | 12.6 | 0.3 | 0.5 | 0 |
| 35 | HYG | 0% | -0.0 | n/a | 5.0 | 0.0 | 0.1 | 0 |
| 36 | CSNDX.SW | 0% | -0.1 | n/a | 15.9 | -0.1 | 0.1 | 0 |
| 37 | AGG | 0% | -0.1 | n/a | 4.1 | -0.1 | -0.5 | 0 |
| 38 | VIG | 0% | -0.2 | n/a | 6.2 | -0.3 | 0.7 | 0 |
| 39 | SHY | 0% | -0.3 | n/a | 2.1 | -0.3 | -0.3 | 0 |
| 40 | USO | 0% | -0.3 | n/a | -16.0 | 0.2 | -1.4 | 0 |

(13 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [moving_momentum_sequence__broad__max-income__v002.md](symbols/broad/moving_momentum_sequence__broad__max-income__v002.md) | 0.1 | 0.5 | 0.1 | -1.6 | 61.9 | 651/554 |
| broad | balanced | [moving_momentum_sequence__broad__balanced__v002.md](symbols/broad/moving_momentum_sequence__broad__balanced__v002.md) | 0.0 | 0.1 | 0.0 | -0.4 | 63.0 | 73/80 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 18,616 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
