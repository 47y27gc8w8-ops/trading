/* Markets dashboard — vanilla JS SPA (hash routes: #/, #/asset/SYM, #/portfolio, #/data) */
"use strict";

const REFRESH_MS = 15000;
const TZ_SHIFT = -new Date().getTimezoneOffset() * 60; // charts show local time
const LC = window.LightweightCharts;
const WATCH = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "SPY"];

const state = { assets: [], bySym: {}, prevPrice: {}, view: null, timer: null, lastOk: 0, loadError: null, feed: null };

/* ------------------------------------------------------------ helpers --- */
const $ = (sel, el = document) => el.querySelector(sel);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const css = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();

async function api(path, opts = {}) {
  const r = await fetch(path, { headers: { "Content-Type": "application/json" }, ...opts });
  if (!r.ok) {
    let msg = r.statusText;
    try { const j = await r.json(); msg = typeof j.detail === "string" ? j.detail : JSON.stringify(j.detail); } catch {}
    throw new Error(msg);
  }
  return r.json();
}

function decimals(v) {
  const a = Math.abs(v);
  return a >= 10 ? 2 : a >= 1 ? 4 : a >= 0.01 ? 5 : 7;
}
const fmtPrice = (v) => v == null ? "—" : v.toLocaleString("en-US", { minimumFractionDigits: decimals(v), maximumFractionDigits: decimals(v) });
const CUR = { USD: "$", USDT: "$", EUR: "€", GBP: "£", pts: "" };
const money = (a, v) => {
  if (v == null) return "—";
  const c = a?.currency;
  if (c == null || c in CUR) return (c == null ? "$" : CUR[c]) + fmtPrice(v);
  return c + " " + fmtPrice(v);  // CHF, ...
};
const fmtUsd = (v, d = 2) => v == null ? "—" : (v < 0 ? "-" : "") + "$" + Math.abs(v).toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });
const fmtSignedUsd = (v) => v == null ? "—" : Math.abs(v) < 0.005 ? "$0.00" : (v > 0 ? "+" : "") + fmtUsd(v);
const fmtQty = (v) => v == null ? "—" : v.toLocaleString("en-US", { maximumFractionDigits: 8 });
const fmtCompact = (v, cur = "$") => v == null ? "—" : cur + Intl.NumberFormat("en-US", { notation: "compact", maximumFractionDigits: 2 }).format(v);
const curPrefix = (a) => { const c = a?.currency; return c == null || c === "pts" ? "$" : c in CUR ? CUR[c] : c + " "; };
const fmtPct = (v, d = 2) => v == null ? "—" : (Math.abs(v) < 0.5 * 10 ** -(d + 2) ? "" : v > 0 ? "+" : "") + (v * 100).toFixed(d) + "%";
/* colour only where the job is "what moved" or "good or bad"; zero and missing stay grey */
const tone = (v, eps = 1e-9) => v == null || Math.abs(v) < eps ? "muted" : v > 0 ? "up" : "down";
const fmtDate = (t) => new Date(t * 1000).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
const fmtDateTime = (t) => new Date(t * 1000).toLocaleString(undefined, { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" });
const fmtClock = (d = new Date()) => d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
function ago(t) {
  const s = Math.max(0, Date.now() / 1000 - t);
  if (s < 90) return "just now";
  if (s < 3600) return Math.round(s / 60) + " min ago";
  if (s < 86400 * 2) return Math.round(s / 3600) + " h ago";
  return Math.round(s / 86400) + " d ago";
}
const base = (sym) => sym.replace(/USDT$/, "").replace(/^\^GSPC$/, "SPX").replace(/^\^/, "").replace(/\..*$/, "");
const kindLabel = (a) => a.type === "crypto" ? "Crypto" : a.symbol.startsWith("^") ? "Index" : a.type === "stock" ? "Stock" : "ETF";
const sessionWord = (a) => a.type === "crypto" ? "24 h" : a.market_state === "REGULAR" ? "today" : "session";
const go = (sym) => (location.hash = "#/asset/" + encodeURIComponent(sym));

/* assets are shown as neutral monograms: identity by letters, colour stays on the data */
function icon(sym, lg = false) {
  const b = base(sym);
  return `<span class="monogram${lg ? " lg" : ""}" aria-hidden="true">${esc(b.length > 4 ? b.slice(0, 3) : b)}</span>`;
}

function sparkline(vals, w = 96, h = 28) {
  if (!vals || vals.length < 2) return `<svg class="spark" width="${w}" height="${h}" aria-hidden="true"></svg>`;
  const mn = Math.min(...vals), mx = Math.max(...vals), r = mx - mn || 1;
  const d = vals.map((v, i) => (i ? "L" : "M") + ((i / (vals.length - 1)) * w).toFixed(1) + " " + (h - 2 - ((v - mn) / r) * (h - 4)).toFixed(1)).join("");
  return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true"><path d="${d}"/></svg>`;
}

let toastT;
function toast(msg, kind = "ok") {
  const t = $("#toast");
  t.textContent = msg; t.className = "toast " + kind; t.hidden = false;
  clearTimeout(toastT); toastT = setTimeout(() => (t.hidden = true), 3500);
}

function setLive(ok) {
  const el = $("#live");
  el.className = "live " + (ok ? "ok" : "err");
  if (ok) state.lastOk = Date.now();
  const last = state.lastOk ? " · last update " + fmtClock(new Date(state.lastOk)) : "";
  $("#live-text").textContent = ok ? "Updated " + fmtClock() : "Offline, retrying" + last;
  const f = state.feed;
  renderFeeds();
  el.title = ok ? `Page refreshes every 15 s · quotes polled every ${f?.poll_seconds || 30} s${f?.generated ? " · last poll " + fmtClock(new Date(f.generated * 1000)) : ""}` : "The dashboard API did not answer";
}

const FEED_NAMES = { binance: "Binance", yahoo: "Yahoo Finance", coingecko: "CoinGecko" };
function renderFeeds() {
  const box = $("#feeds"), src = state.feed?.sources;
  if (!box || !src) return;
  const now = Date.now() / 1000;
  box.innerHTML = `<h3>Quote feeds</h3>` + Object.entries(src).map(([k, v]) => {
    const ok = !v.error && v.last_ok && now - v.last_ok < 600;
    return `<div class="feed ${ok ? "ok" : "err"}" title="${esc(v.error || `${v.count ?? 0} quotes in ${v.ms ?? "?"} ms`)}"><i></i>${esc(FEED_NAMES[k] || k)}<span class="t num">${v.last_ok ? ago(v.last_ok) : "never"}</span></div>`;
  }).join("");
}

/* the paper account's equity sits at the right end of the top bar, refreshed once a minute */
let accountAt = 0;
async function refreshAccount(force = false) {
  if (!force && Date.now() - accountAt < 60000) return;
  accountAt = Date.now();
  try { const p = await getPortfolio(true); $("#account-eq").textContent = fmtUsd(p.equity); } catch {}
}

/* ----------------------------------------------------------- data load --- */
async function loadOverview() {
  try {
    const j = await api("/api/overview");
    state.prevPrice = Object.fromEntries(state.assets.map((a) => [a.symbol, a.price]));
    state.assets = j.assets;
    state.bySym = Object.fromEntries(j.assets.map((a) => [a.symbol, a]));
    state.feed = j.feed;
    state.loadError = null;
    setLive(true);
  } catch (e) { state.loadError = e.message; setLive(false); }
}

function errorBlock(what, retry = "route()") {
  const last = state.lastOk ? ` Last good data ${fmtClock(new Date(state.lastOk))}.` : "";
  return `<div class="error-block">Couldn't load ${esc(what)}.${last} <button class="linkbtn" onclick="${retry}">Retry</button></div>`;
}

function searchAssets(q, limit = 8) {
  q = q.toLowerCase().trim();
  if (!q) return [];
  const scored = [];
  for (const a of state.assets) {
    const s = a.symbol.toLowerCase(), b = base(a.symbol).toLowerCase(), n = a.name.toLowerCase(), al = (a.aliases || "").toLowerCase();
    let sc = null;
    if (q === s || q === b) sc = 0;
    else if (s.startsWith(q) || b.startsWith(q)) sc = 1;
    else if (n.startsWith(q)) sc = 2;
    else if (n.includes(q) || s.includes(q) || al.includes(q)) sc = 3;
    if (sc != null) scored.push([sc, a]);
  }
  return scored.sort((x, y) => x[0] - y[0] || x[1].symbol.localeCompare(y[1].symbol)).slice(0, limit).map((x) => x[1]);
}

/* ------------------------------------------------------------- search --- */
function attachSearch(input, box, onPick, { filter = () => true } = {}) {
  let sel = 0, items = [];
  const render = () => {
    items = searchAssets(input.value, 12).filter(filter);
    if (!input.value.trim()) { box.hidden = true; return; }
    box.hidden = false;
    box.innerHTML = items.length ? items.map((a, i) => `
      <div class="search-item${i === sel ? " sel" : ""}" data-i="${i}">
        ${icon(a.symbol)}
        <div class="meta"><div class="sym">${esc(a.name)}</div><div class="nm">${esc(a.symbol)} · ${kindLabel(a)}</div></div>
        <div class="r"><div class="num">${money(a, a.price)}</div><div class="num ${tone(a.change_24h)}" style="font-size:12px">${fmtPct(a.change_24h)}</div></div>
      </div>`).join("") : `<div class="search-empty">No tracked asset matches “${esc(input.value)}”. Add symbols in config/symbols.yaml.</div>`;
  };
  input.addEventListener("input", () => { sel = 0; render(); });
  input.addEventListener("focus", render);
  input.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") { sel = Math.min(sel + 1, items.length - 1); render(); e.preventDefault(); }
    else if (e.key === "ArrowUp") { sel = Math.max(sel - 1, 0); render(); e.preventDefault(); }
    else if (e.key === "Enter" && items[sel]) { onPick(items[sel]); box.hidden = true; e.preventDefault(); }
    else if (e.key === "Escape") { box.hidden = true; input.blur(); }
  });
  box.addEventListener("mousedown", (e) => {
    const it = e.target.closest(".search-item");
    if (it) { e.preventDefault(); onPick(items[+it.dataset.i]); box.hidden = true; }
  });
  input.addEventListener("blur", () => setTimeout(() => (box.hidden = true), 120));
}

