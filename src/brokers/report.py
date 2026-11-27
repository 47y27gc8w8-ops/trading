#!/usr/bin/env python3
"""Daily e-mail report for all paper bots (one mail, all bots).

    python3 src/brokers/report.py              # scheduled mode: send unless today's report went out already
    python3 src/brokers/report.py --send-now   # send immediately (test)
    python3 src/brokers/report.py --print      # print the text version, send nothing

Runs on the host with the standard library only (systemd timer broker-report.timer, 20:00
Europe/Zurich). Mail goes through msmtp, which reads the SMTP account and password from
~/.msmtprc itself: this script never reads, logs or stores credentials. The recipient is the
`from` address configured in ~/.msmtprc (override with BROKER_REPORT_TO).

Per bot: equity, P&L for the last 24 h and since start, trades (24 h / total), open positions,
max drawdown since start, errors and downtime in the last 24 h.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "data" / "brokers" / "brokers.db"
STATE = ROOT / "data" / "brokers" / "report_state.json"
ZRH = ZoneInfo("Europe/Zurich")
GAP_S = 180          # a gap between equity rows longer than this counts as downtime
STALE_S = 300        # no heartbeat for this long = bot down now


def iso(t: datetime) -> str:
    return t.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def collect(con: sqlite3.Connection, now: datetime) -> list[dict]:
    since = now - timedelta(hours=24)
    out = []
    for b in con.execute("SELECT * FROM bots ORDER BY rowid"):
        bid = b["id"]
        st = con.execute("SELECT * FROM state WHERE bot_id=?", (bid,)).fetchone()
        eq_rows = con.execute("SELECT ts, equity FROM equity WHERE bot_id=? ORDER BY ts", (bid,)).fetchall()
        start = b["start_balance"]
        equity = eq_rows[-1]["equity"] if eq_rows else start
        prev = start
        for r in eq_rows:                     # last value at or before 24 h ago
            if r["ts"] <= iso(since):
                prev = r["equity"]
            else:
                break
        mdd = (st["max_dd"] if st and st["max_dd"] is not None else 0.0)
        # downtime: gaps between consecutive equity rows in the window, plus "down right now"
        down, last_t = 0.0, None
        for r in eq_rows:
            t = parse(r["ts"])
            if t < since:
                last_t = t
                continue
            ref = last_t if last_t and last_t >= since else (since if last_t else None)
            if ref and (t - ref).total_seconds() > GAP_S:
                down += (t - ref).total_seconds()
            last_t = t
        hb = parse(st["heartbeat"]) if st and st["heartbeat"] else None
        if hb and (now - hb).total_seconds() > STALE_S:
            down += (now - max(hb, since)).total_seconds()
        errs = con.execute("SELECT ts, message FROM events WHERE bot_id=? AND level='error' AND ts>? ORDER BY ts",
                           (bid, iso(since))).fetchall()
        restarts = con.execute("SELECT count(*) FROM events WHERE bot_id=? AND kind='start' AND ts>?",
                               (bid, iso(since))).fetchone()[0]
        n24 = con.execute("SELECT count(*) FROM trades WHERE bot_id=? AND ts>?", (bid, iso(since))).fetchone()[0]
        ntot = con.execute("SELECT count(*) FROM trades WHERE bot_id=?", (bid,)).fetchone()[0]
        fx = (st["fx_usdchf"] if st else None) or 0
        pos = [dict(symbol=p["symbol"], value=p["qty"] * (p["last_price_usd"] or p["avg_price_usd"]) * fx,
                    pnl=p["qty"] * (p["last_price_usd"] or p["avg_price_usd"]) * fx - p["cost"])
               for p in con.execute("SELECT * FROM positions WHERE bot_id=? ORDER BY symbol", (bid,))]
        out.append(dict(
            id=bid, strategy=b["strategy"], asset_class=b["asset_class"], timeframe=b["timeframe"],
            status=("down" if hb and (now - hb).total_seconds() > STALE_S else (st["status"] if st else "never ran")),
            message=st["message"] if st else "", equity=equity, start=start,
            pnl_day=equity - prev, pnl_day_pct=(equity / prev - 1) * 100 if prev else 0,
            pnl_total=equity - start, pnl_total_pct=(equity / start - 1) * 100,
            trades_day=n24, trades_total=ntot, positions=pos, max_dd_pct=mdd * 100,
            errors=len(errs), last_error=(errs[-1]["message"] if errs else ""), restarts=restarts,
            downtime_min=down / 60))
    return out


def money(v: float, sign: bool = False) -> str:
    return f"{v:+,.2f}" if sign else f"{v:,.2f}"


def render(rows: list[dict], now: datetime) -> tuple[str, str, str]:
    tot_eq = sum(r["equity"] for r in rows)
    tot_start = sum(r["start"] for r in rows)
    tot_day = sum(r["pnl_day"] for r in rows)
    issues = sum(1 for r in rows if r["errors"] or r["downtime_min"] >= 5 or r["status"] in ("down", "error"))
    local = now.astimezone(ZRH)
    subject = (f"Paper brokers {local:%d.%m.%Y}: {money(tot_eq)} CHF ({money(tot_eq - tot_start, True)} since start, "
               f"{money(tot_day, True)} today)" + (f", {issues} with issues" if issues else ""))
    # ------------------------------------------------------------------ text ---
    t = [f"Paper-trading bots, report of {local:%A %d %B %Y %H:%M} Europe/Zurich", "PAPER ONLY: simulated fills, no real money.", "",
         f"All bots: equity {money(tot_eq)} CHF, since start {money(tot_eq - tot_start, True)} CHF "
         f"({(tot_eq / tot_start - 1) * 100:+.2f}%), last 24 h {money(tot_day, True)} CHF", ""]
    for r in rows:
        t += [f"{r['id']} ({r['strategy']}, {r['asset_class']} {r['timeframe']}) - {r['status']}",
              f"  equity {money(r['equity'])} CHF | 24 h {money(r['pnl_day'], True)} ({r['pnl_day_pct']:+.2f}%) | "
              f"since start {money(r['pnl_total'], True)} ({r['pnl_total_pct']:+.2f}%) | max DD {r['max_dd_pct']:.2f}%",
              f"  trades {r['trades_day']} in 24 h, {r['trades_total']} total | open: "
              + (", ".join(f"{p['symbol']} {money(p['value'])} ({money(p['pnl'], True)})" for p in r["positions"]) or "none"),
              f"  errors {r['errors']} | downtime {r['downtime_min']:.0f} min | restarts {r['restarts']}"
              + (f" | last error: {r['last_error'][:200]}" if r["last_error"] else ""), ""]
    text = "\n".join(t)
    # ------------------------------------------------------------------ html ---
    e = html.escape
    up, down, muted = "#1f9d55", "#d64560", "#666"
    col = lambda v: up if v > 0 else (down if v < 0 else muted)  # noqa: E731
    trs = []
    for r in rows:
        pos = "<br>".join(f"{e(p['symbol'])} {money(p['value'])} <span style='color:{col(p['pnl'])}'>{money(p['pnl'], True)}</span>"
                          for p in r["positions"]) or "<span style='color:#999'>none</span>"
        bad = r["errors"] or r["downtime_min"] >= 5 or r["status"] in ("down", "error")
        health = (f"{r['errors']} errors, {r['downtime_min']:.0f} min down, {r['restarts']} restarts"
                  + (f"<br><small style='color:#999'>{e(r['last_error'][:160])}</small>" if r["last_error"] else ""))
        trs.append(
            f"<tr><td><b>{e(r['id'])}</b><br><small style='color:#888'>{e(r['strategy'])} · {e(r['asset_class'])} {e(r['timeframe'])}"
            f" · {e(r['status'])}</small></td>"
            f"<td align=right><b>{money(r['equity'])}</b></td>"
            f"<td align=right style='color:{col(r['pnl_day'])}'>{money(r['pnl_day'], True)}<br><small>{r['pnl_day_pct']:+.2f}%</small></td>"
            f"<td align=right style='color:{col(r['pnl_total'])}'>{money(r['pnl_total'], True)}<br><small>{r['pnl_total_pct']:+.2f}%</small></td>"
            f"<td align=right>{r['trades_day']} / {r['trades_total']}</td>"
            f"<td>{pos}</td><td align=right style='color:{down if r['max_dd_pct'] < 0 else muted}'>{r['max_dd_pct']:.2f}%</td>"
            f"<td style='color:{down if bad else muted}'>{health}</td></tr>")
    th = "".join(f"<th align=left style='border-bottom:1px solid #ddd;padding:6px'>{h}</th>" for h in
                 ("Bot", "Equity CHF", "24 h", "Since start", "Trades 24 h / total", "Open positions", "Max DD", "Errors / downtime"))
    html_body = f"""<html><body style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;font-size:14px;color:#111">
