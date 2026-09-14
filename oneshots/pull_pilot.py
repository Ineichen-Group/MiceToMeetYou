"""
Pull the pilot annotation sample: an unbiased random sample of papers,
field/date-scoped, exported to a CSV matching the annotation system's
upload schema.

CSV columns:
    title, keywords, abstract, journal          <- shown to annotators
    publication_date, mesh_terms, authors,
    affiliations, oa_status                       <- extras, not shown to
                                                       annotators per the
                                                       annotation guidelines,
                                                       but retained for
                                                       later analysis/validation
    openalex_id, pmid                              <- internal tracking only,
                                                       for joining labels back
                                                       to source records later

Usage:
    python pull_pilot.py
"""

import requests
import time
import csv
import json
from datetime import datetime

# ---- CONFIG ------------------------------------------------------------
MAILTO = "your_email@example.com"      # put a real contact email here
BASE_URL = "https://api.openalex.org/works"
PER_PAGE = 200

PILOT_SIZE = 200

# Field scope -- same bundle used in the MeSH coverage test (see
# docs/dataset.md). Medicine, Pharmacology, Veterinary, Biochem/Genetics.
FIELD_FILTER = "primary_topic.field.id:27|30|34|13"

# Fixed, closed date range for reproducibility -- see the reproducibility
# note in check_mesh_coverage.py / docs/dataset.md. Update PULL_DATE_CUTOFF
# when actually running this and keep it fixed across any reruns of this
# exact pilot pull.
PULL_DATE_CUTOFF = "2026-08-31"   # i.e. today
DATE_RANGE = f"from_publication_date:2016-01-01,to_publication_date:{PULL_DATE_CUTOFF}"

FILTER = f"{DATE_RANGE},type:article,language:en,{FIELD_FILTER}"

SEED = 31   # fixed seed; keep constant if this pilot is ever re-pulled

SELECT_FIELDS = (
    "id,ids,title,keywords,abstract_inverted_index,primary_location,"
    "publication_date,mesh,authorships,open_access,language"
)

OUTPUT_CSV = "pilot_annotation_sample.csv"
OUTPUT_SNAPSHOT = f"pilot_pull_snapshot_{datetime.utcnow().strftime('%Y-%m-%dT%H%M%SZ')}.json"
# ------------------------------------------------------------------------


def reconstruct_abstract(inverted_index):
    """OpenAlex stores abstracts as {word: [positions]}; rebuild the text."""
    if not inverted_index:
        return ""
    position_map = {}
    for word, positions in inverted_index.items():
        for pos in positions:
            position_map[pos] = word
    if not position_map:
        return ""
    max_pos = max(position_map.keys())
    return " ".join(position_map.get(i, "") for i in range(max_pos + 1))