/* ------------------------------------------------------------- charts --- */
function makeChart(el, opts = {}) {
  const narrow = matchMedia("(max-width: 719px)").matches;
  return LC.createChart(el, {
    autoSize: true,
    layout: { background: { color: "transparent" }, textColor: css("--faint"), fontFamily: css("--font"), fontSize: narrow ? 11 : 12, attributionLogo: false },
    grid: { vertLines: { visible: false }, horzLines: { color: css("--grid") } },
    rightPriceScale: { borderVisible: false },
    timeScale: { borderVisible: false, timeVisible: true, secondsVisible: false, rightOffset: 4 },
    crosshair: {
      mode: LC.CrosshairMode.Normal,
      vertLine: { color: css("--control"), width: 1, style: LC.LineStyle.Solid, labelBackgroundColor: css("--night-4") },
      horzLine: { color: css("--control"), width: 1, style: LC.LineStyle.Dashed, labelBackgroundColor: css("--night-4") },
    },
    handleScroll: { vertTouchDrag: false },
    ...opts,
  });
}
const priceFormat = (p) => { const prec = Math.abs(p || 1) >= 1000 ? 0 : decimals(p || 1); return { type: "price", precision: prec, minMove: Math.pow(10, -prec) }; };
/* the accent as the theme switcher last set it (the CSS value may be mid-fade), and an rgba of it */
const accent = () => (window.ARCO ? window.ARCO.accent() : css("--accent"));
const rgba = (hex, a) => { const n = parseInt(hex.replace("#", ""), 16); return `rgba(${n >> 16},${(n >> 8) & 255},${n & 255},${a})`; };
const lineColors = (hex = accent()) => ({ lineColor: hex, topColor: rgba(hex, .22), bottomColor: rgba(hex, 0), crosshairMarkerBackgroundColor: hex });
/* the watched line: the accent, with a short fade under it */
const lineSeries = (chart, p) => chart.addSeries(LC.AreaSeries, {
  ...lineColors(), lineWidth: 2,
  priceLineVisible: false, crosshairMarkerRadius: 4, crosshairMarkerBorderColor: css("--night-2"),
  priceFormat: priceFormat(p),
});
/* a new accent recolours the live charts in place: no reload, no lost zoom */
window.addEventListener("accentchange", (e) => {
  const hex = e.detail.hex;
  overviewView.series?.applyOptions(lineColors(hex));
  assetView.candles?.applyOptions({ priceLineColor: hex });
  portfolioView.series?.applyOptions({ color: hex });
});

/* ============================================================ OVERVIEW === */
const sortState = { crypto: { key: "mcap", asc: true }, etf: { key: "mcap", asc: true }, stock: { key: "mcap", asc: true } };
const TABLE_LIMIT = { crypto: 25, etf: 25, stock: 50 };
const showAll = { crypto: false, etf: false, stock: false };

function assetTable(kind, assets) {
  const s = sortState[kind], crypto = kind === "crypto";
  const cols = [
    ["mcap", kind === "etf" ? "#" : "Rank", "rank hide-sm"], ["name", "Asset", "l"], ["price", "Price"], ["change_24h", crypto ? "24h" : "Session", "hide-sm"], ["change_7d", "7d", "hide-sm"],
    ["range", crypto ? "24h range" : "Day range", "hide-md"], ["volume_24h", crypto ? "Volume 24h" : "Volume (day)", "hide-sm"],
    ["spark", crypto ? "Last 7 days" : "Last 60 sessions", "hide-md"], ["time", "Updated", "hide-lg"],
  ];
  let rows = assets.map((a, i) => ({ ...a, mcap: i }));
  if (s.key !== "mcap" || !s.asc) {
    rows.sort((x, y) => {
      let a = x[s.key], b = y[s.key];
      if (typeof a === "string") return s.asc ? a.localeCompare(b) : b.localeCompare(a);
      a = a ?? -Infinity; b = b ?? -Infinity;
      return s.asc ? a - b : b - a;
    });
  }
  const total = rows.length, cut = !showAll[kind] && total > TABLE_LIMIT[kind];
  if (cut) rows = rows.slice(0, TABLE_LIMIT[kind]);
  const more = total > TABLE_LIMIT[kind] ? `<div class="more"><button class="btn ghost" data-more="${kind}">${cut ? `Show all ${total}` : `Show top ${TABLE_LIMIT[kind]} only`}</button></div>` : "";
  return `<div class="table-wrap"><table data-kind="${kind}"><thead><tr>${cols.map(([k, label, c]) => {
    const sortable = !["range", "spark"].includes(k);
    const sorted = s.key === k && !(k === "mcap" && s.asc);
    return `<th class="${c || ""}${sortable ? " sortable" : ""}${sorted ? " sorted" + (s.asc ? " asc" : "") : ""}" data-k="${k}"${sortable ? ` tabindex="0" aria-sort="${sorted ? (s.asc ? "ascending" : "descending") : "none"}"` : ""}>${label}</th>`;
  }).join("")}</tr></thead>
    <tbody>${rows.map((a) => {
      const prev = state.prevPrice[a.symbol];
      const flash = prev != null && a.price != null && prev !== a.price ? (a.price > prev ? "flash-up" : "flash-down") : "";
      const pos = a.high_24h > a.low_24h ? Math.min(100, Math.max(0, ((a.price - a.low_24h) / (a.high_24h - a.low_24h)) * 100)) : 50;
      const vol = a.symbol.startsWith("^") ? null : a.volume_24h;
      return `<tr class="click" data-sym="${esc(a.symbol)}" tabindex="0">
        <td class="rank num hide-sm">${a.mcap + 1}</td>
        <td class="l"><div class="asset-cell">${icon(a.symbol)}<div style="min-width:0">
          <div class="nm">${esc(a.name)}${a.symbol.startsWith("^") ? '<span class="tag">index</span>' : ""}${a.market_state === "REGULAR" && a.type !== "crypto" ? '<span class="tag">open</span>' : ""}</div>
          <div class="sy"><span class="hide-sm">${esc(a.symbol)}</span><span class="m-sub num">${esc(base(a.symbol))} · 7d ${fmtPct(a.change_7d)}</span></div>
        </div></div></td>
        <td class="num ${flash}">${a.price == null ? '<span class="muted">—</span>' : money(a, a.price)}<span class="m-sub ${tone(a.change_24h)}">${fmtPct(a.change_24h)}</span></td>
        <td class="num hide-sm ${tone(a.change_24h)}">${fmtPct(a.change_24h)}</td>
        <td class="num hide-sm">${fmtPct(a.change_7d)}</td>
        <td class="hide-md">${a.price == null ? '<span class="muted">—</span>' : `<span class="range num">${fmtPrice(a.low_24h)}<span class="track"><i style="left:${pos}%"></i></span>${fmtPrice(a.high_24h)}</span>`}</td>
        <td class="num hide-sm">${vol == null ? '<span class="muted">—</span>' : fmtCompact(vol, curPrefix(a))}</td>
        <td class="hide-md">${sparkline(a.spark)}</td>
        <td class="muted hide-lg">${a.time ? ago(a.time) : "—"}</td>
      </tr>`;
    }).join("")}</tbody></table></div>${more}`;
}

