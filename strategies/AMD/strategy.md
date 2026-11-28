# AMD – Accumulation, Manipulation, Distribution (ICT "Power of 3")

Source: original.md (description written 2026-11-28 from web research). This file is the testable version;
`backtest.py` in this folder implements exactly these rules.

## Idea
The quiet Asian session builds a tight range with stops on both sides (accumulation). Around the
London open price fakes a break out of one side and takes those stops (manipulation / "Judas swing"),
then the real move of the day runs the other way into New York (distribution). Trade the reversal back
into the range after the sweep, as a day trade.

## Market
- Base symbol: **EURUSD** (spot FX, histdata.com M1 bid prices resampled to 15 min, 2010-01 → 2026-11-13).
  The description's other main markets (gold, NQ/ES futures, GBPUSD) are not in the project.
- Screening: the 60 Binance USDT coins (the description says it "might also work on big coins").
- Timeframe: 15-minute bars, session logic in New York time (DST-aware).
- Direction: **long and short**, at most one trade per day, flat every evening.

## Session definitions (NY time)
- Session day D. Asian range = bars from `asia_start` (20:00) on D-1 to 00:00 on D; needs ≥ 50 % of its bars.
- Asian high / low = highest high / lowest low of that range; height = high − low.
- Midnight open = open of the first bar at/after 00:00 (must start before 01:00).
- ATR(14) = RMA of the true range of whole session days, previous days only.

## Buy (long) trigger
At the close of a 15-min bar t that starts in the window [`win_start`, `win_end`) = 02:00–05:00:
- skip the day if `range_max_atr` > 0 and height > `range_max_atr` × ATR(14)
- the lowest low since `win_start` (up to and including t) is **below the Asian low** (sweep), and
- close(t) is **inside the Asian range** (Asian low < close < Asian high) and **above the midnight open**
- optional: `trend_ma` > 0 → previous session close > SMA(`trend_ma`) of session closes
- only the first qualifying bar of the day; enter at the open of bar t+1.

## Sell-short trigger
Mirror image: highest high since `win_start` above the Asian high, close inside the range and below the
midnight open, optional filter previous close < SMA. Enter short at the next open.

## Exits
- Stop (always active, intrabar): sweep low − `stop_buf` × height (long) / sweep high + `stop_buf` × height (short).
- Targets (resting limits, fill at the limit), risk = |entry fill − stop|:
  - `split` (the description): half at the opposite side of the Asian range, half at entry ± `target_r` × risk
  - `range`: everything at the opposite side of the range
  - `r`: everything at entry ± `target_r` × risk
  - The stop is not moved after the first half fills.
- Session exit: anything still open is closed at the open of the first bar at/after `exit_hour` (16:00).
- Stop and target in the same bar → stop assumed.

## Parameters
| name | meaning | description's value | range | step |
|---|---|---|---|---|
| range_max_atr | max Asian range height in daily ATRs (0 = off) | 0.5 ("about half the daily ATR") | 0 – 1.5 | 0.1 |
| stop_buf | stop distance beyond sweep extreme, × range height | 0.1 ("just below") | 0 – 0.5 | 0.05 |
| target_mode | how profit is taken | split | split / range / r | – |
| target_r | runner target in risk multiples | 2.5 ("2–3x") | 1 – 5 | 0.5 |
| trend_ma | daily trend filter SMA (0 = off) | 0 ("optional") | 0, 50, 100, 200 | – |

Fixed (named in the description, not searched): asia_start 20, win_start 2, win_end 5, exit_hour 16, sides both.

## Setup
- In-sample (tuning): 2011-01-01 → 2021-12-31; out-of-sample (validation only): 2022-01-01 → 2026-11-13 (≈ 31 %).
  Crypto coins use the same calendar (BTC from 2018-03 after warm-up).
- Capital 10,000 USD, 100 % of equity as notional per trade, **no leverage**.
- EURUSD costs: no commission, 0.005 % adverse slippage on entry, stop and session fills (≈ 1 pip round trip,
  as in the earlier EURUSD study); limit targets fill at their price. Crypto: 0.10 % fee + 0.05 % slippage per fill.

## Assumptions
- EURUSD as base symbol: first market the description names, and the only one with clean intraday history here.
- 15-min bars: the description allows 1h or 15 min; 15 min resolves sweeps and confirmations much better.
- Shorts included: the description trades both directions explicitly; FX has no borrow cost (swap ignored
  because positions are closed every day before the 17:00 NY rollover).
- "Sweep" = trade below/above the range by any amount; "back inside" = a bar close inside the range.
- Stop buffer is measured in Asian-range heights so the same value works for any price level / symbol.
- "Target: opposite side first, let the rest run to 2–3x risk" = 50/50 split, runner at `target_r` × risk.
- No leverage: returns are small per trade on FX; a real FX account would scale them with leverage (and risk).
- Data are bid prices; the 1 pip round-trip cost covers the spread.

## Open questions
- none asked (all choices above are defaults; see optimization.log)
