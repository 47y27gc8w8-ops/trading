# SMA crossover (trend following)

**Idea:** Prices trend. Be long while the fast moving average is above the slow one and in cash otherwise. The classic version is the 50/200-day "golden cross".

**Rules:** Hold an asset when SMA(`fast`) > SMA(`slow`) at the close. Capital is split 1/N across SPY and QQQ.

**Data:** SPY and QQQ daily, adjusted for dividends, from 1999. In-sample before 2016, out-of-sample from 2016.

**Expectations:** This usually does not beat buy & hold on return. Its value is smaller drawdowns (it sat out most of 2008). It loses through whipsaws in sideways markets.
