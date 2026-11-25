CONFIG = {
    "name": "crypto_utc_overnight_window",
    "asset_class": "crypto",
    "symbols": ["BTCUSDT"],           # spec: BTC/USD
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
    "n": 200,
    "stop_atr": 2.0, "take_profit_atr": 3.0, "max_candles": 48,
}

SPACE = {
    "n": {"min": 50, "max": 300, "step": 25, "hard_min": 2},
    "stop_atr": {"min": 1.0, "max": 4.0, "step": 0.25, "hard_min": 0.5},
    "take_profit_atr": {"min": 1.5, "max": 6.0, "step": 0.5, "hard_min": 0.5},
}


def valid(p: dict) -> bool:
    return True


def buy_signal(df, p):
    # the bar opening 21:00 closes at 22:00 -> entry at the 22:00 open
    c = df["close"]
    return pd.Series(df.index.hour == 21, index=df.index) & (c > sma(c, p["n"]))


def sell_signal(df, p):
    # scheduled exit at the 00:00 UTC open = signal on the bar opening 23:00
    return pd.Series(df.index.hour == 23, index=df.index)
