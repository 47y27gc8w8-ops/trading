/* Markets dashboard — vanilla JS SPA (hash routes: #/, #/asset/SYM, #/portfolio, #/data) */
"use strict";

const REFRESH_MS = 15000;
const TZ_SHIFT = -new Date().getTimezoneOffset() * 60; // charts show local time
const LC = window.LightweightCharts;

const state = { assets: [], bySym: {}, prevPrice: {}, view: null, timer: null, lastOk: 0 };

/* ------------------------------------------------------------ helpers --- */
const $ = (sel, el = document) => el.querySelector(sel);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

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
  return a >= 1000 ? 2 : a >= 10 ? 2 : a >= 1 ? 4 : a >= 0.01 ? 5 : 7;
}
const fmtPrice = (v) => v == null ? "—" : v.toLocaleString("en-US", { minimumFractionDigits: decimals(v), maximumFractionDigits: decimals(v) });
const fmtUsd = (v, d = 2) => v == null ? "—" : (v < 0 ? "-" : "") + "$" + Math.abs(v).toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });
const fmtQty = (v) => v == null ? "—" : v.toLocaleString("en-US", { maximumFractionDigits: 8 });
const fmtCompact = (v) => v == null ? "—" : "$" + Intl.NumberFormat("en-US", { notation: "compact", maximumFractionDigits: 2 }).format(v);
const cls = (v) => v == null ? "muted" : v >= 0 ? "up" : "down";
const fmtPct = (v, sign = true) => v == null ? "—" : (sign && v >= 0 ? "+" : "") + (v * 100).toFixed(2) + "%";
const pill = (v) => `<span class="pill ${cls(v)}">${fmtPct(v)}</span>`;
const fmtDate = (t) => new Date(t * 1000).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
const fmtDateTime = (t) => new Date(t * 1000).toLocaleString(undefined, { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" });
function ago(t) {
  const s = Math.max(0, Date.now() / 1000 - t);
  if (s < 90) return "just now";
  if (s < 3600) return Math.round(s / 60) + " min ago";
  if (s < 86400 * 2) return Math.round(s / 3600) + " h ago";
  return Math.round(s / 86400) + " d ago";
}
const base = (sym) => sym.replace(/USDT$/, "").replace(/^\^GSPC$/, "SPX").replace(/^\^/, "").replace(/\..*$/, "");

const ICON_COLORS = { BTC: "#f7931a", ETH: "#627eea", SOL: "#9945ff", BNB: "#f0b90b", XRP: "#23292f", DOGE: "#c2a633", ADA: "#0033ad", TRX: "#ef0027", LINK: "#2a5ada", AVAX: "#e84142", LTC: "#345d9d", BCH: "#0ac18e", XLM: "#14b6e7", NEAR: "#00c08b", ZEC: "#ecb244", HYPE: "#50d2c1", SPY: "#1f6feb", SPX: "#334155", CSSPX: "#111827", QQQ: "#0e7490" };
function icon(sym, lg = false) {
  const b = base(sym);
  let c = ICON_COLORS[b];
  if (!c) { let h = 0; for (const ch of b) h = (h * 31 + ch.charCodeAt(0)) % 360; c = `hsl(${h} 55% 42%)`; }
  const txt = b.length > 4 ? b.slice(0, 3) : b;
  return `<span class="icon${lg ? " lg" : ""}" style="background:${c};${["XRP", "CSSPX"].includes(b) ? "box-shadow:inset 0 0 0 1px #3a4458" : ""}">${esc(txt)}</span>`;
}

function sparkline(vals, w = 120, h = 36) {
  if (!vals || vals.length < 2) return `<svg class="spark" width="${w}" height="${h}"></svg>`;
  const mn = Math.min(...vals), mx = Math.max(...vals), r = mx - mn || 1;
  const pts = vals.map((v, i) => [(i / (vals.length - 1)) * w, h - 3 - ((v - mn) / r) * (h - 6)]);
  const d = pts.map((p, i) => (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1)).join("");
  const col = vals[vals.length - 1] >= vals[0] ? "var(--up)" : "var(--down)";
  const id = "g" + Math.random().toString(36).slice(2, 8);
  return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none">
    <defs><linearGradient id="${id}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${col}" stop-opacity=".25"/><stop offset="1" stop-color="${col}" stop-opacity="0"/></linearGradient></defs>
    <path d="${d}L${w} ${h}L0 ${h}Z" fill="url(#${id})"/><path d="${d}" fill="none" stroke="${col}" stroke-width="1.6" stroke-linejoin="round"/></svg>`;
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
  $("#live-text").textContent = ok ? "Live · " + new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" }) : "Offline — retrying";
}

/* ----------------------------------------------------------- data load --- */
async function loadOverview() {
  try {
    const j = await api("/api/overview");
    state.prevPrice = Object.fromEntries(state.assets.map((a) => [a.symbol, a.price]));
    state.assets = j.assets;
    state.bySym = Object.fromEntries(j.assets.map((a) => [a.symbol, a]));
    setLive(true);
  } catch (e) { setLive(false); }
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
        <div class="meta"><div class="sym">${esc(a.name)}</div><div class="nm">${esc(a.symbol)} · ${a.type === "crypto" ? "Crypto" : a.symbol.startsWith("^") ? "Index" : "ETF"}</div></div>
        <div style="text-align:right"><div class="num">${fmtPrice(a.price)}</div><div class="num ${cls(a.change_24h)}" style="font-size:12px">${fmtPct(a.change_24h)}</div></div>
      </div>`).join("") : `<div class="search-empty">No tracked asset matches “${esc(input.value)}”.<br><span class="faint">Add symbols in config/symbols.yaml</span></div>`;
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
  return LC.createChart(el, {
    autoSize: true,
    layout: { background: { color: "transparent" }, textColor: "#8a93a6", fontFamily: "Inter, system-ui, sans-serif", attributionLogo: true },
    grid: { vertLines: { color: "rgba(34,42,58,.5)" }, horzLines: { color: "rgba(34,42,58,.5)" } },
    rightPriceScale: { borderColor: "#222a3a" },
    timeScale: { borderColor: "#222a3a", timeVisible: true, secondsVisible: false, rightOffset: 4 },
    crosshair: { mode: LC.CrosshairMode.Normal },
    ...opts,
  });
}

/* ============================================================ OVERVIEW === */
const sortState = { crypto: { key: "mcap", asc: true }, etf: { key: "mcap", asc: true } };

function assetTable(kind, assets) {
  const s = sortState[kind];
  const cols = [
    ["mcap", "#", "l"], ["name", "Asset", "l"], ["price", "Price"], ["change_24h", "24h"], ["change_7d", "7d"],
    ["range", kind === "crypto" ? "24h range" : "Day range", "hide-md"], ["volume_24h", kind === "crypto" ? "Volume 24h" : "Volume (day)", "hide-sm"],
    ["spark", kind === "crypto" ? "Last 7 days" : "Last 60 days", "hide-sm"], ["time", "Updated", "hide-md"],
  ];
  const rows = assets.map((a, i) => ({ ...a, mcap: i }));
  if (s.key !== "mcap" || !s.asc) {
    rows.sort((x, y) => {
      let a = x[s.key], b = y[s.key];
      if (typeof a === "string") return s.asc ? a.localeCompare(b) : b.localeCompare(a);
      a = a ?? -Infinity; b = b ?? -Infinity;
      return s.asc ? a - b : b - a;
    });
  }
  return `<table data-kind="${kind}"><thead><tr>${cols.map(([k, label, c]) =>
    `<th class="${c || ""} ${["range", "spark"].includes(k) ? "" : "sortable"} ${s.key === k ? "sorted" + (s.asc ? " asc" : "") : ""}" data-k="${k}">${label}</th>`).join("")}</tr></thead>
    <tbody>${rows.map((a) => {
      const prev = state.prevPrice[a.symbol];
      const flash = prev != null && a.price != null && prev !== a.price ? (a.price > prev ? "flash-up" : "flash-down") : "";
      const pos = a.high_24h > a.low_24h ? Math.min(100, Math.max(0, ((a.price - a.low_24h) / (a.high_24h - a.low_24h)) * 100)) : 50;
      return `<tr class="click" data-sym="${esc(a.symbol)}">
        <td class="faint num">${a.mcap + 1}</td>
        <td class="l"><div class="asset-cell">${icon(a.symbol)}<div><div class="nm">${esc(a.name)}${a.symbol.startsWith("^") ? '<span class="tag">index</span>' : ""}</div><div class="sy">${esc(a.symbol)}</div></div></div></td>
        <td class="num ${flash}">${a.price == null ? '<span class="faint">loading…</span>' : (a.currency === "pts" ? "" : "$") + fmtPrice(a.price)}</td>
        <td>${pill(a.change_24h)}</td>
        <td class="num ${cls(a.change_7d)}">${fmtPct(a.change_7d)}</td>
        <td class="hide-md">${a.price == null ? "—" : `<span class="faint num" style="font-size:11px">${fmtPrice(a.low_24h)}</span> <span class="range"><i style="left:${pos}%"></i></span> <span class="faint num" style="font-size:11px">${fmtPrice(a.high_24h)}</span>`}</td>
        <td class="num hide-sm">${a.symbol.startsWith("^") ? "—" : fmtCompact(a.volume_24h)}</td>
        <td class="hide-sm">${sparkline(a.spark)}</td>
        <td class="muted hide-md">${a.time ? ago(a.time) : "—"}</td>
      </tr>`;
    }).join("")}</tbody></table>`;
}

const overviewView = {
  async mount(el) {
    el.innerHTML = `<div class="skeleton">Loading markets…</div>`;
    await this.refresh(el);
  },
  async refresh(el) {
    if (!state.assets.length) await loadOverview();
    const crypto = state.assets.filter((a) => a.type === "crypto");
    const etf = state.assets.filter((a) => a.type === "etf");
    const highlights = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "SPY"].map((s) => state.bySym[s]).filter(Boolean);
    const upCount = crypto.filter((a) => (a.change_24h ?? 0) >= 0).length;
    el.innerHTML = `
      <div class="page-head"><div><h1>Market overview</h1>
        <p>${crypto.length} crypto pairs · ${etf.length} ETFs &amp; indices · ${upCount}/${crypto.length} crypto up in 24h</p></div></div>
      <div class="cards">${highlights.map((a) => `
        <div class="panel card" data-sym="${esc(a.symbol)}">
          <div class="card-top">${icon(a.symbol)}<div><div style="font-weight:600">${esc(a.name)}</div><div class="muted" style="font-size:12px">${esc(a.symbol)}</div></div></div>
          <div class="card-price num">$${fmtPrice(a.price)}</div>
          <div class="card-chg num ${cls(a.change_24h)}">${fmtPct(a.change_24h)} <span class="faint">24h</span></div>
          ${sparkline(a.spark, 110, 40)}
        </div>`).join("")}</div>
      <div class="panel mb"><div class="panel-head"><h2>Crypto</h2><span class="sub">Binance spot · USDT · live 1m bars</span></div>${assetTable("crypto", crypto)}</div>
      <div class="panel"><div class="panel-head"><h2>ETFs &amp; indices</h2><span class="sub">Yahoo Finance · daily + 1m (collected after US close)</span></div>${assetTable("etf", etf)}</div>`;
    el.querySelectorAll("[data-sym]").forEach((r) => r.addEventListener("click", () => (location.hash = "#/asset/" + encodeURIComponent(r.dataset.sym))));
    el.querySelectorAll("th.sortable").forEach((th) => th.addEventListener("click", () => {
      const kind = th.closest("table").dataset.kind, s = sortState[kind], k = th.dataset.k;
      if (s.key === k) s.asc = !s.asc; else { s.key = k; s.asc = k === "name" || k === "mcap"; }
      state.prevPrice = {};
      this.refresh(el);
    }));
  },
  async tick(el) { await loadOverview(); await this.refresh(el); },
};

