CONFIG = {
    "name": "crypto_weekly_open_reclaim",
    "asset_class": "crypto",
    "symbols": ["BTCUSDT"],           # spec: BTC/USD
    "timeframe": "4h",              # spec signal timeframe, built per coin from Binance 1m bars (UTC)
    "start": "2018-01-01",
    "oos_start": "2024-01-01",      # repo precedent for crypto strategies
    "end": "2026-11-23",            # frozen at setup: last complete UTC day
    "capital": 10_000.0,
    "position_pct": 1.0,            # user's choice: 100% of equity (spec's risk_fraction sizing not used)
    "fee_pct": 0.10,                # spec: 10 bp commission per side
    "slippage_pct": 0.10,           # spec: 5 bp half-spread + 5 bp adverse slippage per fill
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 1000,             # >= 5x the longest recursive indicator period (EXECUTION.md warm-up)
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


def _week(df):
    def calc():
        key, wopen = bars_since_period_start(df, "W")
        k = key.to_numpy()
        below = (df["close"] < wopen).astype(int)
        # an earlier completed bar of the same UTC week closed below the week open
        earlier_below = below.groupby(k).transform(lambda s: s.shift(1).cummax()).fillna(0).astype(bool)
        same_week = key.eq(key.shift(1))
        return wopen, earlier_below, same_week
    return _memo(("week", id(df)), calc)


def buy_signal(df, p):
    wopen, earlier_below, same_week = _week(df)
    c = df["close"]
    return same_week & (c > wopen) & (c.shift(1) <= wopen) & earlier_below & (c > sma(c, p["n"]))


def sell_signal(df, p):
    wopen, _, _ = _week(df)
    return df["close"] < wopen
