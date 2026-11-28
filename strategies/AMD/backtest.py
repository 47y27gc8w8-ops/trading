"""AMD (ICT Power of 3: Accumulation - Manipulation - Distribution) intraday backtest.

Adapted copy of strategies/backtest.py. The template is long-only with percentage exits;
this strategy needs more, so the machinery was extended (see "Changes to the machinery").

Run inside the backtest container (repo root is /app):

    docker compose run --rm -T backtest python strategies/AMD/backtest.py --period is --trades
    ... --symbols BTCUSDT            crypto instead of EURUSD
    ... --period live                start -> newest data (ignores "end")

Rules (times are New York time, DST-aware; bars are 15 min, labelled by their start)
- Session day D: the Asian range runs from asia_start (e.g. 20:00) on D-1 to 00:00 on D.
  Asian high / low = highest high / lowest low of those bars (>= 50 % of the bars must exist).
  Midnight open = open of the first bar at/after 00:00 (must start before 01:00).
- Skip D if range_max_atr > 0 and (Asian high - Asian low) > range_max_atr x ATR(14) of the
  previous session days (ATR = RMA of true range over whole session days).
- Manipulation window: bars starting in [win_start, win_end).
  Long : the lowest low since win_start is below the Asian low (sweep), and the bar CLOSES
         inside the Asian range and above the midnight open.
  Short: the highest high since win_start is above the Asian high, and the bar closes
         inside the range and below the midnight open.
  Optional trend filter (trend_ma > 0): longs only if the previous session close is above
  its SMA(trend_ma) of session closes, shorts only if below.
  First qualifying bar of the day only -> entry at the next bar's open. One trade per day.
- Stop: sweep extreme (lowest low / highest high since win_start up to the signal bar)
  -/+ stop_buf x Asian range height. Always active, checked intrabar.
- Targets (resting limits, fill at the limit, never better):
  target_mode "split": half at the opposite side of the Asian range, half at entry +/- target_r x risk
  target_mode "range": all at the opposite side of the Asian range
  target_mode "r":     all at entry +/- target_r x risk
  risk = |entry fill - stop|. The stop is not moved after the first half fills.
- Session exit: whatever is still open is closed at the open of the first bar at/after
  exit_hour (or the first bar of the next session day, e.g. after a data gap).
- If stop and a target are touched in the same bar, the stop is assumed (conservative).

Changes to the machinery (vs. the template)
- load_bars: "EURUSD" is read from strategies/AMD/data/eurusd_m15.parquet (histdata.com M1 bid,
  resampled to 15 min; copied from strategies/eurusd_breakout_bl/data). Volume = 0.
- _simulate: long AND short, price-level stop and targets, partial (split) exits, session exit.
  Stop and session exits pay slippage; limit targets don't (EXECUTION.md). Fees on every fill.
- Costs per symbol: COSTS overrides CONFIG fee/slippage (EURUSD: 1 pip round trip).
- A trade record is one trading day (both halves of a split summed); exit_price is the
  quantity-weighted average exit, exit_reason is the reason of the last part to close.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2] if Path(__file__).resolve().parent.name != "strategies" else Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# --------------------------------------------------------------------------
# Strategy definition
# --------------------------------------------------------------------------
CONFIG = {
    "name": "amd",
    "asset_class": "crypto",        # EURUSD is a special case in load_bars; crypto lets screen.py use the coin universe
    "symbols": ["EURUSD"],
    "timeframe": "15min",
    "start": "2011-01-01",
    "oos_start": "2022-01-01",
    "end": "2026-11-13",            # last complete EURUSD day (frozen at setup)
    "capital": 10_000.0,
    "position_pct": 1.0,            # 100 % of equity notional, no leverage
    "fee_pct": 0.10,                # crypto default (Binance spot); EURUSD overridden in COSTS
    "slippage_pct": 0.05,
    "big_loss_pct": 2.0,
    "big_loss_mult": 2.0,
    "warmup_bars": 20_000,          # >= 200 session days of 15-min bars (SMA200 / ATR14 warm-up)
}

# Per-symbol (fee_pct, slippage_pct) overrides. EURUSD: no commission, 0.005 % per fill on
# stop/session/entry fills ~= 0.5 pip each side at 1.10 -> about 1 pip round trip, as in the
# user's earlier EURUSD study (strategies/eurusd_breakout_bl/README.md).
COSTS = {"EURUSD": (0.0, 0.005)}

PARAMS = {
    "asia_start": 20,       # Asian range start hour (NY), previous evening; range ends 00:00
    "win_start": 2,         # manipulation window start hour (NY)
    "win_end": 5,           # window end hour (NY), exclusive
    "exit_hour": 16,        # session close (NY)
    "range_max_atr": 0.5,   # skip day if Asian range > this x daily ATR(14); 0 = off
    "stop_buf": 0.1,        # stop distance beyond the sweep extreme, x Asian range height
    "target_mode": "split",
    "target_r": 2.5,        # "2-3x the risk"
    "trend_ma": 0,          # optional daily trend filter (SMA of session closes); 0 = off
    "sides": "both",
}

SPACE = {
    "range_max_atr": {"min": 0.0, "max": 1.5, "step": 0.1, "hard_min": 0.0},
    "stop_buf": {"min": 0.0, "max": 0.5, "step": 0.05, "hard_min": 0.0},
    "target_mode": {"choices": ["split", "range", "r"]},
    "target_r": {"min": 1.0, "max": 5.0, "step": 0.5, "hard_min": 0.5},
    "trend_ma": {"choices": [0, 50, 100, 200]},
}


def valid(p: dict) -> bool:
    return (0 <= p["win_start"] < p["win_end"] < p["exit_hour"] < p["asia_start"] <= 23
            and p["target_r"] > 0 and p["stop_buf"] >= 0 and p["range_max_atr"] >= 0)


NY = "America/New_York"
_SESSION: dict = {}


def _session(df: pd.DataFrame, p: dict) -> dict:
    """Parameter-light per-bar session arrays, cached per frame and session hours."""
    ck = (id(df), len(df), p["asia_start"], p["win_start"], p["win_end"], p["exit_hour"])
    if ck in _SESSION:
        return _SESSION[ck]
    A, W0, W1, X = p["asia_start"], p["win_start"], p["win_end"], p["exit_hour"]
    ny = df.index.tz_convert(NY)
    hny = (ny.hour + ny.minute / 60.0).to_numpy(float)
    key = (ny + pd.Timedelta(hours=24 - A)).tz_localize(None).normalize().asi8   # session day id
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    asia = hny >= A
    s = pd.DataFrame({"key": key, "o": o, "h": h, "l": l, "c": c, "hny": hny, "asia": asia})

    spacing = pd.Series(df.index[:5000]).diff().median().total_seconds()   # unit-safe (index may be us or ns)
    expected = (24 - A) * 3600 / spacing
    ag = s[asia].groupby("key").agg(ah=("h", "max"), al=("l", "min"), n=("h", "size"))
    ag = ag[ag["n"] >= 0.5 * expected]
    na = s[~asia].groupby("key").agg(mid=("o", "first"), fh=("hny", "first"))
    na = na[na["fh"] < 1.0]
    d = s.groupby("key").agg(o=("o", "first"), h=("h", "max"), l=("l", "min"), c=("c", "last"))
    pc = d["c"].shift(1)
    tr = pd.concat([d["h"] - d["l"], (d["h"] - pc).abs(), (d["l"] - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1 / 14, adjust=False, min_periods=14).mean()

    def bar(series: pd.Series) -> np.ndarray:
        return series.reindex(key).to_numpy(float)

    window = (~asia) & (hny >= W0) & (hny < W1)
    g = pd.Series(np.where(window, l, np.inf)).groupby(key)
    runlo = g.cummin().to_numpy(float)
    runhi = pd.Series(np.where(window, h, -np.inf)).groupby(key).cummax().to_numpy(float)
    out = {
        "key": key, "hny": hny, "window": window,
        "ah": bar(ag["ah"]), "al": bar(ag["al"]), "mid": bar(na["mid"]),
        "atr_prev": bar(atr.shift(1)), "close_prev": bar(d["c"].shift(1)),
        "runlo": runlo, "runhi": runhi,
        "flat": (~asia) & (hny >= X),
        "dclose": d["c"], "pos": d.index.get_indexer(key),
    }
    _SESSION[ck] = out
    return out


def signals(df: pd.DataFrame, p: dict) -> dict:
    """Per bar: dir (+1 long / -1 short / 0), stop level, range target, plus session arrays."""
    S = _session(df, p)
    c = df["close"].to_numpy(float)
    ah, al, mid = S["ah"], S["al"], S["mid"]
    rng = ah - al
    with np.errstate(invalid="ignore"):
        ok = S["window"] & np.isfinite(ah) & np.isfinite(al) & np.isfinite(mid) & np.isfinite(S["atr_prev"]) & (rng > 0)
        if p["range_max_atr"] > 0:
            ok &= rng <= p["range_max_atr"] * S["atr_prev"]
        inside = (c > al) & (c < ah)
        long = ok & (S["runlo"] < al) & inside & (c > mid)
        short = ok & (S["runhi"] > ah) & inside & (c < mid)
        if p["trend_ma"]:
            sma = S["dclose"].rolling(int(p["trend_ma"])).mean().shift(1).to_numpy(float)[S["pos"]]
            long &= S["close_prev"] > sma
            short &= S["close_prev"] < sma
    if p["sides"] == "long":
        short[:] = False
    elif p["sides"] == "short":
        long[:] = False
    anyb = long | short
    first = anyb & (pd.Series(anyb).groupby(S["key"]).cumsum().to_numpy() == 1)
    direction = np.where(first & long, 1, np.where(first & short, -1, 0)).astype(np.int8)
    stop = np.where(direction == 1, S["runlo"] - p["stop_buf"] * rng, S["runhi"] + p["stop_buf"] * rng)
    rtgt = np.where(direction == 1, ah, al)
    return {"dir": direction, "stop": stop, "rtgt": rtgt, "key": S["key"], "flat": S["flat"]}


def buy_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Informational: bars whose close triggers an entry (long or short), filled at the next open."""
    return pd.Series(signals(df, p)["dir"] != 0, index=df.index)


