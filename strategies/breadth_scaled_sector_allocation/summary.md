# breadth_scaled_sector_allocation: optimization summary

Updated 2026-11-24T23:15:18Z · backtest.py version `f869807cf2` · 8,830 parameter sets tested with this version (8,830 rows in results.csv in total) · last run ended: every parameter combination in the grid has been tested

## Setup

- Data: XLB, XLC, XLE, XLF, XLI, XLK, XLP, XLRE, XLU, XLV, XLY (etf, 1d bars)
- In-sample (tuning): 2000-07-01 → 2016-01-01; out-of-sample (validation only): 2016-01-01 → 2026-11-23
- Capital 10,000 USD, 100% of equity per trade, long only
- Fees 0.05% per side, slippage 0.03% per fill. An 'unusually bad trade' loses more than 2.0% of equity and more than 2.0× the median losing trade.
- Ranking uses in-sample results only. A variant is recommended only if it is profitable in-sample AND out-of-sample, has ≥ 20 in-sample and ≥ 5 out-of-sample trades, its out-of-sample return per year reaches ≥ 25% of the in-sample one, and ≥ 60% of its one-step parameter neighbours are profitable too.

## Recommended variants

| profile | file | iter | parameters | signal now |
|---|---|---|---|---|
| max-income | [breadth_scaled_sector_allocation__max-income__v001.md](breadth_scaled_sector_allocation__max-income__v001.md) | 8635 | `{"max_candles": 189, "n": 240, "stop_loss_pct": 25}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLE since 2026-06-01 00:00 @ 56.208069; long XLF since 2026-07-01 00:00 @ 53.677073; long XLK since 2026-05-01 00:00 @ 163.905496; long XLP since 2026-11-02 00:00 @ 89.866948; long XLRE since 2026-11-02 00:00 @ 43.172948; long XLV since 2026-08-03 00:00 @ 163.059661 |
| balanced | [breadth_scaled_sector_allocation__balanced__v001.md](breadth_scaled_sector_allocation__balanced__v001.md) | 8636 | `{"max_candles": 210, "n": 260, "stop_loss_pct": 28}` | long XLB since 2026-11-02 00:00 @ 53.245969; long XLE since 2026-07-01 00:00 @ 52.96827; long XLF since 2026-07-01 00:00 @ 53.686161; long XLK since 2026-05-01 00:00 @ 164.036169; long XLP since 2026-11-02 00:00 @ 89.866948; long XLRE since 2026-11-02 00:00 @ 43.172948; long XLV since 2026-10-01 00:00 @ 168.200439 |
| safe-starter | [breadth_scaled_sector_allocation__safe-starter__v001.md](breadth_scaled_sector_allocation__safe-starter__v001.md) | 8637 | `{"max_candles": 147, "n": 290, "stop_loss_pct": 9}` | long XLB since 2026-08-03 00:00 @ 50.408055; long XLE since 2026-07-01 00:00 @ 53.0053; long XLF since 2026-05-01 00:00 @ 52.165612; long XLP since 2026-11-02 00:00 @ 89.866948; long XLRE since 2026-11-02 00:00 @ 43.172948; long XLV since 2026-07-01 00:00 @ 159.049173 |

### Comparison (IS = in-sample, OOS = out-of-sample)

| metric | max-income IS | max-income OOS | balanced IS | balanced OOS | safe-starter IS | safe-starter OOS |
|---|---|---|---|---|---|---|
| net profit | 17,918.03 | 10,170.82 | 16,957.08 | 11,360.37 | 13,805.34 | 8,039.01 |
| return % | 179.18 | 101.71 | 169.57 | 113.60 | 138.05 | 80.39 |
| return %/year | 6.8 | 6.7 | 6.6 | 7.2 | 5.8 | 5.6 |
| gross profit | 25,936.59 | 17,034.35 | 23,756.11 | 18,133.18 | 23,907.91 | 17,428.59 |
| gross loss | 8,018.55 | 6,863.53 | 6,799.03 | 6,772.81 | 10,102.57 | 9,389.59 |
| trades | 178 | 172 | 163 | 162 | 227 | 208 |
| win rate % | 56.2 | 50.6 | 59.5 | 49.4 | 56.4 | 49.5 |
| avg win | 259.37 | 195.80 | 244.91 | 226.66 | 186.78 | 169.21 |
| avg loss | -102.80 | -80.75 | -103.02 | -82.60 | -102.05 | -89.42 |
| avg result / trade | 100.66 | 59.13 | 104.03 | 70.13 | 60.82 | 38.65 |
| largest single loss | -376.16 | -303.44 | -413.34 | -273.30 | -240.68 | -185.01 |
| largest loss % of equity | -1.97 | -2.32 | -1.49 | -1.56 | -1.02 | -1.11 |
| max drawdown | -2,871.89 | -2,501.41 | -2,147.03 | -2,730.18 | -2,334.83 | -2,675.80 |
| max drawdown % | -16.37 | -15.55 | -16.74 | -16.38 | -14.36 | -15.78 |
| profit factor | 3.23 | 2.48 | 3.49 | 2.68 | 2.37 | 1.86 |
| unusually bad trades | 1 | 1 | 0 | 0 | 0 | 0 |
| … threshold (% of equity) | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| time in market % | 54.7 | 69.9 | 55.6 | 71.1 | 53.7 | 68.4 |
| buy & hold return % | 139.85 | 244.45 | 139.85 | 244.45 | 139.85 | 244.45 |
| OOS efficiency (OOS %/yr ÷ IS %/yr) |  | 0.97 |  | 1.09 |  | 0.97 |
| period | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 | 2000-07-03 → 2015-12-31 | 2016-01-04 → 2026-11-23 |

### Return % by calendar year (whole period, same parameters, mark-to-market)

Shows whether profits are spread over many years or come from one lucky stretch.

| year | max-income | balanced | safe-starter |
|---|---|---|---|
| 2000 | 7.3 | 6.2 | 6.0 |
| 2001 | -11.3 | -12.2 | -10.7 |
| 2002 | -3.5 | -2.9 | -3.6 |
| 2003 | 21.6 | 21.7 | 17.6 |
| 2004 | 9.7 | 13.6 | 13.1 |
| 2005 | 4.5 | 0.8 | 4.8 |
| 2006 | 13.4 | 10.6 | 14.1 |
| 2007 | 11.4 | 11.1 | 8.1 |
| 2008 | -10.3 | -9.2 | -11.0 |
| 2009 | 15.4 | 15.1 | 10.4 |
| 2010 | 7.0 | 8.0 | 3.4 |
| 2011 | 3.0 | 4.6 | -0.8 |
| 2012 | 5.6 | 7.7 | 2.8 |
| 2013 | 28.0 | 26.9 | 28.4 |
| 2014 | 14.0 | 12.4 | 12.7 |
| 2015 | -1.8 | -4.1 | 1.2 |
| 2016 (OOS) | 6.5 | 7.4 | 3.5 |
| 2017 (OOS) | 14.3 | 15.1 | 17.2 |
| 2018 (OOS) | -4.2 | -0.7 | -2.6 |
| 2019 (OOS) | 11.4 | 10.6 | 10.8 |
| 2020 (OOS) | 2.6 | 2.5 | 1.2 |
| 2021 (OOS) | 26.7 | 25.5 | 24.4 |
| 2022 (OOS) | -10.2 | -10.8 | -10.9 |
| 2023 (OOS) | 2.4 | 4.3 | 0.9 |
| 2024 (OOS) | 12.6 | 15.2 | 10.6 |
| 2025 (OOS) | 7.4 | 6.9 | 2.1 |
| 2026 (OOS) | 6.0 | 5.1 | 5.3 |

### Risk in plain language

- **max-income**: Risk looks moderate: the account fell up to 16.4% from a peak in-sample and 15.6% out-of-sample, and the worst single trade cost 2.3% of the account out-of-sample. About 56 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 61% per trade would have kept the worst drawdown near 10% (rough estimate).
- **balanced**: Risk looks moderate: the account fell up to 16.7% from a peak in-sample and 16.4% out-of-sample, and the worst single trade cost 1.6% of the account out-of-sample. About 60 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 60% per trade would have kept the worst drawdown near 10% (rough estimate).
- **safe-starter**: Risk looks moderate: the account fell up to 14.4% from a peak in-sample and 15.8% out-of-sample, and the worst single trade cost 1.1% of the account out-of-sample. About 56 of every 100 trades won in-sample. It earned less than simply buying and holding over the out-of-sample period (but was out of the market part of the time). With 100% of equity per trade; about 63% per trade would have kept the worst drawdown near 10% (rough estimate).

## Pareto front (no other eligible set has both more in-sample profit and a smaller in-sample drawdown)

| iter | params | IS net | IS %/yr | IS max DD % | IS win % | OOS net | OOS %/yr | OOS max DD % | OOS eff. | trades IS/OOS | robust |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7512 | `{"max_candles": 189, "n": 290, "stop_loss_pct": 28}` | 18,675.07 | 7.0 | -15.3 | 58.5 | 11,118.81 | 7.1 | -19.3 | 1.01 | 176/166 | not checked |
| 7775 | `{"max_candles": 189, "n": 290, "stop_loss_pct": 29}` | 18,675.07 | 7.0 | -15.3 | 58.5 | 11,074.22 | 7.1 | -19.5 | 1.01 | 176/166 | not checked |
| 8563 | `{"max_candles": 189, "n": 290, "stop_loss_pct": 27}` | 18,675.07 | 7.0 | -15.3 | 58.5 | 11,163.41 | 7.1 | -19.1 | 1.01 | 176/166 | not checked |
| 7956 | `{"max_candles": 189, "n": 300, "stop_loss_pct": 27}` | 18,482.18 | 7.0 | -15.1 | 57.5 | 11,359.54 | 7.2 | -20.4 | 1.03 | 174/165 | not checked |
| 8055 | `{"max_candles": 189, "n": 300, "stop_loss_pct": 28}` | 18,482.18 | 7.0 | -15.1 | 57.5 | 11,314.18 | 7.2 | -20.6 | 1.03 | 174/165 | not checked |
| 8117 | `{"max_candles": 189, "n": 300, "stop_loss_pct": 29}` | 18,482.18 | 7.0 | -15.1 | 57.5 | 11,268.81 | 7.2 | -20.8 | 1.03 | 174/165 | not checked |
| 7737 | `{"max_candles": 147, "n": 290, "stop_loss_pct": 28}` | 17,036.87 | 6.6 | -14.4 | 64.9 | 9,517.64 | 6.3 | -19.8 | 0.96 | 205/193 | not checked |
| 8167 | `{"max_candles": 147, "n": 290, "stop_loss_pct": 29}` | 17,036.87 | 6.6 | -14.4 | 64.9 | 9,477.64 | 6.3 | -20.0 | 0.95 | 205/193 | not checked |
| 8339 | `{"max_candles": 147, "n": 290, "stop_loss_pct": 27}` | 17,036.87 | 6.6 | -14.4 | 64.9 | 9,557.64 | 6.4 | -19.6 | 0.96 | 205/193 | not checked |
| 7446 | `{"max_candles": 210, "n": 290, "stop_loss_pct": 29}` | 16,131.88 | 6.4 | -13.4 | 59.5 | 11,147.96 | 7.1 | -20.0 | 1.11 | 163/157 | not checked |
| 8682 | `{"max_candles": 210, "n": 290, "stop_loss_pct": 28}` | 16,131.88 | 6.4 | -13.4 | 59.5 | 11,169.63 | 7.1 | -19.9 | 1.11 | 163/157 | not checked |


## Analyst notes

<!-- analyst-notes:start -->
**The parameters barely matter. That's good for robustness and bad for "optimization".** All
8,830 tested sets passed every gate. The description's defaults (SMA 200, stop 15 %, 252 bars)
earn 6.1 %/yr in-sample and 7.5 %/yr out-of-sample. The best variants earn 6.6–7.0 %/yr
in-sample and 5.6–7.2 %/yr out-of-sample. Tuning added about half a point a year in-sample and
nothing reliable out-of-sample. The edge comes from the rule itself: hold the sectors above
their long SMA at 1/N each, with the rest in cash.

**What the variants do differently.** max-income and balanced use a slightly longer SMA
(240–260), a wide stop (25–28 %) and a shorter time cap (~9–10 months). safe-starter uses SMA
290, a tight 9 % stop and a 7-month cap: more trades, smaller single losses (≤ 1.1 % of equity),
less profit.

**Range warning: ignore it.** The stop range was widened to 29 % because the max-income best
sat on the edge. A stop of 25–29 % almost never fires: in-sample results are identical from 27
to 29 %, so the month-end SMA exit does the real work. Pushing further would only drop the stop
the spec requires.

**Stable over time.** OOS efficiency is 0.97–1.09. Losing years are the big bear phases
(2001, 2008, 2022 at about −10 to −12 %, 2018 small). Strong years spread across 2003, 2013,
2017, 2021 and 2024. No single lucky stretch carries the result.

**Main caveat: it lags buy-and-hold.** Out-of-sample the sectors averaged about 12 %/yr
buy-and-hold against ~7 %/yr here. The strategy sits ~30 % in cash even in bull markets, and
this test pays 0 % on cash. A T-bill sleeve would add roughly 1 %/yr on average (more in
2023–2026). What you get for that is the drawdown: about −15 to −20 % instead of the ~−50 %
sector ETFs suffered in 2008. In-sample (2000–2015, two bear markets) it beat buy-and-hold.

**No symbol targeting.** Breadth is measured across the universe, so screening and per-symbol
runs don't apply (see log). The 11-ETF universe is fixed by the spec and chosen in hindsight
(survivorship of the sector scheme itself).

**What I'd paper-trade first:** balanced (SMA 260, stop 28 %, 210 bars), or simply the
description's defaults, which are statistically indistinguishable. Use about 60 % of the
sleeve if you want the worst drawdown near 10 %. Compare it against a 60 % SPY / 40 % T-bill
benchmark, because that's what it effectively competes with.
<!-- analyst-notes:end -->
<!-- analyst-notes:end -->

---

Searching 8,830 parameter sets means some will look good by luck. The out-of-sample gate and the neighbour check reduce that risk but don't remove it. Backtest results don't guarantee future performance: fees, slippage, liquidity, taxes and market behaviour can all differ in live trading.