function moversList(assets, n = 8) {
  let rows = assets.filter((a) => a.change_24h != null).sort((x, y) => y.change_24h - x.change_24h);
  const total = rows.length;
  if (rows.length > 2 * n) rows = rows.slice(0, n).concat(rows.slice(-n).reverse());
  const max = Math.max(0.001, ...rows.map((a) => Math.abs(a.change_24h)));
  const step = [0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 1].find((x) => x >= max) || max;
  return {
    html: `<ol>${rows.map((a, i) => {
      const grp = i === 0 ? `<li class="grp">Biggest gains</li>` : i === n && rows.length === 2 * n ? `<li class="grp">Biggest losses</li>` : "";
      const w = (Math.abs(a.change_24h) / step) * 50;
      return `${grp}<li class="mover" data-sym="${esc(a.symbol)}" tabindex="0" title="${esc(a.name)} · ${kindLabel(a)} · ${sessionWord(a)}">
        <span class="s">${esc(base(a.symbol))}</span>
        <span class="track"><span class="bar ${a.change_24h >= 0 ? "up" : "down"}" style="width:${w.toFixed(2)}%"></span></span>
        <span class="v num ${tone(a.change_24h)}">${fmtPct(a.change_24h)}</span></li>`;
    }).join("")}</ol>
    <div class="axis" aria-hidden="true"><i></i><span class="num"><b style="font-weight:400">${fmtPct(-step, 0)}</b><b style="font-weight:400">0</b><b style="font-weight:400">${fmtPct(step, 0)}</b></span><i></i></div>`,
    n: total,
  };
}

function overviewFinding(crypto, etf, stock = []) {
  const up = crypto.filter((a) => (a.change_24h ?? 0) > 0).length;
  const known = crypto.filter((a) => a.change_24h != null);
  const parts = [];
  if (known.length) {
    const best = known.reduce((m, a) => (a.change_24h > m.change_24h ? a : m));
    parts.push(`<b>${up} of ${crypto.length}</b> coins up over 24 h, ${esc(base(best.symbol))} leading at <span class="num ${tone(best.change_24h)}">${fmtPct(best.change_24h)}</span>`);
  }
  const e = etf.filter((a) => a.change_24h != null);
  if (e.length) {
    const down = e.filter((a) => a.change_24h < 0).length;
    const worst = e.reduce((m, a) => (a.change_24h < m.change_24h ? a : m));
    const bestE = e.reduce((m, a) => (a.change_24h > m.change_24h ? a : m));
    if (down === e.length) parts.push(`every ETF and index fell on the last session, ${esc(base(worst.symbol))} most at <span class="num down">${fmtPct(worst.change_24h)}</span>`);
    else if (down === 0) parts.push(`every ETF and index rose on the last session, ${esc(base(bestE.symbol))} most at <span class="num up">${fmtPct(bestE.change_24h)}</span>`);
    else parts.push(`${down} of ${e.length} ETFs and indices fell on the last session`);
  }
  const st = stock.filter((a) => a.change_24h != null);
  if (st.length) {
    const up = st.filter((a) => a.change_24h > 0).length;
    const best = st.reduce((m, a) => (a.change_24h > m.change_24h ? a : m));
    parts.push(`<b>${up} of ${st.length}</b> stocks up on the ${st.some((a) => a.market_state === "REGULAR") ? "day so far" : "last session"}, ${esc(base(best.symbol))} best at <span class="num ${tone(best.change_24h)}">${fmtPct(best.change_24h)}</span>`);
  }
  return parts.length ? parts.join("; ") + "." : "Waiting for the first prices from the collectors.";
}

/* ---------------------------------------------------- breadth tapes --- */
/* Every tracked asset is one bar, sorted from best to worst change; up bars rise above the zero line,
   down bars hang below it. One scale for all three tapes, so a 2 % stock day and a 2 % coin day look alike. */
const TAPES = [
  ["crypto", "Coins", "24 h"],
  ["etf", "ETFs & indices", "last session"],
  ["stock", "Stocks", "last session"],
];
const STEPS = [0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 1];
function breadthScale(assets) {
  const abs = assets.map((a) => Math.abs(a.change_24h)).filter((v) => v != null && isFinite(v)).sort((x, y) => x - y);
  if (!abs.length) return 0.05;
  const p95 = abs[Math.floor(abs.length * 0.95)] || abs[abs.length - 1];
  return STEPS.find((x) => x >= p95) || 1;
}
const median = (v) => { if (!v.length) return null; const s = [...v].sort((a, b) => a - b), m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };

function breadthHTML() {
  return TAPES.map(([kind, label]) => `
    <div class="tape-row">
      <div class="tape-label"><div class="k">${label}</div><div class="v" id="tl-${kind}"></div></div>
      <div class="tape" id="tape-${kind}" data-kind="${kind}" role="img"></div>
    </div>`).join("") + `<div class="scale" aria-hidden="true"><span id="tape-scale"></span><span class="hide-sm">best to worst</span></div>`;
}

function drawTape(el, assets, cap) {
  const rows = assets.filter((a) => a.change_24h != null && isFinite(a.change_24h)).sort((x, y) => y.change_24h - x.change_24h);
  el._rows = rows;
  const n = rows.length, W = 1000, H = 56, mid = H / 2;
  if (!n) { el.innerHTML = ""; return; }
  const px = el.clientWidth || 600, bw = W / n, gap = px / n >= 4 ? bw * 0.28 : 0;
  const bars = rows.map((a, i) => {
    const v = a.change_24h, h = Math.max(1, Math.min(1, Math.abs(v) / cap) * (mid - 1));
    const cls = Math.abs(v) < 1e-9 ? "z" : v > 0 ? "u" : "d";
    const y = cls === "d" ? mid : mid - h;
    return `<rect class="${cls}" x="${(i * bw).toFixed(2)}" y="${y.toFixed(2)}" width="${Math.max(0.6, bw - gap).toFixed(2)}" height="${cls === "z" ? 1 : h.toFixed(2)}"/>`;
  }).join("");
  el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" aria-hidden="true"><line class="zero" x1="0" x2="${W}" y1="${mid}" y2="${mid}" vector-effect="non-scaling-stroke"/>${bars}<line class="cursor" x1="0" x2="0" y1="0" y2="${H}" vector-effect="non-scaling-stroke" visibility="hidden"/></svg>`;
  const up = rows.filter((a) => a.change_24h > 0).length;
  el.setAttribute("aria-label", `${up} of ${n} up`);
}

function bindTape(el, read) {
  const at = (e) => {
    const rows = el._rows; if (!rows?.length) return null;
    const r = el.getBoundingClientRect(), i = Math.min(rows.length - 1, Math.max(0, Math.floor(((e.clientX - r.left) / r.width) * rows.length)));
    return { i, a: rows[i] };
  };
  const show = (e) => {
    const hit = at(e); if (!hit) return;
    const { i, a } = hit, n = el._rows.length, cur = el.querySelector(".cursor");
    if (cur) { const x = ((i + 0.5) / n) * 1000; cur.setAttribute("x1", x); cur.setAttribute("x2", x); cur.setAttribute("visibility", "visible"); }
    read.innerHTML = `<b>${esc(base(a.symbol))}</b><span>${esc(a.name)}</span><b class="num ${tone(a.change_24h)}">${fmtPct(a.change_24h)}</b><span class="num">${i + 1} of ${n}</span><a href="#/asset/${encodeURIComponent(a.symbol)}">Open</a>`;
    el._hit = a;
  };
  el.addEventListener("pointermove", show);
  el.addEventListener("pointerdown", show);
  el.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") el.querySelector(".cursor")?.setAttribute("visibility", "hidden"); });
  // a mouse click opens the asset; a finger scrubs, then taps "Open" in the read-out
  el.addEventListener("click", (e) => { if (e.pointerType !== "touch" && el._hit && matchMedia("(hover: hover)").matches) go(el._hit.symbol); });
}

