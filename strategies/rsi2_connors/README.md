# Connors RSI(2) mean reversion

**Idea:** In a long-term uptrend, short, sharp pullbacks in equity indices tend to bounce back within days (Connors & Alvarez 2008).

**Rules:** Buy when close > SMA(`trend_sma`) and RSI(`rsi_n`) < `entry`. Sell when close > SMA(`exit_sma`). The original rules use RSI(2) < 10, SMA200 and an SMA5 exit.

**Data:** SPY and QQQ daily, adjusted for dividends, from 1999. In-sample before 2016, out-of-sample from 2016. Costs are 5 bps.

**Expectations:** High win rate, low time in market and a low CAGR in absolute terms. Its edge on SPY is reported to have weakened after about 2010, which the OOS window tests.
