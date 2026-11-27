/* Strategy leaderboard: reads /api/leaderboard (strategies/leaderboard.json) and draws the
   return/drawdown map, the ranking with its drawdown-versus-return bars, and the per-set winners. */
"use strict";

const $ = (s, el = document) => el.querySelector(s);
const PROFILES = { "max-income": "Max income", balanced: "Balanced", "safe-starter": "Safe starter" };
const CLASS_NAMES = { crypto: "coins", etf: "ETFs", stock: "stocks", mixed: "assets" };
const PAGE = 50;
const BEST_PAGE = 12;
const SVGNS = "http://www.w3.org/2000/svg";
const REPO = "https://github.com/47y27gc8w8-ops/trading/blob/main/";

const state = {
  all: [], byId: new Map(), byFile: new Map(), best: {}, front: new Set(),
  profile: "", cls: "", q: "", conf: false, long: false, onePer: false,
  sort: "conservative_yearly_pct", asc: false, showAll: false, bestAll: false, sel: null, L: 1, R: 1,
};

const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
/* a formatted value as an Anton figure, the unit small in the accent: "36.8%" -> 36.8 % */
const fig = (str, unit = "%") => str === "–" ? '<span class="fig">–</span>' : `<span class="fig">${esc(str.replace(/%$/, ""))}<small>${unit}</small></span>`;
const pct = (v, d = 1) => (v == null || Number.isNaN(v) ? "–" : `${v.toFixed(d)}%`);
const signed = (v, d = 1) => (v == null ? "–" : `${v > 0 ? "+" : ""}${v.toFixed(d)}%`);
const human = (s) => { const t = String(s).replace(/_/g, " "); return t.charAt(0).toUpperCase() + t.slice(1); };
const fmtDay = (d) => (d ? new Date(`${d}T00:00:00Z`).toLocaleDateString("en-GB", { day: "numeric", month: "short", timeZone: "UTC" }) : "–");
const fmtInt = (n) => (n == null ? "–" : n.toLocaleString("en-US"));
const clsOf = (e) => (e.classes.length > 1 ? "mixed" : e.classes[0] || "mixed");

function setLabel(e) {
  const n = e.symbols.length;
  const base = n <= 4 ? e.symbols.join(", ") : `Basket of ${n} ${CLASS_NAMES[clsOf(e)]}`;
  const tag = e.tag && !e.symbols.includes(e.tag) ? ` · ${e.tag}` : "";
  return base + tag;
}

/* ------------------------------------------------------------------ data --- */
async function load() {
  let data;
  try {
    const r = await fetch("/api/leaderboard");
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    data = await r.json();
  } catch (err) {
    $("#updated").textContent = "Could not load the leaderboard";
    $("#rank-body").innerHTML = `<tr><td class="l" colspan="12">${esc(err.message)}</td></tr>`;
    return;
  }
  for (const e of data.entries) {
    e.ratio = e.worst_max_dd_pct ? e.conservative_yearly_pct / Math.abs(e.worst_max_dd_pct) : null;
    e.cls = clsOf(e);
    e.label = setLabel(e);
    e.name = human(e.strategy);
    e.hay = `${e.strategy} ${e.name} ${e.tag || ""} ${e.symbols.join(" ")}`.toLowerCase();
    e.isLong = e.signal.long.length > 0;
    state.byId.set(e.id, e);
    if (e.variant_file) state.byFile.set(e.variant_file, e);
  }
  state.all = data.entries;
  state.best = data.best || {};
  state.L = Math.max(...state.all.map((e) => Math.abs(e.worst_max_dd_pct || 0)));
  state.R = Math.max(...state.all.map((e) => Math.max(0, e.conservative_yearly_pct || 0)));
  frontier();

  const g = data.generated ? new Date(data.generated) : null;
  if (g) $("#updated").textContent = `Rebuilt ${g.toLocaleString("en-GB", { day: "numeric", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit", timeZone: "UTC" })} UTC`;
  const strategies = new Set(state.all.map((e) => e.strategy)).size;
  $("#lede").innerHTML = `<b>${state.all.length} variants</b> of <b>${strategies} strategies</b> on <b>${Object.keys(state.best).length} symbol sets</b>, ranked by the worse of their in-sample and out-of-sample yearly return.`;

  const hv = new URLSearchParams(location.hash.slice(1)).get("v");
  const fromHash = hv == null ? null : Number(hv);
  readFilters();
  kpis();
  const rows = filtered();
  select(state.byId.get(fromHash) || rows[0] || state.all[0], false);
  render();
  renderBest();
}

