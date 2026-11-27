/* Accent switcher shared by the SPA and /leaderboard. Loaded in <head> (not deferred) so the stored
   colour is on <html> before the first paint. Fills every [data-swatches] box with four buttons, keeps
   the choice in localStorage and follows other tabs through the storage event. Fires "accentchange" on
   window with the new hex, so charts can recolour without reloading. */
(function () {
  "use strict";
  var KEY = "accent";
  var COLORS = [
    ["amber", "Amber", "#F5A524"],
    ["sky", "Sky", "#3FA9FF"],
    ["lilac", "Lilac", "#A99AF0"],
    ["clay", "Clay", "#E08C84"],
  ];
  var hex = function (id) { for (var i = 0; i < COLORS.length; i++) if (COLORS[i][0] === id) return COLORS[i][2]; return COLORS[0][2]; };
  var valid = function (id) { return COLORS.some(function (c) { return c[0] === id; }); };
  var read = function () { try { var v = localStorage.getItem(KEY); return valid(v) ? v : "amber"; } catch (e) { return "amber"; } };

  function apply(id, announce) {
    var root = document.documentElement;
    if (id === "amber") root.removeAttribute("data-color"); else root.setAttribute("data-color", id);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", "#000000");
    document.querySelectorAll("[data-swatches] button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.c === id)); });
    if (announce) window.dispatchEvent(new CustomEvent("accentchange", { detail: { id: id, hex: hex(id) } }));
  }

  function build() {
    document.querySelectorAll("[data-swatches]").forEach(function (box) {
      if (box.childElementCount) return;
      box.setAttribute("role", "group");
      box.setAttribute("aria-label", "Accent colour");
      box.innerHTML = COLORS.map(function (c) {
        return '<button type="button" data-c="' + c[0] + '" style="--c:' + c[2] + '" title="' + c[1] + '" aria-label="' + c[1] + ' accent"></button>';
      }).join("");
      box.addEventListener("click", function (e) {
        var b = e.target.closest("button[data-c]");
        if (!b) return;
        try { localStorage.setItem(KEY, b.dataset.c); } catch (err) {}
        apply(b.dataset.c, true);
      });
    });
    apply(read(), false);
  }

  window.ARCO = { accent: function () { return hex(read()); }, current: read };
  apply(read(), false);
  window.addEventListener("storage", function (e) { if (e.key === KEY) apply(read(), true); });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build); else build();
})();
