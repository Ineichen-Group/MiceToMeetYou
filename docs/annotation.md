# Annotation Guidelines: Mice to Meet You

## Raw Data

Data will be pulled from OpenAlex. All data will be from the period 2021-2026

### What the annotator will see

For each paper:

- Title
- Keywords
- Abstract
- Journal name

If any of these are not present that is due to the data not being provided by OpenAlex.

### What is stored but not shown to the annotator

- Publication date
- Search/MeSH terms
- Authors
- Affiliations
- Open access classification

## General Decision Flow

```
Q1: Is this a preclinical study?
  ├── No  → STOP. Leave all remaining fields blank.
  └── Yes → continue to Q2, Q3, Q4, Q5 (all apply; not mutually exclusive)
              Q2: Does it use animals?       (In-Vivo / Ex-Vivo / No)
              Q3: Does it use NAMs?          (Yes / No)
              Q4: Disease area(s)            (multi-select)
              Q5: What is being tested?      (Substance / Intervention / Neither / Unclear)
```

A single paper can include selections for both animal study and NAM study (for example; an in-vivo experiment alongside an organoid arm within the same paper). Select all applicable types, these are not mutually exclusive categories.

> A reference document listing NAM type definitions and lab animals (with their groupings) accompanies these guidelines: `reference_nams_and_animals.md`.

## Question by Question Flow

### Q1: Is this a preclinical study?

__DEFINITION:__ A study using one or more of the following:
- In vivo animal experiments
- Ex vivo animal tissue
- In vitro experiments
- Computational (in silico) models
- Other NAM-based research (fully detailed in Q3)

| | |
|---|---|
| Conditional on | - |
| Options | Yes / No |

__INCLUDE__
- Any non-human animal species (embryonic through to adult), studied in vivo or ex vivo.
- Human-derived NAMs (e.g. human iPSC-derived organoids, human cell lines, human tissue explants used as a non-animal model system).
- Studies combining human and non-human data (e.g. an animal model study that also includes a small human validation cohort): include, and annotate the non-clinical portion normally.

__EXCLUDE__
- Reviews, meta-analyses, purely epidemiological studies.
- Pure clinical/patient studies: studies where human tissue, bodily fluid, or human subjects are used in a clinical or diagnostic context (e.g. a retrospective chart review, biomarker assay run on patient blood samples).
    - The distinction from the Include above is: _is the human material being used as a mechanistic/preclinical model system (include) vs. as a clinical/diagnostic sample (exclude).
- Case reports, clinical trials of any phase

If __No__ annotation for this paper is complete, no further questions will be provided.

### Q2: Does the study use animals?

> Note: This question is __not__ mutually exclusive with Q3.

| | |
|---|---|
| Conditional on | Q1 = __Yes__ |
| Options | In-vivo / Ex-vivo / No |

__Governing test:__ Was an animal harmed (inclusive killed) to conduct the study?
- If yes this is considered an animal study regardless of whether the experimental work was conducted on a living animal (in vivo) or on tissue/organs taken from the animal (ex vivo).

__IN-VIVO__
- Experiments performed in/on a living animal.

__EX-VIVO__
- Experiments performed on tissue, organs, other material taken from an animal that was harmed/killed to obtain it.

__NO__
- Exclude established/immortal animal-derived cell lines where no animal was harmed for this study; e.g. a commercial cell line derived from an animal outside of this study and then cultured for the current work.
    - This question is regarding the study as presented here, not the used materials ultimate origin.

### Q2a: Which species group(s)?

| | |
|---|---|
| Conditional on | Q2 != __No__ |
| Options | _see below_ |

Animals should be categorized into one of the groups below. Multiple options may be selected if multiple animal types were used.

