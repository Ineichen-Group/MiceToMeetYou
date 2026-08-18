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
  └── Yes → continue to Q2, Q3, Q4 (all apply; not mutually exclusive)
              Q2: Does it use animals?       (In-Vivo / Ex-Vivo / No)
              Q3: Does it use NAMs?          (Yes / No)
Q4: Disease area(s)            (multi-select)
```

A single paper can include selections for both animal study and NAM study (for example; an in-vivo experiment alongside an organoid arm within the same paper). Select all applicable types, these are not mutually exclusive categories.

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
| Other | Specify |

If unsure about which category a species falls into, and unable to clarify this through further research; select __Other__ and list the species name.

### Q2b: Sex of animals used 

_This will be shown per species group selected in Q2a_ 

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
| Organoids / 3D models | |
| Organ-on-a-chip / microphysiological systems | |
| Ex vivo tissue / explants | Tissue/organs taken from an animal that was harmed to obtain the tissue will __Ex vivo__ in Q2. This selection is for NAM approaches, e.g. the tissue is being used standalone as an experimental or screening platform. Do not re-flag the same fact if already captured in Q2. |
| In silico / computational model | QSAR, PBPK, ML-Based prediction |
| Other | Specify |


If unsure about which category a NAM falls into, and unable to clarify this through further research; select __Other__ and list the model or process name.

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
| Other | Specify |

It is unlikely that __Other__ will be required, it is present only to capture situations not considered during the planning stage. If selecting other, please be as specific as possible in the description.

__SELECTING CATEGORIES:__ Be generous in selections, if a study plausibly fits a chapter, select it. Err towards including a chapter rather than excluding it, multiple selections are possible and the goal is not to find the single best fit. 

--- 


## 5. Worked example

> **Title:** Bone Marrow Transplantation Generates Immature Oocytes and Rescues Long-Term Fertility in a Preclinical Mouse Model of Chemotherapy-Induced Premature Ovarian Failure
>
> **Keywords:** —
>
> **Abstract:** PURPOSE: Although early menopause frequently occurs in female cancer patients after chemotherapy (CTx), bone marrow (BM) transplantation (BMT) has been linked to an unexplained return of ovarian function and fertility in some survivors. Studies modeling this in mice have shown that BMT generates donor-derived oocytes in CTx-treated recipients. However, a subsequent report claimed that ovulated eggs are not derived from BM and that BM-derived oocytes reported previously are misidentified immune cells. This study was conducted to further clarify the impact of BMT on female reproductive function after CTx using a preclinical mouse model. METHODS: Female mice were administered CTx followed by BMT using coat color-mismatched female donors. After housing with males, the number of pregnancies and offspring genotype were recorded. For cell tracking, BM from germline-specific green fluorescent protein-transgenic mice was transplanted into CTx-treated wild-type recipients. Immune cells were sorted from blood and analyzed for germline markers. RESULTS: BMT rescued long-term fertility in CTx-treated females, but all offspring were derived from the recipient germline. Cell tracking showed that donor-derived oocytes were generated in ovaries of recipients after BMT, and two lines of evidence dispelled the claim that these oocytes are misidentified immune cells. CONCLUSION: These data from a preclinical mouse model validate a testable clinical strategy for preserving or resurrecting ovarian function and fertility in female cancer patients after CTx, thus aligning with recommendations of the 2005 National Cancer Institute Breast Cancer Progress Review Group and President's Cancer Panel to prioritize research efforts aimed at improving the quality of life in cancer survivors.

| # | Question | Answer | Notes (illustrative only — not required from annotator) |
|---|---|---|---|
| 1 | Preclinical study? | **Yes** | Mouse model study investigating ovarian function after chemotherapy and bone marrow transplantation. |
| 2 | Uses animals? | **In-Vivo** | |
| 2a | Species group(s) | Rodents | Female mice used as both donors and recipients. |
| 2b | Sex (Rodents) | Female | |
| 3 | Uses NAMs? | **No** | |
| 4 | Disease area | **II — Neoplasms**; **XIV — Genitourinary** | Cancer survivorship context (chemotherapy-induced menopause); ovarian function and fertility as primary outcome. |


--- 

## Changelog 

_2026.08.18_
1. Split rodents into rats and other rodents 
1. Combined Cell lines (2D) and Stem Cell NAMs


## To Do

1. Add further examples to Q2a includes table 




    