/* variants nobody beats: no other variant earns more with a drawdown at least as shallow */
function frontier() {
  const pts = [...state.all].sort((a, b) => b.worst_max_dd_pct - a.worst_max_dd_pct || b.conservative_yearly_pct - a.conservative_yearly_pct);
  let best = -Infinity;
  for (const e of pts) if (e.conservative_yearly_pct > best) { best = e.conservative_yearly_pct; state.front.add(e.id); }
}

function filtered() {
  const q = state.q.trim().toLowerCase();
  let rows = state.all.filter((e) =>
    (!state.profile || e.profile === state.profile) &&
    (!state.cls || e.cls === state.cls) &&
    (!state.conf || !e.low_confidence) &&
    (!state.long || e.isLong) &&
    (!q || q.split(/\s+/).every((w) => e.hay.includes(w))));
  const k = state.sort, dir = state.asc ? 1 : -1;
  rows.sort((a, b) => ((a[k] ?? -Infinity) - (b[k] ?? -Infinity)) * dir || b.conservative_yearly_pct - a.conservative_yearly_pct);
  if (state.onePer) {
    const seen = new Set();
    rows = rows.filter((e) => (seen.has(e.strategy) ? false : seen.add(e.strategy)));
  }
  return rows;
}

/* ------------------------------------------------------------------ KPIs --- */
function kpis() {
  const top = [...state.all].sort((a, b) => b.conservative_yearly_pct - a.conservative_yearly_pct)[0];
  const above = state.all.filter((e) => e.conservative_yearly_pct >= 5).length;
  const tame = state.all.filter((e) => e.conservative_yearly_pct >= 5 && e.worst_max_dd_pct >= -25).length;
  const longs = state.all.filter((e) => e.isLong).length;
  const until = state.all.map((e) => e.signal.data_until).filter(Boolean).sort().pop() || "";
  const low = state.all.filter((e) => e.low_confidence).length;
  $("#kpis").innerHTML = `
    <div class="kpi lead"><div class="k">Top conservative return</div>
      <div class="v up">${fig(pct(top.conservative_yearly_pct))}<small class="per">a year</small></div>
      <button class="s" data-id="${top.id}">${esc(top.name)} · ${esc(top.label)} · DD ${pct(top.worst_max_dd_pct)}</button></div>
    <div class="kpi"><div class="k">At 5%/yr or more</div><div class="v">${above}</div><div class="s">${tame} with DD under 25%</div></div>
    <div class="kpi"><div class="k">On the frontier</div><div class="v">${state.front.size}</div><div class="s">unbeaten on both axes</div></div>
    <div class="kpi"><div class="k">In a position now</div><div class="v">${longs}</div><div class="s">signals as of ${esc(fmtDay(until))}</div></div>
    <div class="kpi"><div class="k">Low confidence</div><div class="v">${low}</div><div class="s">symbol pick may be luck</div></div>`;
  $("#kpis button.s").addEventListener("click", () => { select(top); scrollToDetail(); });
}