def sell_signal(df: pd.DataFrame, p: dict) -> pd.Series:
    """Informational: exits are stop / targets / session close inside _simulate."""
    return pd.Series(False, index=df.index)

# --------------------------------------------------------------------------
# Machinery (extended: EURUSD loader, long/short level-based simulation)
# --------------------------------------------------------------------------

_BARS: dict = {}


def load_bars(asset_class: str, symbol: str, timeframe: str) -> pd.DataFrame:
    """OHLCV with a UTC DatetimeIndex, using the project's loaders (EURUSD: local parquet)."""
    key = (asset_class, symbol, timeframe)
    if key in _BARS:
        return _BARS[key]
    from src.backtest import data  # project loader: Yahoo daily, adjusted for dividends and splits

    if symbol == "EURUSD":
        if timeframe != "15min":
            raise ValueError("EURUSD is only prepared as 15-min bars")
        df = pd.read_parquet(Path(__file__).resolve().parent / "data" / "eurusd_m15.parquet")
        df["volume"] = 0.0
    elif asset_class == "crypto":
        df = _crypto_bars(symbol, "1D" if timeframe == "1d" else timeframe)
    elif timeframe == "1d":
        df = data.load(asset_class, symbol)
    else:
        raise ValueError("Yahoo symbols only have daily history long enough to backtest (1m data covers ~1 month)")
    df = df[["open", "high", "low", "close", "volume"]].astype(float).dropna(subset=["open", "close"])
    _BARS[key] = df
    return df


