# Sector Roc Rotation

## Buy trigger
On each month-end select the top 3 sectors by ROC(63), only if SPY > its SMA(200); equal-weight selected assets.

Use only completed bars. Unless explicitly scheduled otherwise, enter at the next bar open, not retrospectively on the signal close.

## Sell trigger
- Signal/rebalance exit: At each month-end sell assets no longer selected or if SPY <= SMA(200).
- Protective stop: each holding has a hard stop 15% below its cost basis, maintained under the no-loosening rule in EXECUTION.md.
- Time exit: close each holding after 252 held daily bars at next daily open.
- No fixed take-profit target: the selection/rebalance exit above governs ordinary exits.

## Parameters
| Parameter | Start | Min | Max | Notes |
|---|---:|---:|---:|---|
| k | 3 | 1 | 5 | Number of selected holdings |
| n | 63 | 21 | 252 | Signal lookback/period; bars unless explicitly stated otherwise |
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
- Sector-only fixed universe; rank descending. No positive-ROC requirement beyond the broad-market filter.

## Intended market and data
- Category: Rotation and portfolio allocation.
- Candidate instruments/universe: XLB XLE XLF XLI XLK XLP XLU XLV XLY XLRE XLC.
- Signal timeframe: 1d; month-end decisions.
- Position model: portfolio.
- Venue: choose and record a single supported exchange/broker before testing. Symbols are research examples, not a verification of current availability, liquidity, borrow, suitability or performance. For US-listed examples confirm your jurisdiction and brokerage eligibility.
- Required observations: complete OHLCV, sufficient indicator warm-up, aligned benchmark/pair bars if referenced, and corporate-action/total-return data for relevant securities; borrowing and carry data additionally mandatory for pairs.

## Research status and provenance
- Status: unbacktested research specification. No measured returns, win rate, Sharpe ratio, drawdown or asset-specific optimization is claimed.
- Provenance: Faber-style sector rotation adaptation.
- Interpretation: A mechanical research hypothesis built from the cited signal concepts. Added parameter ranges, stops, position sizing, time limits and instrument choices are author-designed unless explicitly stated otherwise.
- The filename original.md denotes this bundle's baseline version; it does not claim verbatim reproduction of an original publication. A citation supports the underlying concept, not every supplied threshold or the profitability of this implementation.

## Sources
- S05: StockCharts: Faber sector rotation — https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/fabers-sector-rotation-trading-strategy
  Scope: Monthly sector ranking and broad-market SMA10-month filter; alternative ranking/weights are adaptations.

## Validation requirements
- Run the protocol in ../../VALIDATION.md with realistic costs, lookahead checks, untouched out-of-sample data and multiple-testing controls across the entire library.
- Unit-test cross/lag boundaries and indicator values; confirm stop/target handling and every parameter-order constraint. Paper-trade before any live deployment.
