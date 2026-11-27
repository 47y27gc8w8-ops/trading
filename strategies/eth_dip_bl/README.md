# eth_dip_bl: ETH 4h RSI dip buyer

Source: `eth_dip.md` (user idea). Quick ~5-minute exploration, not a full optimisation.

## Rules as written (defaults in `backtest.py` PARAMS)
- ETHUSDT, Binance spot, 4h bars, long only, 100 % of equity per trade.
- Buy: Wilder RSI(14) closes below 25, filled at the next 4h open.
- Sell: RSI(14) closes above 55, filled at the next open.
- Stop: -6 % from the entry fill, checked intrabar (gaps fill at the open).
- Costs: 0.10 % fee per side + 0.05 % slippage per fill.
- In-sample 2018-01-01 .. 2023-12-31 (used for tuning), out-of-sample 2024-01-01 .. 2026-11-23 (only reported).

Tuning extras (not in the idea): `trend_sma` (only buy while close > SMA of N 4h bars), `max_bars` (time exit).

## Files
- `backtest.py` strategy + simulator (copied from `strategies/backtest.py` template)
- `tune.py` 150 s random search over SPACE, IS fitness = yearly return / |max DD|, min 20 trades
- `results.jsonl` all 6,522 tested candidates (IS metrics); `best.json` baseline + IS top 10 with OOS check

```bash
docker compose run --rm -T backtest python strategies/eth_dip_bl/backtest.py --period oos --trades
docker compose run --rm -T backtest python strategies/eth_dip_bl/tune.py --seconds 150
```

## Results (see best.json)
| variant | IS return / maxDD / trades | OOS return / maxDD / trades |
|---|---|---|
| idea as written (14 / 25 / 55, stop 6 %) | -79.8 % / -90 % / 142 | -26.2 % / -41 % / 55 |
| IS #1: RSI7 <25 >75, no stop, SMA200, 60-bar exit | +394 % / -46 % / 59 | -12.5 % / -38 % / 21 |
| IS #3: RSI10 <35 >60, no stop, SMA200 | +201 % / -50 % / 85 | +21.0 % / -35 % / 39 |
| IS #4: RSI14 <25 >60, no stop, SMA600 | +148 % / -41 % / 20 | +21.9 % / -10 % / 9 |
| best with stop <= 6 %: RSI7 <25 >75, stop 6, SMA200, 60 bars | +104 % / -37 % / 80 | -33.1 % / -49 % / 25 |
| ETH buy & hold | +211 % | -24.1 % |

## Findings
- The idea as written loses money in both periods: on 4h ETH, RSI<25 often happens early in a sell-off, and the -6 % stop gets hit (win rate 34 % IS).
- No candidate without the trend filter was profitable in-sample. Only 327 of 6,522 candidates had positive fitness.
- The good-looking variants drop or widen the stop, so single trades lost 20-40 % of equity in-sample. That breaks the "one bad trade can't wreck the account" requirement.
- The IS winner lost money out-of-sample. The OOS-positive variants have few trades (9-39) and were picked from ~6,500 tries, so treat them as hints, not a strategy.

Caveats: single symbol, no survivorship issue but heavy multiple testing; OOS includes a -24 % ETH period.
