#!/usr/bin/env python3
"""Progress of the 120-spec strategy library optimization, as a plain-text email.

Reads every worktree's strategies/ folder, the running optimizer containers and queue
processes, and merges all strategies/leaderboard.json files. Host python3, stdlib only.

  python3 scripts/library_progress.py --print          status to stdout, sends nothing
  python3 scripts/library_progress.py --mode daily     send the daily update now
  python3 scripts/library_progress.py --mode final     send the final report now
  python3 scripts/library_progress.py --auto           what cron runs every hour:
      daily update once per day in the 12:00 hour Europe/Zurich (MET/MEST);
      final report once, when no queue process or optimizer container is left,
      then this script removes its own crontab line (marker "# library-progress").
Add --dry-run to print an email instead of sending it.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

MAIN = Path("/home/luca/trading")
LIB_COMMIT = "6946552"  # "Add 120-strategy research library as optimizer inputs"
SEND = Path.home() / ".claude/skills/long-task-email/scripts/send_email.py"
STATE = MAIN / "logs/library-progress.state.json"
MARKER = "# library-progress"
TZ = ZoneInfo("Europe/Zurich")
SLOTS = 3
QUEUE_PAT = r"library_queue\.sh|run_queue\.sh|shard2_queue\.sh"


def sh(cmd: str) -> str:
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout


def library() -> list[str]:
    out = sh(f"git -C {MAIN} ls-tree --name-only -r {LIB_COMMIT} strategies/")
    return sorted({p.split("/")[1] for p in out.split() if p.endswith("/original.md")})


def roots() -> list[Path]:
    return [MAIN] + sorted(Path(p) for p in glob.glob(str(MAIN / ".claude/worktrees/*")) if Path(p).is_dir())


def run_finished(log: Path) -> bool:
    if not log.exists():
        return False
    ends = re.findall(r"note: run end: ([^\n]*)", log.read_text(errors="replace"))
    return bool(ends) and "stopped by signal" not in ends[-1]


def screen_empty(d: Path) -> bool:
    f = d / "screen.csv"
    if not f.exists() or not run_finished(d / "optimization.log"):
        return False
    rows = f.read_text().splitlines()
    return len(rows) > 1 and not any(",ok," in r or r.endswith(",ok") for r in rows[1:])


def queued_names(procs) -> set[str]:
    """Strategy names a live queue process still holds: from its arguments, and for queue
    scripts that carry their list inside the file, from the script's text."""
    text = []
    for line in procs:
        text.append(line)
        for tok in line.split():
            if tok.endswith(".sh") and os.path.isfile(tok):
                text.append(Path(tok).read_text(errors="replace"))
    return set(re.findall(r"[a-z0-9_]+", " ".join(text)))


def status(names, running, queued=frozenset()):
    st = {}
    for n in names:
        dirs = [r / "strategies" / n for r in roots() if (r / "strategies" / n / "backtest.py").exists()]
        done = [d for d in dirs if run_finished(d / "symbols/broad/optimization.log")]
        empty = [d for d in dirs if screen_empty(d)]
        if f"tso-{n}" in running:
            s, where = "running", dirs
        elif done:
            s, where = "done", done
        elif empty:
            s, where = "done (no symbol passed the screen)", empty
        elif dirs and n in queued:
            s, where = "waiting", dirs
        elif [d for d in dirs if (d / "summary.md").exists() and run_finished(d / "optimization.log")
              and not (d / "symbols/broad").exists()]:
            s, where = "done", [d for d in dirs if (d / "summary.md").exists()]   # hand-run (no broad basket stage)
        elif dirs:
            s, where = "stalled", dirs
        else:
            s, where = "not runnable", []
        st[n] = (s, where)
    return st