const overviewView = {
  chart: null, series: null,
  watch: localStorage.getItem("watch") || "BTCUSDT",
  async mount(el) {
    if (!state.assets.length) await loadOverview();
    if (!state.assets.length) {
      el.innerHTML = `<div class="title-row"><div><h1>Markets</h1></div></div><div class="panel">${errorBlock("market prices")}</div>`;
      return;
    }
    if (!state.bySym[this.watch]) this.watch = WATCH.find((s) => state.bySym[s]) || state.assets[0].symbol;
    el.classList.add("rise");
    el.innerHTML = `
      <div class="title-row"><div><h1>Markets</h1><p class="lede" id="ov-lede"></p></div></div>
      <section class="panel mb" aria-label="Market breadth">
        <div class="panel-head"><h2>Market breadth</h2><div class="tape-read" id="tape-read"></div></div>
        <div class="breadth" id="breadth">${breadthHTML()}</div>
      </section>
      <div class="lead-row">
        <section class="panel lead" aria-label="Watchlist chart">
          <div class="watch" id="watch" role="tablist"></div>
          <div class="lead-meta"><span id="lead-what"></span><a class="muted" id="lead-open" href="#/">Open chart →</a></div>
          <div class="lead-chart"><div class="fill" id="lead-chart"></div></div>
        </section>
        <section class="panel movers">
          <div class="panel-head"><h2>24 h movers</h2><span class="sub" id="movers-sub"></span></div>
          <div id="movers"></div>
        </section>
      </div>
      <section class="panel mb"><div class="panel-head"><h2>Coins</h2><span class="sub">Binance spot · by market cap</span></div><div id="t-crypto"></div></section>
      <section class="panel mb"><div class="panel-head"><h2>ETFs and indices</h2><span class="sub">Yahoo Finance</span></div><div id="t-etf"></div></section>
      <section class="panel"><div class="panel-head"><h2>Stocks</h2><span class="sub">S&amp;P 500, SMI and large caps · by market cap</span></div><div id="t-stock"></div></section>`;
    $("#watch").addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b || b.dataset.sym === this.watch) return;
      this.watch = b.dataset.sym; localStorage.setItem("watch", this.watch);
      this.renderWatch(); this.loadLead();
    });
    el.addEventListener("click", (e) => {
      const mb = e.target.closest("button[data-more]");
      if (mb) { showAll[mb.dataset.more] = !showAll[mb.dataset.more]; state.prevPrice = {}; this.renderTables(); return; }
      const r = e.target.closest(".mover[data-sym], tr[data-sym]"); if (r) go(r.dataset.sym);
      const th = e.target.closest("th.sortable"); if (th) this.sort(th);
    });
    el.addEventListener("keydown", (e) => {
      if (e.key !== "Enter" && e.key !== " ") return;
      const r = e.target.closest(".mover[data-sym], tr[data-sym]"); if (r) { e.preventDefault(); go(r.dataset.sym); }
      const th = e.target.closest("th.sortable"); if (th) { e.preventDefault(); this.sort(th); }
    });
    TAPES.forEach(([k]) => bindTape($("#tape-" + k), $("#tape-read")));
    this.chart = makeChart($("#lead-chart"));
    this.render();
    await this.loadLead();
  },
  sort(th) {
    const kind = th.closest("table").dataset.kind, s = sortState[kind], k = th.dataset.k;
    if (s.key === k) s.asc = !s.asc; else { s.key = k; s.asc = k === "name" || k === "mcap"; }
    state.prevPrice = {};
    this.renderTables();
    $(`table[data-kind="${kind}"] th[data-k="${k}"]`)?.focus();
  },
  leadSpec(a) {
    return a.type === "crypto"
      ? { tf: "1h", limit: 168, what: "Last 7 days · hourly closes · USDT" }
      : { tf: "1d", limit: 126, what: `Last 6 months · daily closes · ${a.currency === "pts" ? "points" : a.currency || "USD"}` };
  },
  renderWatch() {
    const list = WATCH.map((s) => state.bySym[s]).filter(Boolean);
    $("#watch").innerHTML = list.map((a) => `
      <button role="tab" aria-selected="${a.symbol === this.watch}" class="${a.symbol === this.watch ? "on" : ""}" data-sym="${esc(a.symbol)}">
        <span class="k">${esc(a.type === "crypto" ? a.name : base(a.symbol) + " · " + a.name.replace(/^(State Street |iShares |Vanguard )?(SPDR )?/, ""))}</span>
        <span class="v num">${money(a, a.price)}</span>
        <span class="d num ${tone(a.change_24h)}">${fmtPct(a.change_24h)} <span class="muted">${sessionWord(a)}</span></span>
      </button>`).join("");
    const a = state.bySym[this.watch];
    $("#lead-what").textContent = this.leadSpec(a).what;
    $("#lead-open").href = "#/asset/" + encodeURIComponent(a.symbol);
    $("#lead-open").textContent = `Open ${base(a.symbol)} chart →`;
  },
  render() {
    const crypto = state.assets.filter((a) => a.type === "crypto");
    const etf = state.assets.filter((a) => a.type === "etf");
    const stock = state.assets.filter((a) => a.type === "stock");
    $("#ov-lede").innerHTML = overviewFinding(crypto, etf, stock);
    this.renderBreadth({ crypto, etf, stock });
    this.renderWatch();
    const m = moversList(state.assets);
    $("#movers").innerHTML = m.html;
    $("#movers-sub").textContent = `of ${m.n} assets`;
    this.renderTables();
  },
  renderBreadth(by) {
    const cap = breadthScale(state.assets);
    for (const [kind, , when] of TAPES) {
      const list = by[kind], known = list.filter((a) => a.change_24h != null);
      const up = known.filter((a) => a.change_24h > 0).length, md = median(known.map((a) => a.change_24h));
      $("#tl-" + kind).innerHTML = `<b class="num">${up}</b> of <span class="num">${known.length}</span> up · median <span class="num ${tone(md)}">${fmtPct(md)}</span>`;
      $("#tape-" + kind).title = `${up} of ${known.length} ${kind === "crypto" ? "coins" : kind === "etf" ? "ETFs and indices" : "stocks"} up over the ${when}`;
      drawTape($("#tape-" + kind), list, cap);
    }
    $("#tape-scale").textContent = `Coins over 24 h, the rest over the last session · scale ±${(cap * 100).toFixed(0)}%`;
    if (!$("#tape-read").innerHTML) $("#tape-read").innerHTML = `<span>${state.assets.length} assets</span>`;
  },
  renderTables() {
    $("#t-crypto").innerHTML = assetTable("crypto", state.assets.filter((a) => a.type === "crypto"));
    $("#t-etf").innerHTML = assetTable("etf", state.assets.filter((a) => a.type === "etf"));
    $("#t-stock").innerHTML = assetTable("stock", state.assets.filter((a) => a.type === "stock"));
  },
  async loadLead() {
    const sym = this.watch, a = state.bySym[sym], spec = this.leadSpec(a);
    if (this.series) { this.chart.removeSeries(this.series); this.series = null; }
    this.series = lineSeries(this.chart, a.price);
    this.series.priceScale().applyOptions({ scaleMargins: { top: 0.1, bottom: 0.08 } });
    this.chart.applyOptions({ timeScale: { timeVisible: spec.tf !== "1d" } });
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(sym)}&tf=${spec.tf}&limit=${spec.limit}`);
      if (sym !== this.watch || !this.series) return;
      this.leadBars = j.bars.map((b) => ({ time: b.time + TZ_SHIFT, value: b.close }));
      this.series.setData(this.leadBars);
      this.chart.timeScale().fitContent();
    } catch (e) { toast("Chart: " + e.message, "err"); }
  },
  async tick() {
    await loadOverview();
    if (state.view !== this || !this.chart) return;
    this.render();
    const sym = this.watch, spec = this.leadSpec(state.bySym[sym]);
    if (!this.leadBars?.length) return;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(sym)}&tf=${spec.tf}&limit=2`);
      if (sym !== this.watch || !this.series) return;
      for (const b of j.bars) {
        const p = { time: b.time + TZ_SHIFT, value: b.close }, last = this.leadBars[this.leadBars.length - 1];
        if (p.time < last.time) continue;
        if (p.time === last.time) this.leadBars[this.leadBars.length - 1] = p; else this.leadBars.push(p);
        this.series.update(p);
      }
    } catch {}
  },
  unmount() { if (this.chart) { this.chart.remove(); this.chart = null; this.series = null; } },
};

