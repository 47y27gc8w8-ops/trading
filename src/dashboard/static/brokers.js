/* Paper brokers: /api/brokers (bots), /api/brokers/equity (curves), /api/brokers/trades and
   /api/system (psutil, every 5 s). Read-only: this page never trades. */
"use strict";

const $ = (s, el = document) => el.querySelector(s);
const SVGNS = "http://www.w3.org/2000/svg";
const SYS_MS = 5000, BOTS_MS = 30000, CURVES_MS = 300000;
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const chf = (v, d = 2) => (v == null ? "–" : v.toLocaleString("de-CH", { minimumFractionDigits: d, maximumFractionDigits: d }));
const sgn = (v, d = 2) => (v == null ? "–" : `${v > 0 ? "+" : v < 0 ? "−" : ""}${chf(Math.abs(v), d)}`);
const pct = (v, d = 2) => (v == null ? "–" : `${v > 0 ? "+" : v < 0 ? "−" : ""}${Math.abs(v).toFixed(d)}%`);
const cls = (v) => (v > 0 ? "up" : v < 0 ? "down" : "");
const human = (s) => { const t = String(s).replace(/_/g, " "); return t.charAt(0).toUpperCase() + t.slice(1); };
const bytes = (b) => { const u = ["B", "KB", "MB", "GB", "TB"]; let i = 0; while (b >= 1024 && i < 4) { b /= 1024; i++; } return `${b.toFixed(b >= 100 || i < 2 ? 0 : 1)} ${u[i]}`; };
const ago = (iso) => {
  if (!iso) return "–";
  const s = (Date.now() - Date.parse(iso)) / 1000;
  if (s < 90) return "just now";
  if (s < 3600) return `${Math.round(s / 60)} min ago`;
  if (s < 86400 * 2) return `${Math.round(s / 3600)} h ago`;
  return `${Math.round(s / 86400)} days ago`;
};
const when = (iso) => new Date(iso).toLocaleString("en-GB", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
const symShort = (s) => s.replace(/USDT$/, "");

const state = { bots: [], range: "all", cpuHist: [] };

/* -------------------------------------------------------------- system --- */
function meter(k, right, v, unit, frac, sub, extra = "") {
  const lvl = frac >= 0.9 ? "crit" : frac >= 0.75 ? "hot" : "";
  return `<div class="meter"><div class="k"><span>${k}</span><span>${right}</span></div>
    <div class="v">${v}<small>${unit}</small></div>
    <div class="bar" role="meter" aria-label="${k}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(frac * 100)}"><i class="${lvl}" style="width:${(frac * 100).toFixed(1)}%"></i></div>
    <div class="s">${sub}</div>${extra}</div>`;
}

function spark(vals) {
  if (vals.length < 2) return "";
  const w = 300, h = 34, n = vals.length;
  const pts = vals.map((v, i) => `${((i / (n - 1)) * w).toFixed(1)},${(h - (Math.min(100, v) / 100) * h).toFixed(1)}`);
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true">
    <path class="area" d="M0,${h} L${pts.join(" L")} L${w},${h} Z"/><path d="M${pts.join(" L")}"/></svg>`;
}

async function loadSystem() {
  try {
    const r = await fetch("/api/system");
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    const s = await r.json();
    state.cpuHist.push(s.cpu_pct);
    if (state.cpuHist.length > 60) state.cpuHist.shift();
    const up = s.uptime_s, days = Math.floor(up / 86400), hrs = Math.floor((up % 86400) / 3600);
    $("#meters").innerHTML =
      meter("CPU", `${s.cpu_count} cores`, s.cpu_pct.toFixed(0), "%", s.cpu_pct / 100,
        `Load ${s.load.map((x) => x.toFixed(2)).join(" · ")}`, spark(state.cpuHist)) +
      meter("Memory", bytes(s.mem_total), s.mem_pct.toFixed(0), "%", s.mem_pct / 100,
        `${bytes(s.mem_used)} used${s.swap_total ? ` · swap ${bytes(s.swap_used)}` : ""}`) +
      meter("Disk", bytes(s.disk_total), s.disk_pct.toFixed(0), "%", s.disk_pct / 100,
        `${bytes(s.disk_used)} used · ${bytes(s.disk_total - s.disk_used)} free`) +
      `<div class="meter facts"><div class="k"><span>Host</span><span>h0melab</span></div><dl>
        <dt>Uptime</dt><dd>${days} d ${hrs} h</dd>
        <dt>Temperature</dt><dd>${s.temp_c != null ? `${s.temp_c.toFixed(0)} °C` : "–"}</dd>
        <dt>Bots running</dt><dd>${state.bots.filter((b) => b.status === "running" || b.status === "idle").length} / ${state.bots.length || "–"}</dd>
        <dt>Updated</dt><dd>${new Date(s.ts).toLocaleTimeString("en-GB")}</dd></dl></div>`;
    $("#sys-sub").textContent = "CPU, memory and disk, refreshed every 5 seconds.";
  } catch (err) {
    $("#sys-sub").textContent = `System stats unavailable: ${err.message}`;
  }
}

/* ---------------------------------------------------------------- bots --- */
function renderKpis(bots) {
  const eq = bots.reduce((a, b) => a + b.equity, 0);
  const start = bots.reduce((a, b) => a + b.start_balance, 0);
  const day = bots.reduce((a, b) => a + b.pnl_day, 0);
  const ok = bots.filter((b) => b.status === "running" || b.status === "idle").length;
  const trades = bots.reduce((a, b) => a + b.trades, 0);
  const best = [...bots].sort((a, b) => b.pnl_total_pct - a.pnl_total_pct)[0];
  $("#kpis").innerHTML = `
    <div class="kpi lead"><div class="k">All bots · equity</div><div class="v">${chf(eq, 0)}<span class="per">CHF</span></div>
      <div class="s">from ${chf(start, 0)} CHF paper money</div></div>
    <div class="kpi"><div class="k">Since start</div><div class="v ${cls(eq - start)}">${pct(start ? (eq / start - 1) * 100 : 0)}</div><div class="s">${sgn(eq - start)} CHF</div></div>
    <div class="kpi"><div class="k">Last 24 h</div><div class="v ${cls(day)}">${sgn(day, 0)}</div><div class="s">CHF across all bots</div></div>
    <div class="kpi"><div class="k">Bots up</div><div class="v">${ok}<span style="font-size:.5em;color:var(--muted)"> / ${bots.length}</span></div><div class="s">${bots.filter((b) => b.status === "idle").length} idle (market closed)</div></div>
    <div class="kpi"><div class="k">Paper trades</div><div class="v">${trades}</div><div class="s">${best ? `best: ${esc(best.id)} ${pct(best.pnl_total_pct)}` : ""}</div></div>`;
}

function renderBots(bots) {
  $("#bots-count").textContent = bots.length;
  $("#bots-body").innerHTML = bots.map((b) => {
    const pos = b.positions.length
      ? `<div class="pos">${b.positions.slice(0, 6).map((p) => `<span class="chip" title="${esc(p.symbol)}: ${chf(p.value)} CHF, ${sgn(p.pnl)} CHF"><b>${esc(symShort(p.symbol))}</b> ${chf(p.value, 0)}</span>`).join("")}${b.positions.length > 6 ? `<span class="chip">+${b.positions.length - 6}</span>` : ""}</div>`
      : '<span class="muted">Flat</span>';
    const t = b.last_trade;
    const lt = t ? `<div class="lt"><span class="${t.side}">${t.side === "buy" ? "Bought" : "Sold"}</span> <b>${esc(symShort(t.symbol))}</b> · ${chf(t.notional, 0)} CHF${t.pnl != null ? ` · <span class="${cls(t.pnl)}">${sgn(t.pnl)}</span>` : ""}<br>${ago(t.ts)}</div>` : '<span class="muted">No trades yet</span>';
    const set = b.symbols.length <= 3 ? b.symbols.map(symShort).join(", ") : `${b.symbols.length} ${b.asset_class === "crypto" ? "coins" : "ETFs"}`;
    return `<tr>
      <td class="l"><span class="nm">${esc(b.id)}</span><small class="p">${esc(human(b.strategy))} · ${esc(set)} · ${esc(b.timeframe)}</small></td>
      <td class="l"><span class="st ${esc(b.status)}"><i></i>${esc(b.status)}</span><span class="st-msg" title="${esc(b.message)}">${b.status === "down" ? `no heartbeat ${ago(b.heartbeat)}` : esc(b.message || "")}</span></td>
      <td><b>${chf(b.equity)}</b></td>
      <td><span class="${cls(b.pnl_day)}">${sgn(b.pnl_day)}</span><small class="p">${pct(b.pnl_day_pct)}</small></td>
      <td><span class="${cls(b.pnl_total)}">${sgn(b.pnl_total)}</span><small class="p">${pct(b.pnl_total_pct)}</small></td>
      <td class="hide-sm"><span class="${b.max_dd_pct < 0 ? "down" : ""}">${b.max_dd_pct.toFixed(2)}%</span>${b.errors_24h ? `<small class="p down">${b.errors_24h} errors 24 h</small>` : ""}</td>
      <td class="l hide-md">${pos}</td>
      <td class="l hide-sm">${lt}</td></tr>`;
  }).join("") || '<tr><td class="l" colspan="8">No bots in the database yet.</td></tr>';
}

/* -------------------------------------------------------------- curves --- */
function curveSvg(pts, start) {
  const w = 300, h = 120, padL = 0, padR = 40;
  const vals = pts.map((p) => p[1]);
  let lo = Math.min(start, ...vals), hi = Math.max(start, ...vals);
  if (hi - lo < start * 0.002) { lo -= start * 0.001; hi += start * 0.001; }
  const t0 = pts[0][0], t1 = pts[pts.length - 1][0] || t0 + 1;
  const x = (t) => padL + ((t - t0) / Math.max(1, t1 - t0)) * (w - padL - padR);
  const y = (v) => 6 + (1 - (v - lo) / (hi - lo)) * (h - 18);
  const last = vals[vals.length - 1];
  const dir = last >= start ? "up" : "down";
  const line = pts.map((p) => `${x(p[0]).toFixed(1)},${y(p[1]).toFixed(1)}`).join(" L");
  const yb = y(start).toFixed(1);
  return `<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="Equity from ${chf(vals[0], 0)} to ${chf(last, 0)} CHF">
    <line class="base" x1="0" x2="${w - padR}" y1="${yb}" y2="${yb}"/>
    <path class="ar ${dir}" d="M${x(pts[0][0]).toFixed(1)},${yb} L${line} L${x(t1).toFixed(1)},${yb} Z"/>
    <path class="ln ${dir}" d="M${line}"/>
    <text x="${w - padR + 4}" y="${(+yb + 3).toFixed(1)}">${chf(start, 0)}</text>
    <text x="${w - padR + 4}" y="10">${chf(hi, 0)}</text>
    <text x="${w - padR + 4}" y="${h - 4}">${chf(lo, 0)}</text>
    <line class="hl" x1="0" x2="0" y1="0" y2="${h - 12}" visibility="hidden"/><circle class="hd-dot" r="3" visibility="hidden"/>
  </svg>`;
}

function attachHover(card, pts, start) {
  const svg = card.querySelector("svg");
  if (!svg) return;
  const read = card.querySelector(".read");
  const w = 300, h = 120, padR = 40;
  const vals = pts.map((p) => p[1]);
  let lo = Math.min(start, ...vals), hi = Math.max(start, ...vals);
  if (hi - lo < start * 0.002) { lo -= start * 0.001; hi += start * 0.001; }
  const t0 = pts[0][0], t1 = pts[pts.length - 1][0] || t0 + 1;
  const hl = svg.querySelector(".hl"), dot = svg.querySelector(".hd-dot");
  const move = (ev) => {
    const r = svg.getBoundingClientRect();
    const fx = Math.max(0, Math.min(1, (ev.clientX - r.left) / (r.width * (w - padR) / w)));
    const t = t0 + fx * (t1 - t0);
    let i = 0; while (i < pts.length - 1 && pts[i + 1][0] <= t) i++;
    const p = pts[i];
    const px = ((p[0] - t0) / Math.max(1, t1 - t0)) * (w - padR), py = 6 + (1 - (p[1] - lo) / (hi - lo)) * (h - 18);
    hl.setAttribute("x1", px); hl.setAttribute("x2", px); hl.setAttribute("visibility", "visible");
    dot.setAttribute("cx", px); dot.setAttribute("cy", py); dot.setAttribute("visibility", "visible");
    read.textContent = `${when(p[0] * 1000)} · ${chf(p[1])} CHF (${pct((p[1] / start - 1) * 100)})`;
  };
  svg.addEventListener("pointermove", move);
  svg.addEventListener("pointerleave", () => { hl.setAttribute("visibility", "hidden"); dot.setAttribute("visibility", "hidden"); read.textContent = ""; });
}

async function loadCurves() {
  try {
    const r = await fetch(`/api/brokers/equity?range=${state.range}`);
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    const { curves } = await r.json();
    const box = $("#curves");
    box.innerHTML = "";
    for (const b of state.bots) {
      const pts = curves[b.id] || [];
      const card = document.createElement("article");
      card.className = "curve";
      const first = pts.length ? pts[0][1] : b.start_balance;
      card.innerHTML = `<div class="hd"><span class="nm">${esc(b.id)}</span><span class="eq">${chf(b.equity, 0)}<small>CHF</small></span></div>
        <div class="sub2"><span>${esc(human(b.strategy))}</span><span class="${cls(b.equity - first)}">${pct(first ? (b.equity / first - 1) * 100 : 0)} in range</span></div>
        ${pts.length >= 2 ? curveSvg(pts, b.start_balance) : '<div class="empty">Not enough history yet</div>'}
        <div class="read" aria-live="polite"></div>`;
      box.appendChild(card);
      if (pts.length >= 2) attachHover(card, pts, b.start_balance);
    }
  } catch (err) {
    $("#curves").innerHTML = `<p class="muted">Could not load equity curves: ${esc(err.message)}</p>`;
  }
}

async function loadTrades() {
  try {
    const r = await fetch("/api/brokers/trades?limit=25");
    if (!r.ok) throw new Error(r.statusText);
    const { trades } = await r.json();
    $("#trades-body").innerHTML = trades.map((t) => `<tr>
      <td class="l">${when(t.ts)}</td><td class="l">${esc(t.bot_id)}</td>
      <td class="l"><span class="${t.side === "buy" ? "up" : "down"}"><b>${t.side === "buy" ? "Buy" : "Sell"}</b></span> ${Number(t.qty.toPrecision(6))} ${esc(symShort(t.symbol))}</td>
      <td>${t.price_usd.toPrecision(6)}</td><td>${chf(t.notional)}</td><td class="hide-sm">${chf(t.fee)}</td>
      <td>${t.pnl == null ? '<span class="muted">–</span>' : `<span class="${cls(t.pnl)}">${sgn(t.pnl)}</span>`}</td>
      <td class="l hide-md"><div class="why" title="${esc(t.reason)}">${esc(t.reason)}</div></td></tr>`).join("")
      || '<tr><td class="l" colspan="8">No paper trades yet.</td></tr>';
  } catch (err) {
    $("#trades-body").innerHTML = `<tr><td class="l" colspan="8">${esc(err.message)}</td></tr>`;
  }
}

async function loadBots() {
  try {
    const r = await fetch("/api/brokers");
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    const data = await r.json();
    state.bots = data.bots;
    renderKpis(data.bots);
    renderBots(data.bots);
    const up = data.bots.filter((b) => b.status === "running" || b.status === "idle").length;
    $("#live").className = `live ${up === data.bots.length ? "ok" : "err"}`;
    $("#live-text").textContent = `${up}/${data.bots.length} bots up`;
    $("#updated").textContent = `Updated ${new Date(data.generated).toLocaleTimeString("en-GB")}`;
    if (!state.curvesAt || Date.now() - state.curvesAt > CURVES_MS) { state.curvesAt = Date.now(); loadCurves(); }
    await loadTrades();
  } catch (err) {
    $("#updated").textContent = "Could not load the bots";
    $("#live-text").textContent = "Offline";
    $("#bots-body").innerHTML = `<tr><td class="l" colspan="8">${esc(err.message)}</td></tr>`;
  }
}

$("#range").addEventListener("click", (ev) => {
  const b = ev.target.closest("button");
  if (!b) return;
  for (const x of $("#range").querySelectorAll("button")) x.classList.toggle("on", x === b);
  state.range = b.dataset.v;
  loadCurves();
});

loadBots().then(loadSystem);
setInterval(loadSystem, SYS_MS);
setInterval(() => { if (!document.hidden) loadBots(); }, BOTS_MS);
