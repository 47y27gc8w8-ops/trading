CONFIG = {
    "name": "bollinger_squeeze_release",
    "asset_class": "crypto",
    "symbols": ["ETHUSDT"],           # spec: ETH/USD
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
    "lookback": 120,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "lookback": {"min": 60, "max": 252, "step": 12, "hard_min": 10},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 9, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def _bbw(df):
    def calc():
        bl, mid, bu = bbands(df, 20, 2.0)
        return 100 * (bu - bl) / mid
    return _memo(("bbw", id(df)), calc)


def buy_signal(df, p):
    w = _bbw(df)
    q = _memo(("bbwq", id(df), int(p["lookback"])), lambda: prior_quantile(w, p["lookback"], 0.10))
    _, _, bu = bbands(df, 20, 2.0)
    return (w.shift(1) <= q.shift(1)) & (df["close"] > bu)


def sell_signal(df, p):
    return df["close"] < sma(df["close"], 20)
