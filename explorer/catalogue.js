import { TfIdfIndex, vendorDocumentText } from "./rag.js";

export class CatalogueStore {
  constructor(bundle) {
    this.taxonomy = bundle.taxonomy;
    this.vendors = bundle.vendors;
    this.ideas = bundle.ideas || {};
    this.frozenIds = new Set(bundle.frozen_segment_ids || []);

    this.segLabels = new Map(
      this.taxonomy.segments.map((s) => [s.id, s.label])
    );
    this.segCategories = new Map(
      this.taxonomy.segments.map((s) => [s.id, s.category || ""])
    );
    this.catLabels = new Map(
      (this.taxonomy.categories || []).map((c) => [c.id, c.label])
    );

    this.enrichedVendors = this.vendors.map((v) => this.enrichVendor(v));
    this.vendorById = new Map(this.enrichedVendors.map((v) => [v.id, v]));

    const documents = this.enrichedVendors.map((vendor) => ({
      vendor_id: vendor.id,
      text: vendorDocumentText(vendor, this.segLabels),
    }));
    this.ragIndex = new TfIdfIndex(documents);
  }

  enrichVendor(vendor) {
    const segments = vendor.segments || [];
    const segmentLabels = segments.map((s) => this.segLabels.get(s) || s);
    const categories = [
      ...new Set(
        segments
          .map((s) => this.catLabels.get(this.segCategories.get(s) || "") || "")
          .filter(Boolean)
      ),
    ];
    return {
      ...vendor,
      segment_labels: segmentLabels,
      categories,
      frozen_segment: segments.some((s) => this.frozenIds.has(s)),
    };
  }

  segmentStats() {
    const counts = new Map();
    for (const vendor of this.vendors) {
      for (const seg of vendor.segments || []) {
        counts.set(seg, (counts.get(seg) || 0) + 1);
      }
    }
    return this.taxonomy.segments.map((seg) => ({
      id: seg.id,
      label: seg.label,
      category: seg.category || "",
      category_label: this.catLabels.get(seg.category || "") || "",
      count: counts.get(seg.id) || 0,
      frozen: this.frozenIds.has(seg.id),
      description: seg.description || "",
    }));
  }

  meta() {
    const countBy = (field, fallback = "unknown") => {
      const map = new Map();
      for (const vendor of this.vendors) {
        const key = vendor[field] || fallback;
        map.set(key, (map.get(key) || 0) + 1);
      }
      return Object.fromEntries(map);
    };

    return {
      vendor_count: this.vendors.length,
      segment_count: this.taxonomy.segments.length,
      category_count: (this.taxonomy.categories || []).length,
      frozen_segment_count: this.frozenIds.size,
      idea_count: Object.keys(this.ideas).length,
      pricing_models: this.taxonomy.pricing_models || [],
      target_markets: this.taxonomy.target_markets || [],
      verification_statuses: this.taxonomy.verification_statuses || [],
      france_market_levels: this.taxonomy.france_market_levels || [],
      categories: (this.taxonomy.categories || []).map((c) => ({
        id: c.id,
        label: c.label,
      })),
      aggregates: {
        pricing_model: countBy("pricing_model"),
        verification_status: countBy("verification_status"),
        france_market: countBy("france_market"),
      },
      ideas: this.ideas,
      generated_at: null,
    };
  }

  filterVendors({
    q = "",
    segment = "",
    category = "",
    pricing_model = "",
    target_market = "",
    verification_status = "",
    france_market = "",
    hq_country = "",
    limit = 100,
    offset = 0,
  } = {}) {
    let results = [...this.enrichedVendors];

    if (segment) {
      results = results.filter((v) => (v.segments || []).includes(segment));
    }
    if (category) {
      results = results.filter((v) =>
        (v.segments || []).some((s) => this.segCategories.get(s) === category)
      );
    }
    if (pricing_model) {
      results = results.filter((v) => v.pricing_model === pricing_model);
    }
    if (target_market) {
      results = results.filter((v) => v.target_market === target_market);
    }
    if (verification_status) {
      results = results.filter((v) => v.verification_status === verification_status);
    }
    if (france_market) {
      results = results.filter((v) => v.france_market === france_market);
    }
    if (hq_country) {
      results = results.filter((v) => v.hq_country === hq_country);
    }

    if (q.trim()) {
      const qLower = q.toLowerCase();
      const scored = [];
      for (const vendor of results) {
        const haystack = [
          vendor.name,
          vendor.description,
          (vendor.capabilities || []).join(" "),
          (vendor.segment_labels || []).join(" "),
        ]
          .join(" ")
          .toLowerCase();
        if (haystack.includes(qLower)) {
          scored.push([1, vendor]);
          continue;
        }
        for (const [ragScore, idx] of this.ragIndex.search(q, this.vendors.length)) {
          if (this.ragIndex.documents[idx].vendor_id === vendor.id) {
            scored.push([ragScore, vendor]);
            break;
          }
        }
      }
      scored.sort((a, b) => b[0] - a[0]);
      results = scored.map(([, vendor]) => vendor);
    }

    const total = results.length;
    return {
      total,
      offset,
      limit,
      vendors: results.slice(offset, offset + limit),
    };
  }
}

export async function loadCatalogue() {
  const res = await fetch("./catalogue-bundle.json");
  if (!res.ok) {
    throw new Error(
      "catalogue-bundle.json introuvable — lancez : node explorer/build.mjs"
    );
  }
  const bundle = await res.json();
  const store = new CatalogueStore(bundle);
  const meta = store.meta();
  meta.generated_at = bundle.generated_at;
  return { store, meta, segments: store.segmentStats() };
}
