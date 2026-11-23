"""Binance public data archive (data.binance.vision): S3 listing, checksummed downloads.

Listing the bucket tells us exactly which files exist, so we never probe
months before a listing or after a delisting (no 404 storms).
"""
from __future__ import annotations

import hashlib
import os
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
FILES = "https://data.binance.vision/"
_NS = {"s": "http://s3.amazonaws.com/doc/2006-03-01/"}
session = requests.Session()

# Not useful as trading history: stablecoin/fiat legs and leveraged tokens.
STABLE_FIAT = {
    "USDC", "BUSD", "TUSD", "FDUSD", "USDP", "PAX", "DAI", "USDS", "USDSB", "SUSD", "UST", "USTC", "PYUSD",
    "EUR", "GBP", "AUD", "TRY", "BRL", "RUB", "ZAR", "UAH", "NGN", "BIDR", "IDRT", "BKRW", "EURI", "AEUR",
    "USD1", "XUSD", "BFUSD", "USDE", "RLUSD", "PAXG", "XAUT", "U", "VAI", "USDD", "FRAX", "BVND",
    "BULL", "BEAR",  # leveraged BTC tokens
}
LEVERAGED_SUFFIXES = ("UP", "DOWN", "BULL", "BEAR")


class Retryable(Exception):
    pass


@retry(retry=retry_if_exception_type((Retryable, requests.ConnectionError, requests.Timeout)),
       wait=wait_exponential(multiplier=2, max=120), stop=stop_after_attempt(8), reraise=True)
def _get(url: str, **kw) -> requests.Response:
    r = session.get(url, timeout=kw.pop("timeout", 60), **kw)
    if r.status_code in (418, 429) or r.status_code >= 500:
        raise Retryable(f"HTTP {r.status_code} for {url}")
    return r


def ls(prefix: str, delimiter: bool = True) -> tuple[list[str], list[tuple[str, int]]]:
    """List the archive bucket: (sub-prefixes, [(key, size)]), following pagination."""
    prefixes, keys, marker = [], [], None
    while True:
        params = {"prefix": prefix}
        if delimiter:
            params["delimiter"] = "/"
        if marker:
            params["marker"] = marker
        r = _get(S3, params=params)
        r.raise_for_status()
        x = ET.fromstring(r.content)
        ps = [p.find("s:Prefix", _NS).text for p in x.findall("s:CommonPrefixes", _NS)]
        ks = [(c.find("s:Key", _NS).text, int(c.find("s:Size", _NS).text)) for c in x.findall("s:Contents", _NS)]
        prefixes += ps
        keys += ks
        if x.find("s:IsTruncated", _NS).text != "true" or not (ps or ks):
            return prefixes, keys
        marker = max([k for k, _ in ks] + ps)


def zips(prefix: str) -> dict[str, int]:
    """{period: size} for the .zip files under a prefix, period = 'YYYY-MM' or 'YYYY-MM-DD'."""
    _, keys = ls(prefix, delimiter=False)
    out = {}
    for k, size in keys:
        if k.endswith(".zip"):
            name = k.rsplit("/", 1)[1][:-4]          # BTCUSDT-1m-2024-01 / BTCUSDT-trades-2024-01
            parts = name.split("-")
            out["-".join(p for p in parts if p.isdigit())] = size
    return out


def all_usdt_pairs() -> list[str]:
    """Every USDT spot pair Binance ever published 1m klines for (incl. delisted), minus
    stablecoin/fiat legs and leveraged tokens."""
    prefixes, _ = ls("data/spot/monthly/klines/")
    out = []
    for p in prefixes:
        s = p.rstrip("/").rsplit("/", 1)[1]
        if not s.endswith("USDT") or not s.isascii():
            continue
        b = s[:-4]
        if not b or b in STABLE_FIAT or (b.endswith(LEVERAGED_SUFFIXES) and len(b) > 4):
            continue
        out.append(s)
    return sorted(out)


def download(key: str, dest: Path | None = None) -> bytes | Path | None:
    """Download + SHA256-verify an archive file. In memory, or streamed to `dest` (big files).
    Returns None if the file doesn't exist."""
    url = FILES + key
    r = _get(url + ".CHECKSUM")
    if r.status_code == 404:
        return None
    r.raise_for_status()
    expected = r.text.split()[0].lower()
    h = hashlib.sha256()
    if dest is None:
        r = _get(url)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        h.update(r.content)
        if h.hexdigest() != expected:
            raise RuntimeError(f"checksum mismatch for {key}")
        return r.content
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name("." + dest.name + ".part")
    with _get(url, stream=True, timeout=300) as r:
        if r.status_code == 404:
            return None
        r.raise_for_status()
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(8 << 20):
                h.update(chunk)
                f.write(chunk)
    if h.hexdigest() != expected:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"checksum mismatch for {key}")
    os.replace(tmp, dest)
    return dest