<h2 style="margin:0 0 4px">Paper brokers · {local:%d %B %Y}</h2>
<p style="margin:0 0 12px;color:#666">Report of {local:%H:%M} Europe/Zurich. Paper trading only: simulated fills, no real money.</p>
<p style="font-size:16px">All bots: <b>{money(tot_eq)} CHF</b> ·
<span style="color:{col(tot_eq - tot_start)}">{money(tot_eq - tot_start, True)} since start ({(tot_eq / tot_start - 1) * 100:+.2f}%)</span> ·
<span style="color:{col(tot_day)}">{money(tot_day, True)} in the last 24 h</span></p>
<table cellspacing=0 cellpadding=6 style="border-collapse:collapse;font-size:13px">
<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table>
<p style="color:#888;font-size:12px">Each bot started with 10,000 CHF; fills pay 0.1 % fee and 0.05 % slippage. 24 h P&amp;L compares with the equity 24 hours ago.
Downtime = gaps of more than 3 minutes in a bot's equity record. Dashboard: http://h0melab:3000/brokers</p>
</body></html>"""
    return subject, text, html_body


def recipient() -> str:
    to = os.environ.get("BROKER_REPORT_TO")
    if to:
        return to
    rc = Path.home() / ".msmtprc"
    for line in rc.read_text().splitlines():   # only the non-secret `from` line is looked at
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "from":
            return parts[1]
    sys.exit("no recipient: set BROKER_REPORT_TO or a `from` line in ~/.msmtprc")


def send(subject: str, text: str, html_body: str) -> None:
    to = recipient()
    msg = EmailMessage()
    msg["From"] = f"Trading Homelab <{to}>"
    msg["To"] = to
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="h0melab")
    msg.set_content(text)
    msg.add_alternative(html_body, subtype="html")
    r = subprocess.run(["msmtp", to], input=msg.as_bytes(), capture_output=True, timeout=120)
    if r.returncode != 0:
        sys.exit(f"msmtp failed (exit {r.returncode}): {r.stderr.decode(errors='replace')[:500]}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--send-now", action="store_true", help="send immediately, even if today's report went out")
    ap.add_argument("--print", action="store_true", help="print the text report, send nothing")
    a = ap.parse_args()
    now = datetime.now(timezone.utc)
    today = now.astimezone(ZRH).date().isoformat()
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    if not (a.send_now or a.print) and state.get("last_sent") == today:
        print(f"report for {today} already sent, nothing to do")
        return
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True, timeout=30)
    con.row_factory = sqlite3.Row
    subject, text, html_body = render(collect(con, now), now)
    if a.print:
        print(subject, "\n", text, sep="")
        return
    send(subject, text, html_body)
    if not a.send_now:   # a manual test must not stop tonight's scheduled report
        STATE.write_text(json.dumps({"last_sent": today, "at": iso(now), "subject": subject}))
    print(f"sent: {subject}")


if __name__ == "__main__":
    main()