def _crypto_bars(symbol: str, timeframe: str) -> pd.DataFrame:
    """UTC bars of any size built from the Binance 1m partitions, cached per symbol and timeframe
    (rebuilt when the 1m data is newer and the cache is older than 6 h)."""
    import time

    import duckdb

    from src.common.storage import CRYPTO_1M, DATA

    cache = DATA / "cache" / f"bars_{symbol}_{timeframe}.parquet"
    src_dir = CRYPTO_1M / f"symbol={symbol}"
    if not src_dir.exists():
        raise ValueError(f"no crypto data for {symbol}")
    newest = max(p.stat().st_mtime for p in src_dir.rglob("*.parquet"))
    if cache.exists() and (cache.stat().st_mtime >= newest or time.time() - cache.stat().st_mtime < 6 * 3600):
        df = pd.read_parquet(cache)
    else:
        secs = int(pd.Timedelta(timeframe).total_seconds())
        df = duckdb.sql(f"""
            SELECT to_timestamp(floor(epoch(open_time) / {secs}) * {secs}) AS date,
                   arg_min(open, open_time) AS open, max(high) AS high, min(low) AS low,
                   arg_max(close, open_time) AS close, sum(quote_volume) AS volume
            FROM read_parquet('{src_dir}/*/*/*.parquet')
            GROUP BY 1 ORDER BY 1
        """).df()
        df["date"] = pd.to_datetime(df["date"], utc=True)
        df = df.iloc[:-1]  # last bucket may be incomplete
        cache.parent.mkdir(parents=True, exist_ok=True)
        tmp = cache.with_suffix(f".{os.getpid()}.tmp")  # atomic: parallel runs may build the same cache
        df.to_parquet(tmp, index=False)
        tmp.replace(cache)
    return df.set_index("date").sort_index()


