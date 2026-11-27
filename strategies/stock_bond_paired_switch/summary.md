# stock_bond_paired_switch: optimization summary

Updated 2026-11-27T12:06:48Z · backtest.py version `c52945f714` · 6,306 parameter sets tested with this version (6,306 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: SPY, TLT (etf, 1d bars)
- In-sample (tuning): 2004-01-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [stock_bond_paired_switch__max-income__v001.md](stock_bond_paired_switch__max-income__v001.md) | 6304 | `{"max_candles": 252, "n": 84, "stop_loss_pct": 20}` | long SPY since 2026-05-01 00:00 @ 717.829936 |
| balanced | [stock_bond_paired_switch__balanced__v001.md](stock_bond_paired_switch__balanced__v001.md) | 6305 | `{"max_candles": 252, "n": 42, "stop_loss_pct": 20}` | long TLT since 2026-11-02 00:00 @ 81.854551 |
| safe-starter | [stock_bond_paired_switch__safe-starter__v001.md](stock_bond_paired_switch__safe-starter__v001.md) | 6306 | `{"max_candles": 273, "n": 252, "stop_loss_pct": 25}` | long SPY since 2026-10-01 00:00 @ 764.589293 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 21,260.88 | 7,449.73 | 10,505.52 | 7,985.07 | 9,373.89 | 13,921.73 |
| return % | 212.61 | 74.50 | 105.06 | 79.85 | 93.74 | 139.22 |
| return %/year | 10.0 | 5.2 | 6.2 | 5.5 | 5.7 | 8.3 |
| gross profit | 30,749.23 | 15,023.08 | 17,481.46 | 16,008.02 | 14,786.97 | 20,836.77 |
| gross loss | 9,488.35 | 7,573.35 | 6,975.94 | 8,022.95 | 5,413.07 | 6,915.04 |
| trades | 28 | 31 | 46 | 42 | 24 | 18 |
| win rate % | 60.7 | 51.6 | 56.5 | 47.6 | 62.5 | 50.0 |
| avg win | 1,808.78 | 938.94 | 672.36 | 800.40 | 985.80 | 2,315.20 |
| avg loss | -862.58 | -504.89 | -348.80 | -364.68 | -601.45 | -768.34 |
| avg result / trade | 759.32 | 240.31 | 228.38 | 190.12 | 390.58 | 773.43 |
| largest single loss | -2,920.08 | -1,200.83 | -821.09 | -1,417.15 | -1,843.63 | -1,974.83 |
| largest loss % of equity | -8.39 | -6.45 | -8.16 | -9.24 | -8.58 | -12.70 |
| max drawdown | -9,258.53 | -2,681.06 | -2,420.35 | -4,943.08 | -5,072.11 | -3,797.63 |
| max drawdown % | -23.31 | -18.83 | -22.66 | -29.78 | -27.54 | -19.35 |
| profit factor | 3.24 | 1.98 | 2.51 | 2.00 | 2.73 | 3.01 |
| unusually bad trades | 3 | 0 | 4 | 6 | 1 | 1 |
| … threshold (% of equity) | 4.4 | 7.8 | 4.6 | 3.7 | 7.4 | 11.0 |
| time in market % | 45.5 | 43.5 | 45.5 | 42.0 | 48.7 | 43.6 |
| buy & hold return % | 127.89 | 159.80 | 127.89 | 159.80 | 127.89 | 159.80 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.53 |  | 0.90 |  | 1.47 |
| period | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2004-01-02 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2004 | 1.7 | -4.0 | 1.4 |
| 2005 | 9.2 | -8.1 | -2.0 |
| 2006 | 12.7 | 17.3 | 10.9 |
| 2007 | 6.4 | -7.0 | 1.3 |
| 2008 | 16.2 | 6.7 | 34.0 |
| 2009 | 6.4 | 3.5 | 1.9 |
| 2010 | 19.9 | -3.2 | -3.0 |
| 2011 | 37.0 | 32.2 | -9.1 |
| 2012 | -11.9 | 1.5 | 3.2 |
| 2013 | 26.7 | 28.1 | 32.3 |
| 2014 | 19.8 | 12.7 | 19.6 |
| 2015 | -13.6 | 2.8 | -11.6 |
| 2016 (OOS) | -3.9 | 3.3 | -8.2 |
| 2017 (OOS) | 13.0 | 13.4 | 21.7 |
| 2018 (OOS) | -2.2 | -6.7 | -8.8 |
| 2019 (OOS) | 3.7 | -2.8 | 2.0 |
| 2020 (OOS) | 16.3 | 26.6 | 9.6 |
| 2021 (OOS) | 17.1 | 18.1 | 28.8 |
| 2022 (OOS) | -9.9 | -25.5 | -12.7 |
| 2023 (OOS) | 8.8 | 13.3 | 15.6 |
| 2024 (OOS) | 17.1 | 14.3 | 23.4 |
| 2025 (OOS) | 1.5 | 16.7 | 16.6 |
| 2026 (OOS) | -3.9 | -1.1 | 6.0 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 23.3% from a peak in-sample and 18.8% out-of-sample, and the worst single trade cost 6.5% of the account out-of-sample. About 61 of every 100 trades won in-sample. Out-of-sample it earned 5.2% a year against 10.0% in-sample, so expect clearly less than the in-sample numbers suggest. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 43% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 22.7% from a peak in-sample and 29.8% out-of-sample, and the worst single trade cost 9.2% of the account out-of-sample. About 57 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 34% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 27.5% from a peak in-sample and 19.4% out-of-sample, and the worst single trade cost 12.7% of the account out-of-sample. About 62 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 36% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 243 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 23}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 588 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 18}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 1501 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 15}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 2208 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 24}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 2352 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 21}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 2403 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 17}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 2870 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 16}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 3188 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 25}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 3256 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 14}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 3450 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 19}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 3517 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 20}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 3686 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 22}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 4474 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 28}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 4766 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 29}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 6002 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 27}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 6196 | `{"max_candles": 168, "n": 84, "stop_loss_pct": 26}` | 21,875.07 | 10.2 | -19.6 | 56.7 | 5,791.12 | 4.3 | -20.1 | 0.42 | 30/32 | not checked |
| 1366 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 20}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 1492 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 21}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 1579 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 23}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 1615 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 18}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 1772 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 17}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 1990 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 22}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 2056 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 25}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 2075 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 19}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |
| 2996 | `{"max_candles": 126, "n": 63, "stop_loss_pct": 13}` | 18,172.09 | 9.0 | -19.0 | 60.5 | 7,055.46 | 5.0 | -19.5 | 0.56 | 43/38 | not checked |

(8 more on the front, see results.csv)


## Analyst notes

<!-- analyst-notes:start -->
(none yet)
<!-- analyst-notes:end -->

---

Searching 6,306 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