| __Group__ | __Includes (non-exhaustive)__ |
|---|---|
| Mice | - |
| Rats | - |
| Other Rodents | Rabbits, guinea pigs |
| Non-Human Primates | ... |
| Pigs / Swine | - |
| Dogs / Canines | - |
| Fish | Zebrafish |
| Birds / Avian | - |
| Livestock (non-rodent, non-swine) | Cattle, Sheep, Goats |
| Invertebrates | Drosophila/insects, C. elegans |
| Other | Species name (free text, required) |
| Unclear / Not reported | Keywords (free text) |

See the reference document for a fuller list of species and the group each maps to.

__OTHER__
- Use for any species that is identified but does not fit a group above (e.g. horse, cat, ferret, amphibians, reptiles), or if unsure which group a species falls into and unable to clarify through further research.
- The text entry is __required__: enter the species name.
- More than one Other can be added. After selecting Other, a __+__ control adds a further Other entry. Each entry has its own species name, and each appears as a separate item (headed by the text entered) in Q2b so sex can be reported per species.
- Species that turn up often in Other may later be promoted to their own group.

__UNCLEAR / NOT REPORTED__
- Use when Q2 is In-vivo or Ex-vivo (an animal was used) but the species cannot be determined from the title, keywords, abstract or journal name (e.g. "in vivo experiments", "animal model", "model animals" with no species named).
- A text field is provided: enter any keywords that hint at the animal (e.g. "xenograft", "tumor-bearing", "wound model", "behavioural test"). Leave the field empty only if there is nothing to go on.
- Difference from __Other__: Other = the species __is__ identified but does not fit any group above. Unclear / Not reported = the species __is not__ identified.
- Do not guess a species from the model type alone (e.g. do not assume "xenograft" means mice); use this option instead and record the keyword.
- Can be selected alongside other groups (e.g. mice named for one experiment, an unnamed animal used for another).

### Q2b: Sex of animals used

_This will be shown per species group selected in Q2a (including Unclear / Not reported). Each Other entry is shown separately, headed by the species name entered, so sex is recorded for each one individually (e.g. "Horse: Male", "Axolotl: Mixed")._

| | |
|---|---|
| Conditional on | Q2 != __No__ |
| Options | Female / Male / Mixed / Not reported |

### Q3: Does the study use NAMs?

| | |
|---|---|
| Conditional on | Q1 = __Yes__ |
| Options | Yes / No |

__DEFINITION:__ Non-Animal Methods (NAMs) are used to asses biological activity or to predict effect without direct use of a live animal. This includes in vitro models, organoids, computational tools, microphysiological systems. These may be derived from human or animal source material. The source species does not change whether something is considered to be a NAM.



### Q3a: Which NAM type(s)?

| | |
|---|---|
| Conditional on | Q3 = __Yes__ |
| Options | _see below_ |


NAMs should be categorised into the labels below, multiple selections are possible.

| NAM | Notes |
|---|---|
| Cell lines / primary cells (2D) | Includes stem cell-derived models, iPSC, ESC (human or animal origin) |
| Human cells / tissue | Any human-derived cells or tissue used as the model system (e.g. human cell lines, iPSC-derived cells, PBMCs, human organoids, biopsy or autopsy tissue used mechanistically). Added as an extra tag; see note below. |
| Organoids / 3D models | |
| Organ-on-a-chip / microphysiological systems | |
| Ex vivo tissue / explants | Tissue/organs taken from an animal that was harmed to obtain the tissue will __Ex vivo__ in Q2. This selection is for NAM approaches, e.g. the tissue is being used standalone as an experimental or screening platform. Do not re-flag the same fact if already captured in Q2. |
| In silico / computational model | QSAR, PBPK, ML-Based prediction |
| Other | Specify |

