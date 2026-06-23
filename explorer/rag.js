const TOKEN_RE = /[a-z0-9àâäéèêëïîôùûüçœæ]+/gi;

export function tokenize(text) {
  return (text.match(TOKEN_RE) || []).map((t) => t.toLowerCase());
}

function cosineSimilarity(a, b) {
  if (!a.size || !b.size) return 0;
  let dot = 0;
  for (const [key, val] of a) {
    dot += val * (b.get(key) || 0);
  }
  let normA = 0;
  let normB = 0;
  for (const val of a.values()) normA += val * val;
  for (const val of b.values()) normB += val * val;
  if (!normA || !normB) return 0;
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

export class TfIdfIndex {
  constructor(documents) {
    this.documents = documents;
    this.docTokens = documents.map((doc) => tokenize(doc.text));
    const df = new Map();
    for (const tokens of this.docTokens) {
      for (const token of new Set(tokens)) {
        df.set(token, (df.get(token) || 0) + 1);
      }
    }
    const n = documents.length;
    this.idf = new Map();
    for (const [token, freq] of df) {
      this.idf.set(token, Math.log((n + 1) / (freq + 1)) + 1);
    }
  }

  vector(tokens) {
    const tf = new Map();
    for (const token of tokens) {
      tf.set(token, (tf.get(token) || 0) + 1);
    }
    const vec = new Map();
    for (const [token, count] of tf) {
      if (this.idf.has(token)) {
        vec.set(token, count * this.idf.get(token));
      }
    }
    return vec;
  }

  search(query, topK = 8) {
    const qVec = this.vector(tokenize(query));
    if (!qVec.size) return [];
    const scored = [];
    for (let idx = 0; idx < this.docTokens.length; idx += 1) {
      const score = cosineSimilarity(qVec, this.vector(this.docTokens[idx]));
      if (score > 0) scored.push([score, idx]);
    }
    scored.sort((a, b) => b[0] - a[0]);
    return scored.slice(0, topK);
  }
}

export function vendorDocumentText(vendor, segLabels) {
  const segments = (vendor.segments || [])
    .map((s) => segLabels.get(s) || s)
    .join(" ");
  const capabilities = (vendor.capabilities || []).join(" ");
  return [
    vendor.name,
    vendor.description,
    segments,
    capabilities,
    vendor.pricing_model,
    vendor.target_market,
    vendor.geography,
    vendor.hq_country,
    vendor.france_market,
    vendor.pricing_notes,
    vendor.notes,
  ]
    .filter(Boolean)
    .join(" ");
}

export function synthesizeLocal(query, hits) {
  if (!hits.length) {
    return `Aucun acteur pertinent trouvé pour « ${query} ». Essayez des termes plus larges (segment, capacité, pays).`;
  }
  const lines = [`**${hits.length} acteur(s)** correspondent à « ${query} » :\n`];
  for (const hit of hits.slice(0, 6)) {
    const seg = (hit.segment_labels || []).join(", ");
    const desc = hit.description.slice(0, 160).trim();
    lines.push(`- **${hit.name}** — ${seg}. ${desc}…`);
  }
  if (hits.length > 6) {
    lines.push(`\n… et ${hits.length - 6} autre(s) dans les sources ci-dessous.`);
  }
  return lines.join("\n");
}

export function rankForQuery(query, store, topK = 8) {
  const queryTokens = new Set(tokenize(query));
  const scored = store.ragIndex.search(query, topK * 4);
  const hits = [];
  const seen = new Set();

  for (const [score, idx] of scored) {
    const vendorId = store.ragIndex.documents[idx].vendor_id;
    if (seen.has(vendorId)) continue;
    const vendor = store.vendorById.get(vendorId);
    let boost = 0;

    for (const seg of vendor.segments || []) {
      const labelTokens = new Set(tokenize(store.segLabels.get(seg) || ""));
      for (const token of queryTokens) {
        if (labelTokens.has(token)) boost += 0.25;
      }
      if (query.toLowerCase().includes(seg.replace(/-/g, " ")) || query.toLowerCase().includes(seg)) {
        boost += 0.35;
      }
    }

    const nameTokens = new Set(tokenize(vendor.name || ""));
    for (const token of queryTokens) {
      if (nameTokens.has(token)) boost += 0.2;
    }

    const finalScore = score + boost;
    if (finalScore <= 0) continue;
    hits.push({ ...vendor, relevance: Math.round(finalScore * 10000) / 10000 });
    seen.add(vendorId);
  }

  hits.sort((a, b) => b.relevance - a.relevance);
  return hits.slice(0, topK);
}

export function ask(query, store, topK = 8) {
  const hits = rankForQuery(query, store, topK);
  return {
    query,
    answer: synthesizeLocal(query, hits),
    mode: "local",
    sources: hits,
  };
}
