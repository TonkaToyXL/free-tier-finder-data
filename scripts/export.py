#!/usr/bin/env python3
"""Regenerate data files, README table and CHANGELOG from the Free Tier Finder source data."""
import csv, json, os, re, sys
from urllib.parse import urlparse, parse_qs

SRC = sys.argv[1] if len(sys.argv) > 1 else "/workspace/ftf5/data"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://freetierfinder.com"
REF_KEYS = {"ref", "via", "aff", "affiliate", "referral", "fpr", "utm_source", "utm_medium", "utm_campaign", "partner", "coupon"}

def slug(n): return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")

def official(url):
    if not url: return ""
    q = parse_qs(urlparse(url).query)
    if any(k.lower() in REF_KEYS for k in q) or re.search(r"(affiliate|referral|/ref/|/go/)", url, re.I):
        raise SystemExit(f"Affiliate-like URL rejected: {url}")
    return url

def load(n): return json.load(open(os.path.join(SRC, n)))

FIELDS = ["name", "category", "what_you_get", "how_to_get_it", "requirements", "catch",
          "no_card_status", "official_source_url", "date_checked", "page_url"]

tools = [{
    "name": t["name"], "category": t["category"],
    "what_you_get": t.get("get") or t.get("free_tier_includes", ""),
    "how_to_get_it": t.get("how", ""), "requirements": t.get("requires", ""),
    "catch": t.get("catch", ""), "no_card_status": t.get("credit_card_required", ""),
    "official_source_url": official(t.get("facts_source") or t.get("pricing_url")),
    "date_checked": t.get("facts_checked") or t.get("last_verified", ""),
    "page_url": f"{SITE}/tool/{slug(t['name'])}",
} for t in load("tools.json")]
tools.sort(key=lambda r: (r["category"].lower(), r["name"].lower()))

promos = [{
    "name": p["tool"], "category": p.get("type", ""),
    "what_you_get": p.get("get") or p.get("detail", ""),
    "how_to_get_it": p.get("how", ""), "requirements": p.get("requires", ""),
    "catch": p.get("catch", ""), "no_card_status": p.get("credit_card_required", "Not stated by vendor"),
    "official_source_url": official(p.get("facts_source") or p.get("source")),
    "date_checked": p.get("facts_checked") or p.get("verified", ""),
    "page_url": f"{SITE}/promo/{slug(p['tool'])}",
    "title": p.get("title", ""), "expires": p.get("expires", ""),
} for p in load("promos.json")]
promos.sort(key=lambda r: r["name"].lower())

dropped = [{"name": d[0], "reason": d[1]} for d in load("dropped.json")]

os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
def wj(n, o): json.dump(o, open(os.path.join(ROOT, "data", n), "w"), indent=2, ensure_ascii=False); open(os.path.join(ROOT, "data", n), "a").write("\n")
def wc(n, rows, f):
    with open(os.path.join(ROOT, "data", n), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=f, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
wj("tools.json", tools); wj("promos.json", promos); wj("dropped.json", dropped)
wc("tools.csv", tools, FIELDS); wc("promos.csv", promos, FIELDS + ["title", "expires"])

latest = max(r["date_checked"] for r in tools + promos)

# README table
cats = {}
for t in tools: cats.setdefault(t["category"], []).append(t)
esc = lambda s: s.replace("|", "\\|").replace("\n", " ")
lines = []
for c in sorted(cats, key=str.lower):
    lines += [f"### {c}", "", "| Tool | Free tier | Card required | Checked |", "| --- | --- | --- | --- |"]
    lines += [f"| [{esc(t['name'])}]({t['page_url']}) | {esc(t['what_you_get'])} | {esc(t['no_card_status'])} | {t['date_checked']} |" for t in cats[c]]
    lines.append("")
lines += ["### Promos and startup credits", "", "| Offer | Type | Expires | Checked |", "| --- | --- | --- | --- |"]
lines += [f"| [{esc(p['name'])}: {esc(p['title'])}]({p['page_url']}) | {esc(p['category'])} | {esc(p['expires'])} | {p['date_checked']} |" for p in promos]
table = "\n".join(lines)

tpl = open(os.path.join(ROOT, "scripts", "README.template.md")).read()
open(os.path.join(ROOT, "README.md"), "w").write(
    tpl.replace("{{TABLE}}", table).replace("{{TOOLS}}", str(len(tools)))
       .replace("{{PROMOS}}", str(len(promos))).replace("{{DATE}}", latest)
       .replace("{{BADGE_DATE}}", latest.replace("-", "--")))

# CHANGELOG
cl = load("changelog.json")
out = ["# Changelog", "", "Entry-level changes recorded at each recheck. Newest first.", "", f"## {latest}", "",
       f"- Dataset published: {len(tools)} tools, {len(promos)} promos, {len(dropped)} retired entries.", ""]
out += ["### Entry updates", ""] + [f"- {k}: {esc(v)}" for k, v in cl.items()] + [""]
open(os.path.join(ROOT, "CHANGELOG.md"), "w").write("\n".join(out))
print(f"tools={len(tools)} promos={len(promos)} dropped={len(dropped)} categories={len(cats)} latest={latest}")
