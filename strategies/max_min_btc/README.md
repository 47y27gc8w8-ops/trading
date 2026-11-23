# Bitcoin MAX / MIN

**Idea:** In Quantpedia's research (Padysak & Vojtko 2022, revisited to 2024), BTC tended to keep rising after closing at a 10-day **max** (trend) and to bounce after a 10-day **min** (reversion). Holding BTC only on the days after either signal captured most of the upside with far less time in the market.

**Rules:** If today's close is the `lookback`-day max (mode `max`), min (`min`) or either (`both`), hold BTC for the next `hold_days` days.

**Data:** BTCUSDT daily from 2017-08. In-sample before 2024, out-of-sample from 2024. Costs are 15 bps.

**Caveats:** One asset and about 6.5 years of in-sample data, so it is easy to overfit. Watch the OOS column.