/* =============================================================== ASSET === */
const TFS = ["1m", "5m", "15m", "1h", "4h", "1d", "1w"];
const assetView = {
  chart: null, tf: localStorage.getItem("tf") || "1h",
  async mount(el, sym) {
    this.sym = sym;
    if (!state.assets.length) await loadOverview();
    const a = state.bySym[sym];
    if (!a) {
      el.innerHTML = `<a class="back" href="#/">← Markets</a><div class="title-row"><div><h1>${esc(sym)}</h1>
        <p class="lede">${state.loadError ? "The price feed is not answering." : "This symbol is not tracked. Add it in config/symbols.yaml."}</p></div></div>
        ${state.loadError ? `<div class="panel">${errorBlock("this asset")}</div>` : ""}`;
      return;
    }
    this.a = a;
    const crypto = a.type === "crypto";
    el.classList.add("rise");
    el.innerHTML = `
      <a class="back" href="#/">← Markets</a>
      <div class="title-row">
        <div class="asset-title">${icon(sym, true)}
          <div><h1>${esc(a.name)}</h1><div class="sy">${esc(sym)} · ${crypto ? "Binance spot" : esc(a.exchange || "Yahoo Finance")} · ${kindLabel(a)}${a.currency && a.currency !== "pts" ? " · " + esc(a.currency) : ""}</div></div>
        </div>
        <div class="quote"><span class="px num" id="a-price"></span><span class="chg num" id="a-chg"></span></div>
      </div>
      <div class="side-layout">
        <section class="panel chart-panel">
          <div class="panel-head">
            <div class="tabs" id="tfs" role="tablist" aria-label="Timeframe">${TFS.map((t) => `<button role="tab" data-tf="${t}" class="${t === this.tf ? "on" : ""}" aria-selected="${t === this.tf}">${t}</button>`).join("")}</div>
            <div class="ohlc" id="legend" aria-live="off"></div>
          </div>
          <div class="chart-wrap" id="chart"></div>
        </section>
        <div class="stack">
          <section class="panel"><div class="panel-head"><h2>${crypto ? "Last 24 hours" : "Last session"}</h2><span class="sub" id="a-when"></span></div><div class="stats" id="stats"></div></section>
          ${a.tradable ? `<section class="panel" id="trade-panel"></section>` : !sym.startsWith("^") ? `<section class="panel"><div class="panel-head"><h2>Paper trade</h2></div><p class="plain">This asset trades in ${esc(a.currency)}. The paper portfolio is kept in USD, so only USD and USDT assets can be traded for now.</p></section>` : `<section class="panel"><div class="panel-head"><h2>Paper trade</h2></div><p class="plain">An index can't be bought. Use <a href="#/asset/SPY">SPY</a> or <a href="#/asset/CSSPX.SW">CSSPX.SW</a> for S&amp;P 500 exposure.</p></section>`}
        </div>
      </div>`;
    $("#tfs").addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      this.tf = b.dataset.tf; localStorage.setItem("tf", this.tf);
      $("#tfs").querySelectorAll("button").forEach((x) => { x.classList.toggle("on", x === b); x.setAttribute("aria-selected", x === b); });
      this.loadBars();
    });
    this.renderHeader();
    if (a.tradable) renderTradeForm($("#trade-panel"), sym, true);
    this.buildChart();
    await this.loadBars();
  },
  renderHeader() {
    const a = state.bySym[this.sym] || this.a, crypto = a.type === "crypto";
    $("#a-price").textContent = money(a, a.price);
    $("#a-chg").innerHTML = `<span class="${tone(a.change_24h)}">${fmtPct(a.change_24h)}</span> <span class="muted">${sessionWord(a)}</span>`;
    $("#a-when").textContent = a.time ? (crypto ? "last trade " : a.market_state === "REGULAR" ? "market open · last trade " : "market closed · last trade ") + (Date.now() / 1000 - a.time < 86400 ? new Date(a.time * 1000).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) : fmtDate(a.time)) : "";
    const st = [
      ["High", money(a, a.high_24h)], ["Low", money(a, a.low_24h)],
      ["Change 7 d", fmtPct(a.change_7d)], ["Volume", a.symbol.startsWith("^") ? '<span class="muted">—</span>' : fmtCompact(a.volume_24h, curPrefix(a))],
    ];
    if (a.bid && a.ask) st.push(["Bid", money(a, a.bid)], ["Ask", money(a, a.ask)]);
    if (a.market_cap) st.push(["Market cap", fmtCompact(a.market_cap, curPrefix(a))]);
    if (a.type === "crypto" && a.rank) st.push(["Rank", "#" + a.rank]);
    $("#stats").innerHTML = st.map(([k, v]) => `<div class="stat"><div class="k">${k}</div><div class="v num">${v}</div></div>`).join("");
  },
  buildChart() {
    this.chart = makeChart($("#chart"));
    const up = css("--positive"), down = css("--negative");
    this.candles = this.chart.addSeries(LC.CandlestickSeries, {
      upColor: up, downColor: down, borderVisible: false, wickUpColor: up, wickDownColor: down,
      priceLineColor: accent(), priceFormat: priceFormat(this.a.price),
    });
    this.volume = this.chart.addSeries(LC.HistogramSeries, { color: "rgba(236,244,207,.16)", priceFormat: { type: "volume" }, priceScaleId: "vol", lastValueVisible: false, priceLineVisible: false });
    this.chart.priceScale("vol").applyOptions({ scaleMargins: { top: 0.84, bottom: 0 } });
    this.candles.priceScale().applyOptions({ scaleMargins: { top: 0.06, bottom: 0.2 } });
    this.chart.subscribeCrosshairMove((p) => this.legend(p));
    this.chart.timeScale().subscribeVisibleLogicalRangeChange((r) => {
      if (r && r.from < 30 && this.hasMore && !this.loadingMore) this.loadMore();
    });
  },
  legend(p) {
    const d = p && p.time ? p.seriesData.get(this.candles) : this.bars?.[this.bars.length - 1];
    if (!d) return;
    const chg = d.open ? d.close / d.open - 1 : null;
    $("#legend").innerHTML = `<span>O <b>${fmtPrice(d.open)}</b></span><span>H <b>${fmtPrice(d.high)}</b></span><span>L <b>${fmtPrice(d.low)}</b></span><span>C <b>${fmtPrice(d.close)}</b></span><span class="${tone(chg)}">${fmtPct(chg)}</span>`;
  },
  toSeries(bars) {
    return bars.map((b) => ({ time: b.time + TZ_SHIFT, open: b.open, high: b.high, low: b.low, close: b.close, volume: b.volume }));
  },
  vol(b) { return { time: b.time, value: b.volume }; },
  showEmpty(msg) {
    let n = $("#chart .chart-empty");
    if (!msg) { n?.remove(); return; }
    if (!n) { n = document.createElement("div"); n.className = "chart-empty"; $("#chart").append(n); }
    n.textContent = msg;
  },
  async loadBars() {
    const tf = this.tf, sym = this.sym;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(sym)}&tf=${tf}&limit=1500`);
      if (tf !== this.tf || sym !== this.sym || !this.chart) return;
      this.bars = this.toSeries(j.bars);
      this.hasMore = j.has_more;
      this.candles.setData(this.bars);
      this.volume.setData(this.bars.map((b) => this.vol(b)));
      this.chart.applyOptions({ timeScale: { timeVisible: !["1d", "1w"].includes(tf) } });
      const n = this.bars.length;
      const show = matchMedia("(max-width: 719px)").matches ? 70 : 160;
      if (n) this.chart.timeScale().setVisibleLogicalRange({ from: Math.max(0, n - show), to: n + 4 });
      this.showEmpty(n ? "" : `No ${tf} bars for this asset yet.${this.a.type !== "crypto" ? " Yahoo keeps about 30 days of intraday bars; the collector stores them from setup onward." : ""}`);
      if (!n) $("#legend").innerHTML = ""; else this.legend(null);
    } catch (e) { this.showEmpty(`Couldn't load ${tf} bars. ${e.message}`); }
  },
  async loadMore() {
    this.loadingMore = true;
    const tf = this.tf, first = this.bars[0].time - TZ_SHIFT;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(this.sym)}&tf=${tf}&limit=1500&end=${first}`);
      if (tf !== this.tf || !this.chart || !j.bars.length) { this.hasMore = false; return; }
      const older = this.toSeries(j.bars).filter((b) => b.time < this.bars[0].time);
      this.bars = older.concat(this.bars);
      this.hasMore = j.has_more;
      const range = this.chart.timeScale().getVisibleLogicalRange();
      this.candles.setData(this.bars);
      this.volume.setData(this.bars.map((b) => this.vol(b)));
      if (range) this.chart.timeScale().setVisibleLogicalRange({ from: range.from + older.length, to: range.to + older.length });
    } catch {} finally { this.loadingMore = false; }
  },
  async tick() {
    await loadOverview();
    if (state.view !== this || !state.bySym[this.sym] || !this.chart) return;
    this.renderHeader();
    const tp = $("#trade-panel"); if (tp) updateTradeEstimate(tp);
    if (!this.bars?.length) return;
    const tf = this.tf;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(this.sym)}&tf=${tf}&limit=3`);
      if (tf !== this.tf || !this.chart) return;
      for (const b of this.toSeries(j.bars)) {
        const last = this.bars[this.bars.length - 1];
        if (b.time < last.time) continue;
        if (b.time === last.time) this.bars[this.bars.length - 1] = b; else this.bars.push(b);
        this.candles.update(b); this.volume.update(this.vol(b));
      }
      this.legend(null);
    } catch {}
  },
  unmount() { if (this.chart) { this.chart.remove(); this.chart = null; } },
};

/* ======================================================== TRADE FORM ==== */
let portfolioCache = null;
async function getPortfolio(force = false) {
  if (!portfolioCache || force) portfolioCache = await api("/api/portfolio");
  return portfolioCache;
}

