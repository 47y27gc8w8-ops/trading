# Breadth Scaled Sector Allocation

Source: original.md (120-strategy research library, 2026-11-24). This file is the testable version.

## Idea
Hold the US sector ETFs that are in an uptrend (above their 200-day SMA), and scale total
exposure with market breadth: the fewer sectors in an uptrend, the more of the sleeve sits in
cash. Each eligible sector gets weight B / count(eligible) = 1 / N, where N is the size of the
universe, so breadth scaling and equal weighting are the same thing.

## Market
- Symbols: XLB XLC XLE XLF XLI XLK XLP XLRE XLU XLV XLY (Select Sector SPDRs, Yahoo daily, adjusted = total return)
- Timeframe: daily bars for fills and stop checks; decisions at month-end closes
- Direction: long only, one portfolio over all 11 symbols, no leverage (sum of weights ≤ 100 %)

## Buy trigger (month-end rebalance)
At the close of the last daily bar of each complete calendar month t:
- Universe U = symbols with a close at t and a defined SMA(n) (n completed bars since listing).
- Eligible = `close > SMA(n)`; B = |eligible| / |U|.
- Target weight of each eligible symbol = B / |eligible| = 1 / |U|; the rest is cash.
- Orders fill at the open of the next bar. Sells first (ineligible symbols fully, overweight ones
  trimmed), then buys to target. Buys are scaled down proportionally if cash is short.
- If a symbol already in U has no bar at t, that rebalance is skipped (weights unchanged).

## Sell trigger
First of:
- Rebalance: symbol ineligible at a month-end → sold at the next open; eligible ones are resized
  to 1/|U| (trims keep the cost basis E and the age).
- Hard stop: daily low ≤ E × (1 − stop_loss_pct/100) → sold at the stop, or at the open on a
  gap down. On additions E becomes the weighted-average cost and stop = max(old stop, new E × (1 − sl)).
- Time exit: after max_candles completed held bars (entry bar = 1), sold at the next open.
  Resizing doesn't reset the age.
- A stopped or time-exited symbol is not bought again until a later month-end decision, and
  never on the same execution bar.
- No take-profit.

## Parameters
| name | meaning | description's value | range | step | hard limits |
|---|---|---|---|---|---|
| n | SMA length (days) for eligibility and breadth | 200 | 100–300 | 10 | 20–380 (warm-up) |
| stop_loss_pct | hard stop below cost basis, % | 15 | 8–25 | 1 | 2–50 |
| max_candles | held daily bars before time exit | 252 | 126–504 | 21 | 21–1260 |

No order constraints between parameters. Grid: 21 × 18 × 19 = 7,182 sets.

## Setup
- Data: 1998-12-22 → 2026-11-23 (XLRE from 2015-10-08, XLC from 2018-06-19)
- In-sample 2000-07-01 → 2016-01-01 (9 sectors); out-of-sample 2016-01-01 → 2026-11-23 (XLRE and XLC join once warmed up)
- Capital 10,000 USD, whole sleeve, fractional shares
- Fees 0.05 % per side, slippage 0.03 % per fill (repo default for US ETFs)

## Assumptions
- Point-in-time universe: an ETF counts toward breadth only once it is listed and has n bars
  (the spec says don't backfill before listing; counting unlisted funds as "not eligible"
  would cap 2000–2015 exposure at 9/11 for funds that didn't exist).
- Cash earns 0 % (the spec allows this as an explicitly labeled conservative scenario). With
  ~45 % average cash this understates returns versus a T-bill sleeve, by roughly half the T-bill yield.
- Sizing: whole sleeve with explicit target weights (the spec's portfolio rule), so there's no
  risk_fraction sizing. This matches the user's 100 %-equity choice for library specs.
- Adjusted Yahoo closes are used both for signals and fills (no separate raw execution
  series in the project).
- Monthly resizing has no tolerance band (the spec has none), so small trims and top-ups
  every month pay fees.
- Each holding from first buy to full close is one "trade" in the metrics. Partial trims and
  additions are included in its P&L.

## Open questions
- none. Screening, per-symbol and basket runs don't apply: breadth is measured across the
  whole universe, so a one-symbol run would turn into a different strategy.
