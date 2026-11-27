# Ratio RSI recovery (formalized)

Source: `original.md` (library spec), EXECUTION.md "Pair execution" / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_pairs.py`; rule = `signals()`, execution = `_simulate_pair()`).

> **Borrow cost is an assumption (3.0 %/yr), not historical data.** The spec says to disable
> this strategy without borrow/carry history; the user chose to run it with a labelled assumption.

## Rule
- **Spec buy trigger:** R=C_A/C_B. RSI(R,14) crosses above 30 after being below it and 126-day daily-return correlation >0.6; buy A/short B equal dollars.
- **Spec exit:** Signal/rebalance exit: RSI(R,14)>60 or RSI(R,14)<15.
- **Formal:** R = C_A / C_B; entry RSI(R, n) crosses above level (prev <= level < now) and 126-day return correlation > 0.6; exit RSI > 60 or RSI < 15; equal dollars.
- **Fills:** decided at bar t's close, both legs filled at the next synchronized open (both need a bar).
- **Protective exits (OR):** per-leg hard stop leg_stop_pct (long below, short above its entry fill;
  a stop forces the other leg out); net pair P&L incl. fees and borrow <= -pair_stop_pct % of entry
  gross at a close -> next open; time exit after max_candles held bars (entry bar = 1) -> next open.

## Setup
| | |
|---|---|
| Legs | ETHUSDT / BTCUSDT |
| Data | Binance 1m -> UTC daily bars |
| In-sample | 2018-01-01 -> 2024-01-01 |
| Out-of-sample | 2024-01-01 -> 2026-11-23 (frozen) |
| Capital / sizing | 10,000 USD sleeve, gross pair notional 100 % of equity |
| Costs | fee 0.10 % + slippage 0.10 % per fill, both legs |
| Borrow (short leg) | **3.0 %/yr, assumed** |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `n` | 14 |
| `level` | 30 |
| `pair_stop_pct` | 5.0 |
| `leg_stop_pct` | 8.0 |
| `max_candles` | 40 |

## Search space
| Parameter | Range |
|---|---|
| `n` | {"min": 7, "max": 28, "step": 1, "hard_min": 2, "hard_max": 50} |
| `level` | {"min": 20, "max": 40, "step": 1, "hard_min": 16, "hard_max": 59} |
| `pair_stop_pct` | {"min": 2.0, "max": 10.0, "step": 0.5, "hard_min": 0.5, "hard_max": 30.0} |
| `leg_stop_pct` | {"min": 4.0, "max": 15.0, "step": 1.0, "hard_min": 1.0, "hard_max": 50.0} |
| `max_candles` | {"min": 10, "max": 80, "step": 5, "hard_min": 2, "hard_max": 252} |

## Assumptions
- Binance spot ETHUSDT/BTCUSDT closes stand in for ETH/USD and BTC/USD (one venue, same quote). Crypto margin borrow of BTC assumed at 3 %/yr (stress 6 %, 10 %). RSI warm-up 5 x n bars; exit levels 60/15 fixed.
- BORROW COST ASSUMED (user decision 2026-11-27): the spec says to disable pairs without historical borrow/carry data; there is none, so the short leg pays a constant labelled fee (CONFIG borrow_fee_pct_yr: 0.25 %/yr for these easy-to-borrow ETFs/large caps, 3 %/yr for crypto margin) on its market value per calendar day; stress runs at higher fees are logged after the optimization. Borrow recalls and margin calls are not modelled.
- short proceeds earn 0 % and the long leg is paid from the sleeve (no margin interest): conservative carry; total-return (adjusted) closes on both legs, so the short leg pays the dividends it is short (dividend-in-lieu).
- gross notional G = 100 % of sleeve equity at entry (equal dollars: G/2 each; ratio 1:beta: long G/(1+beta), short beta*G/(1+beta)); quantities frozen at entry.
- same-bar ambiguity: if a leg's stop is touched intrabar, that leg fills at its stop and the other leg at its worst bar extreme (long: low, short: high); if both legs touch, the long leg is assumed first. Gaps through a stop fill both legs at the open.
- no new entry on a bar where a position was closed, and no entry when the exit condition (or a forced window end) is true on the signal bar.
- costs: library convention (ETFs fee 0.05 % + slippage 0.03 % per fill; crypto 0.10 % + 0.10 %), both legs, entry and exit.
- IAU, EWA, EWC and VDE were not in the project; their Yahoo daily history was fetched on 2026-11-27 (src.collectors.yahoo_daily.update, full history) without adding them to config/symbols.yaml, so the nightly job doesn't refresh them.
