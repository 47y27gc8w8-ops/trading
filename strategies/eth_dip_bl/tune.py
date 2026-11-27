"""Time-boxed random search over SPACE on the in-sample period only; OOS is reported, never used to choose.

    docker compose run --rm -T backtest python strategies/eth_dip_bl/tune.py --seconds 150
Writes results.jsonl (every candidate) and best.json (IS-best + OOS check) next to this file.
"""
import argparse, itertools, json, random, sys, time

from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import backtest as bt  # noqa: E402



def fitness(m):
    """Calmar-like: yearly return / |max DD|, needs >= 20 trades. Higher is better."""
    if m["n_trades"] < 20 or m["max_dd_pct"] == 0:
        return -99.0
    return m["yearly_return_pct"] / abs(m["max_dd_pct"])


def grid():
    keys = list(bt.SPACE)
    vals = []
    for k in keys:
        s = bt.SPACE[k]
        if "choices" in s:
            vals.append(s["choices"])
        else:
            v, out = s["min"], []
            while v <= s["max"] + 1e-9:
                out.append(v); v += s["step"]
            vals.append(out)
    return [dict(zip(keys, c)) for c in itertools.product(*vals)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=150)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    cands = [p for p in grid() if bt.valid(p)]
    random.Random(a.seed).shuffle(cands)
    cands.insert(0, dict(bt.PARAMS))  # baseline first
    t0, rows = time.time(), []
    with open(HERE / "results.jsonl", "w") as f:
        for p in cands:
            if time.time() - t0 > a.seconds:
                break
            m = bt.run(p, "is")["metrics"]
            row = {"params": p, "fitness": round(fitness(m), 4), "is": {k: m[k] for k in (
                "return_pct", "yearly_return_pct", "max_dd_pct", "n_trades", "win_rate", "profit_factor", "largest_loss_pct")}}
            rows.append(row); f.write(json.dumps(row) + "\n")
    rows.sort(key=lambda r: r["fitness"], reverse=True)
    top = rows[:10]
    for r in top:
        m = bt.run(r["params"], "oos")["metrics"]
        r["oos"] = {k: m[k] for k in ("return_pct", "yearly_return_pct", "max_dd_pct", "n_trades", "win_rate",
                                      "profit_factor", "largest_loss_pct", "buy_hold_return_pct")}
    base = next(r for r in rows if r["params"] == bt.PARAMS)
    base["oos"] = {k: v for k, v in bt.run(bt.PARAMS, "oos")["metrics"].items() if k in top[0]["oos"]}
    out = {"tested": len(rows), "of": len(cands), "seconds": round(time.time() - t0, 1), "baseline": base, "top10": top}
    (HERE / "best.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
