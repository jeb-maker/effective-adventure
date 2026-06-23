const state = {
  meta: null,
  segments: [],
  offset: 0,
  limit: 40,
  total: 0,
  debounce: null,
};

const els = {
  globalStats: document.getElementById("global-stats"),
  filterQ: document.getElementById("filter-q"),
  filterCategory: document.getElementById("filter-category"),
  filterSegment: document.getElementById("filter-segment"),
  filterPricing: document.getElementById("filter-pricing"),
  filterTarget: document.getElementById("filter-target"),
  filterVerification: document.getElementById("filter-verification"),
  filterFrance: document.getElementById("filter-france"),
  filterHq: document.getElementById("filter-hq"),
  resetFilters: document.getElementById("reset-filters"),
  segmentChart: document.getElementById("segment-chart"),
  vendorList: document.getElementById("vendor-list"),
  resultsCount: document.getElementById("results-count"),
  pageInfo: document.getElementById("page-info"),
  prevPage: document.getElementById("prev-page"),
  nextPage: document.getElementById("next-page"),
  ragMode: document.getElementById("rag-mode"),
  ragMessages: document.getElementById("rag-messages"),
  ragForm: document.getElementById("rag-form"),
  ragInput: document.getElementById("rag-input"),
};

async function fetchJson(url, options) {
  const res = await fetch(url, options);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || res.statusText);
  }
  return res.json();
}

function fillSelect(select, values, formatter = (v) => v) {
  values.forEach((value) => {
    const opt = document.createElement("option");
    opt.value = value;
    opt.textContent = formatter(value);
    select.appendChild(opt);
  });
}

function renderStats(meta) {
  els.globalStats.innerHTML = [
  { label: "Vendeurs", value: meta.vendor_count },
  { label: "Segments", value: meta.segment_count },
  { label: "Gelés", value: meta.frozen_segment_count },
  { label: "Idées liées", value: meta.idea_count },
  ].map(
    (item) =>
      `<div class="stat-card"><strong>${item.value}</strong><span>${item.label}</span></div>`
  ).join("");
}

function renderSegmentChart(segments) {
  const top = [...segments].sort((a, b) => b.count - a.count).slice(0, 12);
  const max = Math.max(...top.map((s) => s.count), 1);
  els.segmentChart.innerHTML = top.map((seg) => `
    <div class="chart-row" title="${seg.label}">
      <span class="chart-label">${seg.label}</span>
      <div class="chart-bar"><span style="width:${(seg.count / max) * 100}%"></span></div>
      <span>${seg.count}</span>
    </div>
  `).join("");
}

function tag(text, className = "") {
  return `<span class="tag ${className}">${text}</span>`;
}

function renderVendorCard(vendor) {
  const segments = (vendor.segment_labels || []).map((s) => tag(s, "accent")).join("");
  const flags = [
    vendor.pricing_model ? tag(vendor.pricing_model) : "",
    vendor.target_market ? tag(vendor.target_market) : "",
    vendor.verification_status ? tag(vendor.verification_status, vendor.verification_status === "verified" ? "accent" : "warn") : "",
    vendor.hq_country ? tag(`HQ ${vendor.hq_country}`) : "",
    vendor.france_market ? tag(`FR ${vendor.france_market}`) : "",
    vendor.frozen_segment ? tag("segment gelé", "frozen") : "",
  ].join("");

  return `
    <article class="vendor-card">
      <header>
        <h3><a href="${vendor.url}" target="_blank" rel="noopener">${vendor.name}</a></h3>
      </header>
      <p>${vendor.description}</p>
      <div class="tags">${segments}${flags}</div>
    </article>
  `;
}

function currentFilters() {
  return {
    q: els.filterQ.value.trim(),
    category: els.filterCategory.value,
    segment: els.filterSegment.value,
    pricing_model: els.filterPricing.value,
    target_market: els.filterTarget.value,
    verification_status: els.filterVerification.value,
    france_market: els.filterFrance.value,
    hq_country: els.filterHq.value.trim().toUpperCase(),
  };
}

function filtersToQuery(filters, offset) {
  const params = new URLSearchParams();
  Object.entries(filters).forEach(([key, value]) => {
    if (value) params.set(key, value);
  });
  params.set("limit", String(state.limit));
  params.set("offset", String(offset));
  return params.toString();
}

