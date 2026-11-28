# AMD idea (Accumulation – Manipulation – Distribution)

"AMD" here is the ICT / smart-money "Power of 3" idea, **not** the AMD stock.
The thought: every trading day runs through three phases.

1. **Accumulation** – during the quiet Asian session price chops sideways in a tight range.
   Stops pile up just above the range high and just below the range low.
2. **Manipulation** ("Judas swing") – around the London open price makes a fake move out of
   that range, takes out the stops on one side, and then turns around.
3. **Distribution** – the real move of the day goes the other way, through the whole range,
   and usually runs into the New York session.

So a bullish day looks like: open, dip below the open / Asian low, then close near the high.
A bearish day is the mirror image.

## How I would trade it

- Use hourly (or 15-minute) candles. Times are New York time.
- **Asian range:** highest high and lowest low from 20:00 (previous day) to 00:00.
  Also note the **midnight open** (the open of the 00:00 candle).
- Skip the day if the Asian range is unusually wide (bigger than half of the daily ATR(14)) –
  then there was no real "accumulation".
- **Manipulation window:** 02:00 – 05:00 (London open).
- **Long:** in the window price trades *below* the Asian low (sweep), then a candle **closes back
  inside the range** and above the midnight open. Buy at the next candle open.
  - Stop: just below the lowest low of the sweep.
  - Target: the opposite side of the Asian range first; let the rest run to 2–3x the risk.
- **Short:** mirror image – sweep above the Asian high, close back inside and below the midnight open.
  - Stop: just above the highest high of the sweep.
- Only one trade per day. If nothing happens by 05:00, no trade.
- Close anything still open at the end of the New York session (16:00) – it is a day trade.
- Optional filter: only take longs if the higher timeframe trend is up (for example the daily
  close above the 50-day average), only shorts if it is down.

## Where I think it works

Mostly sold for forex (EURUSD, GBPUSD), gold and index futures (NQ / ES), because those trade
around the clock and have clear Asian / London / New York sessions. Might also work on big coins
(BTC, ETH) which trade 24/7. Probably useless on normal stocks/ETFs, since they have no
overnight Asian session in the regular data.

## What I'm not sure about

- Almost all material is from trading-education sites and TradingView posts, not real tests.
  Many details (session times, what counts as a "sweep", the confirmation candle) differ per source.
- One blog that tested it on 18 years of gold found the Judas-swing pattern on about 50 % of days –
  basically a coin flip. In hindsight any wick can be called a "manipulation", so the rules above
  must be strict and fixed in advance.
- I'd like to know if it beats just buying and holding, and on which symbols it actually works.

## Sources

- LuxAlgo – AMD trading strategy: https://luxalgo.com/blog/accumulation-manipulation-distribution-amd-trading-strategy
- Tradezella – AMD model: https://www.tradezella.com/strategies/amd-model
- MQL5 – ICT Power of Three guide: https://www.mql5.com/en/blogs/post/771729
- MQL5 – Power of Three and Judas swing tested on 18 years of gold: https://www.mql5.com/en/blogs/post/778873
- FXNX – Asian range liquidity / London Judas swing: https://fxnx.com/en/blog/ict-asian-range-liquidity-trading-london-judas-swing-trap
- FX Replay – ICT AMD PO3 strategy: https://www.fxreplay.com/informative-strategies/ict-amd-po3-strategy