/* ------------------------------------------------------------------- map --- */
function drawMap(rows) {
  const box = $("#map");
  const W = box.clientWidth, H = box.clientHeight;
  if (!W || !H) return;
  const padL = 40, padR = 8, padT = 10, padB = 30;
  const xMin = -Math.ceil(state.L / 10) * 10, xMax = 0;
  const yMin = Math.min(0, Math.floor(Math.min(...state.all.map((e) => e.conservative_yearly_pct)) / 5) * 5);
  const yMax = Math.ceil(state.R / 5) * 5;
  const x = (v) => padL + ((v - xMin) / (xMax - xMin)) * (W - padL - padR);
  const y = (v) => padT + (1 - (v - yMin) / (yMax - yMin)) * (H - padT - padB);
  const shown = new Set(rows.map((e) => e.id));

  let g = `<g class="grid">`;
  for (let v = xMin; v <= 0; v += 10) g += `<line x1="${x(v)}" x2="${x(v)}" y1="${padT}" y2="${H - padB}" class="${v === 0 ? "zero" : ""}"/>`;
  for (let v = yMin; v <= yMax; v += 5) g += `<line x1="${padL}" x2="${W - padR}" y1="${y(v)}" y2="${y(v)}" class="${v === 0 ? "zero" : ""}"/>`;
  g += `</g><g class="ax">`;
  for (let v = xMin; v <= 0; v += 10) g += `<text x="${x(v)}" y="${H - padB + 18}" text-anchor="middle">${v}%</text>`;
  for (let v = yMin; v <= yMax; v += 5) g += `<text x="${padL - 8}" y="${y(v) + 4}" text-anchor="end">${v}%</text>`;
  g += `<text class="t" x="${W - padR}" y="${y(yMax) + 14}" text-anchor="end">%/yr, worse of both periods ↑</text>`;
  g += `<text class="t" x="${x(xMin)}" y="${H - padB - 8}" text-anchor="start">← deeper worst drawdown</text></g>`;

  const fr = state.all.filter((e) => state.front.has(e.id)).sort((a, b) => b.worst_max_dd_pct - a.worst_max_dd_pct);
  let path = "";
  fr.forEach((e, i) => {
    const px = x(e.worst_max_dd_pct), py = y(e.conservative_yearly_pct);
    path += i ? `H${px.toFixed(1)}V${py.toFixed(1)}` : `M${x(0).toFixed(1)},${py.toFixed(1)}H${px.toFixed(1)}`;
  });
  // draw grey first, frontier on top
  const order = [...state.all].sort((a, b) => state.front.has(a.id) - state.front.has(b.id));
  let dots = "";
  for (const e of order) {
    const f = state.front.has(e.id) ? " f" : "";
    const off = shown.has(e.id) ? "" : " off";
    dots += `<circle class="d${f}${off}" data-id="${e.id}" cx="${x(e.worst_max_dd_pct).toFixed(1)}" cy="${y(e.conservative_yearly_pct).toFixed(1)}" r="${f ? 4.5 : 3.5}"/>`;
  }
  const s = state.sel;
  const sel = s ? `<circle class="sel" cx="${x(s.worst_max_dd_pct)}" cy="${y(s.conservative_yearly_pct)}" r="9"/>` : "";
  box.innerHTML = `<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">${g}<path class="front" d="${path}"/>${dots}${sel}<circle class="hov" r="0"/></svg>`;
  box._scale = { x, y };
}

function mapEvents() {
  const box = $("#map");
  const read = $("#map-read");
  const show = (e) => {
    read.innerHTML = e ? `<b>${esc(e.name)}</b> · ${esc(e.label)} · ${pct(e.conservative_yearly_pct)}/yr · DD ${pct(e.worst_max_dd_pct)}` : "";
  };
  box.addEventListener("pointerover", (ev) => {
    const id = ev.target.dataset && ev.target.dataset.id;
    if (id != null) show(state.byId.get(Number(id)));
  });
  box.addEventListener("pointerleave", () => show(null));
  box.addEventListener("click", (ev) => {
    const id = ev.target.dataset && ev.target.dataset.id;
    if (id != null) { select(state.byId.get(Number(id))); render(); }
  });
  new ResizeObserver(() => drawMap(filtered())).observe(box);
}

/* --------------------------------------------------------------- ranking --- */
function bar(e, i) {
  const span = state.L + state.R;
  const z = (state.L / span) * 100;
  const dd = (Math.abs(e.worst_max_dd_pct || 0) / span) * 100;
  const rt = (Math.max(0, e.conservative_yearly_pct || 0) / span) * 100;
  return `<div class="dv" style="--z:${z.toFixed(2)}%"><i class="dd" style="width:${dd.toFixed(2)}%;--dl:${Math.min(i, 20) * 25}ms"></i><i class="rt" style="width:${rt.toFixed(2)}%;--dl:${Math.min(i, 20) * 25 + 80}ms"></i></div>`;
}