def finished_times(st):
    """Finish time of every done strategy (mtime of the broad log or of screen.csv)."""
    out = []
    for n, (s, where) in st.items():
        if s.startswith("done"):
            d = where[0]
            f = d / "symbols/broad/optimization.log"
            if not f.exists():
                f = d / ("screen.csv" if s != "done" else "summary.md")
            out.append(datetime.fromtimestamp(f.stat().st_mtime, timezone.utc))
    return sorted(out)


def leaderboard():
    entries, seen = [], set()
    for r in roots():
        f = r / "strategies/leaderboard.json"
        if not f.exists():
            continue
        for e in json.loads(f.read_text()).get("entries", []):
            k = (e["strategy"], e.get("tag"), tuple(e.get("symbols") or []), e["profile"])
            if k in seen or e.get("stale"):
                continue
            seen.add(k)
            entries.append(e)
    entries.sort(key=lambda e: e.get("conservative_yearly_pct") or -1e9, reverse=True)
    return entries


def fmt_entry(e):
    syms = e.get("symbols") or []
    where = (f"basket of {len(syms)}" if e.get("tag") == "broad"
             else e.get("tag") or (",".join(syms) if len(syms) <= 3 else f"{len(syms)} symbols"))
    return (f"  {e['strategy']:<36} {where:<18} {e['profile']:<12} "
            f"{e['conservative_yearly_pct']:>6.1f} %/yr  DD {e['worst_max_dd_pct']:>6.1f} %  "
            f"size for ~10% DD {e.get('position_pct_for_10pct_dd', 0):.0f} %")


def report(mode: str):
    names = library()
    running = set(sh("docker ps --format '{{.Names}}'").split())
    procs = []   # real queue processes only ("bash <queue>.sh args"), not the shells that launched them
    for l in sh(f"pgrep -af '{QUEUE_PAT}'").splitlines():
        t = l.split()
        if len(t) > 2 and os.path.basename(t[1]) == "bash" and re.search(QUEUE_PAT, t[2]) and "--container" not in t:
            procs.append(" ".join(t[1:]))
    st = status(names, running, queued_names(procs))
    groups = {}
    for n, (s, _) in st.items():
        groups.setdefault(s.split(" (")[0] if s.startswith("done") else s, []).append(n)
    done = [n for n, (s, _) in st.items() if s.startswith("done")]
    pending = groups.get("waiting", []) + groups.get("running", [])
    now = datetime.now(timezone.utc)
    times = finished_times(st)
    last24 = [t for t in times if t > now - timedelta(hours=24)]
    if pending:
        rate = len(last24) / 24 if len(last24) >= 3 else SLOTS / 1.6   # strategies per hour
        eta = now + timedelta(hours=len(pending) / rate)
        eta_s = f"{eta.astimezone(TZ):%a %d %b %H:%M} Swiss time (at {rate * 24:.0f} strategies/day)"
    else:
        eta_s = "-"
    lb = [e for e in leaderboard() if e["strategy"] in names]
    improved = sorted({e["strategy"] for e in lb})
    tso = sorted(x for x in running if x.startswith("tso-"))

    L = []
    if mode == "final":
        L += ["The library optimization is finished: no queue or optimizer container is running any more.", ""]
    L += [f"Library: {len(names)} strategies",
          f"  done (backtested and optimized): {len(done)}"
          f" ({len([n for n in done if st[n][0] != 'done'])} of them stopped at the screen: no symbol passed)",
          f"  with at least one validated variant on a leaderboard: {len([n for n in improved if n in names])}",
          f"  running now: {len(groups.get('running', []))}   waiting in a queue: {len(groups.get('waiting', []))}"
          f"   stalled: {len(groups.get('stalled', []))}",
          f"  not runnable on the per-symbol engine: {len(groups.get('not runnable', []))}",
          f"  finished in the last 24 h: {len(last24)}",
          f"  estimated end of the queues: {eta_s}", ""]
    if groups.get("stalled"):
        L += [f"Stalled ({len(groups['stalled'])}): set up but unfinished and in no running queue. "
              "Ask Claude to re-queue them:", "  " + ", ".join(groups["stalled"]), ""]
    L += [f"Running containers ({len(tso)}/{SLOTS} slots): {', '.join(tso) or 'none'}"]
    L += [f"Queue processes alive: {len(procs)}", ""]
    if mode != "final" and last24:
        L += ["Finished in the last 24 h:"] + [f"  {n}" for n in done
                                              if any(t > now - timedelta(hours=24) for t in finished_times({n: st[n]}))] + [""]
    if pending:
        L += ["Still to run:"] + [f"  {n} ({st[n][0]})" for n in pending] + [""]
    top = lb[:15 if mode == "final" else 8]
    if top:
        L += ["Best validated variants so far (conservative %/yr = the lower of in-sample and out-of-sample;",
              "DD = worst drawdown at 100% of equity per trade):"] + [fmt_entry(e) for e in top] + [""]
    if mode == "final":
        no_var = [n for n in done if n not in improved]
        if no_var:
            L += [f"Optimized, but no variant passed the out-of-sample and robustness checks ({len(no_var)}):",
                  "  " + ", ".join(no_var), ""]
    if groups.get("not runnable"):
        L += [f"Not runnable without new engine work or data ({len(groups['not runnable'])}): US 5-minute intraday specs "
              "(no intraday stock history), pair specs (no borrow data) and portfolio/rotation specs (the engine tests "
              "one symbol at a time). Tell Claude if you want any of these built.",
              "  " + ", ".join(groups["not runnable"]), ""]
    if mode == "final":
        L += ["Next steps:",
              "  1. Merge the worktree branches into main (each holds its strategies' results), then run",
              "     leaderboard.py once in main for one combined LEADERBOARD.md.",
              "  2. Ask Claude for analyst notes on the strategies with validated variants and pick what to paper-trade.",
              "  3. Decide on the not-runnable specs above.",
              "This daily email stops now (cron line removed)."]
    else:
        L += ["Progress: tail -f ~/trading/logs/library-queue-*.log    Containers: docker ps --filter name=tso-"]
    L += ["", "Backtest results only; nothing trades. Past results don't guarantee future returns."]
    subj = (f"[Claude] Done: library optimization finished, {len(done)}/{len(names)} strategies"
            if mode == "final" else
            f"[Claude] Library update: {len(done)}/{len(names)} done, {len(pending)} to go")
    finished = not pending and not procs and not tso
    return subj, "\n".join(L), finished


