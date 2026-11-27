# Absolute Momentum Monthly

Source: original.md (research-library spec, 2026-11). This file is the testable version.

## Idea
Time-series momentum, long or cash: hold the asset while its trailing 12-month total return
beats T-bills. A protective ATR stop and target, plus a 12-month time limit, cap each trade.

## Market
- Symbols: SPY (base run), GLD (spec's second instrument, run separately); screening over the
  project's ETF list (indices and ^IRX excluded: not tradable)
- Data: Yahoo daily bars, adjusted for dividends and splits (= total return)
- Signal timeframe: completed calendar months (signal at the last daily close of the month);
  fills, stops and targets on daily bars
- Cash: ^IRX (13-week T-bill yield, % p.a., Yahoo, since 1960)
- Direction: long only, one position at a time

## Definitions
- Monthly bar: open = first daily open, high/low = max/min, close = last daily close of a
  calendar month that is complete in the data.
- `ROC(n)` = close_m / close_m[n months ago] − 1 (adjusted closes, so total return).
- Monthly cash return of month k = ^IRX month-end yield of month k−1 / 100 / 12 (the rate known
  when the month starts). `Cash(n)` = product of (1 + monthly cash) over the same n months − 1.
  A missing yield gives no signal (no zero substitution).
- `ExcessROC(n)` = (ROC(n) − Cash(n)) × 100, in percentage points.
- `ATR(14)` on monthly bars: TR = max(H−L, |H−C[1]|, |L−C[1]|), Wilder RMA (alpha 1/14, SMA seed).

## Buy trigger
At a month-end close: `ExcessROC(n) > hurdle` and flat → buy at the next daily open.
Entry is skipped if the signal month's ATR ≤ 0 / missing or the stop would be ≤ 0.
(The entry veto is automatic: entry needs excess > hurdle ≥ 0, the exit needs excess ≤ 0.)

## Sell trigger
First of (with E = entry fill and A = ATR(14) of the signal month, both frozen at entry):
- Signal exit: at a month-end close `ExcessROC(n) ≤ 0` → sell at the next daily open
- Stop: daily low ≤ E − stop_atr × A → fill at that level (or the open if it gaps below)
- Target: daily high ≥ E + take_profit_atr × A → fill at that level (or the open if it gaps above)
- Time exit: after `max_candles` completed held months → sell at the next daily open
- If stop and target are both touched in one daily bar, the stop is assumed.

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | ROC / cash lookback, months | 12 | 6–18 (hard 2–36) | 1 |
| hurdle | entry needs excess ROC > this, pp | 0 | 0–3 | 0.25 |
| stop_atr | stop distance, × monthly ATR | 2 | 1–4 | 0.25 |
| take_profit_atr | target distance, × monthly ATR | 3 | 1.5–6 | 0.5 |
| max_candles | completed held months before time exit | 12 | 6–24 | 1 |

`risk_fraction` (spec 0.005) is not used: the user chose 100% of equity per trade.
No order constraints between parameters in the spec.

## Setup
- Data: SPY from 1993-01, GLD from 2004-11, ^IRX from 1960. Frozen end 2026-11-23 (last
  complete monthly signal: 2026-10).
- In-sample: 1995-01-01 → 2016-01-01; out-of-sample: 2016-01-01 → 2026-11-23
- Each symbol trades only after 504 daily bars (~24 months) of its own history
- Capital 10,000 USD, 100% of equity per trade, fractional units
- Fees 0.05% per side, slippage 0.03% per fill (US ETF defaults)

## Assumptions
- Cash series = ^IRX month-end yield, monthly rate = yield/12, known at the start of the month.
  It's a discount-basis yield, so it slightly understates the true return. Chosen by the user.
- `hurdle` units = percentage points of excess return (the spec says "units given in trigger").
- Position size = 100% of equity, not the spec's risk_fraction sizing (user's choice, so results
  are comparable with the leaderboard).
- Costs: the skill's US-ETF defaults (8 bp per side incl. slippage), a bit above the spec's 5 bp.
- Fills from adjusted prices (the project has no separate raw execution series).
- min_trades_is lowered to 12: a monthly strategy trades about twice a year, and GLD has only
  ~9 in-sample years.

## Open questions
- Cash series: answered, add ^IRX. Sizing: answered, 100% of equity.