function render() {
  const rows = filtered();
  $("#rank-count").textContent = rows.length === state.all.length ? `${rows.length}` : `${rows.length} of ${state.all.length}`;
  const list = state.showAll ? rows : rows.slice(0, PAGE);
  const body = $("#rank-body");
  if (!rows.length) {
    body.innerHTML = `<tr><td class="l" colspan="12"><span class="muted">No variant matches these filters.</span></td></tr>`;
  } else {
    body.innerHTML = list.map((e, i) => {
      const n = e.signal.long.length;
      const now = n ? (n === 1 && e.symbols.length === 1 ? `Long since ${e.signal.long[0].since}` : `Long ${n} of ${e.symbols.length}`) : "Flat";
      return `<tr data-id="${e.id}" class="${state.sel && state.sel.id === e.id ? "sel" : ""}" tabindex="0" aria-label="${esc(e.name)}, ${esc(e.label)}">
        <td class="l rk${i < 3 && state.sort === "conservative_yearly_pct" && !state.asc ? " top" : ""}">${i + 1}</td>
        <td class="l"><div class="nm">${esc(e.name)}</div><div class="set">${esc(e.label)}${e.low_confidence ? ' · <span class="lc">low confidence</span>' : ""}</div></td>
        <td class="l prof hide-md">${PROFILES[e.profile] || esc(e.profile)}</td>
        <td class="bar">${bar(e, i)}</td>
        <td class="fig up">${pct(e.conservative_yearly_pct)}</td>
        <td class="fig down hide-sm">${pct(e.worst_max_dd_pct)}</td>
        <td class="hide-md">${pct(e.is_yearly_pct)}</td>
        <td class="hide-md">${pct(e.oos_yearly_pct)}</td>
        <td class="hide-lg">${pct(e.oos_win_rate, 0)}</td>
        <td class="hide-lg">${fmtInt(e.oos_trades)}</td>
        <td class="hide-md">${e.ratio == null ? "–" : e.ratio.toFixed(2)}</td>
        <td class="l hide-sm"><span class="now${n ? " long" : ""}">${now}</span></td></tr>`;
    }).join("");
    body.querySelectorAll("tr").forEach((tr, i) => { if (i < 24) { tr.classList.add("enter"); tr.style.setProperty("--dl", `${i * 22}ms`); } });
  }
  const more = $("#more");
  more.hidden = rows.length <= PAGE;
  more.textContent = state.showAll ? `Show the top ${PAGE}` : `Show all ${rows.length}`;
  document.querySelectorAll("#rank th[data-k]").forEach((th) => {
    const on = th.dataset.k === state.sort && !th.classList.contains("bar-h");
    th.classList.toggle("sorted", on);
    th.classList.toggle("asc", on && state.asc);
    th.setAttribute("aria-sort", on ? (state.asc ? "ascending" : "descending") : "none");
  });
  drawMap(rows);
  $("#map-sub").textContent = rows.length === state.all.length
    ? "Each dot is one variant. Up is more return, left is a deeper loss."
    : `${rows.length} variants match the filters; the rest are dimmed.`;
}

/* ---------------------------------------------------------------- detail --- */
function select(e, push = true) {
  if (!e) return;
  state.sel = e;
  if (push) history.replaceState(null, "", `#v=${e.id}`);
  document.querySelectorAll("#rank-body tr").forEach((tr) => tr.classList.toggle("sel", Number(tr.dataset.id) === e.id));
  drawMap(filtered());
  const max = Math.max(Math.abs(e.is_yearly_pct || 0), Math.abs(e.oos_yearly_pct || 0), Math.abs(e.worst_max_dd_pct || 0), 1);
  const b = (label, v) => `<div class="d-bar"><span>${label}</span><span class="tr"><i class="${v < 0 ? "neg" : ""}" style="width:${(Math.abs(v || 0) / max * 100).toFixed(1)}%"></i></span><b>${pct(v)}</b></div>`;
  const params = Object.entries(e.params || {}).map(([k, v]) => `<dt>${esc(k.replace(/_/g, " "))}</dt><dd>${esc(typeof v === "object" ? JSON.stringify(v) : v)}</dd>`).join("");
  const longs = e.signal.long;
  const sig = longs.length
    ? longs.slice(0, 12).map((l) => `<span class="chip long"><b>${esc(l.symbol)}</b> since ${esc(l.since)}</span>`).join("") + (longs.length > 12 ? `<span class="chip">+${longs.length - 12} more</span>` : "")
    : `<span class="chip">Flat, no open position</span>`;
  const period = e.oos_period ? `${e.oos_period[0]} to ${e.oos_period[1]}` : "–";
  $("#detail .detail-body").innerHTML = `
    <div><p class="d-name">${esc(e.name)}</p><p class="d-set">${esc(e.label)} · ${PROFILES[e.profile] || esc(e.profile)}</p></div>
    ${e.low_confidence ? `<p class="warn">Low confidence: this symbol topped a screen whose ranking didn't hold up in-sample, so it may have been picked by luck. The strategy's broad basket is the safer read.</p>` : ""}
    <div class="d-figs">
      <div class="d-main"><div class="v up">${fig(pct(e.conservative_yearly_pct))}</div><div class="k">a year, worse period</div></div>
      <div><div class="v down">${fig(pct(e.worst_max_dd_pct))}</div><div class="k">worst drawdown</div></div>
    </div>
    <div class="d-bars">${b("In-sample", e.is_yearly_pct)}${b("Out-of-sample", e.oos_yearly_pct)}${b("Largest loss", e.largest_loss_pct)}</div>
    <dl class="facts">
      <dt>Win rate, in / out</dt><dd>${pct(e.is_win_rate, 0)} / ${pct(e.oos_win_rate, 0)}</dd>
      <dt>Trades, in / out</dt><dd>${fmtInt(e.is_trades)} / ${fmtInt(e.oos_trades)}</dd>
      <dt>Out-of-sample efficiency</dt><dd>${e.oos_efficiency == null ? "–" : e.oos_efficiency.toFixed(2)}</dd>
      <dt>Size for a 10% drawdown</dt><dd>${pct(e.position_pct_for_10pct_dd, 0)} of equity</dd>
      <dt>Out-of-sample period</dt><dd>${esc(period)}</dd>
    </dl>
    <div><h3 class="d-h">Signal now${e.signal.data_until ? `, data to ${esc(e.signal.data_until)}` : ""}</h3><div class="signal">${sig}</div></div>
    ${params ? `<div><h3 class="d-h">Parameters</h3><dl class="facts">${params}</dl></div>` : ""}
    ${e.variant_file ? `<a class="d-link" href="${REPO}${esc(e.variant_file)}" target="_blank" rel="noopener">Open the variant file on GitHub</a>` : ""}`;
}