def _simulate(df: pd.DataFrame, sig: dict, p: dict, lo: int, hi: int, capital: float, symbol: str):
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    fee_pct, slip_pct = COSTS.get(symbol, (CONFIG["fee_pct"], CONFIG["slippage_pct"]))
    fee, slip = fee_pct / 100, slip_pct / 100
    D, STP, RT, key, flat = sig["dir"], sig["stop"], sig["rtgt"], sig["key"], sig["flat"]
    mode, R = p["target_mode"], float(p["target_r"])
    idx = df.index
    cash, trades = capital, []
    equity = np.full(hi - lo, np.nan)
    last = lo                                        # first bar index not yet written to equity
    for s in np.flatnonzero(D[lo:hi]) + lo:
        e = s + 1
        if s < last or e >= hi or key[e] != key[s] or flat[e]:
            continue
        d = int(D[s])
        ep = o[e] * (1 + d * slip)                   # entry fill (buy higher / sell lower)
        stop = STP[s]
        risk = d * (ep - stop)
        if not np.isfinite(risk) or risk <= 0:       # opened beyond the stop: no trade
            continue
        tr = ep + d * R * risk
        rt = RT[s] if d * (RT[s] - ep) > 0 else ep  # entry already past the range target: that part exits at entry
        legs = {"split": [[0.5, rt], [0.5, tr]], "range": [[1.0, rt]], "r": [[1.0, tr]]}[mode]
        q = cash * CONFIG["position_pct"] / (ep * (1 + fee))
        equity[last - lo:e - lo] = cash
        realized = -q * ep * fee                     # entry fee
        rem, value_out, reason = 1.0, 0.0, None

        def close(frac: float, raw: float, slipped: bool) -> None:
            nonlocal realized, rem, value_out
            xp = raw * (1 - d * slip) if slipped else raw
            realized += d * q * frac * (xp - ep) - q * frac * xp * fee
            value_out += frac * xp
            rem -= frac

        j = e
        while j < hi:
            if key[j] != key[e] or flat[j]:
                close(rem, o[j], True)
                reason = "session"
                break
            if (d == 1 and l[j] <= stop) or (d == -1 and h[j] >= stop):
                close(rem, min(o[j], stop) if d == 1 else max(o[j], stop), True)
                reason = "stop"
                break
            for leg in legs:
                if leg[0] > 0 and ((d == 1 and h[j] >= leg[1]) or (d == -1 and l[j] <= leg[1])):
                    close(leg[0], leg[1], False)
                    leg[0] = 0.0
                    reason = "target"
            if rem <= 1e-9:                          # all targets filled in bar j
                break
            equity[j - lo] = cash + realized + d * q * rem * (c[j] - ep)
            j += 1
        open_at_end = reason is None
        if open_at_end:
            j = hi - 1
            close(rem, c[j], True)
            reason = "end"
            j = hi
        x = min(j, hi - 1)                           # bar of the (last) exit
        pnl = realized
        trades.append({
            "symbol": symbol, "side": "long" if d == 1 else "short",
            "entry_time": str(idx[e]), "exit_time": str(idx[x]),
            "entry_price": ep, "exit_price": value_out, "qty": q, "pnl": pnl,
            "pnl_pct_of_equity": pnl / cash * 100, "bars": max(0, x - e), "exit_reason": reason,
            "stop": stop, "risk_r": round(pnl / (q * risk), 3),
        })
        cash += pnl
        last = j
        if open_at_end:
            break
    equity[last - lo:] = np.where(np.isnan(equity[last - lo:]), cash, equity[last - lo:])
    eq = pd.Series(equity, index=idx[lo:hi]).ffill().fillna(capital)
    return trades, eq


def _bounds(idx: pd.DatetimeIndex, period: str) -> tuple[int, int]:
    ts = lambda s: pd.Timestamp(s, tz="UTC") if s else None  # noqa: E731
    start, oos, end = ts(CONFIG["start"]), ts(CONFIG["oos_start"]), ts(CONFIG.get("end"))
    if end is not None:
        end = end + pd.Timedelta(days=1)           # "end" is the last included day
    a, b = {"is": (start, oos), "oos": (oos, end), "all": (start, end), "live": (start, None)}[period]
    lo = idx.searchsorted(a) if a is not None else 0
    hi = idx.searchsorted(b) if b is not None else len(idx)
    if period != "oos":
        lo = max(lo, int(CONFIG.get("warmup_bars", 0)))
    return int(lo), int(hi)


