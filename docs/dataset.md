# Dataset

This document describes where the corpus comes from, how it's scoped, and
what we know so far about its structure. It's a living document — update it
as sourcing decisions change or new findings come in, but keep dated
findings (like the coverage test below) as point-in-time snapshots rather
than editing them after the fact.

## Primary source: OpenAlex

[OpenAlex](https://openalex.org) is the primary data source for pulling
paper metadata (title, abstract, authors, affiliations, publication date,
open access status, topic/field classification, and — where available —
MeSH terms).

**Why OpenAlex over PubMed directly:** independent coverage studies put
OpenAlex's recall of PubMed-indexed biomedical literature at 93–98%+,
meaning very little is lost by using OpenAlex as the single primary source
rather than querying PubMed separately. OpenAlex also ingests preprints and
non-MEDLINE journals that PubMed doesn't cover.

**Why not also query PubMed separately:** not needed for coverage. The one
thing PubMed uniquely offers — MeSH terms — is already present as a field on
OpenAlex work records for PubMed-sourced works, so it can be pulled from the
same OpenAlex query rather than a second API. See the coverage findings
below for how much of the corpus that actually applies to.

**Other sources considered and ruled out:** Scopus, Web of Science, Embase.
These are paywalled and their marginal recall gain over OpenAlex (a few
percentage points, per published comparisons) doesn't justify the
integration cost for this project.

## Field/domain scoping

Pulls are scoped using OpenAlex's `primary_topic.field.id` filter to reduce
volume before any classification happens. Current field bundle:

| Field ID | Field | Domain |
|---|---|---|
| 27 | Medicine | Health Sciences |
| 30 | Pharmacology, Toxicology & Pharmaceutics | Life Sciences |
| 34 | Veterinary | Health Sciences |
| 13 | Biochemistry, Genetics & Molecular Biology | Life Sciences |

This bundle is a starting point, not final — see [Open questions](#open-questions).

## MeSH / PMID coverage findings

MeSH terms are a useful pre-filter signal (e.g. `Animals` vs `Humans` check
tags) but are only present on OpenAlex records that trace back to a PubMed
entry, and OpenAlex doesn't support filtering *on* MeSH directly — it can
only be retrieved per-record as a `select` field. Before relying on it, we
tested how much of the corpus actually carries MeSH terms, at increasingly
narrow field/domain scopes.

**Method:** random samples (OpenAlex `sample` parameter, fixed seed) of
1,000 works per filter level, `type:article` only, publication date range
2015-01-01 to 2026-07-01. Produced by [`oneshots/check_mesh_coverage.py`](../oneshots/check_mesh_coverage.py).

**Run date:** 2026-07-01 (see reproducibility note below)

| Filter level | PMID | MeSH | PMID + MeSH | Neither |
|---|---|---|---|---|
| All scholarly works (baseline) | 213 (21.3%) | 140 (14.0%) | 140 (14.0%) | 787 (78.7%) |
| Health Sciences domain | 466 (46.6%) | 344 (34.4%) | 344 (34.4%) | 534 (53.4%) |
| Life Sciences domain | 435 (43.5%) | 336 (33.6%) | 336 (33.6%) | 565 (56.5%) |
| Medicine field only | 517 (51.7%) | 385 (38.5%) | 385 (38.5%) | 483 (48.3%) |
| Medicine OR Pharmacology OR Vet OR Biochem/Genetics fields | 522 (52.2%) | 388 (38.8%) | 388 (38.8%) | 478 (47.8%) |

**Takeaways:**
- MeSH coverage rises sharply moving from "all scholarly works" to
  "Health Sciences domain" (14.0% → 34.4%), then rises more slowly with
  further narrowing, plateauing around 38-39% at the narrowest field-bundle
  level tested. Further field narrowing is unlikely to meaningfully improve
  this ratio.
- Even at the narrowest scope tested, ~48% of the corpus has neither a
  PMID nor MeSH terms. This was further broken down by publication year and
  source type (see below).
- **Implication:** MeSH is a useful, free pre-filter/validation signal for
  roughly a third of the corpus, but classification for the majority of
  papers has to rely on title/abstract content (keyword heuristics, then
  the trained classifier) rather than MeSH.

### Secondary breakdowns (by year, by source type)

Run on the narrowest filter level above, larger sample (n=1000), to test
two hypotheses about the "neither" group:

- **By publication year:** tests whether "neither" papers are concentrated
  in recent years (= MEDLINE indexing lag, which resolves over time) vs.
  spread evenly across the full date range (= a structural gap that won't
  resolve on its own). Finding: mostly structural — MeSH coverage is
  fairly flat across 2015-2022 (~32-48%), with only a modest decline in the
  most recent 1-2 years consistent with indexing lag on very recent papers.
- **By source type:** tests whether "neither" papers are concentrated in
  preprints/repositories vs. peer-reviewed journals. Finding: repositories
  have much lower MeSH coverage than journals (~18% vs ~40%), but
  repositories are a small fraction of the sample (~8%) — most of the
  "neither" group is ordinary journal articles that simply aren't
  MEDLINE-indexed, not preprints slipping through the `type:article` filter.

*(Numbers from the specific run that produced these findings are in the
oneshot's snapshot JSON output, not reproduced here — see the
reproducibility note below.)*

### Reproducibility note

The oneshot script (`oneshots/check_mesh_coverage.py`) uses a fixed random
seed and a fixed, closed publication-date range (`from_publication_date` /
`to_publication_date`), so the **query** is repeatable. This does **not**
guarantee a byte-identical **result** if rerun later: OpenAlex is a living
dataset, and MeSH terms in particular get attached to existing records
retroactively as PubMed indexing catches up (see the year-lag finding
above). Rerunning the same query next month may return slightly different
percentages for the same nominal filter, because the underlying records
changed, not because the sampling logic did.

The script saves a timestamped JSON snapshot of the exact work IDs sampled
alongside the summary stats, so a specific run's result can be pointed back
to even if a later rerun differs.

## Annotation sample pull strategy

See [`docs/annotation.md`](annotation.md) for the annotation guidelines
themselves. The pull strategy for the ~2,000-paper human annotation set is
documented separately here since it concerns sourcing, not labeling.

