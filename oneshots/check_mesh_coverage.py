"""
Sample works from OpenAlex at several filter levels (broad -> narrow) and
check what fraction of each sample:
  - have a PMID (i.e. were sourced from / linked to PubMed)
  - have a non-empty `mesh` field

Usage:
    python check_mesh_coverage.py

Edit FILTERS below to add/remove levels, or to swap in the field/domain IDs
that actually match your pull criteria.

Useful OpenAlex field IDs (domain in parens):
  27 Medicine (Health Sciences)      34 Veterinary (Health Sciences)
  11 Agricultural & Biological Sci.  13 Biochemistry, Genetics & Mol Bio
  24 Immunology and Microbiology     28 Neuroscience
  30 Pharmacology, Toxicology & Pharmaceutics
  29 Nursing   35 Dentistry   36 Health Professions
  (all Life Sciences unless noted)
Domain IDs: 1 = Life Sciences, 4 = Health Sciences
"""

import requests
import time

# ---- CONFIG ----------------------------------------------------------
SAMPLE_SIZE = 1000                  # works to sample PER FILTER LEVEL
PER_PAGE = 200                      # OpenAlex max per_page is 200
MAILTO = "example@email.com"        # for polite pool
PULL_DATE_CUTOFF = "2026-07-01"     # Latest date from which to pull

BASE_URL = "https://api.openalex.org/works"

DATE_RANGE = f"from_publication_date:2015-01-01,to_publication_date:{PULL_DATE_CUTOFF}"

FILTERS = [
    ("All scholarly works (baseline)",
     f"{DATE_RANGE},type:article"),
 
    ("Health Sciences domain",
     f"{DATE_RANGE},type:article,"
     "primary_topic.domain.id:4"),
 
    ("Life Sciences domain",
     f"{DATE_RANGE},type:article,"
     "primary_topic.domain.id:1"),
 
    ("Medicine field only",
     f"{DATE_RANGE},type:article,"
     "primary_topic.field.id:27"),
 
    ("Medicine OR Pharmacology OR Vet OR Biochem/Genetics fields",
     f"{DATE_RANGE},type:article,"
     "primary_topic.field.id:27|30|34|13"),
]


def fetch_sample(n, filter_str, mailto):
    """
    Use OpenAlex's `sample` parameter to get a random sample directly
    (avoids bias from paging through results in a fixed order).
    """
    results = []
    seed = 31  
    fetched = 0

    while fetched < n:
        page_size = min(PER_PAGE, n - fetched)
        params = {
            "filter": filter_str,
            "sample": page_size,
            "seed": seed,
            "select": "id,ids,mesh,primary_location",
            "mailto": mailto,
        }
        resp = requests.get(BASE_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        batch = data.get("results", [])
        if not batch:
            break
        results.extend(batch)
        fetched += len(batch)
        # sample endpoint doesn't paginate the same way; if we need more
        # than one page, bump the seed so we don't get the exact same set
        seed += 1
        time.sleep(0.2)

    return results[:n]


def analyze(results):
    total = len(results)
    has_pmid = 0
    has_mesh = 0
    has_both = 0
    has_neither = 0

    for w in results:
        ids = w.get("ids", {}) or {}
        pmid = ids.get("pmid")
        mesh = w.get("mesh") or []

        pmid_present = bool(pmid)
        mesh_present = len(mesh) > 0

        has_pmid += pmid_present
        has_mesh += mesh_present
        has_both += pmid_present and mesh_present
        has_neither += (not pmid_present) and (not mesh_present)

    def pct(x):
        return f"{x} ({100 * x / total:.1f}%)" if total else "0 (0.0%)"

    return {
        "total": total,
        "pmid": pct(has_pmid),
        "mesh": pct(has_mesh),
        "both": pct(has_both),
        "pmid_no_mesh": pct(has_pmid - has_both),
        "neither": pct(has_neither),
    }


if __name__ == "__main__":
    rows = []
    for label, filter_str in FILTERS:
        print(f"Fetching sample for: {label}")
        print(f"  filter = {filter_str}")
        try:
            sample = fetch_sample(SAMPLE_SIZE, filter_str, MAILTO)
            stats = analyze(sample)
            stats["label"] = label
            rows.append(stats)
            print(f"  -> got {stats['total']} works\n")
        except Exception as e:
            print(f"  -> FAILED: {e}\n")
        time.sleep(0.5)

    # Summary table
    print("\n" + "=" * 100)
    print(f"{'Filter level':<50} {'PMID':>12} {'MeSH':>14} {'PMID+MeSH':>14} {'Neither':>14}")
    print("-" * 100)
    for r in rows:
        print(f"{r['label']:<50} {r['pmid']:>12} {r['mesh']:>14} {r['both']:>14} {r['neither']:>14}")