def run(params: dict | None = None, period: str = "is", symbols: list[str] | None = None) -> dict:
    """Backtest one parameter set on one period ("is", "oos", "all", "live").
    Returns {"metrics", "trades", "equity"}."""
    p = {**PARAMS, **(params or {})}
    syms = list(symbols or CONFIG["symbols"])
    per_cap = CONFIG["capital"] / len(syms)
    all_trades, curves, bh = [], [], []
    for sym in syms:
        df = load_bars(CONFIG["asset_class"], sym, CONFIG["timeframe"])
        lo, hi = _bounds(df.index, period)
        if hi - lo < 2:
            continue
        t, eq = _simulate(df, signals(df, p), p, lo, hi, per_cap, sym)
        all_trades += t
        curves.append(eq)
        bh.append(df["close"].iloc[hi - 1] / df["open"].iloc[lo] - 1)
    if not curves:
        raise ValueError(f"no bars for period {period}")
    equity = pd.concat(curves, axis=1).sort_index().ffill()
    equity = equity.fillna(per_cap).sum(axis=1)
    all_trades.sort(key=lambda t: t["exit_time"])
    m = metrics(all_trades, equity, len(syms))
    m["open_positions"] = [{"symbol": t["symbol"], "since": t["entry_time"], "entry_price": round(t["entry_price"], 6),
                            "side": t["side"]}
                           for t in all_trades if t["exit_reason"] == "end"]
    m["buy_hold_return_pct"] = round(float(np.mean(bh)) * 100, 2)
    return {"metrics": m, "trades": all_trades, "equity": equity}


def metrics(trades: list[dict], equity: pd.Series, n_symbols: int = 1) -> dict:
    pnl = np.array([t["pnl"] for t in trades], float)
    loss_pct = np.array([t["pnl_pct_of_equity"] for t in trades if t["pnl"] <= 0], float)
    big_thr = max(CONFIG["big_loss_pct"], CONFIG.get("big_loss_mult", 0) * abs(float(np.median(loss_pct))) if len(loss_pct) else 0.0)
    years = max((equity.index[-1] - equity.index[0]).days / 365.25, 1 / 365.25)
    growth = 1 + pnl.sum() / CONFIG["capital"]
    wins, losses = pnl[pnl > 0], pnl[pnl <= 0]
    gp, gl = float(wins.sum()), float(-losses.sum())
    dd = equity / equity.cummax() - 1
    dd_abs = (equity - equity.cummax()).min()
    worst = min(trades, key=lambda t: t["pnl"]) if trades else None
    cap = CONFIG["capital"]
    r = lambda v, d=2: round(float(v), d)  # noqa: E731
    return {
        "start": str(equity.index[0]), "end": str(equity.index[-1]),
        "net_profit": r(pnl.sum()), "return_pct": r(pnl.sum() / cap * 100),
        "yearly_return_pct": r((growth ** (1 / years) - 1) * 100 if growth > 0 else -100.0), "years": r(years),
        "gross_profit": r(gp), "gross_loss": r(gl),
        "n_trades": len(pnl), "win_rate": r(len(wins) / len(pnl) * 100 if len(pnl) else 0.0),
        "avg_win": r(wins.mean() if len(wins) else 0.0), "avg_loss": r(losses.mean() if len(losses) else 0.0),
        "avg_trade": r(pnl.mean() if len(pnl) else 0.0),
        "largest_loss": r(min(0.0, pnl.min()) if len(pnl) else 0.0),
        "largest_loss_pct": r(min(0.0, worst["pnl_pct_of_equity"]) if worst else 0.0),
        "max_dd": r(dd_abs), "max_dd_pct": r(dd.min() * 100),
        "profit_factor": r(gp / gl, 3) if gl > 0 else (999.0 if gp > 0 else 0.0),
        "n_big_losses": int(sum(t["pnl_pct_of_equity"] < -big_thr for t in trades)),
        "big_loss_threshold_pct": r(big_thr),
        "exposure_pct": r(sum(t["bars"] for t in trades) / max(1, len(equity)) / n_symbols * 100),
        "open_at_end": bool(trades and trades[-1]["exit_reason"] == "end"),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--period", choices=["is", "oos", "all", "live"], default="is")
    ap.add_argument("--symbols", default=None, help="comma-separated symbols instead of CONFIG['symbols']")
    ap.add_argument("--params", default="{}", help="JSON object overriding PARAMS")
    ap.add_argument("--trades", action="store_true", help="also print the trade list")
    a = ap.parse_args()
    p = {**PARAMS, **json.loads(a.params)}
    if not valid(p):
        sys.exit(f"invalid params: {p}")
    res = run(p, a.period, a.symbols.split(",") if a.symbols else None)
    out = {"config": CONFIG, "params": p, "period": a.period, "metrics": res["metrics"]}
    if a.trades:
        out["trades"] = res["trades"]
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
