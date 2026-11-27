# Gap-down reversal strength (formalized)

Source: `original.md` (library spec), EXECUTION.md (US 5-minute rules) / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_intraday.py`; rule = `signals()`, execution = `_simulate_intraday()`).

## Rule
- **Spec buy trigger:** Session open < prior-session low; between 10:00 and 12:00 local C crosses above prior-session low, and C > session VWAP.
- **Spec exit:** Signal/rebalance exit: C >= prior-session midpoint.
- **Formal:** Session open < prior-session low; bar closing 10:00-12:00: C crosses above the prior-session low and C > VWAP. Exit C >= prior-session midpoint.
- **Fill:** next 5-minute bar's open; no fill at/after the earlier of 15:00 and 60 minutes before the
  session close, none on the session's last bar.
- **Exits (OR, earliest wins):** stop at fill - stop_atr x ATR(14) of the signal bar; target at
  fill + take_profit_atr x the same ATR; signal exit at the next open; time exit after max_candles
  held bars (entry bar = 1); scheduled liquidation at the open of the session's last bar.

## Setup
| | |
|---|---|
| Symbol | QQQ |
| Data | Alpaca SIP 5-minute bars, regular session, split + dividend adjusted |
| In-sample | 2016-03-01 -> 2023-01-01 |
| Out-of-sample | 2023-01-01 -> 2026-11-25 (frozen) |
| Capital / sizing | 10,000 USD, 100 % of equity per trade |
| Costs | fee 0.05 % per fill, slippage 0.03 % on market/stop fills |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `stop_atr` | 2.0 |
| `take_profit_atr` | 3.0 |
| `max_candles` | 24 |

## Search space
| Parameter | Range |
|---|---|
| `stop_atr` | {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25, "hard_max": 10.0} |
| `take_profit_atr` | {"min": 1.5, "max": 6.0, "step": 0.25, "hard_min": 0.25, "hard_max": 15.0} |
| `max_candles` | {"min": 12, "max": 48, "step": 2, "hard_min": 2, "hard_max": 78} |

## Assumptions
- no entry limit per session (spec sets none); prior-session levels are regular-session high/low/close.
- data: Alpaca SIP 5-minute bars (free plan, history from 2016), split + dividend adjusted (adjustment=all) and used for signals and fills; regular session 09:30-16:00 America/New_York only. Early closes come from the data itself (the session's last bar), so the scheduled liquidation and the 'earlier of 15:00 and 60 minutes before the close' entry cutoff follow the real calendar.
- sizing: 100 % of equity per trade instead of the spec's risk_fraction sizing (user's choice for all library specs with risk_fraction, so results compare across the leaderboard); risk_fraction is therefore not optimized.
- time windows refer to the signal bar's CLOSE time (bars are labelled by close, EXECUTION.md); crosses need both bars in the same session; frozen levels (opening ranges, lunch range, prior-session levels) only exist once complete.
- fills: market/stop fills pay slippage 0.03 % and every fill pays fee 0.05 % (library convention for US stocks/ETFs); the resting target limit fills at its price without slippage; a gap above the target fills at the target (never better than the limit); stop first when one bar touches both.
- ATR(14), ADX(14) and EMA run continuously across sessions (overnight gaps count in the true range); warm-up 5 x period bars. Session VWAP anchors at 09:30 with TP = (H+L+C)/3.
- participation cap not modelled (10k sleeve in the most liquid US names).
- IS 2016-03-01 -> 2023-01-01, OOS 2023-01-01 -> 2026-11-25: Alpaca's free history starts in 2016, so the library's usual 2016 split for Yahoo daily data can't apply.
