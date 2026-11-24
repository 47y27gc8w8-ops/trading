# Cointegration Gated Residual

## Buy trigger
At each month-end fit log(A)=alpha+beta*log(B) on preceding 252 bars; require beta>0 and Engle-Granger cointegration p<0.05. Freeze model and residual mean/std for next month. Enter long A/short B ratio 1:beta when residual z<-2.

Use only completed bars. Unless explicitly scheduled otherwise, enter at the next bar open, not retrospectively on the signal close.

## Sell trigger
- Signal/rebalance exit: Frozen residual z>=0 or <=-4; close at next month-end before refitting.
- Protective pair exit: net pair P&L <= -5% of entry gross notional, checked each daily close; close both legs next synchronized open.
- Hard stops: long leg 8% below its entry; short leg 8% above its entry; either stop forces the other leg out.
- Time exit: close both legs after 40 completed held daily bars at next synchronized open.
- No fixed profit target; use the spread/signal exit above.

## Parameters
| Parameter | Start | Min | Max | Notes |
|---|---:|---:|---:|---|
| n | 252 | 126 | 504 | Signal lookback/period; bars unless explicitly stated otherwise |
| p | 0.05 | 0.01 | 0.1 | Maximum Engle-Granger test p-value |
| pair_stop_pct | 5 | 2 | 10 | Percent loss of entry gross notional; close-based |
| leg_stop_pct | 8 | 4 | 15 | Always-active adverse price stop per leg; percent |
| max_candles | 40 | 10 | 80 | Daily bars; exit at next open |

Start values are research baselines, not optimized estimates. Min/Max are proposed testing bounds, not confidence intervals or live-safety guarantees. Numeric literals not represented in this table are fixed constants; changing them creates a new configuration that must be recorded. The trigger text displays the Start configuration; use the named parameters in the registry templates when varying them. Enforce all parameter-order constraints below.

## Fixed rules
- One pair at a time, long A and short B only; no reverse-direction pair, pyramiding or averaging down.
- Gross entry notional at most 100% of assigned strategy sleeve; actual broker margin and borrow permissions are mandatory.
- Per-leg hard stops remain active. The pair-P&L stop is close-based, not an intrabar guaranteed loss limit.
- Borrow/carry/dividends, synchronized fills, leg risk and recalls must be modeled; disable this strategy if those inputs are unavailable.
- All mandatory data, indicator, execution, cost and sizing conventions in ../../EXECUTION.md and ../../INDICATORS.md apply to this strategy. These documents are part of the specification, not optional reading.
- Entry veto: do not open if a strategy-specific close-based signal exit is already true on the signal bar. Protective stops/targets are set only after a valid entry fill.
- Exits take priority over entries. Do not trade on incomplete candles, future-selected pivots, or forward-filled reference prices.
- Engle-Granger implementation: statsmodels coint(Alog, Blog, trend=c, maxlag=1, autolag=None). Do not replace by ordinary ADF critical values. Illustration only; test may fail and then no trade.

## Intended market and data
- Category: Relative value and cross-market.
- Candidate instruments/universe: A=GLD; B=IAU; ETFs.
- Signal timeframe: 1d.
- Position model: pair.
- Venue: choose and record a single supported exchange/broker before testing. Symbols are research examples, not a verification of current availability, liquidity, borrow, suitability or performance. For US-listed examples confirm your jurisdiction and brokerage eligibility.
- Required observations: complete OHLCV, sufficient indicator warm-up, aligned benchmark/pair bars if referenced, and corporate-action/total-return data for relevant securities; borrowing and carry data additionally mandatory for pairs.

## Research status and provenance
- Status: unbacktested research specification. No measured returns, win rate, Sharpe ratio, drawdown or asset-specific optimization is claimed.
- Provenance: Author-designed quantitative adaptation of cited concepts; not a claimed published standalone system.
- Interpretation: A mechanical research hypothesis built from the cited signal concepts. Added parameter ranges, stops, position sizing, time limits and instrument choices are author-designed unless explicitly stated otherwise.
- The filename original.md denotes this bundle's baseline version; it does not claim verbatim reproduction of an original publication. A citation supports the underlying concept, not every supplied threshold or the profitability of this implementation.

## Sources
- S16: Quantpedia: Pairs Trading with Stocks; Gatev et al. summary and bibliography — https://quantpedia.com/strategies/pairs-trading-with-stocks
  Scope: Secondary synthesis of distance, cointegration and related pair methods; no guarantee of persistent convergence.

## Validation requirements
- Run the protocol in ../../VALIDATION.md with realistic costs, lookahead checks, untouched out-of-sample data and multiple-testing controls across the entire library.
- Unit-test cross/lag boundaries and indicator values; confirm stop/target handling and every parameter-order constraint. Paper-trade before any live deployment.