function scrollToDetail() {
  if (window.matchMedia("(max-width: 1099px)").matches) $("#detail").scrollIntoView({ behavior: "smooth", block: "start" });
}

/* ------------------------------------------------------------ best per set --- */
function renderBest() {
  const rows = Object.entries(state.best).map(([set, profs]) => {
    const cells = ["max-income", "balanced", "safe-starter"].map((p) => (profs[p] ? state.byFile.get(profs[p].variant_file) : null));
    const top = Math.max(...cells.filter(Boolean).map((e) => e.conservative_yearly_pct));
    return { set, cells, top };
  }).sort((a, b) => b.top - a.top);
  const list = state.bestAll ? rows : rows.slice(0, BEST_PAGE);
  $("#best-body").innerHTML = list.map((r) => `<tr>
      <td class="l">${esc(r.set)}</td>
      ${r.cells.map((e, i) => {
        const p = Object.values(PROFILES)[i];
        if (!e) return `<td class="l blank" data-p="${p}"><span class="empty">–</span></td>`;
        return `<td class="l" data-p="${p}" data-id="${e.id}"><span class="cell"><span class="nm">${esc(e.name)}</span><span class="f"><b>${pct(e.conservative_yearly_pct)}</b>/yr · DD <em>${pct(e.worst_max_dd_pct)}</em>${e.low_confidence ? " · low confidence" : ""}</span></span></td>`;
      }).join("")}</tr>`).join("");
  const more = $("#best-more");
  more.hidden = rows.length <= BEST_PAGE;
  more.textContent = state.bestAll ? `Show the top ${BEST_PAGE}` : `Show all ${rows.length}`;
}

/* -------------------------------------------------------------- controls --- */
function readFilters() {
  state.conf = $("#f-conf").checked;
  state.long = $("#f-long").checked;
  state.onePer = $("#f-best").checked;
}

function wire() {
  for (const [id, key] of [["#f-profile", "profile"], ["#f-class", "cls"]]) {
    $(id).addEventListener("click", (ev) => {
      const btn = ev.target.closest("button");
      if (!btn) return;
      $(id).querySelectorAll("button").forEach((b) => b.classList.toggle("on", b === btn));
      state[key] = btn.dataset.v;
      render();
    });
  }
  for (const id of ["#f-conf", "#f-long", "#f-best"]) $(id).addEventListener("change", () => { readFilters(); render(); });
  let t;
  $("#q").addEventListener("input", (ev) => { clearTimeout(t); t = setTimeout(() => { state.q = ev.target.value; render(); }, 120); });
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "/" && document.activeElement !== $("#q")) { ev.preventDefault(); $("#q").focus(); }
  });
  document.querySelectorAll("#rank th[data-k] button").forEach((b) => b.addEventListener("click", () => {
    const k = b.closest("th").dataset.k;
    if (state.sort === k) state.asc = !state.asc; else { state.sort = k; state.asc = false; }
    render();
  }));
  const pick = (ev) => {
    const el = ev.target.closest("[data-id]");
    if (!el) return;
    select(state.byId.get(Number(el.dataset.id)));
    scrollToDetail();
  };
  $("#rank-body").addEventListener("click", pick);
  $("#rank-body").addEventListener("keydown", (ev) => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); pick(ev); } });
  $("#best-body").addEventListener("click", pick);
  $("#more").addEventListener("click", () => { state.showAll = !state.showAll; render(); });
  $("#best-more").addEventListener("click", () => { state.bestAll = !state.bestAll; renderBest(); });
  mapEvents();
}

wire();
load();