function renderTradeForm(el, sym, fixed) {
  el.dataset.side = el.dataset.side || "buy";
  el.dataset.sym = sym || "";
  const side = el.dataset.side;
  el.innerHTML = `
    <div class="panel-head"><h2>Paper trade</h2><span class="sub">fills at the last stored price</span></div>
    <div class="form">
      <div class="tabs side" role="tablist" aria-label="Side">
        <button role="tab" data-v="buy" class="${side === "buy" ? "on" : ""}" aria-selected="${side === "buy"}">Buy</button>
        <button role="tab" data-v="sell" class="${side === "sell" ? "on" : ""}" aria-selected="${side === "sell"}">Sell</button>
      </div>
      ${fixed ? "" : `<label class="field">Asset<div class="sym-pick"><input class="input text" id="tf-sym" placeholder="Search, e.g. sol or spy" autocomplete="off" value="${esc(sym || "")}"><div class="search-results" hidden></div></div></label>`}
      <div class="form-row">
        <label class="field">Quantity<input class="input" id="tf-qty" type="number" inputmode="decimal" min="0" step="any" placeholder="0"></label>
        <label class="field">Amount, USD<input class="input" id="tf-amt" type="number" inputmode="decimal" min="0" step="any" placeholder="0.00"></label>
      </div>
      <div class="form-row">
        <label class="field">Limit price<input class="input" id="tf-price" type="number" inputmode="decimal" min="0" step="any" placeholder="last"></label>
        <label class="field">Fee, %<input class="input" id="tf-fee" type="number" inputmode="decimal" min="0" step="0.01" value="0.1"></label>
      </div>
      <div class="kv">
        <div><span>Price</span><b class="num" id="tf-px">—</b></div>
        <div><span>Fee</span><b class="num" id="tf-feev">—</b></div>
        <div><span id="tf-total-l">Total cost</span><b class="num" id="tf-total">—</b></div>
        <div><span id="tf-avail-l">Available cash</span><b class="num" id="tf-avail">—</b></div>
      </div>
      <button class="btn primary block" id="tf-submit" disabled>Enter a quantity</button>
    </div>`;
  const tabs = el.querySelector(".tabs.side");
  tabs.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    el.dataset.side = b.dataset.v;
    tabs.querySelectorAll("button").forEach((x) => { x.classList.toggle("on", x === b); x.setAttribute("aria-selected", x === b); });
    updateTradeEstimate(el);
  });
  if (!fixed) {
    const inp = $("#tf-sym", el);
    attachSearch(inp, el.querySelector(".sym-pick .search-results"), (a) => { inp.value = a.symbol; el.dataset.sym = a.symbol; updateTradeEstimate(el); },
      { filter: (a) => a.tradable });
    inp.addEventListener("change", () => { el.dataset.sym = inp.value.trim(); updateTradeEstimate(el); });
  }
  const qty = $("#tf-qty", el), amt = $("#tf-amt", el);
  qty.addEventListener("input", () => { const p = tradePrice(el); amt.value = p && qty.value ? (qty.value * p).toFixed(2) : ""; updateTradeEstimate(el); });
  amt.addEventListener("input", () => { const p = tradePrice(el); qty.value = p && amt.value ? +(amt.value / p).toPrecision(8) : ""; updateTradeEstimate(el); });
  ["#tf-price", "#tf-fee"].forEach((s) => $(s, el).addEventListener("input", () => updateTradeEstimate(el)));
  $("#tf-submit", el).addEventListener("click", () => submitTrade(el));
  getPortfolio(true).then(() => updateTradeEstimate(el)).catch(() => {});
  updateTradeEstimate(el);
}

function tradePrice(el) {
  const p = parseFloat($("#tf-price", el).value);
  return p > 0 ? p : state.bySym[el.dataset.sym]?.price;
}

function updateTradeEstimate(el) {
  if (!el || !$("#tf-qty", el)) return;
  const sym = el.dataset.sym, a = state.bySym[sym];
  const p = tradePrice(el), q = parseFloat($("#tf-qty", el).value) || 0, fee = (parseFloat($("#tf-fee", el).value) || 0) / 100;
  const buy = el.dataset.side === "buy", notional = q * (p || 0), f = notional * fee, total = buy ? notional + f : notional - f;
  $("#tf-px", el).textContent = p ? "$" + fmtPrice(p) : "—";
  $("#tf-feev", el).textContent = q ? fmtUsd(f) : "—";
  $("#tf-total-l", el).textContent = buy ? "Total cost" : "You receive";
  $("#tf-total", el).textContent = q ? fmtUsd(total) : "—";
  const pf = portfolioCache;
  const held = pf?.positions.find((x) => x.symbol === sym)?.qty || 0;
  if (pf) {
    $("#tf-avail-l", el).textContent = buy ? "Available cash" : "You hold";
    $("#tf-avail", el).textContent = buy ? fmtUsd(pf.cash) : `${fmtQty(held)} ${base(sym || "")}`.trim();
  }
  // the button says why it can't act
  const btn = $("#tf-submit", el);
  let label = null;
  if (!a || !a.tradable) label = "Pick an asset";
  else if (!(q > 0)) label = "Enter a quantity";
  else if (!p) label = "No price yet";
  else if (pf && buy && total > pf.cash + 1e-9) label = "Not enough cash";
  else if (pf && !buy && q > held + 1e-12) label = held ? `You hold ${fmtQty(held)} ${base(sym)}` : `No ${base(sym)} to sell`;
  btn.disabled = !!label || btn.dataset.busy === "1";
  btn.textContent = label || `${buy ? "Buy" : "Sell"} ${fmtQty(q)} ${base(sym)}`;
}

async function submitTrade(el) {
  const sym = el.dataset.sym, qty = parseFloat($("#tf-qty", el).value), price = parseFloat($("#tf-price", el).value);
  if (!sym || !state.bySym[sym]) return toast("Pick an asset first", "err");
  if (!(qty > 0)) return toast("Enter a quantity or amount", "err");
  const btn = $("#tf-submit", el); btn.dataset.busy = "1"; btn.disabled = true;
  try {
    const t = await api("/api/portfolio/trades", { method: "POST", body: JSON.stringify({
      symbol: sym, side: el.dataset.side, qty, price: price > 0 ? price : null, fee_pct: parseFloat($("#tf-fee", el).value) || 0 }) });
    toast(`${t.side === "buy" ? "Bought" : "Sold"} ${fmtQty(t.qty)} ${base(t.symbol)} at $${fmtPrice(t.price)}`);
    $("#tf-qty", el).value = ""; $("#tf-amt", el).value = "";
    await getPortfolio(true);
    if (state.view === portfolioView) portfolioView.tick($("#app"), true);
  } catch (e) { toast(e.message, "err"); }
  finally { btn.dataset.busy = ""; updateTradeEstimate(el); }
}

/* =========================================================== PORTFOLIO === */
/* allocation: one hue in steps (largest position darkest), cash in neutral grey */
const SHADES = [1, 0.74, 0.56, 0.42, 0.32, 0.24];
const shade = (i) => `color-mix(in srgb, var(--accent) ${Math.round(SHADES[Math.min(i, SHADES.length - 1)] * 100)}%, transparent)`;

