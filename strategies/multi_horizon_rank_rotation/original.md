# Multi Horizon Rank Rotation

## Buy trigger
At month-end rank each asset by mean cross-sectional percentile rank of ROC(21), ROC(63), ROC(126), ROC(252); select top 3 with C > SMA(200); equal-weight.

Use only completed bars. Unless explicitly scheduled otherwise, enter at the next bar open, not retrospectively on the signal close.

## Sell trigger
- Signal/rebalance exit: At month-end sell assets outside the selected group or below SMA(200).
- Protective stop: each holding has a hard stop 15% below its cost basis, maintained under the no-loosening rule in EXECUTION.md.
- Time exit: close each holding after 252 held daily bars at next daily open.
- No fixed take-profit target: the selection/rebalance exit above governs ordinary exits.

## Parameters
| Parameter | Start | Min | Max | Notes |
|---|---:|---:|---:|---|
| k | 3 | 1 | 5 | Number of selected holdings |
| stop_loss_pct | 15 | 8 | 25 | Percent below holding cost; never loosen on additions |
| max_candles | 252 | 126 | 504 | Held daily bars per holding; rebalance does not reset age |

Start values are research baselines, not optimized estimates. Min/Max are proposed testing bounds, not confidence intervals or live-safety guarantees. Numeric literals not represented in this table are fixed constants; changing them creates a new configuration that must be recorded. The trigger text displays the Start configuration; use the named parameters in the registry templates when varying them. Enforce all parameter-order constraints below.

## Fixed rules
- Long only; multiple holdings only as explicitly selected by the portfolio rule. Total notional <=100% of the assigned strategy sleeve; no leverage.
- Hard protective stop on every holding, monitored daily or finer, even though rebalancing is monthly.
- Rebalance only at next open after completed month-end data; deterministic ranking ties use alphabetical ticker order.
- A stopped component cannot be re-added until a later month-end decision. Missing eligibility means cash, not an invented substitute.
- All mandatory data, indicator, execution, cost and sizing conventions in ../../EXECUTION.md and ../../INDICATORS.md apply to this strategy. These documents are part of the specification, not optional reading.
- Exits take priority over entries. Do not trade on incomplete candles, future-selected pivots, or forward-filled reference prices.


## Intended market and data
- Category: Rotation and portfolio allocation.
- Candidate instruments/universe: SPY EFA EEM IEF TLT GLD VNQ DBC.
- Signal timeframe: 1d; month-end decisions.
- Position model: portfolio.
- Venue: choose and record a single supported exchange/broker before testing. Symbols are research examples, not a verification of current availability, liquidity, borrow, suitability or performance. For US-listed examples confirm your jurisdiction and brokerage eligibility.
- Required observations: complete OHLCV, sufficient indicator warm-up, aligned benchmark/pair bars if referenced, and corporate-action/total-return data for relevant securities; borrowing and carry data additionally mandatory for pairs.

## Research status and provenance
- Status: unbacktested research specification. No measured returns, win rate, Sharpe ratio, drawdown or asset-specific optimization is claimed.
- Provenance: Author-designed quantitative adaptation of cited concepts; not a claimed published standalone system.
- Interpretation: Author-designed multi-horizon ranking adaptation.
- The filename original.md denotes this bundle's baseline version; it does not claim verbatim reproduction of an original publication. A citation supports the underlying concept, not every supplied threshold or the profitability of this implementation.

## Sources
- S05: StockCharts: Faber sector rotation — https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/fabers-sector-rotation-trading-strategy
  Scope: Monthly sector ranking and broad-market SMA10-month filter; alternative ranking/weights are adaptations.
- S21: StockCharts: Rate of Change — https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc
  Scope: ROC momentum and multi-horizon trend interpretation.

## Validation requirements
- Run the protocol in ../../VALIDATION.md with realistic costs, lookahead checks, untouched out-of-sample data and multiple-testing controls across the entire library.
- Unit-test cross/lag boundaries and indicator values; confirm stop/target handling and every parameter-order constraint. Paper-trade before any live deployment.
