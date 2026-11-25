CONFIG = {
    "name": "rolling_resistance_retest",
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
    "n": 20,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "n": {"min": 10, "max": 60, "step": 5, "hard_min": 2},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
    "max_candles": {"min": 24, "max": 96, "step": 9, "hard_min": 1},
}


def valid(p: dict) -> bool:
    return True


def _B(df, p):
    # B for a signal at t = HH(H, n) as of t-3, i.e. the resistance broken by the close of t-2
    return _memo(("B", id(df), int(p["n"])), lambda: hh(df["high"], p["n"]).shift(3))


def buy_signal(df, p):
    B = _B(df, p)
    c, h, l = df["close"], df["high"], df["low"]
    return (c.shift(2) > B) & (l.shift(1) <= B) & (c.shift(1) >= B) & (c > h.shift(1))


def sell_signal(df, p):
    # entry veto at the signal bar; while held, the frozen B comes from entry_level
    return pd.Series(False, index=df.index)


def entry_level(df, p):
    return _B(df, p)
