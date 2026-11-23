# Donchian channel breakout (Turtle style)

**Idea:** A breakout to a new N-day high starts a trend. Ride it until price makes a new shorter-term low.

**Rules:** Enter when close > the highest high of the previous `entry_n` days. Exit when close < the lowest low of the previous `exit_n` days. Each coin gets an equal 1/N sleeve, long-only.

**Data:** 16 Binance USDT pairs, daily. In-sample before 2024, out-of-sample from 2024. Costs are 15 bps.

**Caveats:** Survivorship bias. The original Turtles also used ATR position sizing and pyramiding, which are not included yet and are good candidates for code-change experiments.
