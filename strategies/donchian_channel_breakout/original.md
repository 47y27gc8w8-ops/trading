# Donchian Channel Breakout

## Buy trigger
C > HH(H,55)[1] and C[1] <= HH(H,55)[2].

Use only completed bars. Unless explicitly scheduled otherwise, enter at the next bar open, not retrospectively on the signal close.

## Sell trigger
- Signal/rebalance exit: C < LL(L,20)[1].
- Take profit: resting limit at entry fill + 3 * signal-bar ATR(14).
- Stop loss: always-active stop at entry fill - 2 * signal-bar ATR(14).
- Time exit: after 48 completed held bars, sell at next bar open if still held.
- These exits are OR conditions with the strategy-specific signal exit above; the earliest executable exit wins.

## Parameters
| Parameter | Start | Min | Max | Notes |
|---|---:|---:|---:|---|
| n | 55 | 20 | 100 | Signal lookback/period; bars unless explicitly stated otherwise |
| exit_n | 20 | 5 | 40 | Exit channel lookback in bars |
| stop_atr | 2 | 1 | 4 | Multiple of signal-bar ATR(14), frozen at entry |
| take_profit_atr | 3 | 1.5 | 6 | Multiple of the same frozen ATR above fill |
| max_candles | 48 | 24 | 96 | Completed held signal-timeframe bars |
| risk_fraction | 0.005 | 0.001 | 0.01 | Fraction of assigned sleeve equity at initial stop |

Start values are research baselines, not optimized estimates. Min/Max are proposed testing bounds, not confidence intervals or live-safety guarantees. Numeric literals not represented in this table are fixed constants; changing them creates a new configuration that must be recorded. The trigger text displays the Start configuration; use the named parameters in the registry templates when varying them. Enforce all parameter-order constraints below.

## Fixed rules
- Long only, maximum one open position total; listed instruments are alternative test targets, not a simultaneous basket.
- Stop loss is always active after entry; gaps, liquidity and outages can produce worse fills.
- No leverage, pyramiding, averaging down or same-bar re-entry; size from assigned sleeve equity using the initial stop distance.
- Skip missing history, invalid indicators, untradable lots or non-positive stop levels; do not invent data.
- All mandatory data, indicator, execution, cost and sizing conventions in ../../EXECUTION.md and ../../INDICATORS.md apply to this strategy. These documents are part of the specification, not optional reading.
- Entry veto: do not open if a strategy-specific close-based signal exit is already true on the signal bar. Protective stops/targets are set only after a valid entry fill.
- Exits take priority over entries. Do not trade on incomplete candles, future-selected pivots, or forward-filled reference prices.
- Require exit_n < n.

## Intended market and data
- Category: Breakout and volatility expansion.
- Candidate instruments/universe: BTC/USD; spot crypto.
- Signal timeframe: 1d.
- Position model: single.
- Venue: choose and record a single supported exchange/broker before testing. Symbols are research examples, not a verification of current availability, liquidity, borrow, suitability or performance. For US-listed examples confirm your jurisdiction and brokerage eligibility.
- Required observations: complete OHLCV, sufficient indicator warm-up, aligned benchmark/pair bars if referenced, and corporate-action/total-return data for relevant securities; borrowing and carry data additionally mandatory for pairs.

## Research status and provenance
- Status: unbacktested research specification. No measured returns, win rate, Sharpe ratio, drawdown or asset-specific optimization is claimed.
- Provenance: Author-designed quantitative adaptation of cited concepts; not a claimed published standalone system.
- Interpretation: A mechanical research hypothesis built from the cited signal concepts. Added parameter ranges, stops, position sizing, time limits and instrument choices are author-designed unless explicitly stated otherwise.
- The filename original.md denotes this bundle's baseline version; it does not claim verbatim reproduction of an original publication. A citation supports the underlying concept, not every supplied threshold or the profitability of this implementation.

## Sources
- S01: StockCharts: strategy and model catalogue — https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models
  Scope: Concept catalogue; not evidence that any supplied adaptation is profitable.
- S06: Moskowitz, Ooi, Pedersen: Time Series Momentum (2012), AQR research page — https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum
  Scope: Primary research concerns 58 futures/forward contracts, not these spot-crypto or ETF implementations.

## Validation requirements
- Run the protocol in ../../VALIDATION.md with realistic costs, lookahead checks, untouched out-of-sample data and multiple-testing controls across the entire library.
- Unit-test cross/lag boundaries and indicator values; confirm stop/target handling and every parameter-order constraint. Paper-trade before any live deployment.