const portfolioView = {
  chart: null,
  async mount(el) {
    if (!state.assets.length) await loadOverview();
    el.innerHTML = `<div class="portfolio rise">
      <div class="title-row"><div><h1>Paper portfolio</h1><p class="lede" id="pf-lede">Loading the account…</p></div></div>
      <section class="panel kpis" id="pf-kpis" aria-label="Account totals"></section>
      <div class="side-layout">
        <div class="stack">
          <section class="panel"><div class="panel-head"><h2>Positions</h2><span class="sub" id="pf-npos"></span></div><div id="pf-pos"></div></section>
          <section class="panel"><div class="panel-head"><h2>Equity</h2><span class="sub">daily close, marked to market · USD</span></div><div id="pf-equity"></div></section>
          <section class="panel"><div class="panel-head"><h2>Trade history</h2><span class="sub" id="pf-ntr"></span></div><div id="pf-trades"></div></section>
          <section class="panel"><div class="panel-head"><h2>Account</h2></div>
            <div class="account-form">
              <label class="field" for="pf-start">Starting cash, USD</label>
              <div class="row"><input class="input" id="pf-start" type="number" inputmode="decimal" min="1" step="100"><button class="btn" id="pf-save">Save</button></div>
              <p>Changing it re-bases the return. Trades are kept.</p>
              <button class="btn danger" id="pf-reset">Delete all trades and reset</button>
            </div>
          </section>
        </div>
        <div class="stack">
          <section class="panel" id="pf-trade"></section>
        </div>
      </div></div>`;
    renderTradeForm($("#pf-trade"), "", false);
    $("#pf-save").addEventListener("click", () => this.settings(false));
    $("#pf-reset").addEventListener("click", () => {
      const n = portfolioCache?.trades.length || 0;
      if (confirm(`Delete ${n === 1 ? "the 1 paper trade" : `all ${n} paper trades`} and start again with the starting cash?`)) this.settings(true);
    });
    el.addEventListener("click", async (e) => {
      const del = e.target.closest("[data-del]");
      if (del) {
        if (!confirm(`Delete this ${del.dataset.desc}? Cash and positions will be recalculated.`)) return;
        try { await api("/api/portfolio/trades/" + del.dataset.del, { method: "DELETE" }); toast("Trade deleted"); this.tick(el, true); }
        catch (err) { toast(err.message, "err"); }
        return;
      }
      const r = e.target.closest("tr[data-sym]"); if (r) go(r.dataset.sym);
    });
    await this.tick(el, true);
  },
  async settings(reset) {
    const v = parseFloat($("#pf-start").value);
    if (!(v > 0)) return toast("Starting cash must be more than 0", "err");
    try { await api("/api/portfolio/settings", { method: "PUT", body: JSON.stringify({ starting_cash: v, reset }) }); toast(reset ? "Portfolio reset" : "Starting cash saved"); this.tick($("#app"), true); }
    catch (e) { toast(e.message, "err"); }
  },
  renderEquity(p) {
    const box = $("#pf-equity");
    if (p.equity_curve.length < 2) {
      if (this.chart) { this.chart.remove(); this.chart = null; }
      box.innerHTML = `<div class="empty-line">${p.trades.length ? "The equity line starts after the first full day with a position." : "Equity is drawn day by day once you place the first trade."} Today: <b class="num">${fmtUsd(p.equity)}</b></div>`;
      return;
    }
    if (!this.chart) {
      box.innerHTML = `<div class="equity-wrap" id="pf-chart"></div>`;
      this.chart = makeChart($("#pf-chart"), { timeScale: { borderColor: css("--control"), timeVisible: false } });
      this.series = this.chart.addSeries(LC.LineSeries, { color: accent(), lineWidth: 2, priceLineVisible: false, priceFormat: { type: "price", precision: 2, minMove: 0.01 } });
      this.series.createPriceLine({ price: p.starting_cash, color: css("--faint"), lineWidth: 1, lineStyle: LC.LineStyle.Dashed, axisLabelVisible: false, title: "start" });
    }
    this.series.setData(p.equity_curve);
    this.chart.timeScale().fitContent();
  },
  async tick(el, first = false) {
    if (!first) await loadOverview();
    let p;
    try { p = await getPortfolio(true); }
    catch (e) {
      if (state.view === this) $("#pf-lede").innerHTML = `<span class="down">Couldn't load the paper account.</span> <button class="linkbtn" onclick="portfolioView.tick($('#app'), true)">Retry</button>`;
      return;
    }
    if (state.view !== this) return;
    if (first || document.activeElement !== $("#pf-start")) $("#pf-start").value = p.starting_cash;
    $("#account-eq").textContent = fmtUsd(p.equity);
    const n = p.positions.length, nt = p.trades.length;
    $("#pf-lede").innerHTML = nt
      ? `<b class="num ${tone(p.total_return)}">${fmtPct(p.total_return)}</b> on <span class="num">${fmtUsd(p.starting_cash)}</span> starting cash since ${fmtDate(Math.min(...p.trades.map((t) => t.time)))} · ${n} open position${n === 1 ? "" : "s"}`
      : `Starting cash <b class="num">${fmtUsd(p.starting_cash)}</b> · no trades yet. Prices are the stored market data; no broker, no real money.`;
    const k = [
      ["Equity", fmtUsd(p.equity), `<span class="num ${tone(p.total_return)}">${fmtPct(p.total_return)}</span> since start`, "lead"],
      ["Cash", fmtUsd(p.cash), `${p.equity ? ((p.cash / p.equity) * 100).toFixed(1) : "0.0"}% of equity`],
      ["In positions", fmtUsd(p.positions_value), `${n} open`],
      ["Unrealized P&amp;L", `<span class="${tone(p.unrealized_pnl, 0.005)}">${fmtSignedUsd(p.unrealized_pnl)}</span>`, "on open positions"],
      ["Realized P&amp;L", `<span class="${tone(p.realized_pnl, 0.005)}">${fmtSignedUsd(p.realized_pnl)}</span>`, `after <span class="num">${fmtUsd(p.fees_paid)}</span> fees`],
    ];
    $("#pf-kpis").innerHTML = k.map(([a, b, c, lead]) => `<div class="kpi${lead ? " lead" : ""}"><div class="k">${a}</div><div class="v num">${b}</div><div class="s">${c}</div></div>`).join("");
    this.renderEquity(p);

    $("#pf-npos").textContent = n ? `${n} open · cash ${p.equity ? ((p.cash / p.equity) * 100).toFixed(1) : 0}%` : "";
    if (n) {
      const pos = [...p.positions].sort((x, y) => y.value - x.value);
      const segs = [...pos.map((x, i) => [x.weight, shade(i)]), [p.equity ? p.cash / p.equity : 1, "var(--night-4)"]];
      $("#pf-pos").innerHTML = `<div class="alloc" aria-hidden="true">${segs.filter(([w]) => w > 0).map(([w, c]) => `<span style="flex:${w} 1 0;background:${c}"></span>`).join("")}</div>
        <div class="alloc-cap"><span>Allocation by value</span><span><span class="swatch" style="background:var(--night-4)"></span>Cash</span></div>
        <div class="table-wrap"><table><thead><tr><th class="l">Asset</th><th class="hide-sm">Quantity</th><th class="hide-md">Avg cost</th><th class="hide-sm">Price</th><th>Value</th><th>P&amp;L</th><th class="hide-sm">Weight</th></tr></thead><tbody>
        ${pos.map((x, i) => `<tr class="click" data-sym="${esc(x.symbol)}" tabindex="0">
          <td class="l"><div class="asset-cell">${icon(x.symbol)}<div style="min-width:0"><div class="nm">${esc(x.name)}</div>
            <div class="sy"><span class="hide-sm">${esc(x.symbol)}</span><span class="m-sub num">${fmtQty(x.qty)} ${esc(base(x.symbol))} · avg $${fmtPrice(x.avg_cost)}</span></div></div></div></td>
          <td class="num hide-sm">${fmtQty(x.qty)}</td><td class="num hide-md">$${fmtPrice(x.avg_cost)}</td><td class="num hide-sm">$${fmtPrice(x.price)}</td>
          <td class="num">${fmtUsd(x.value)}</td>
          <td class="num"><span class="${tone(x.pnl, 0.005)}">${fmtSignedUsd(x.pnl)}</span><div class="muted" style="font-size:12px">${fmtPct(x.pnl_pct)}</div></td>
          <td class="num hide-sm"><span class="swatch" style="background:${shade(i)}"></span>${(x.weight * 100).toFixed(1)}%</td></tr>`).join("")}</tbody></table></div>`;
    } else {
      $("#pf-pos").innerHTML = `<div class="empty-line">No open positions. All <b class="num">${fmtUsd(p.cash)}</b> is in cash; buy something in <b>Paper trade</b>.</div>`;
    }

    $("#pf-ntr").textContent = nt ? `${nt} trade${nt === 1 ? "" : "s"} · newest first` : "";
    $("#pf-trades").innerHTML = nt ? `<div class="scroll-frame"><table><thead><tr><th class="l">Time</th><th class="l">Asset</th><th class="l">Side</th><th>Quantity</th><th>Price</th><th class="hide-sm">Fee</th><th>Cash</th><th><span class="sr">Delete</span></th></tr></thead><tbody>
      ${[...p.trades].sort((x, y) => y.time - x.time).map((t) => {
        const cash = t.side === "buy" ? -(t.qty * t.price + t.fee) : t.qty * t.price - t.fee;
        const desc = `${t.side} of ${fmtQty(t.qty)} ${base(t.symbol)} on ${fmtDateTime(t.time)}`;
        return `<tr><td class="l muted num">${fmtDateTime(t.time)}</td><td class="l">${esc(base(t.symbol))}</td>
        <td class="l">${t.side === "buy" ? "Buy" : "Sell"}</td>
        <td class="num">${fmtQty(t.qty)}</td><td class="num">$${fmtPrice(t.price)}</td><td class="num hide-sm">${fmtUsd(t.fee)}</td>
        <td class="num">${fmtSignedUsd(cash)}</td>
        <td><button class="btn icon" data-del="${esc(t.id)}" data-desc="${esc(desc)}" aria-label="Delete ${esc(desc)}" title="Delete trade"><svg viewBox="0 0 16 16"><path d="M4 4l8 8M12 4l-8 8"/></svg></button></td></tr>`;
      }).join("")}</tbody></table></div>`
      : `<div class="empty-line">No trades yet. Each paper buy or sell is listed here and can be deleted.</div>`;
    updateTradeEstimate($("#pf-trade"));
  },
  unmount() { if (this.chart) { this.chart.remove(); this.chart = null; } },
};
window.portfolioView = portfolioView;

/* ================================================================ DATA === */
function storagePanel(h, mb) {
  const u = h.storage, ar = h.archive || {};
  if (!u) return "";
  const gb = (b) => (b / 1024 ** 3).toFixed(b >= 10 * 1024 ** 3 ? 0 : 2) + " GB";
  const ds = Object.entries(u.datasets).filter(([, v]) => v > 0).sort((a, b) => b[1] - a[1]);
  const pct = u.pct * 100, days = ar.book_days || [];
  return `<section class="panel mb">
    <div class="panel-head"><h2>Storage budget</h2><span class="sub">${gb(u.total)} of ${gb(u.budget)} · ${gb(u.disk_free)} free on disk</span></div>
    <div class="storage">
      <div class="meter"><div style="width:${Math.max(0.5, Math.min(100, pct)).toFixed(1)}%;background:${pct >= 95 ? "var(--negative)" : pct >= 80 ? "var(--warning, #d6a64a)" : "var(--accent)"}"></div></div>
      <div class="stats">${ds.map(([k, v]) => `<div class="stat"><div class="k">${esc(k)}</div><div class="v num">${gb(v)}</div></div>`).join("")}</div>
      <p class="note">Archive: 1 m candles for <b>${ar.klines_pairs ?? "—"}</b> USDT pairs (incl. delisted) · every trade for <b>${ar.trades_pairs ?? "—"}</b> coins (${ar.trades_files ?? 0} files) · best bid/ask recorded on <b>${days.length}</b> day(s)${days.length ? ` since ${esc(days[0])}` : ""}. Book ticks are a rolling window capped at ${gb(u.book_max)}; backfills stop at 95 % of the budget.</p>
    </div></section>`;
}