async function loadVendors(resetOffset = false) {
  if (resetOffset) state.offset = 0;
  const filters = currentFilters();
  const query = filtersToQuery(filters, state.offset);
  const data = await fetchJson(`/api/vendors?${query}`);
  state.total = data.total;

  els.resultsCount.textContent = `${data.total} résultat(s)`;
  els.pageInfo.textContent = `Page ${Math.floor(state.offset / state.limit) + 1}`;
  els.prevPage.disabled = state.offset === 0;
  els.nextPage.disabled = state.offset + state.limit >= data.total;

  if (!data.vendors.length) {
    els.vendorList.innerHTML = `<div class="empty">Aucun vendeur ne correspond aux filtres.</div>`;
    return;
  }
  els.vendorList.innerHTML = data.vendors.map(renderVendorCard).join("");
}

function bindFilters() {
  const inputs = [
    els.filterQ,
    els.filterCategory,
    els.filterSegment,
    els.filterPricing,
    els.filterTarget,
    els.filterVerification,
    els.filterFrance,
    els.filterHq,
  ];
  inputs.forEach((el) => {
    el.addEventListener("input", () => {
      clearTimeout(state.debounce);
      state.debounce = setTimeout(() => loadVendors(true), 250);
    });
    el.addEventListener("change", () => loadVendors(true));
  });

  els.resetFilters.addEventListener("click", () => {
    inputs.forEach((el) => { el.value = ""; });
    loadVendors(true);
  });

  els.prevPage.addEventListener("click", () => {
    state.offset = Math.max(0, state.offset - state.limit);
    loadVendors();
  });
  els.nextPage.addEventListener("click", () => {
    state.offset += state.limit;
    loadVendors();
  });
}

function renderMarkdown(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
}

function appendMessage(role, text, sources = null) {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  if (role === "assistant") {
    div.innerHTML = renderMarkdown(text);
  } else {
    div.textContent = text;
  }

  if (sources && sources.length) {
    const block = document.createElement("div");
    block.className = "sources";
    block.innerHTML = "<strong>Sources</strong>";
    sources.forEach((src) => {
      const item = document.createElement("div");
      item.className = "source-item";
      item.innerHTML = `• <a href="${src.url}" target="_blank" rel="noopener">${src.name}</a> — ${(src.segment_labels || []).join(", ")} (score ${src.relevance ?? "—"})`;
      block.appendChild(item);
    });
    div.appendChild(block);
  }

  els.ragMessages.appendChild(div);
  els.ragMessages.scrollTop = els.ragMessages.scrollHeight;
}

async function askRag(query) {
  appendMessage("user", query);
  els.ragInput.value = "";
  appendMessage("assistant", "Recherche en cours…");

  try {
    const data = await fetchJson("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, top_k: 8 }),
    });
    els.ragMessages.lastChild.remove();
    appendMessage("assistant", data.answer, data.sources);
    els.ragMode.textContent = `Mode : ${data.mode}`;
  } catch (err) {
    els.ragMessages.lastChild.remove();
    appendMessage("assistant", `Erreur : ${err.message}`);
  }
}

async function init() {
  const [meta, segmentsPayload] = await Promise.all([
    fetchJson("/api/meta"),
    fetchJson("/api/segments"),
  ]);

  state.meta = meta;
  state.segments = segmentsPayload.segments;

  renderStats(meta);
  renderSegmentChart(state.segments);

  fillSelect(els.filterCategory, meta.categories.map((c) => c.id), (id) => {
    const cat = meta.categories.find((c) => c.id === id);
    return cat ? cat.label : id;
  });
  fillSelect(els.filterSegment, state.segments.map((s) => s.id), (id) => {
    const seg = state.segments.find((s) => s.id === id);
    return seg ? seg.label : id;
  });
  fillSelect(els.filterPricing, meta.pricing_models);
  fillSelect(els.filterTarget, meta.target_markets);
  fillSelect(els.filterVerification, meta.verification_statuses);
  fillSelect(els.filterFrance, meta.france_market_levels);

  els.ragMode.textContent = meta.llm_available
    ? "Mode : OpenAI (si OPENAI_API_KEY)"
    : "Mode : synthèse locale TF-IDF";

  bindFilters();
  await loadVendors(true);

  els.ragForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = els.ragInput.value.trim();
    if (query) askRag(query);
  });
}

init().catch((err) => {
  document.body.innerHTML = `<pre style="padding:2rem;color:#ff8f8f">Échec chargement : ${err.message}</pre>`;
});