/* =============================================================== ASSET === */
const TFS = ["1m", "5m", "15m", "1h", "4h", "1d", "1w"];
const assetView = {
  chart: null, tf: localStorage.getItem("tf") || "1h", side: "buy",
  async mount(el, sym) {
    this.sym = sym;
    if (!state.assets.length) await loadOverview();
    const a = state.bySym[sym];
    if (!a) { el.innerHTML = `<div class="empty"><b>Unknown asset “${esc(sym)}”</b>Not in config/symbols.yaml.</div>`; return; }
    this.a = a;
    el.innerHTML = `
      <a class="back" href="#/">← Overview</a>
      <div class="page-head">
        <div class="asset-head">${icon(sym, true)}
          <div><h1>${esc(a.name)}</h1><div class="muted">${esc(sym)} · ${a.type === "crypto" ? "Binance spot" : "Yahoo Finance"}</div></div>
          <div style="margin-left:18px"><div class="px num" id="a-price">${fmtPrice(a.price)}</div><div id="a-chg" class="num"></div></div>
        </div>
        <div class="seg" id="tfs">${TFS.map((t) => `<button data-tf="${t}" class="${t === this.tf ? "on" : ""}">${t}</button>`).join("")}</div>
      </div>
      <div class="asset-layout">
        <div class="panel"><div class="chart-wrap" id="chart"><div class="chart-legend" id="legend"></div></div></div>
        <div class="grid" style="align-content:start">
          <div class="panel"><div class="stats" id="stats"></div></div>
          ${a.tradable ? `<div class="panel" id="trade-panel"></div>` : `<div class="panel note" style="border-top:0">Indices can't be traded — use SPY or CSSPX.SW for S&amp;P 500 exposure.</div>`}
        </div>
      </div>`;
    $("#tfs").addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      this.tf = b.dataset.tf; localStorage.setItem("tf", this.tf);
      $("#tfs").querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b));
      this.loadBars();
    });
    this.renderHeader();
    if (a.tradable) renderTradeForm($("#trade-panel"), sym, true);
    this.buildChart();
    await this.loadBars();
  },
  renderHeader() {
    const a = state.bySym[this.sym] || this.a;
    $("#a-price").textContent = (a.currency === "pts" ? "" : "$") + fmtPrice(a.price);
    $("#a-chg").innerHTML = `${pill(a.change_24h)} <span class="faint" style="font-size:12px">24h</span>`;
    const st = [
      ["24h high", fmtPrice(a.high_24h)], ["24h low", fmtPrice(a.low_24h)],
      ["7d change", `<span class="${cls(a.change_7d)}">${fmtPct(a.change_7d)}</span>`],
      ["Volume", a.symbol.startsWith("^") ? "—" : fmtCompact(a.volume_24h)],
      ["Last bar", a.time ? (Date.now() / 1000 - a.time < 86400 ? new Date(a.time * 1000).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) : fmtDate(a.time)) : "—"], ["Quote", a.currency || "USD"],
    ];
    $("#stats").innerHTML = st.map(([k, v]) => `<div class="stat"><div class="k">${k}</div><div class="v num">${v}</div></div>`).join("");
  },
  buildChart() {
    const el = $("#chart");
    this.chart = makeChart(el);
    const p = this.a.price || 1, prec = decimals(p);
    this.candles = this.chart.addSeries(LC.CandlestickSeries, {
      upColor: "#10b981", downColor: "#f43f5e", borderVisible: false, wickUpColor: "#10b981", wickDownColor: "#f43f5e",
      priceFormat: { type: "price", precision: prec, minMove: Math.pow(10, -prec) },
    });
    this.volume = this.chart.addSeries(LC.HistogramSeries, { priceFormat: { type: "volume" }, priceScaleId: "vol", lastValueVisible: false, priceLineVisible: false });
    this.chart.priceScale("vol").applyOptions({ scaleMargins: { top: 0.82, bottom: 0 } });
    this.candles.priceScale().applyOptions({ scaleMargins: { top: 0.08, bottom: 0.22 } });
    this.chart.subscribeCrosshairMove((p) => this.legend(p));
    this.chart.timeScale().subscribeVisibleLogicalRangeChange((r) => {
      if (r && r.from < 30 && this.hasMore && !this.loadingMore) this.loadMore();
    });
  },
  legend(p) {
    const d = p && p.time ? p.seriesData.get(this.candles) : this.bars?.[this.bars.length - 1];
    if (!d) { $("#legend").innerHTML = ""; return; }
    const c = d.close >= d.open ? "up" : "down";
    $("#legend").innerHTML = `<span>O <b class="${c}">${fmtPrice(d.open)}</b></span><span>H <b class="${c}">${fmtPrice(d.high)}</b></span><span>L <b class="${c}">${fmtPrice(d.low)}</b></span><span>C <b class="${c}">${fmtPrice(d.close)}</b></span>`;
  },
  toSeries(bars) {
    return bars.map((b) => ({ time: b.time + TZ_SHIFT, open: b.open, high: b.high, low: b.low, close: b.close, volume: b.volume }));
  },
  vol(b) { return { time: b.time, value: b.volume, color: b.close >= b.open ? "rgba(16,185,129,.35)" : "rgba(244,63,94,.35)" }; },
  async loadBars() {
    const tf = this.tf, sym = this.sym;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(sym)}&tf=${tf}&limit=1500`);
      if (tf !== this.tf || sym !== this.sym) return;
      this.bars = this.toSeries(j.bars);
      this.hasMore = j.has_more;
      this.candles.setData(this.bars);
      this.volume.setData(this.bars.map((b) => this.vol(b)));
      this.chart.applyOptions({ timeScale: { timeVisible: !["1d", "1w"].includes(tf) } });
      const n = this.bars.length;
      if (n) this.chart.timeScale().setVisibleLogicalRange({ from: Math.max(0, n - 160), to: n + 4 });
      if (!n) $("#legend").innerHTML = `<span>No ${tf} data for this asset${this.a.type === "etf" ? " (Yahoo keeps ~30 days of intraday bars; we collect from setup onward)" : ""}</span>`;
      else this.legend(null);
    } catch (e) { toast("Chart: " + e.message, "err"); }
  },
  async loadMore() {
    this.loadingMore = true;
    const tf = this.tf, first = this.bars[0].time - TZ_SHIFT;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(this.sym)}&tf=${tf}&limit=1500&end=${first}`);
      if (tf !== this.tf || !j.bars.length) { this.hasMore = false; return; }
      const older = this.toSeries(j.bars).filter((b) => b.time < this.bars[0].time);
      this.bars = older.concat(this.bars);
      this.hasMore = j.has_more;
      const range = this.chart.timeScale().getVisibleLogicalRange();
      this.candles.setData(this.bars);
      this.volume.setData(this.bars.map((b) => this.vol(b)));
      if (range) this.chart.timeScale().setVisibleLogicalRange({ from: range.from + older.length, to: range.to + older.length });
    } finally { this.loadingMore = false; }
  },
  async tick() {
    await loadOverview();
    if (!state.bySym[this.sym]) return;
    this.renderHeader();
    if (!this.bars?.length) return;
    const tf = this.tf;
    try {
      const j = await api(`/api/bars?symbol=${encodeURIComponent(this.sym)}&tf=${tf}&limit=3`);
      if (tf !== this.tf) return;
      for (const b of this.toSeries(j.bars)) {
        const last = this.bars[this.bars.length - 1];
        if (b.time < last.time) continue;
        if (b.time === last.time) this.bars[this.bars.length - 1] = b; else this.bars.push(b);
        this.candles.update(b); this.volume.update(this.vol(b));
      }
      this.legend(null);
    } catch {}
    const tp = $("#trade-panel"); if (tp) updateTradeEstimate(tp);
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
  el.innerHTML = `
    <div class="panel-head"><h2>Paper trade</h2><div class="seg side"><button data-v="buy" class="on">Buy</button><button data-v="sell">Sell</button></div></div>
    <div class="form">
      ${fixed ? "" : `<label class="field">Asset<div class="sym-pick"><input class="input" id="tf-sym" placeholder="Search… e.g. sol, spy" autocomplete="off" value="${esc(sym || "")}"><div class="search-results" hidden></div></div></label>`}
      <div class="form-row">
        <label class="field">Quantity<input class="input" id="tf-qty" type="number" min="0" step="any" placeholder="0.00"></label>
        <label class="field">Amount (USD)<input class="input" id="tf-amt" type="number" min="0" step="any" placeholder="0.00"></label>
      </div>
      <div class="form-row">
        <label class="field">Price (blank = last)<input class="input" id="tf-price" type="number" min="0" step="any" placeholder="market"></label>
        <label class="field">Fee %<input class="input" id="tf-fee" type="number" min="0" step="0.01" value="0.1"></label>
      </div>
      <div>
        <div class="summary-line"><span>Est. price</span><b class="num" id="tf-px">—</b></div>
        <div class="summary-line"><span>Fee</span><b class="num" id="tf-feev">—</b></div>
        <div class="summary-line"><span id="tf-total-l">Total cost</span><b class="num" id="tf-total">—</b></div>
        <div class="summary-line"><span id="tf-avail-l">Available cash</span><b class="num" id="tf-avail">—</b></div>
      </div>
      <button class="btn buy" id="tf-submit">Buy</button>
    </div>`;
  const side = el.querySelector(".seg.side");
  side.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    el.dataset.side = b.dataset.v;
    side.querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b));
    const s = $("#tf-submit", el); s.className = "btn " + b.dataset.v; s.textContent = b.dataset.v === "buy" ? "Buy" : "Sell";
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
  const p = tradePrice(el), q = parseFloat($("#tf-qty", el).value) || 0, fee = (parseFloat($("#tf-fee", el).value) || 0) / 100;
  const buy = el.dataset.side === "buy", notional = q * (p || 0), f = notional * fee;
  $("#tf-px", el).textContent = p ? "$" + fmtPrice(p) : "—";
  $("#tf-feev", el).textContent = q ? fmtUsd(f) : "—";
  $("#tf-total-l", el).textContent = buy ? "Total cost" : "You receive";
  $("#tf-total", el).textContent = q ? fmtUsd(buy ? notional + f : notional - f) : "—";
  const pf = portfolioCache;
  if (pf) {
    if (buy) { $("#tf-avail-l", el).textContent = "Available cash"; $("#tf-avail", el).textContent = fmtUsd(pf.cash); }
    else {
      const held = pf.positions.find((x) => x.symbol === el.dataset.sym)?.qty || 0;
      $("#tf-avail-l", el).textContent = "You hold"; $("#tf-avail", el).textContent = fmtQty(held) + " " + base(el.dataset.sym || "");
    }
  }
}

async function submitTrade(el) {
  const sym = el.dataset.sym, qty = parseFloat($("#tf-qty", el).value), price = parseFloat($("#tf-price", el).value);
  if (!sym || !state.bySym[sym]) return toast("Pick an asset first", "err");
  if (!(qty > 0)) return toast("Enter a quantity or amount", "err");
  const btn = $("#tf-submit", el); btn.disabled = true;
  try {
    const t = await api("/api/portfolio/trades", { method: "POST", body: JSON.stringify({
      symbol: sym, side: el.dataset.side, qty, price: price > 0 ? price : null, fee_pct: parseFloat($("#tf-fee", el).value) || 0 }) });
    toast(`${t.side === "buy" ? "Bought" : "Sold"} ${fmtQty(t.qty)} ${base(t.symbol)} @ $${fmtPrice(t.price)}`);
    $("#tf-qty", el).value = ""; $("#tf-amt", el).value = "";
    await getPortfolio(true); updateTradeEstimate(el);
    if (state.view === portfolioView) portfolioView.tick($("#app"));
  } catch (e) { toast(e.message, "err"); }
  finally { btn.disabled = false; }
}

/* =========================================================== PORTFOLIO === */
const PALETTE = ["#6366f1", "#10b981", "#f59e0b", "#06b6d4", "#ec4899", "#8b5cf6", "#84cc16", "#f97316", "#14b8a6", "#e11d48"];
const portfolioView = {
  chart: null,
  async mount(el) {
    if (!state.assets.length) await loadOverview();
    el.innerHTML = `
      <div class="page-head"><div><h1>Paper portfolio</h1><p>Simulated trades at stored market prices · no broker, no real money</p></div>
        <div style="display:flex;gap:8px;align-items:center">
          <label class="field" style="flex-direction:row;align-items:center;gap:8px">Starting cash
            <input class="input" id="pf-start" type="number" min="1" step="100" style="width:130px"></label>
          <button class="btn sm" id="pf-save">Save</button><button class="btn sm danger" id="pf-reset">Reset</button>
        </div></div>
      <div class="kpis" id="pf-kpis"></div>
      <div class="port-layout">
        <div class="grid">
          <div class="panel"><div class="panel-head"><h2>Equity</h2><span class="sub">daily, marked to market · USD</span></div><div id="pf-chart" style="height:260px;position:relative"></div></div>
          <div class="panel"><div class="panel-head"><h2>Positions</h2><span class="sub" id="pf-npos"></span></div><div id="pf-alloc"></div><div id="pf-pos"></div></div>
          <div class="panel"><div class="panel-head"><h2>Trade history</h2></div><div id="pf-trades"></div></div>
        </div>
        <div class="panel" id="pf-trade"></div>
      </div>`;
    renderTradeForm($("#pf-trade"), "", false);
    $("#pf-save").addEventListener("click", () => this.settings(false));
    $("#pf-reset").addEventListener("click", () => { if (confirm("Delete all paper trades and start over?")) this.settings(true); });
    this.chart = makeChart($("#pf-chart"), { timeScale: { borderColor: "#222a3a", timeVisible: false } });
    this.series = this.chart.addSeries(LC.AreaSeries, { lineColor: "#818cf8", topColor: "rgba(99,102,241,.35)", bottomColor: "rgba(99,102,241,0)", lineWidth: 2,
      priceFormat: { type: "price", precision: 2, minMove: 0.01 } });
    await this.tick(el, true);
  },
  async settings(reset) {
    const v = parseFloat($("#pf-start").value);
    if (!(v > 0)) return toast("Starting cash must be > 0", "err");
    try { await api("/api/portfolio/settings", { method: "PUT", body: JSON.stringify({ starting_cash: v, reset }) }); toast(reset ? "Portfolio reset" : "Saved"); this.tick($("#app"), true); }
    catch (e) { toast(e.message, "err"); }
  },
  async tick(el, first = false) {
    if (!first) await loadOverview();
    let p;
    try { p = await getPortfolio(true); } catch (e) { toast("Portfolio: " + e.message, "err"); return; }
    if (state.view !== this) return;
    if (first || document.activeElement !== $("#pf-start")) $("#pf-start").value = p.starting_cash;
    const k = [
      ["Equity", fmtUsd(p.equity), `<span class="${cls(p.total_return)}">${fmtPct(p.total_return)} total</span>`],
      ["Cash", fmtUsd(p.cash), `<span class="muted">${p.equity ? ((p.cash / p.equity) * 100).toFixed(1) : 0}% of equity</span>`],
      ["Positions", fmtUsd(p.positions_value), `<span class="muted">${p.positions.length} open</span>`],
      ["Unrealized P&L", `<span class="${cls(p.unrealized_pnl)}">${fmtUsd(p.unrealized_pnl)}</span>`, ""],
      ["Realized P&L", `<span class="${cls(p.realized_pnl)}">${fmtUsd(p.realized_pnl)}</span>`, `<span class="muted">fees ${fmtUsd(p.fees_paid)}</span>`],
    ];
    $("#pf-kpis").innerHTML = k.map(([a, b, c]) => `<div class="panel kpi"><div class="k">${a}</div><div class="v num">${b}</div><div class="s">${c}</div></div>`).join("");
    this.series.setData(p.equity_curve.length ? p.equity_curve : [{ time: Math.floor(Date.now() / 86400000) * 86400, value: p.equity }]);
    this.chart.timeScale().fitContent();
    $("#pf-npos").textContent = p.positions.length ? `${p.positions.length} position${p.positions.length > 1 ? "s" : ""}` : "";
    const segs = [...p.positions.map((x, i) => [x.symbol, x.weight, PALETTE[i % PALETTE.length]]), ["Cash", p.equity ? p.cash / p.equity : 1, "#334155"]];
    $("#pf-alloc").innerHTML = `<div class="alloc">${segs.map(([, w, c]) => `<span style="width:${(w * 100).toFixed(2)}%;background:${c}"></span>`).join("")}</div>
      <div class="legend">${segs.map(([s, w, c]) => `<span><i style="background:${c}"></i>${esc(s === "Cash" ? s : base(s))} ${(w * 100).toFixed(1)}%</span>`).join("")}</div>`;
    $("#pf-pos").innerHTML = p.positions.length ? `<table><thead><tr><th>Asset</th><th>Qty</th><th>Avg cost</th><th>Price</th><th class="hide-sm">24h</th><th>Value</th><th>P&amp;L</th></tr></thead><tbody>
      ${p.positions.map((x) => `<tr class="click" data-sym="${esc(x.symbol)}">
        <td><div class="asset-cell">${icon(x.symbol)}<div><div class="nm">${esc(x.name)}</div><div class="sy">${esc(x.symbol)}</div></div></div></td>
        <td class="num">${fmtQty(x.qty)}</td><td class="num">$${fmtPrice(x.avg_cost)}</td><td class="num">$${fmtPrice(x.price)}</td>
        <td class="hide-sm">${pill(x.change_24h)}</td><td class="num">${fmtUsd(x.value)}</td>
        <td class="num ${cls(x.pnl)}">${fmtUsd(x.pnl)}<div style="font-size:11px">${fmtPct(x.pnl_pct)}</div></td></tr>`).join("")}</tbody></table>`
      : `<div class="empty"><b>No open positions</b>Use the paper trade panel to buy your first asset.</div>`;
    $("#pf-pos").querySelectorAll("tr[data-sym]").forEach((r) => r.addEventListener("click", () => (location.hash = "#/asset/" + encodeURIComponent(r.dataset.sym))));
    $("#pf-trades").innerHTML = p.trades.length ? `<table><thead><tr><th>Time</th><th class="l">Asset</th><th class="l">Side</th><th>Qty</th><th>Price</th><th class="hide-sm">Fee</th><th>Total</th><th></th></tr></thead><tbody>
      ${p.trades.map((t) => `<tr><td class="muted">${fmtDateTime(t.time)}</td><td class="l">${esc(t.symbol)}</td>
        <td class="l"><span class="pill ${t.side === "buy" ? "up" : "down"}">${t.side.toUpperCase()}</span></td>
        <td class="num">${fmtQty(t.qty)}</td><td class="num">$${fmtPrice(t.price)}</td><td class="num hide-sm">${fmtUsd(t.fee)}</td>
        <td class="num">${fmtUsd(t.qty * t.price + (t.side === "buy" ? t.fee : -t.fee))}</td>
        <td><button class="btn sm ghost danger" data-del="${t.id}" title="Delete trade">✕</button></td></tr>`).join("")}</tbody></table>`
      : `<div class="empty">No trades yet.</div>`;
    $("#pf-trades").querySelectorAll("[data-del]").forEach((b) => b.addEventListener("click", async () => {
      if (!confirm("Delete this trade? Cash and positions will be recalculated.")) return;
      try { await api("/api/portfolio/trades/" + b.dataset.del, { method: "DELETE" }); toast("Trade deleted"); this.tick(el, true); }
      catch (e) { toast(e.message, "err"); }
    }));
    updateTradeEstimate($("#pf-trade"));
  },
  unmount() { if (this.chart) { this.chart.remove(); this.chart = null; } },
};

/* ================================================================ DATA === */
const dataView = {
  async mount(el) { el.innerHTML = `<div class="skeleton">Scanning data store… (cached for 5 min)</div>`; await this.tick(el); },
  async tick(el) {
    let h;
    try { h = await api("/api/health"); } catch (e) { el.innerHTML = `<div class="empty"><b>Couldn't load data health</b>${esc(e.message)}</div>`; return; }
    if (state.view !== this) return;
    const yr = h.yahoo_intraday;
    const mb = (b) => (b / 1e6).toFixed(1) + " MB";
    el.innerHTML = `
      <div class="page-head"><div><h1>Data health</h1><p>Coverage, gaps and freshness of the local Parquet store · scanned ${ago(h.generated)}</p></div></div>
      <div class="kpis">
        <div class="panel kpi"><div class="k">Total rows</div><div class="v num">${h.rows.reduce((s, r) => s + (r.rows || 0), 0).toLocaleString()}</div></div>
        <div class="panel kpi"><div class="k">Size on disk</div><div class="v num">${mb(h.rows.reduce((s, r) => s + (r.size || 0), 0))}</div></div>
        <div class="panel kpi"><div class="k">Yahoo 1m collector</div><div class="v" style="font-size:16px">${yr ? (yr.failed.length ? `<span class="down">failed: ${esc(yr.failed.join(", "))}</span>` : `<span class="up">OK</span>`) : "never run"}</div><div class="s muted">${yr ? "last run " + ago(Date.parse(yr.time) / 1000) : ""} · daily 22:30 UTC</div></div>
      </div>
      <div class="panel"><table><thead><tr><th>Symbol</th><th class="l">Dataset</th><th>First</th><th>Last</th><th>Rows</th><th>Gaps</th><th>Missing bars</th><th>Freshness</th><th>Size</th></tr></thead><tbody>
      ${h.rows.map((r) => `<tr class="click" data-sym="${esc(r.symbol)}"><td><div class="asset-cell">${icon(r.symbol)}<span class="nm">${esc(r.symbol)}</span></div></td>
        <td class="l muted">${r.dataset}</td><td class="num">${r.first ? fmtDate(r.first) : "—"}</td>
        <td class="num">${r.last ? (r.dataset === "etf 1d" ? fmtDate(r.last) : fmtDateTime(r.last)) : "—"}</td>
        <td class="num">${(r.rows || 0).toLocaleString()}</td><td class="num">${r.gaps ?? "—"}</td><td class="num">${r.missing != null ? r.missing.toLocaleString() : "—"}</td>
        <td>${r.lag_min != null ? `<span class="pill ${r.lag_min < 5 ? "up" : "down"}">${r.lag_min < 5 ? "live" : Math.round(r.lag_min) + " min behind"}</span>` : `<span class="muted">${r.last ? ago(r.last) : "—"}</span>`}</td>
        <td class="num muted">${r.size ? mb(r.size) : "—"}</td></tr>`).join("")}</tbody></table>
      <div class="note">Crypto gaps are counted 24/7 and are mostly real exchange outages (e.g. Binance maintenance). ETF 1m gaps are counted within each session — thin tickers like CSSPX.SW only have bars in minutes with trades.</div></div>`;
    el.querySelectorAll("tr[data-sym]").forEach((r) => r.addEventListener("click", () => (location.hash = "#/asset/" + encodeURIComponent(r.dataset.sym))));
  },
};

