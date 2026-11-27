"""EUR/USD London breakout: vectorised day-by-day simulation on 1-minute bars.

Rules (spec in README.md, defaults = the original description):
  * Asian range = high/low of 00:00-07:00 UTC (the 15m candles 00:00..06:45; identical
    to the 1m high/low of the same window).
  * Entry window [entry_start, entry_end) UTC.  Long when price breaks above
    Asian high + buffer; optional short when it breaks below Asian low - buffer.
    entry_mode "touch":   stop order, filled at max(minute open, level) (gaps fill worse).
    entry_mode "close15": a 15m candle must close beyond the level; filled at that close.
  * Stop: Asian high - stop_frac * range for longs (stop_frac=1 -> Asian low, the spec).
  * Take profit: entry + tp_mult * range (spec: 2x the range).  tp_mult=0 -> no TP.
  * Flat at exit_hour UTC (spec 16:00) at the last available price before it.
  * One trade per day.  Stop and TP in the same minute -> stop (conservative).
  * Costs: cost_pips per round trip (spread + slippage; data are bid prices).
Results are in pips and in R (= pnl / initial risk).
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
PIP = 1e-4
N_MIN = 17 * 60  # 00:00 .. 16:59 UTC

DEFAULT = dict(entry_mode="touch", entry_start=7, entry_end=16, buffer_pips=0.0,
               stop_frac=1.0, tp_mult=2.0, exit_hour=16, direction="long",
               min_range_pips=0.0, max_range_pips=1e9, cost_pips=1.0)


@dataclass
class Days:
    dates: pd.DatetimeIndex
    O: np.ndarray
    H: np.ndarray
    L: np.ndarray
    C: np.ndarray
    valid: np.ndarray  # enough data + not DST-ambiguous + weekday


def load_days(min_cov: float = 0.8) -> Days:
    cache = HERE / "data" / "days.npz"
    if cache.exists():
        z = np.load(cache, allow_pickle=False)
        return Days(pd.DatetimeIndex(z["dates"]).tz_localize("UTC"), z["O"], z["H"], z["L"], z["C"], z["valid"])
    m1 = pd.read_parquet(HERE / "data" / "eurusd_m1.parquet")
    q = pd.read_parquet(HERE / "data" / "day_quality.parquet")
    m1 = m1[m1.index.hour < 17]
    day = m1.index.normalize()
    dates = pd.DatetimeIndex(sorted(set(day[m1.index.day_of_week < 5])))
    di = dates.get_indexer(day)
    keep = di >= 0
    mi = (m1.index.hour * 60 + m1.index.minute).to_numpy()
    arrs = {}
    for c in ("open", "high", "low", "close"):
        a = np.full((len(dates), N_MIN), np.nan, dtype=np.float64)
        a[di[keep], mi[keep]] = m1[c].to_numpy()[keep]
        arrs[c] = a
    q = q.reindex(dates)
    valid = ((q.asia_min >= 420 * min_cov) & (q.london_min >= 540 * min_cov)
             & ~q.dst_ambiguous.fillna(True).astype(bool)).to_numpy()
    np.savez_compressed(cache, dates=dates.tz_localize(None).to_numpy(), O=arrs["open"], H=arrs["high"],
                        L=arrs["low"], C=arrs["close"], valid=valid)
    return Days(dates, arrs["open"], arrs["high"], arrs["low"], arrs["close"], valid)


def _first(mask: np.ndarray) -> np.ndarray:
    """index of first True per row, N_MIN if none."""
    has = mask.any(axis=1)
    return np.where(has, mask.argmax(axis=1), N_MIN)


def _last_valid_before(C: np.ndarray, end: int) -> np.ndarray:
    sub = C[:, :end]
    ok = ~np.isnan(sub)
    idx = end - 1 - ok[:, ::-1].argmax(axis=1)
    out = sub[np.arange(len(C)), idx]
    out[~ok.any(axis=1)] = np.nan
    return out


def simulate(d: Days, p: dict) -> pd.DataFrame:
    """One row per valid day with a trade: date, dir, entry, stop, tp, exit, reason, pips, R."""
    p = {**DEFAULT, **p}
    n = len(d.dates)
    cols = np.arange(N_MIN)
    hi = np.nanmax(d.H[:, :420], axis=1)
    lo = np.nanmin(d.L[:, :420], axis=1)
    rng = hi - lo
    rp = rng / PIP
    ok = d.valid & (rp > 0) & (rp >= p["min_range_pips"]) & (rp <= p["max_range_pips"])
    a, b = int(p["entry_start"] * 60), int(p["entry_end"] * 60)
    x = int(p["exit_hour"] * 60)
    b = min(b, x)
    buf = p["buffer_pips"] * PIP
    win = (cols >= a) & (cols < b)

    res = {}
    for side in ("long", "short"):
        if p["direction"] not in (side, "both"):
            continue
        sgn = 1 if side == "long" else -1
        level = (hi + buf) if sgn > 0 else (lo - buf)
        if p["entry_mode"] == "touch":
            hit = (d.H >= level[:, None]) if sgn > 0 else (d.L <= level[:, None])
            e = _first(hit & win)
            ee = np.minimum(e, N_MIN - 1)
            o = d.O[np.arange(n), ee]
            o = np.where(np.isnan(o), level, o)
            px = np.maximum(o, level) if sgn > 0 else np.minimum(o, level)
            start = e + 1
        else:  # close15: 15m close beyond level, filled at that close
            nb = N_MIN // 15
            Cb = d.C.reshape(n, nb, 15)
            okb = ~np.isnan(Cb)
            lastidx = 14 - okb[:, :, ::-1].argmax(axis=2)
            c15 = np.take_along_axis(Cb, lastidx[:, :, None], axis=2)[:, :, 0]
            c15[~okb.any(axis=2)] = np.nan
            bend = np.arange(nb) * 15 + 15  # minute after the block
            bwin = (np.arange(nb) * 15 >= a) & (bend <= b)
            hitb = (c15 > level[:, None]) if sgn > 0 else (c15 < level[:, None])
            eb = _first_n(hitb & bwin, nb)
            e = np.where(eb < nb, eb * 15 + 14, N_MIN)
            px = np.where(eb < nb, c15[np.arange(n), np.minimum(eb, nb - 1)], np.nan)
            start = e + 1
        entered = ok & (e < b)
        stop = hi - p["stop_frac"] * rng if sgn > 0 else lo + p["stop_frac"] * rng
        risk = (px - stop) * sgn
        entered &= risk > 0
        tp = px + sgn * p["tp_mult"] * rng if p["tp_mult"] > 0 else np.full(n, np.nan)
        after = (cols[None, :] >= start[:, None]) & (cols[None, :] < x)
        s_hit = (d.L <= stop[:, None]) if sgn > 0 else (d.H >= stop[:, None])
        si = _first(s_hit & after)
        if p["tp_mult"] > 0:
            t_hit = (d.H >= tp[:, None]) if sgn > 0 else (d.L <= tp[:, None])
            ti = _first(t_hit & after)
        else:
            ti = np.full(n, N_MIN)
        eod = _last_valid_before(d.C, x)
        so = d.O[np.arange(n), np.minimum(si, N_MIN - 1)]
        so = np.where(np.isnan(so), stop, so)
        stop_px = np.minimum(so, stop) if sgn > 0 else np.maximum(so, stop)
        reason = np.where(si <= ti, np.where(si < N_MIN, "stop", "time"), "tp")
        exit_px = np.where(reason == "stop", stop_px, np.where(reason == "tp", tp, eod))
        exit_min = np.where(reason == "stop", si, np.where(reason == "tp", ti, x))
        pips = (exit_px - px) * sgn / PIP - p["cost_pips"]
        R = pips / (risk / PIP)
        res[side] = dict(e=np.where(entered, e, N_MIN), px=px, stop=stop, tp=tp, exit=exit_px,
                         reason=reason, pips=pips, R=R, risk=risk / PIP, exit_min=exit_min, sgn=sgn)

    if not res:
        return pd.DataFrame()
    sides = list(res)
    if len(sides) == 2:
        pick_long = res["long"]["e"] <= res["short"]["e"]
        same = res["long"]["e"] == res["short"]["e"]
    out = {}
    for k in ("e", "px", "stop", "tp", "exit", "reason", "pips", "R", "risk", "exit_min"):
        if len(sides) == 2:
            out[k] = np.where(pick_long, res["long"][k], res["short"][k])
        else:
            out[k] = res[sides[0]][k]
    dirn = (np.where(pick_long, 1, -1) if len(sides) == 2 else np.full(n, res[sides[0]]["sgn"]))
    traded = out["e"] < N_MIN
    if len(sides) == 2:
        traded &= ~same  # both levels in the same minute: skip (can't tell which came first)
    df = pd.DataFrame({k: v for k, v in out.items()}, index=d.dates)
    df["dir"] = dirn
    df["range_pips"] = rp
    return df[traded]


def _first_n(mask: np.ndarray, n: int) -> np.ndarray:
    has = mask.any(axis=1)
    return np.where(has, mask.argmax(axis=1), n)


def metrics(tr: pd.DataFrame, d: Days, start=None, end=None, risk_pct: float = 1.0) -> dict:
    """Stats over valid days in [start, end).  Daily return = risk_pct% * R (0 on no-trade days)."""
    days = d.dates[d.valid]
    if start is not None:
        days = days[days >= pd.Timestamp(start, tz="UTC")]
    if end is not None:
        days = days[days < pd.Timestamp(end, tz="UTC")]
    t = tr[tr.index.isin(days)]
    r = pd.Series(0.0, index=days)
    r.loc[t.index] = t.R.to_numpy() * risk_pct / 100
    eq = (1 + r).cumprod()
    yrs = max(len(days) / 252, 1e-9)
    sd = r.std()
    gains, losses = t.pips[t.pips > 0].sum(), -t.pips[t.pips < 0].sum()
    return {
        "days": int(len(days)), "trades": int(len(t)),
        "win_rate": round(float((t.pips > 0).mean()), 3) if len(t) else None,
        "avg_R": round(float(t.R.mean()), 3) if len(t) else None,
        "total_R": round(float(t.R.sum()), 1),
        "avg_pips": round(float(t.pips.mean()), 2) if len(t) else None,
        "total_pips": round(float(t.pips.sum()), 0),
        "profit_factor": round(float(gains / losses), 2) if losses > 0 else None,
        "sharpe": round(float(r.mean() / sd * np.sqrt(252)), 2) if sd > 0 else 0.0,
        "cagr_pct": round(float((eq.iloc[-1] ** (1 / yrs) - 1) * 100), 2) if len(eq) else 0.0,
        "max_dd_pct": round(float((1 - eq / eq.cummax()).max() * 100), 1) if len(eq) else 0.0,
        "t_stat": round(float(t.R.mean() / t.R.std() * np.sqrt(len(t))), 2) if len(t) > 2 else None,
    }
