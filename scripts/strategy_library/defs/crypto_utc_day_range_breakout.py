CONFIG = {
    "name": "crypto_utc_day_range_breakout",
    "asset_class": "crypto",
    "symbols": ["ETHUSDT"],           # spec: ETH/USD
    "timeframe": "1h",              # spec signal timeframe, built per coin from Binance 1m bars (UTC)
    "start": "2018-01-01",
    "oos_start": "2024-01-01",      # repo precedent for crypto strategies
    "end": "2026-11-23",            # frozen at setup: last complete UTC day
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice: 100% of equity (spec's risk_fraction sizing not used)
    "fee_pct": 0.10,                # spec: 10 bp commission per side
    "slippage_pct": 0.10,           # spec: 5 bp half-spread + 5 bp adverse slippage per fill
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 1500,             # >= 5x the longest recursive indicator period (EXECUTION.md warm-up)
}

PARAMS = {
    "n": 50,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "n": {"min": 20, "max": 100, "step": 10, "hard_min": 2},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 9, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def _prev_day(df):
    def calc():
        day = df.index.floor("1D")
        g = df.groupby(day)
        hi, lo = g["high"].max(), g["low"].min()
        prev_hi = pd.Series(hi.shift(1).reindex(day).to_numpy(), index=df.index)   # preceding completed UTC day
        prev_lo = pd.Series(lo.shift(1).reindex(day).to_numpy(), index=df.index)
        prev_day = pd.Series(pd.Series(hi.index, index=hi.index).shift(1).reindex(day).to_numpy(), index=df.index)
        ok = (pd.Series(day, index=df.index) - prev_day) == pd.Timedelta("1D")   # no gap in the data
        return prev_hi.where(ok), prev_lo.where(ok)
    return _memo(("pday", id(df)), calc)


def buy_signal(df, p):
    pdh, _ = _prev_day(df)
    c = df["close"]
    close_hour = (df.index + pd.Timedelta("1h")).hour       # decision at the bar's close time
    in_window = pd.Series((close_hour >= 6) & (close_hour <= 20), index=df.index)
    return cross_above(c, pdh) & (c > ema(c, p["n"])) & in_window


def sell_signal(df, p):
    pdh, pdl = _prev_day(df)
    return df["close"] < (pdh + pdl) / 2