/* ============================================================== ROUTER === */
async function route() {
  const el = $("#app");
  const h = location.hash.replace(/^#\/?/, "");
  if (state.view?.unmount) state.view.unmount();
  let view, arg, tab;
  if (h.startsWith("asset/")) { view = assetView; arg = decodeURIComponent(h.slice(6)); tab = null; }
  else if (h === "portfolio") { view = portfolioView; tab = "portfolio"; }
  else if (h === "data") { view = dataView; tab = "data"; }
  else { view = overviewView; tab = "overview"; }
  document.querySelectorAll(".tabs a").forEach((a) => a.classList.toggle("active", a.dataset.tab === tab));
  state.view = view;
  window.scrollTo(0, 0);
  await view.mount(el, arg);
  document.title = (view === assetView && state.bySym[arg] ? `${base(arg)} $${fmtPrice(state.bySym[arg].price)} · ` : "") + "Markets · Homelab";
}

function startTimer() {
  clearInterval(state.timer);
  state.timer = setInterval(async () => {
    if (document.hidden || !state.view?.tick) return;
    await state.view.tick($("#app"));
    if (state.view === assetView && state.bySym[assetView.sym]) document.title = `${base(assetView.sym)} $${fmtPrice(state.bySym[assetView.sym].price)} · Markets · Homelab`;
  }, REFRESH_MS);
}

document.addEventListener("keydown", (e) => {
  if (e.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) { e.preventDefault(); $("#search").focus(); }
});
document.addEventListener("visibilitychange", () => { if (!document.hidden && state.view?.tick) state.view.tick($("#app")); });

attachSearch($("#search"), $("#search-results"), (a) => { $("#search").value = ""; $("#search").blur(); location.hash = "#/asset/" + encodeURIComponent(a.symbol); });
window.addEventListener("hashchange", route);
loadOverview().then(() => { route(); startTimer(); });
