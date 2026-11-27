# Intraday lunch compression break (formalized)

Source: `original.md` (library spec), EXECUTION.md (US 5-minute rules) / INDICATORS.md. Code: `backtest.py`
(built by `scripts/portfolio_lib/build_intraday.py`; rule = `signals()`, execution = `_simulate_intraday()`).

## Rule
- **Spec buy trigger:** After 13:00 local, C crosses above the frozen high of the 11:30-13:00 range, that range width < 3*ATR(14) at 13:00, and C > VWAP.
- **Spec exit:** Signal/rebalance exit: C < frozen lunch-range midpoint.
- **Formal:** Lunch range = bars 11:30-13:00, frozen with ATR(14) at the bar closing 13:00; width < k x that ATR. Bar closing after 13:00 up to 15:00: C crosses above the lunch high and C > VWAP. Exit C < lunch-range midpoint. One entry per session.
- **Fill:** next 5-minute bar's open; no fill at/after the earlier of 15:00 and 60 minutes before the
  session close, none on the session's last bar; max one entry per session.
- **Exits (OR, earliest wins):** stop at fill - stop_atr x ATR(14) of the signal bar; target at
  fill + take_profit_atr x the same ATR; signal exit at the next open; time exit after max_candles
  held bars (entry bar = 1); scheduled liquidation at the open of the session's last bar.

## Setup
| | |
|---|---|
| Symbol | SPY |
| Data | Alpaca SIP 5-minute bars, regular session, split + dividend adjusted |
| In-sample | 2016-03-01 -> 2023-01-01 |
| Out-of-sample | 2023-01-01 -> 2026-11-25 (frozen) |
| Capital / sizing | 10,000 USD, 100 % of equity per trade |
| Costs | fee 0.05 % per fill, slippage 0.03 % on market/stop fills |

## Parameters (start values = spec)
| Parameter | Start |
|---|---|
| `k` | 3.0 |
| `stop_atr` | 2.0 |
| `take_profit_atr` | 3.0 |
| `max_candles` | 24 |

## Search space
| Parameter | Range |
|---|---|
| `k` | {"min": 1.5, "max": 5.0, "step": 0.25, "hard_min": 0.25, "hard_max": 20.0} |
| `stop_atr` | {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.25, "hard_max": 10.0} |
| `take_profit_atr` | {"min": 1.5, "max": 6.0, "step": 0.25, "hard_min": 0.25, "hard_max": 15.0} |
| `max_candles` | {"min": 12, "max": 48, "step": 2, "hard_min": 2, "hard_max": 78} |

## Assumptions
- lunch range = bars starting 11:30 to 12:55 (closing 11:35-13:00), frozen with the ATR(14) of the bar closing 13:00; entries on bars closing 13:05-15:00.
- data: Alpaca SIP 5-minute bars (free plan, history from 2016), split + dividend adjusted (adjustment=all) and used for signals and fills; regular session 09:30-16:00 America/New_York only. Early closes come from the data itself (the session's last bar), so the scheduled liquidation and the 'earlier of 15:00 and 60 minutes before the close' entry cutoff follow the real calendar.
- sizing: 100 % of equity per trade instead of the spec's risk_fraction sizing (user's choice for all library specs with risk_fraction, so results compare across the leaderboard); risk_fraction is therefore not optimized.
- time windows refer to the signal bar's CLOSE time (bars are labelled by close, EXECUTION.md); crosses need both bars in the same session; frozen levels (opening ranges, lunch range, prior-session levels) only exist once complete.
- fills: market/stop fills pay slippage 0.03 % and every fill pays fee 0.05 % (library convention for US stocks/ETFs); the resting target limit fills at its price without slippage; a gap above the target fills at the target (never better than the limit); stop first when one bar touches both.
- ATR(14), ADX(14) and EMA run continuously across sessions (overnight gaps count in the true range); warm-up 5 x period bars. Session VWAP anchors at 09:30 with TP = (H+L+C)/3.
- participation cap not modelled (10k sleeve in the most liquid US names).
- IS 2016-03-01 -> 2023-01-01, OOS 2023-01-01 -> 2026-11-25: Alpaca's free history starts in 2016, so the library's usual 2016 split for Yahoo daily data can't apply.