__HUMAN CELLS / TISSUE__
- The human-origin counterpart to the animal-focused Ex vivo row. Human material does not appear in Q2 (no animal), so this label is how human tissue-based models are captured.
- It is a __source-based__ label and works as an __extra tag__ alongside the format-based labels. Whenever the model is human-derived, select Human cells / tissue __and__ the label(s) describing its format (2D cells, organoid, chip, explant). Example: human iPSC-derived RPE cells = Cell lines / primary cells (2D) + Human cells / tissue.
- Multiple selections remain possible, e.g. human 2D cells plus a mouse organoid arm = Cell lines (2D) + Human cells / tissue + Organoids / 3D models.
- Animal-derived models do not receive this tag.
- The Q1 rule still applies: human material used as a clinical/diagnostic sample is not preclinical and the paper would already have been excluded.

If unsure about which category a NAM falls into, and unable to clarify this through further research; select __Other__ and list the model or process name (text required).

### Q4: What disease area does this research target?

| | |
|---|---|
| Conditional on | Q1 = __Yes__ |
| Options | _see below_ |

__Abridged ICD-10 chapter list__
Chapters XVIII-XXII have been omitted as these do not meaningfully apply in animal/preclinical research contexts.

| Chapter | Title |
|---|---|
| I | Certain infectious and parasitic diseases |
| II | Neoplasms |
| III | Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism |
| IV | Endocrine, nutritional and metabolic diseases |
| V | Mental and behavioural disorders |
| VI | Diseases of the nervous system |
| VII | Diseases of the eye and adnexa |
| VIII | Diseases of the ear and mastoid process |
| IX | Diseases of the circulatory system |
| X | Diseases of the respiratory system |
| XI | Diseases of the digestive system |
| XII | Diseases of the skin and subcutaneous tissue |
| XIII | Diseases of the musculoskeletal system and connective tissue |
| XIV | Diseases of the genitourinary system |
| XV | Pregnancy, childbirth and the puerperium |
| XVI | Certain conditions originating in the perinatal period |
| XVII | Congenital malformations, deformations and chromosomal abnormalities |

