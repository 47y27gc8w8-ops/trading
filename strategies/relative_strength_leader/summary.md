# relative_strength_leader: optimization summary

Updated 2026-11-25T13:29:15Z · backtest.py version `e67222673e` · 42,440 parameter sets tested with this version (42,440 rows in results.csv in total) · last run ended: see base optimization.log

## Setup

- Data: MSFT (etf, 1d bars)
- In-sample (tuning): 2000-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [relative_strength_leader__max-income__v001.md](relative_strength_leader__max-income__v001.md) | 42440 | `{"max_candles": 84, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| balanced | [relative_strength_leader__balanced__v001.md](relative_strength_leader__balanced__v001.md) | 42440 | `{"max_candles": 84, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | flat (data up to 2026-11-24 00:00) |
| safe-starter | none | | | |

Note: one parameter set wins max-income, balanced. The search found no meaningfully different trade-off, so none is forced.

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS |
|---|---|---|---|---|
| net profit | 1,502.00 | 800.25 | 1,502.00 | 800.25 |
| return % | 15.02 | 8.00 | 15.02 | 8.00 |
| return %/year | 0.9 | 0.7 | 0.9 | 0.7 |
| gross profit | 8,951.53 | 5,888.31 | 8,951.53 | 5,888.31 |
| gross loss | 7,449.53 | 5,088.06 | 7,449.53 | 5,088.06 |
| trades | 71 | 46 | 71 | 46 |
| win rate % | 53.5 | 54.4 | 53.5 | 54.4 |
| avg win | 235.57 | 235.53 | 235.57 | 235.53 |
| avg loss | -225.74 | -242.29 | -225.74 | -242.29 |
| avg result / trade | 21.15 | 17.40 | 21.15 | 17.40 |
| largest single loss | -820.45 | -696.56 | -820.45 | -696.56 |
| largest loss % of equity | -8.14 | -6.35 | -8.14 | -6.35 |
| max drawdown | -1,837.59 | -1,971.42 | -1,837.59 | -1,971.42 |
| max drawdown % | -17.12 | -16.23 | -17.12 | -16.23 |
| profit factor | 1.20 | 1.16 | 1.20 | 1.16 |
| unusually bad trades | 9 | 6 | 9 | 6 |
| … threshold (% of equity) | 2.7 | 3.3 | 2.7 | 3.3 |
| time in market % | 5.6 | 6.3 | 5.6 | 6.3 |
| buy & hold return % | 35.51 | 944.05 | 35.51 | 944.05 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.81 |  | 0.81 |
| period | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-01-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced |
|---|---|---|
| 2000 | -7.4 | -7.4 |
| 2001 | -1.3 | -1.3 |
| 2002 | 0.0 | 0.0 |
| 2003 | 4.2 | 4.2 |
| 2004 | -0.6 | -0.6 |
| 2005 | -0.3 | -0.3 |
| 2006 | -3.2 | -3.2 |
| 2007 | 8.8 | 8.8 |
| 2008 | -5.9 | -5.9 |
| 2009 | 13.0 | 13.0 |
| 2010 | 3.5 | 3.5 |
| 2011 | 0.5 | 0.5 |
| 2012 | 0.4 | 0.4 |
| 2013 | -1.6 | -1.6 |
| 2014 | 2.5 | 2.5 |
| 2015 | 3.2 | 3.2 |
| 2016 (OOS) | -1.3 | -1.3 |
| 2017 (OOS) | 6.7 | 6.7 |
| 2018 (OOS) | 4.9 | 4.9 |
| 2019 (OOS) | 3.0 | 3.0 |
| 2020 (OOS) | 0.4 | 0.4 |
| 2021 (OOS) | 0.2 | 0.2 |
| 2022 (OOS) | -5.5 | -5.5 |
| 2023 (OOS) | 7.1 | 7.1 |
| 2024 (OOS) | -3.8 | -3.8 |
| 2025 (OOS) | -8.1 | -8.1 |
| 2026 (OOS) | 5.2 | 5.2 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 16.2% out-of-sample, and the worst single trade cost 6.3% of the account out-of-sample. About 54 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 58% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 17.1% from a peak in-sample and 16.2% out-of-sample, and the worst single trade cost 6.3% of the account out-of-sample. About 54 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 58% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | `{"max_candles": 84, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | 0.83 |
| 21 | `{"max_candles": 84, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 23 | `{"max_candles": 72, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 24 | `{"max_candles": 96, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 86 | `{"max_candles": 48, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 234 | `{"max_candles": 48, "n": 90, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 695.04 | 0.6 | -16.3 | 0.70 | 71/46 | not checked |
| 619 | `{"max_candles": 132, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 814 | `{"max_candles": 120, "n": 90, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 1158 | `{"max_candles": 96, "n": 90, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 695.04 | 0.6 | -16.3 | 0.70 | 71/46 | not checked |
| 1466 | `{"max_candles": 156, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 1529 | `{"max_candles": 192, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 1731 | `{"max_candles": 180, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 1999 | `{"max_candles": 180, "n": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 358.60 | 0.3 | -15.8 | 0.36 | 71/46 | not checked |
| 2210 | `{"max_candles": 84, "n": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 358.60 | 0.3 | -15.8 | 0.36 | 71/46 | not checked |
| 2438 | `{"max_candles": 168, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 2836 | `{"max_candles": 120, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 3016 | `{"max_candles": 180, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 3025 | `{"max_candles": 60, "n": 90, "stop_atr": 4.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 3278 | `{"max_candles": 156, "n": 90, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 695.04 | 0.6 | -16.3 | 0.70 | 71/46 | not checked |
| 3388 | `{"max_candles": 60, "n": 90, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 695.04 | 0.6 | -16.3 | 0.70 | 71/46 | not checked |
| 3615 | `{"max_candles": 132, "n": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 358.60 | 0.3 | -15.8 | 0.36 | 71/46 | not checked |
| 3777 | `{"max_candles": 108, "n": 90, "stop_atr": 3.75, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 3963 | `{"max_candles": 108, "n": 90, "stop_atr": 3.0, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 358.60 | 0.3 | -15.8 | 0.36 | 71/46 | not checked |
| 4081 | `{"max_candles": 132, "n": 90, "stop_atr": 3.5, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 800.25 | 0.7 | -16.2 | 0.81 | 71/46 | not checked |
| 5269 | `{"max_candles": 108, "n": 90, "stop_atr": 3.25, "take_profit_atr": 1.5}` | 1,502.00 | 0.9 | -17.1 | 53.5 | 695.04 | 0.6 | -16.3 | 0.70 | 71/46 | not checked |

(105 more on the front, see results.csv)

## Screening: where does the strategy work? (in-sample ranking)

468 of 538 symbols had enough history. Ranked by how much of the sampled parameter space is profitable in-sample (a strategy that only works for one lucky setting on a symbol ranks low). OOS columns are shown for information and were not used for the ranking.

| # | symbol | profitable sets IS | median IS %/yr | best IS %/yr | buy&hold IS %/yr | default IS %/yr | default OOS %/yr | sets passing all gates |
|---|---|---|---|---|---|---|---|---|
| 1 | MO | 100% | 4.7 | 10.2 | 22.4 | 3.6 | 1.1 | 20 |
| 2 | O | 100% | 3.6 | 7.3 | 17.5 | 3.5 | 1.3 | 16 |
| 3 | TRMB | 98% | 6.5 | 11.7 | 10.9 | 7.4 | 0.7 | 30 |
| 4 | TSCO | 98% | 3.2 | 13.6 | 32.5 | 7.0 | 1.2 | 25 |
| 5 | AFL | 98% | 2.1 | 5.5 | 7.9 | 2.4 | 1.4 | 46 |
| 6 | EXR | 97% | 9.2 | 18.0 | 25.2 | 10.5 | 1.1 | 40 |
| 7 | MA | 97% | 6.2 | 13.9 | 27.3 | 6.4 | 0.6 | 12 |
| 8 | DAL | 97% | 5.6 | 15.7 | 37.1 | 12.8 | 0.9 | 29 |
| 9 | V | 97% | 4.3 | 10.3 | 27.3 | 3.8 | -1.7 | 8 |
| 10 | BX | 97% | 4.0 | 11.5 | 14.0 | 8.7 | -0.8 | 21 |
| 11 | ESS | 97% | 4.0 | 6.8 | 17.7 | 5.7 | -0.9 | 3 |
| 12 | HST | 97% | 3.9 | 9.9 | 7.1 | 4.1 | -5.9 | 7 |
| 13 | COO | 97% | 3.5 | 10.3 | 14.8 | 5.8 | 0.6 | 12 |
| 14 | ARE | 97% | 2.9 | 7.0 | 10.8 | 5.2 | -1.2 | 2 |
| 15 | DTE | 97% | 2.6 | 5.8 | 11.2 | 4.0 | 0.7 | 29 |
| 16 | FE | 97% | 2.1 | 5.6 | 7.0 | 2.9 | 1.6 | 36 |
| 17 | DXCM | 95% | 6.9 | 19.6 | 21.5 | 8.0 | -0.5 | 10 |
| 18 | TDG | 95% | 5.7 | 11.1 | 32.2 | 4.8 | 1.3 | 25 |
| 19 | DHI | 95% | 5.5 | 10.7 | 15.8 | 9.8 | -0.9 | 26 |
| 20 | SPG | 95% | 5.5 | 11.1 | 20.0 | 8.6 | -0.6 | 24 |
| 21 | FRT | 95% | 5.2 | 8.3 | 18.9 | 3.8 | 2.3 | 27 |
| 22 | MCO | 95% | 4.8 | 10.1 | 15.9 | 6.0 | 2.9 | 22 |
| 23 | HSIC | 95% | 3.8 | 10.4 | 21.6 | 3.5 | -2.2 | 2 |
| 24 | UDR | 95% | 3.4 | 6.7 | 15.5 | 2.8 | -1.6 | 8 |
| 25 | BKNG | 95% | 2.3 | 7.3 | 10.7 | -0.6 | 0.8 | 25 |
| 26 | SRE | 95% | 2.3 | 4.9 | 15.2 | 4.0 | -2.9 | 0 |
| 27 | MCK | 95% | 1.9 | 5.5 | 15.2 | 0.4 | -0.9 | 47 |
| 28 | ULTA | 94% | 10.7 | 18.1 | 56.2 | 15.7 | 2.4 | 10 |
| 29 | PODD | 94% | 8.5 | 20.9 | 12.8 | 11.3 | -1.1 | 22 |
| 30 | MELI | 94% | 6.7 | 21.4 | 29.6 | 14.1 | -0.5 | 32 |
| 31 | MNST | 94% | 5.3 | 16.8 | 48.5 | -1.0 | 2.6 | 33 |
| 32 | REG | 94% | 5.1 | 9.2 | 13.7 | 4.8 | 3.3 | 14 |
| 33 | STX | 94% | 4.3 | 10.7 | 9.2 | 4.3 | 3.4 | 18 |
| 34 | KDP | 94% | 4.1 | 13.6 | 27.5 | 3.2 | -3.1 | 7 |
| 35 | COR | 94% | 3.7 | 8.6 | 23.9 | 5.4 | -0.8 | 9 |
| 36 | PAYX | 94% | 3.3 | 7.2 | 7.2 | 4.8 | 2.0 | 19 |
| 37 | ROST | 94% | 2.8 | 7.7 | 23.0 | 7.7 | 1.6 | 3 |
| 38 | D | 94% | 2.4 | 4.4 | 12.6 | 1.8 | -1.0 | 3 |
| 39 | ED | 94% | 1.8 | 4.6 | 9.4 | 1.7 | 1.2 | 35 |
| 40 | AIG | 94% | 1.6 | 7.9 | -16.4 | 1.3 | 2.2 | 42 |

(428 more in screen.csv)

## Results by symbol / basket

Each row is a separate optimization (symbols/<tag>/). Conservative %/yr = the lower of in-sample and out-of-sample.

| symbols | profile | file | IS %/yr | OOS %/yr | conservative %/yr | worst max DD % | win % IS | trades IS/OOS |
|---|---|---|---|---|---|---|---|---|
| broad | max-income | [relative_strength_leader__broad__max-income__v002.md](symbols/broad/relative_strength_leader__broad__max-income__v002.md) | 3.2 | 2.6 | 2.6 | -7.2 | 35.0 | 32740/25865 |
| broad | balanced | [relative_strength_leader__broad__balanced__v001.md](symbols/broad/relative_strength_leader__broad__balanced__v001.md) | 0.6 | 0.2 | 0.2 | -4.2 | 46.3 | 53428/40331 |


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 42,440 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
