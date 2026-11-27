# Bond Duration Momentum Switch

Source: original.md (research-library spec, 2026-11). This file is the testable version.

## Idea
Treasury duration rotation: once a month hold whichever of short (SHY), intermediate (IEF) or
long (TLT) Treasuries had the best recent total return, but only if that return is positive;
otherwise sit in cash. A hard stop and a one-year holding cap limit each holding.

## Market
- Universe: SHY, IEF, TLT (Yahoo daily, adjusted for dividends and splits = total return).
  It is ONE portfolio: at most one ETF held at a time, 100% of the sleeve. The three tickers are
  not traded separately.
- Signal timeframe: daily bars; decisions only at month-end closes, fills at the next daily open.
- Direction: long only, no leverage.

## Definitions
- Month end = the last daily bar of a calendar month that is complete in the data (the next bar
  exists and is in a later month).
- `ROC(n)` = close_t / close_{t−n} − 1 on adjusted daily closes (total return), n daily bars.
- Leader = the member with the highest ROC(n); ties go to the alphabetically first ticker.
- Dates are the intersection of the three ETFs' trading days (no forward fill). If any member
  lacks n bars of history at a month end, that rebalance is skipped (holdings unchanged).

## Buy trigger
At a month-end close: if the leader's ROC(n) > 0 and the portfolio doesn't already hold it →
buy the leader with 100% of equity at the next daily open (after any sell at that open).

## Sell trigger
For the current holding, the first of:
- Rebalance exit: at a month-end close the leader is a different ticker, or every ROC(n) ≤ 0 →
  sell at the next open.
- Hard stop: daily low ≤ E × (1 − stop_loss_pct/100), E = entry fill → fill at that level, or
  at the open if it gaps below. Active from the entry bar. After a stop the portfolio stays in
  cash until the next month-end decision (which may re-select the same ticker).
- Time exit: after `max_candles` completed held daily bars (entry bar = 1) → sell at the next
  open. A rebalance doesn't reset the age (keeping the leader is not a new entry). The
  time-exited ticker can't be re-bought at that same open; a later month end may re-select it.
- No profit target.
Order at an open: exits first (a gap through the stop is reported as a stop), then the buy.

## Parameters
| name | meaning | spec value | range | step |
|---|---|---|---|---|
| n | ROC lookback, daily bars | 63 | 21–126 (hard 5–220) | 3 |
| stop_loss_pct | hard stop below entry fill, % | 15 | 8–25 (hard 1–60) | 1 |
| max_candles | held daily bars before the time exit | 252 | 126–504 (hard 21–1260) | 21 |

No order constraints between parameters. Grid: 36 × 18 × 19 = 12,312 combinations.

## Setup
- Data: all three from 2002-07-30. Frozen end 2026-11-23.
- In-sample: 2003-07-01 → 2016-01-01 (12.5 years, includes 2008 and the 2013 taper tantrum);
  out-of-sample: 2016-01-01 → 2026-11-23 (includes the 2022 bond crash)
- Capital 10,000 USD, 100% of equity in the selected ETF, fractional units
- Fees 0.05% per side, slippage 0.03% per fill (US ETF defaults)

## Assumptions
- Uninvested cash earns 0%. EXECUTION.md allows this only as a labeled conservative scenario;
  it's what every strategy on the leaderboard uses, so results stay comparable. ^IRX is in the
  project and could be added as a cash yield later (the spec's buy rule compares to 0, not to
  T-bills, so the signal doesn't need it).
- ROC lookback counted in daily bars (spec: "bars unless explicitly stated otherwise"; timeframe 1d).
- Start 2003-07-01 so that every n up to ~220 bars has full history at the first decision.
- Costs: the skill's US-ETF defaults (8 bp per side incl. slippage), a bit above the spec's 5 bp.
- Fills from adjusted prices (the project has no separate raw execution series).
- "No-loosening" stop rule is moot: there are no additions to an existing holding.
- Screening, broad-basket and per-symbol runs don't apply: the strategy is defined by its
  three-ETF universe. Testing it on single ETFs or other baskets would be a different strategy.

## Open questions
- none