def send(subj, body, dry):
    if dry:
        print(subj, "\n", body, sep="")
        return True
    r = subprocess.run([sys.executable, str(SEND), "--subject", subj], input=body, text=True)
    return r.returncode == 0


def remove_cron():
    cur = sh("crontab -l")
    new = "".join(l + "\n" for l in cur.splitlines() if MARKER not in l)
    subprocess.run(["crontab", "-"], input=new, text=True, check=True)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--print", action="store_true")
    g.add_argument("--mode", choices=["daily", "final"])
    g.add_argument("--auto", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.print:
        subj, body, fin = report("daily")
        print(subj, f"(finished={fin})\n", body, sep="\n")
        return
    if a.mode:
        subj, body, _ = report(a.mode)
        send(subj, body, a.dry_run)
        return
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    if state.get("final_sent"):
        remove_cron()
        return
    subj, body, fin = report("daily")
    if fin:
        subj, body, _ = report("final")
        if send(subj, body, a.dry_run) and not a.dry_run:
            state["final_sent"] = datetime.now(timezone.utc).isoformat()
            STATE.write_text(json.dumps(state))
            remove_cron()
        return
    local = datetime.now(TZ)
    if local.hour == 12 and state.get("last_daily") != local.date().isoformat():
        if send(subj, body, a.dry_run) and not a.dry_run:
            state["last_daily"] = local.date().isoformat()
            STATE.write_text(json.dumps(state))


if __name__ == "__main__":
    main()
