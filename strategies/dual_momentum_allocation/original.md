# Dual Momentum Allocation

## Buy trigger
At month-end choose the higher ROC(252) asset among SPY/EFA if its ROC(252) exceeds IEF ROC(252); otherwise choose IEF if its ROC(252) > 0, else cash. Assign 100% to selected asset.

Use only completed bars. Unless explicitly scheduled otherwise, enter at the next bar open, not retrospectively on the signal close.

## Sell trigger
- Signal/rebalance exit: At month-end sell any asset not chosen by this rule.
- Protective stop: each holding has a hard stop 15% below its cost basis, maintained under the no-loosening rule in EXECUTION.md.
- Time exit: close each holding after 252 held daily bars at next daily open.
- No fixed take-profit target: the selection/rebalance exit above governs ordinary exits.

## Parameters
| Parameter | Start | Min | Max | Notes |
|---|---:|---:|---:|---|
| n | 252 | 126 | 300 | Signal lookback/period; bars unless explicitly stated otherwise |
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
- Candidate instruments/universe: SPY EFA IEF.
- Signal timeframe: 1d; month-end decisions.
- Position model: portfolio.
- Venue: choose and record a single supported exchange/broker before testing. Symbols are research examples, not a verification of current availability, liquidity, borrow, suitability or performance. For US-listed examples confirm your jurisdiction and brokerage eligibility.
- Required observations: complete OHLCV, sufficient indicator warm-up, aligned benchmark/pair bars if referenced, and corporate-action/total-return data for relevant securities; borrowing and carry data additionally mandatory for pairs.

## Research status and provenance
- Status: unbacktested research specification. No measured returns, win rate, Sharpe ratio, drawdown or asset-specific optimization is claimed.
- Provenance: Author-designed quantitative adaptation of cited concepts; not a claimed published standalone system.
- Interpretation: Author-defined relative-plus-absolute momentum proxy; not an exact reproduction of a named commercial system.
- The filename original.md denotes this bundle's baseline version; it does not claim verbatim reproduction of an original publication. A citation supports the underlying concept, not every supplied threshold or the profitability of this implementation.

## Sources
- S06: Moskowitz, Ooi, Pedersen: Time Series Momentum (2012), AQR research page — https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum
  Scope: Primary research concerns 58 futures/forward contracts, not these spot-crypto or ETF implementations.
- S18: Quantpedia: Paired Switching — https://quantpedia.com/strategies/paired-switching
  Scope: Long-only rotation between assets, distinct from long-short spread arbitrage.

## Validation requirements
- Run the protocol in ../../VALIDATION.md with realistic costs, lookahead checks, untouched out-of-sample data and multiple-testing controls across the entire library.
- Unit-test cross/lag boundaries and indicator values; confirm stop/target handling and every parameter-order constraint. Paper-trade before any live deployment.