The full ICD-10 listings with more information may be found [here](https://icd.who.int/browse10/2019/en#/II).

__Additional labels__

| Label | Notes |
|---|---|
| Veterinary / non-human animal health | |
| Agricultural | |
| Basic research | Preclinical work that does not target a specific disease or health condition, so that edge cases can be assigned a label. See note below. |
| Other | Specify |

__BASIC RESEARCH__
- Use when the study is preclinical (Q1 = Yes) but investigates fundamental biology, methods or tools without a disease, health condition, or applied (veterinary/agricultural) target. Examples: behavioural genetics in Drosophila, a general cell-signalling mechanism in a standard cell line, development of a new imaging or assay method validated on tissue.
- Not a disease area in the ICD sense; it records that no disease target was identified.
- If a disease is named as the motivation or model (e.g. "relevance to Alzheimer's"), select the disease chapter instead of, or alongside, Basic research.
- Difference from __Other__: Other = a disease/applied target exists but is not covered by the list. Basic research = no disease/applied target.

It is unlikely that __Other__ will be required, it is present only to capture situations not considered during the planning stage. If selecting other, please be as specific as possible in the description.

__SELECTING CATEGORIES:__ Be generous in selections, if a study plausibly fits a chapter, select it. Err towards including a chapter rather than excluding it, multiple selections are possible and the goal is not to find the single best fit.

### Q5: What is being tested?


| | |
|---|---|
| Conditional on | Q1 = __Yes__ |
| Options | Substance / Intervention / Neither (descriptive) / Unclear |

Multiple selections are possible between __Substance__ and __Intervention__. __Neither__ and __Unclear__ cannot be combined with any other option.

__GOVERNING TEST:__ What is the study varying, compared against a control or baseline, in order to learn about its effect? Record only this __main__ item. Do not record controls, comparators, or agents used only to create the disease model.

__SUBSTANCE__
- Something administered, applied or added: a drug or compound, biologic, extract, nanoparticle, nutrient, microorganism, toxicant.

__INTERVENTION__
- A manipulation that is not a substance: genetic modification, surgery or procedure, device or physical treatment (e.g. radiation, electrical stimulation), behavioural or lifestyle regime, transplantation.

__NEITHER (DESCRIPTIVE)__
- Nothing is tested for its effect: characterisation, mapping, method or tool development, basic mechanism without a tested agent or manipulation.

__UNCLEAR__
- Something appears to be tested but the abstract does not make clear what.

__Edge cases__
- Gene therapy, cell therapy, and similar products that are both a substance and a manipulation: select __Substance__, __Intervention__ or __both__. Any of these is acceptable; the free-text name and description are what allow the dataset to be regrouped later. Engineered microorganisms or exosomes given as the therapy are likewise acceptable under either route (e.g. Microorganism / probiotic, or Genetic modification).
- Disease induction is not the thing tested. In the worked example below, chemotherapy induces ovarian failure and is not recorded; bone marrow transplantation is the intervention being tested. A diet used only to induce disease (e.g. a high-fat diet for an obesity model) is likewise not recorded.
- A microorganism is recorded as a Substance when the study asks what the microorganism does (e.g. a bacterial strain given to mice to test its effect). It is not recorded when it only creates a disease model for testing something else.
- A knockout or transgenic animal counts as an Intervention (genetic modification) only if the study is testing the effect of that gene change. A standard disease-model strain used as the platform is not recorded.
- Diets: if the study varies a named ingredient or composition (e.g. soybean vs fish oil), record Substance (Nutrient / diet component). If it varies feeding pattern, quantity or timing (fasting, calorie restriction), record Intervention (Behavioural / environmental / lifestyle).
- Breed, strain or genotype comparisons (e.g. sire breeds, natural polymorphisms) are not recorded: select Neither (descriptive), unless a substance or intervention is also tested.
- Truncated abstracts: annotate from the title and the visible text. Select Unclear only when there is no clear signal about what is tested.

### Q5a: Which type(s) of substance?

| | |
|---|---|
| Conditional on | Q5 includes __Substance__ |
| Options | _see below_ |

Multiple selections are possible.

| Type | Examples |
|---|---|
| Small molecule / drug | Chemotherapeutics, antibiotics, kinase inhibitors, flavonoids |
| Biologic | Antibodies, proteins, peptides, vaccines |
| Nucleic acid therapeutic | siRNA, antisense, mRNA |
| Natural product / extract | Herbal or plant extracts, microbial metabolites. A purified single compound is acceptable here or under Small molecule / drug; enter its name either way |
| Nanomaterial / delivery system | Nanoparticles, liposomes, exosome-based carriers |
| Nutrient / diet component / supplement | Vitamins, fatty acids, dietary formulations |
| Microorganism / probiotic | Bacterial strains, microbiota preparations |
| Environmental chemical / toxicant | Pollutants, heavy metals, industrial chemicals |
| Other | Specify (text required) |

__Name of the substance(s)__ (free text, required): enter the name as given in the abstract. If the abstract describes the substance only generically (e.g. "a novel nanodevice", "hybrid compounds"), enter a short description or "not named". The field must not be left blank.

### Q5b: Which type(s) of intervention?

| | |
|---|---|
| Conditional on | Q5 includes __Intervention__ |
| Options | _see below_ |

Multiple selections are possible.

| Type | Examples |
|---|---|
| Genetic modification | Knockout, knockdown, CRISPR editing, overexpression, transgenic |
| Surgical / procedural | Surgery, injury or ischaemia procedures, implantation |
| Device / physical | Radiation, electrical or magnetic stimulation, ultrasound, imaging-guided delivery |
| Behavioural / environmental / lifestyle | Exercise, housing or enrichment, diet regime, stress paradigm |
| Transplantation | Bone marrow, cell or organ transplantation |
| Other | Specify (text required) |

__Short description of the intervention__ (free text, required): e.g. "CRISPR knockout of TTC30A", "bone marrow transplantation". If the abstract gives no specifics, enter "not specified". The field must not be left blank.

---


## Worked example

> **Title:** Bone Marrow Transplantation Generates Immature Oocytes and Rescues Long-Term Fertility in a Preclinical Mouse Model of Chemotherapy-Induced Premature Ovarian Failure
>
> **Keywords:** —
>
> **Abstract:** PURPOSE: Although early menopause frequently occurs in female cancer patients after chemotherapy (CTx), bone marrow (BM) transplantation (BMT) has been linked to an unexplained return of ovarian function and fertility in some survivors. Studies modeling this in mice have shown that BMT generates donor-derived oocytes in CTx-treated recipients. However, a subsequent report claimed that ovulated eggs are not derived from BM and that BM-derived oocytes reported previously are misidentified immune cells. This study was conducted to further clarify the impact of BMT on female reproductive function after CTx using a preclinical mouse model. METHODS: Female mice were administered CTx followed by BMT using coat color-mismatched female donors. After housing with males, the number of pregnancies and offspring genotype were recorded. For cell tracking, BM from germline-specific green fluorescent protein-transgenic mice was transplanted into CTx-treated wild-type recipients. Immune cells were sorted from blood and analyzed for germline markers. RESULTS: BMT rescued long-term fertility in CTx-treated females, but all offspring were derived from the recipient germline. Cell tracking showed that donor-derived oocytes were generated in ovaries of recipients after BMT, and two lines of evidence dispelled the claim that these oocytes are misidentified immune cells. CONCLUSION: These data from a preclinical mouse model validate a testable clinical strategy for preserving or resurrecting ovarian function and fertility in female cancer patients after CTx, thus aligning with recommendations of the 2005 National Cancer Institute Breast Cancer Progress Review Group and President's Cancer Panel to prioritize research efforts aimed at improving the quality of life in cancer survivors.

| # | Question | Answer | Notes (illustrative only — not required from annotator) |
|---|---|---|---|
| 1 | Preclinical study? | **Yes** | Mouse model study investigating ovarian function after chemotherapy and bone marrow transplantation. |
| 2 | Uses animals? | **In-Vivo** | |
| 2a | Species group(s) | Mice | Female mice used as both donors and recipients. |
| 2b | Sex (Mice) | Female | |
| 3 | Uses NAMs? | **No** | |
| 4 | Disease area | **II — Neoplasms**; **XIV — Genitourinary** | Cancer survivorship context (chemotherapy-induced menopause); ovarian function and fertility as primary outcome. |
| 5 | What is tested? | **Intervention** | Bone marrow transplantation is what is tested. Chemotherapy only induces the ovarian failure model, so Substance is not selected. |
| 5b | Intervention type(s) | Transplantation | |


---

## Changelog

_2026.08.18_
1. Split rodents into rats and other rodents
1. Combined Cell lines (2D) and Stem Cell NAMs

_2026.10.05_
1. Q2a: added "Unclear / Not reported" option with a keywords text field; Q2b now also applies to this group
1. Q3a: added "Human cells / tissue" NAM class
1. Q4: added "Basic research" additional label
1. Worked example: species group updated from "Rodents" to "Mice" to match the 2026.08.18 split
1. Added pointer to the new reference document (NAM definitions, lab animal groupings)
1. Human cells / tissue defined as an extra tag used alongside format-based NAM labels; multiple selection retained
1. Q2a: no new species groups for now; Other now requires a species name, and multiple Other entries are allowed (each reported separately in Q2b)

1. Added Q5 "What is being tested?" (Substance / Intervention / Neither / Unclear) with cascading Q5a (substance type) and Q5b (intervention type). Main item only; cell and gene therapies may be recorded as Substance, Intervention or both (merged at analysis). Breed/genotype comparisons are not recorded (Neither). Diet, pathogen and truncated-abstract rules added as edge cases (tested on 24 pilot papers). The substance name (Q5a) and intervention description (Q5b) are required free text, with "not named" / "not specified" accepted.
