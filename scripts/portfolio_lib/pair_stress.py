#!/usr/bin/env python3
"""Borrow-cost stress test for the pair specs: re-run the latest saved variant of every profile with
higher assumed borrow fees and log the result as an optimize.py note (run inside the backtest container).

    python scripts/portfolio_lib/pair_stress.py [name ...]
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "/app")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pairs as bp  # noqa: E402

ROOT = Path("/app")
LEVELS = {"etf": (1.0, 3.0), "crypto": (6.0, 10.0)}


def latest_variants(folder: Path) -> dict:
    best = {}
    for f in folder.glob(f"{folder.name}__*__v*.md"):
        m = re.match(rf"{folder.name}__(.+)__v(\d+)\.md$", f.name)
        if m and (m.group(1) not in best or int(m.group(2)) > best[m.group(1)][0]):
            best[m.group(1)] = (int(m.group(2)), f)
    return {k: v[1] for k, v in sorted(best.items())}


def main(names: list[str]) -> None:
    for name in names:
        folder = ROOT / "strategies" / name
        spec = importlib.util.spec_from_file_location(name, folder / "backtest.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        base = m.CONFIG["borrow_fee_pct_yr"]
        variants = latest_variants(folder)
        if not variants:
            subprocess.run(["python", "/opt/tso/optimize.py", str(folder), "--note",
                            "borrow stress: no saved variant to stress-test"], check=True, stdout=subprocess.DEVNULL)
            continue
        parts = []
        for prof, f in variants.items():
            params = json.loads(re.search(r"```json\n(.*?)\n```", f.read_text(), re.S).group(1))
            row = []
            for b in (base, *LEVELS[m.CONFIG["asset_class"]]):
                m.CONFIG["borrow_fee_pct_yr"] = b
                i, o = m.run(params, "is")["metrics"], m.run(params, "oos")["metrics"]
                row.append(f"{b:g} %/yr: IS {i['yearly_return_pct']:+.2f} %/yr, OOS {o['yearly_return_pct']:+.2f} %/yr")
            m.CONFIG["borrow_fee_pct_yr"] = base
            parts.append(f"{f.stem.split('__', 1)[1]} -> " + "; ".join(row))
        note = "borrow stress (assumed fee on the short leg, base then stress levels): " + " | ".join(parts)
        subprocess.run(["python", "/opt/tso/optimize.py", str(folder), "--note", note], check=True, stdout=subprocess.DEVNULL)
        print(name, "stressed", len(variants), "variants", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or list(bp.SPECS))