const dataView = {
  async mount(el) {
    el.innerHTML = `<div class="title-row"><div><h1>Data health</h1><p class="lede">Scanning the Parquet store… (cached for 10 min, the first scan takes about 10 s)</p></div></div>`;
    el.addEventListener("click", (e) => { const r = e.target.closest("tr[data-sym]"); if (r) go(r.dataset.sym); });
    el.addEventListener("keydown", (e) => { const r = e.target.closest("tr[data-sym]"); if (r && e.key === "Enter") go(r.dataset.sym); });
    await this.tick(el);
  },
  async tick(el) {
    let h;
    try { h = await api("/api/health"); }
    catch (e) {
      if (state.view !== this) return;
      el.innerHTML = `<div class="title-row"><div><h1>Data health</h1></div></div><div class="panel">${errorBlock("data health", "dataView.tick(document.getElementById('app'))")}</div>`;
      return;
    }
    if (state.view !== this) return;
    const yr = h.yahoo_intraday;
    const mb = (b) => b >= 1e9 ? (b / 1e9).toFixed(2) + " GB" : (b / 1e6).toFixed(1) + " MB";
    const rows = h.rows.reduce((s, r) => s + (r.rows || 0), 0), size = h.rows.reduce((s, r) => s + (r.size || 0), 0);
    const feeds = h.rows.filter((r) => r.lag_min != null), live = feeds.filter((r) => r.lag_min < 5);
    const stale = feeds.filter((r) => r.lag_min >= 5);
    const yOk = yr && !yr.failed.length;
    const fd = h.feed || {}, srcs = Object.entries(fd.sources || {});
    const fresh = fd.generated && Date.now() / 1000 - fd.generated < 3 * (fd.poll_seconds || 30);
    const srcOk = srcs.filter(([, v]) => !v.error && v.last_ok && Date.now() / 1000 - v.last_ok < 600);
    const nQuotes = state.assets.filter((a) => a.fetched && Date.now() / 1000 - a.fetched < 120).length;
    const lede = [
      feeds.length ? `<b>${live.length} of ${feeds.length}</b> live crypto feeds under 5 min behind${stale.length ? `; behind: ${stale.map((r) => esc(base(r.symbol))).join(", ")}` : ""}` : "No live feeds found",
      yr ? `Yahoo 1 m collector ${yOk ? "ran fine" : `<span class="down">failed for ${yr.failed.length > 8 ? yr.failed.length + " symbols" : esc(yr.failed.join(", "))}</span>`} ${ago(Date.parse(yr.time) / 1000)}` : "Yahoo 1 m collector has never run",
      fd.generated ? `quote poller ${fresh ? "running" : '<span class="down">stalled</span>'}, last poll ${ago(fd.generated)} (${srcs.map(([k, v]) => `${esc(k)} ${v.error ? '<span class="down">error</span>' : "ok"}`).join(", ")})` : '<span class="down">quote poller has not written yet</span>',
      `store scanned ${ago(h.generated)}`,
    ].join(" · ");
    el.innerHTML = `
      <div class="title-row"><div><h1>Data health</h1><p class="lede">${lede}.</p></div></div>
      <section class="panel kpis four" aria-label="Store totals">
        <div class="kpi"><div class="k">Rows stored</div><div class="v num">${rows.toLocaleString("en-US")}</div><div class="s">${h.rows.length} datasets</div></div>
        <div class="kpi"><div class="k">Size on disk</div><div class="v num">${mb(size)}</div><div class="s">Parquet, local</div></div>
        <div class="kpi"><div class="k">Live quotes</div><div class="v num ${fresh ? "" : "down"}">${nQuotes}<span class="muted" style="font-size:14px"> /${h.symbols || state.assets.length}</span></div><div class="s">polled every ${fd.poll_seconds || 30} s · ${srcOk.length}/${srcs.length} sources OK · ${mb(h.quotes_size || 0)} snapshots</div></div>
        <div class="kpi"><div class="k">Yahoo 1 m collector</div><div class="v ${yr ? (yOk ? "" : "down") : "muted"}">${yr ? (yOk ? "OK" : `${yr.failed.length} failed`) : "Never run"}</div><div class="s">${yr ? "last run " + ago(Date.parse(yr.time) / 1000) + " · " : ""}hourly on weekdays · ${live.length}/${feeds.length} crypto 1 m feeds live</div></div>
      </section>
      ${storagePanel(h, mb)}
      <section class="panel">
        <div class="panel-head"><h2>Datasets</h2><span class="sub">times in your local zone</span></div>
        <div class="scroll-frame table-wrap"><table><thead><tr><th class="l">Symbol</th><th class="l">Dataset</th><th>First bar</th><th>Last bar</th><th>Rows</th><th>Gaps</th><th>Missing bars</th><th class="l">Freshness</th><th>Size</th></tr></thead><tbody>
        ${h.rows.map((r) => `<tr class="click" data-sym="${esc(r.symbol)}" tabindex="0"><td class="l"><div class="asset-cell">${icon(r.symbol)}<span class="nm">${esc(r.symbol)}</span></div></td>
          <td class="l muted">${esc(r.dataset)}</td><td class="num">${r.first ? fmtDate(r.first) : "—"}</td>
          <td class="num">${r.last ? (r.dataset.endsWith(" 1d") ? fmtDate(r.last) : fmtDateTime(r.last)) : "—"}</td>
          <td class="num">${(r.rows || 0).toLocaleString("en-US")}</td><td class="num">${r.gaps ?? '<span class="muted">—</span>'}</td><td class="num">${r.missing != null ? r.missing.toLocaleString("en-US") : '<span class="muted">—</span>'}</td>
          <td class="l">${r.lag_min != null ? `<span class="pill ${r.lag_min < 5 ? "pos" : "neg"}">${r.lag_min < 5 ? "Live" : Math.round(r.lag_min) + " min behind"}</span>` : `<span class="muted">${r.last ? ago(r.last) : "—"}</span>`}</td>
          <td class="num muted">${r.size ? mb(r.size) : "—"}</td></tr>`).join("")}</tbody></table></div>
        <div class="note">Crypto gaps are counted around the clock and are mostly real exchange outages, such as Binance maintenance. ETF 1 m gaps are counted within each session; thin tickers like CSSPX.SW only have bars in minutes with trades.</div>
      </section>`;
  },
};
window.dataView = dataView;

/* ============================================================== ROUTER === */
async function route() {
  const el = $("#app");
  const h = location.hash.replace(/^#\/?/, "");
  if (state.view?.unmount) state.view.unmount();
  let view, arg, tab;
  if (h.startsWith("asset/")) { view = assetView; arg = decodeURIComponent(h.slice(6)); tab = "overview"; }
  else if (h === "portfolio") { view = portfolioView; tab = "portfolio"; }
  else if (h === "data") { view = dataView; tab = "data"; }
  else { view = overviewView; tab = "overview"; }
  document.querySelectorAll(".rail a.nav").forEach((a) => {
    const on = a.dataset.tab === tab;
    a.classList.toggle("active", on);
    if (on) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
  });
  // a fresh node per view, so listeners never pile up across navigations
  const fresh = el.cloneNode(false); el.replaceWith(fresh);
  state.view = view;
  window.scrollTo(0, 0);
  await view.mount(fresh, arg);
  setTitle();
}
window.route = route;

function setTitle() {
  const a = state.view === assetView ? state.bySym[assetView.sym] : null;
  document.title = (a ? `${base(a.symbol)} ${money(a, a.price)} · ` : "") + "Markets · Homelab";
}

function startTimer() {
  clearInterval(state.timer);
  state.timer = setInterval(async () => {
    if (document.hidden || !state.view?.tick) return;
    await state.view.tick($("#app"));
    refreshAccount();
    setTitle();
  }, REFRESH_MS);
}

document.addEventListener("keydown", (e) => {
  if (e.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) { e.preventDefault(); $("#search").focus(); }
});
document.addEventListener("visibilitychange", () => { if (!document.hidden && state.view?.tick) state.view.tick($("#app")); });

attachSearch($("#search"), $("#search-results"), (a) => { $("#search").value = ""; $("#search").blur(); go(a.symbol); });
window.addEventListener("hashchange", route);
function bootFrame() {
  const h = location.hash.replace(/^#\/?/, "");
  const title = h === "portfolio" ? "Paper portfolio" : h === "data" ? "Data health" : h.startsWith("asset/") ? decodeURIComponent(h.slice(6)) : "Markets";
  const bar = (w, ht = 14) => `<span class="skel" style="width:${w};height:${ht}px"></span>`;
  $("#app").innerHTML = `<div class="title-row"><div><h1>${esc(title)}</h1><p class="lede">${bar("34em")}</p></div></div>
    <section class="panel mb"><div class="panel-head"><h2>${h ? "Loading" : "Market breadth"}</h2></div><div class="breadth">${[1, 2, 3].map(() => `<div class="tape-row"><div class="tape-label">${bar("9em")}</div>${bar("100%", 40)}</div>`).join("")}</div></section>`;
}
bootFrame();
loadOverview().then(() => { route(); startTimer(); refreshAccount(true); });
