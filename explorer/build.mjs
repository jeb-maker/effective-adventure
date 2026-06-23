#!/usr/bin/env node
/** Génère catalogue-bundle.json à partir des JSON versionnés du dépôt. */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, "..");
const CATALOGUE = path.join(ROOT, "catalogue-saas");
const VENDORS_DIR = path.join(CATALOGUE, "vendors");
const OUT = path.join(__dirname, "catalogue-bundle.json");

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function loadVendors() {
  const vendors = [];
  for (const name of fs.readdirSync(VENDORS_DIR).sort()) {
    if (!name.endsWith(".json")) continue;
    const data = readJson(path.join(VENDORS_DIR, name));
    vendors.push(...(data.vendors || []));
  }
  return vendors;
}

function loadFrozenIds() {
  const frozenPath = path.join(CATALOGUE, "frozen-segments.json");
  if (!fs.existsSync(frozenPath)) return [];
  const data = readJson(frozenPath);
  return (data.frozen || []).map((item) => item.segment_id);
}

const taxonomy = readJson(path.join(CATALOGUE, "taxonomy.json"));
const ideas = readJson(path.join(ROOT, "idees", "catalogue-segments.json"));
const vendors = loadVendors();
const frozenSegmentIds = loadFrozenIds();

const bundle = {
  generated_at: new Date().toISOString().slice(0, 10),
  taxonomy,
  ideas: ideas.ideas || {},
  frozen_segment_ids: frozenSegmentIds,
  vendors,
};

fs.writeFileSync(OUT, JSON.stringify(bundle), "utf8");
const sizeKb = Math.round(fs.statSync(OUT).size / 1024);
console.log(`Écrit ${OUT} — ${vendors.length} vendeurs (${sizeKb} Ko)`);