def fetch_sample_page(n, filter_str, seed, mailto):
    """One random sample page of up to n works matching filter_str."""
    params = {
        "filter": filter_str,
        "sample": min(n, PER_PAGE),
        "seed": seed,
        "select": SELECT_FIELDS,
        "mailto": mailto,
    }
    resp = requests.get(BASE_URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("results", [])


def fetch_valid_sample(target, filter_str, start_seed, mailto, max_rounds=25):
    """
    Pull works until `target` of them have a usable abstract, deduping by
    OpenAlex ID across rounds. Each round uses the next seed in sequence,
    so the overall pull stays deterministic for a given start_seed even
    though the number of rounds needed depends on how many works lack an
    abstract.

    Returns (valid_works, skipped_no_abstract, seen_ids, next_seed) so a
    caller can keep pulling further replacements later using the same
    dedup set and seed sequence.
    """
    valid = []
    seen_ids = set()
    skipped_no_abstract = 0
    seed = start_seed

    for _ in range(max_rounds):
        if len(valid) >= target:
            break
        needed = target - len(valid)
        batch = fetch_sample_page(needed, filter_str, seed, mailto)
        if not batch:
            seed += 1
            continue

        for w in batch:
            wid = w.get("id")
            if wid in seen_ids:
                continue
            seen_ids.add(wid)

            if not reconstruct_abstract(w.get("abstract_inverted_index")):
                skipped_no_abstract += 1
                continue

            valid.append(w)
            if len(valid) >= target:
                break

        seed += 1
        time.sleep(0.2)

    return valid[:target], skipped_no_abstract, seen_ids, seed


def fetch_one_replacement(filter_str, seed, seen_ids, mailto, max_rounds=25):
    """
    Pull a single new work (usable abstract, not already in seen_ids),
    continuing the seed sequence from where the caller left off. Returns
    (work, next_seed), or (None, next_seed) if nothing new turns up.
    """
    for _ in range(max_rounds):
        batch = fetch_sample_page(PER_PAGE, filter_str, seed, mailto)
        seed += 1
        if not batch:
            continue
        for w in batch:
            wid = w.get("id")
            if wid in seen_ids:
                continue
            seen_ids.add(wid)
            if reconstruct_abstract(w.get("abstract_inverted_index")):
                return w, seed
        time.sleep(0.2)
    return None, seed


def format_keywords(keywords_field):
    """OpenAlex `keywords` is a list of {id, display_name, score} dicts."""
    if not keywords_field:
        return ""
    return ", ".join(k.get("display_name", "") for k in keywords_field if k.get("display_name"))


def format_mesh(mesh_field):
    """OpenAlex `mesh` is a list of dicts with a descriptor_name field."""
    if not mesh_field:
        return ""
    return "; ".join(m.get("descriptor_name", "") for m in mesh_field if m.get("descriptor_name"))


def format_authors(authorships_field):
    if not authorships_field:
        return ""
    names = []
    for a in authorships_field:
        author = a.get("author") or {}
        name = author.get("display_name")
        if name:
            names.append(name)
    return "; ".join(names)


def format_affiliations(authorships_field):
    if not authorships_field:
        return ""
    seen = []
    for a in authorships_field:
        for inst in a.get("institutions", []) or []:
            name = inst.get("display_name")
            if name and name not in seen:
                seen.append(name)
    return "; ".join(seen)


def describe_work(w):
    ids = w.get("ids", {}) or {}
    loc = w.get("primary_location") or {}
    source = loc.get("source") or {}
    oa = w.get("open_access") or {}
    abstract = reconstruct_abstract(w.get("abstract_inverted_index"))

    print(f"    Title:        {w.get('title', '')}")
    print(f"    Journal:      {source.get('display_name', '') or '(missing)'}")
    print(f"    Pub date:     {w.get('publication_date', '')}")
    print(f"    Keywords:     {format_keywords(w.get('keywords'))}")
    print(f"    Abstract:     {abstract[:300]}{'...' if len(abstract) > 300 else ''}")
    print(f"    Authors:      {format_authors(w.get('authorships'))}")
    print(f"    Affiliations: {format_affiliations(w.get('authorships'))}")
    print(f"    OA status:    {oa.get('oa_status', '')}")
    print(f"    Language:     {w.get('language', '')}")
    print(f"    OpenAlex ID:  {w.get('id', '')}")
    print(f"    PMID:         {ids.get('pmid', '')}")


def review_missing_journals(results, filter_str, seen_ids, seed, mailto):
    """
    Walk through results missing a journal, print available data for each,
    and ask whether to keep or replace it. Replacements are pulled live
    and substituted in place. Returns the (possibly modified) results list.
    """
    for i, w in enumerate(results):
        loc = w.get("primary_location") or {}
        source = loc.get("source") or {}
        journal = source.get("display_name", "") or ""
        if journal:
            continue

        print(f"\nPaper {i + 1}/{len(results)} is missing a journal:")
        describe_work(w)

        while True:
            choice = input("  Keep this paper? [k]eep / [r]eplace: ").strip().lower()
            if choice in ("k", "keep"):
                break
            if choice in ("r", "replace"):
                print("  Fetching a replacement...")
                replacement, seed = fetch_one_replacement(filter_str, seed, seen_ids, mailto)
                if replacement is None:
                    print("  No replacement found -- keeping original paper.")
                    break
                results[i] = replacement
                print("  Replacement found:")
                describe_work(replacement)
                loc = replacement.get("primary_location") or {}
                source = loc.get("source") or {}
                if not (source.get("display_name") or ""):
                    print("  (Replacement is also missing a journal -- reviewing again.)")
                    w = replacement
                    continue
                break
            print("  Please enter 'k' or 'r'.")

    return results


def write_csv(results, path):
    fieldnames = [
        "title", "keywords", "abstract", "journal",
        "publication_date", "mesh_terms", "authors", "affiliations", "oa_status",
        "language", "openalex_id", "pmid",
    ]

    missing_journal = 0

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for w in results:
            ids = w.get("ids", {}) or {}
            loc = w.get("primary_location") or {}
            source = loc.get("source") or {}
            oa = w.get("open_access") or {}

            journal = source.get("display_name", "") or ""
            if not journal:
                missing_journal += 1

            writer.writerow({
                "title": w.get("title", "") or "",
                "keywords": format_keywords(w.get("keywords")),
                "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
                "journal": journal,
                "publication_date": w.get("publication_date", "") or "",
                "mesh_terms": format_mesh(w.get("mesh")),
                "authors": format_authors(w.get("authorships")),
                "affiliations": format_affiliations(w.get("authorships")),
                "oa_status": oa.get("oa_status", "") or "",
                "language": w.get("language", "") or "",
                "openalex_id": w.get("id", ""),
                "pmid": ids.get("pmid", ""),
            })

    print(f"Wrote {len(results)} rows to {path}")
    print(f"Missing journal (written, but flagged): {missing_journal}")


if __name__ == "__main__":
    print(f"Pulling {PILOT_SIZE} papers with usable abstracts...")
    print(f"  filter = {FILTER}")
    print(f"  seed   = {SEED}")

    results, skipped_no_abstract, seen_ids, next_seed = fetch_valid_sample(
        PILOT_SIZE, FILTER, SEED, MAILTO
    )
    print(f"  -> got {len(results)} usable works")
    print(f"  -> skipped (no abstract): {skipped_no_abstract}\n")

    results = review_missing_journals(results, FILTER, seen_ids, next_seed, MAILTO)

    write_csv(results, OUTPUT_CSV)

    snapshot = {
        "run_timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "filter": FILTER,
        "seed": SEED,
        "pilot_size_requested": PILOT_SIZE,
        "pilot_size_returned": len(results),
        "skipped_no_abstract": skipped_no_abstract,
        "sampled_work_ids": [w["id"] for w in results],
    }
    with open(OUTPUT_SNAPSHOT, "w") as f:
        json.dump(snapshot, f, indent=2)
    print(f"Saved reproducibility snapshot to {OUTPUT_SNAPSHOT}")
