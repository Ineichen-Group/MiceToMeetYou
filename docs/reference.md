# Reference: NAM Types and Lab Animals

Companion to the *Mice to Meet You* annotation guidelines. Use it to decide which Q3a label a model system falls under, and which Q2a species group an animal belongs to.

---

## Part 1. NAM types and definitions

**Non-Animal Methods (NAMs)** assess biological activity or predict effect without direct use of a live animal. They may be built from human or animal source material; the source species does not change whether something is a NAM. Material only counts as an animal study (Q2) if an animal was harmed for *this* study.

| Q3a label | Definition | Typical examples | Not this (see instead) |
|---|---|---|---|
| **Cell lines / primary cells (2D)** | Cells grown as a monolayer or in suspension on plastic/glass. Includes immortalised or established lines, primary cells, and stem cell-derived cultures (iPSC, ESC) of human or animal origin. | HEK293, HeLa, A549, Jurkat, CHO; primary fibroblasts; iPSC-derived neurons or RPE cells | Cells grown as spheroids or in a matrix → Organoids / 3D |
| **Human cells / tissue** | Extra tag for any human-derived cells or tissue used as the model system. Source-based label, selected alongside the format label. | Human cell lines, iPSC-derived cells, human organoids, PBMCs, human biopsy or autopsy tissue used mechanistically | Human material used as a clinical/diagnostic sample → excluded at Q1 |
| **Organoids / 3D models** | Cells cultured in three dimensions that self-organise or mimic tissue architecture. | Intestinal or brain organoids, tumour spheroids, 3D bioprinted tissue, scaffold/hydrogel cultures, 3D angiogenesis assays | Flat monolayer cultures → Cell lines (2D) |
| **Organ-on-a-chip / microphysiological systems** | Engineered microfluidic devices culturing cells or tissue under controlled flow, mechanical or multi-tissue conditions to mimic organ function. | Lung-on-a-chip, gut-on-a-chip, multi-organ body-on-a-chip, blood-brain-barrier chips | Static 3D cultures without fluidics → Organoids / 3D |
| **Ex vivo tissue / explants** | Tissue or organ slices kept viable outside the body and used standalone as an experimental or screening platform. Animal-derived tissue where an animal was harmed for this study is already captured as Ex-vivo in Q2; do not re-flag it. | Precision-cut liver slices, skin explants, retinal explants, isolated perfused organs | Cells dissociated and cultured → Cell lines / primary cells |
| **In silico / computational model** | Mathematical or computer models used to predict biological activity, toxicity or pharmacokinetics. | QSAR, PBPK, molecular docking, ML-based prediction, systems-biology models | Statistical analysis of clinical/epidemiological data → not a NAM; likely excluded at Q1 |
| **Other** | Anything that does not fit above. Specify the model or process name. | Cell-free systems with a biological readout, if you judge them a NAM | — |

### Overlap rules (current draft)
- **Human cells / tissue** is a source-based extra tag, selected in addition to the format-based label. Example: human iPSC-derived cells = Cell lines / primary cells (2D) + Human cells / tissue. Animal-derived models do not get this tag.
- **Ex vivo tissue / explants** (Q3a) vs **Ex-vivo** (Q2): animal tissue from an animal sacrificed for this study is Ex-vivo in Q2, and need not be repeated here. Human tissue has no Q2 equivalent, so it goes under Human cells / tissue (or Ex vivo tissue / explants where it is used as an explant platform).
- Multiple labels may be selected for one paper.

---

## Part 2. Lab animals and their groupings

Each animal maps to one Q2a species group (left). Higher levels show the broader taxonomy, for orientation.

### Hierarchy

```
Animals
├── Vertebrates
│   ├── Mammals
│   │   ├── Rodents
│   │   │   ├── Mice                      [Q2a: Mice]
│   │   │   ├── Rats                      [Q2a: Rats]
│   │   │   └── Other rodents             [Q2a: Other Rodents]
│   │   │       guinea pig, hamster, gerbil, chinchilla, mole-rat, squirrel
│   │   ├── Lagomorphs                    [Q2a: Other Rodents]
│   │   │   rabbit
│   │   ├── Non-human primates            [Q2a: Non-Human Primates]
│   │   │   rhesus macaque, cynomolgus macaque, marmoset, squirrel monkey,
│   │   │   baboon, chimpanzee, African green monkey
│   │   ├── Pigs / swine                  [Q2a: Pigs / Swine]
│   │   │   domestic pig, minipig
│   │   ├── Dogs / canines                [Q2a: Dogs / Canines]
│   │   │   beagle, other dog breeds
│   │   ├── Livestock (non-rodent, non-swine)  [Q2a: Livestock]
│   │   │   cattle, sheep, goat, horse
│   │   └── Other mammals                 [Q2a: Other]
│   │       cat, ferret, bat, opossum, dolphin, etc.
│   ├── Birds                             [Q2a: Birds / Avian]
│   │   chicken, quail, zebra finch, pigeon, turkey
│   ├── Fish                              [Q2a: Fish]
│   │   zebrafish, medaka, stickleback, salmon, trout
│   ├── Amphibians                        [Q2a: Other]
│   │   Xenopus (frog), axolotl
│   └── Reptiles                          [Q2a: Other]
│       lizard, snake, turtle
└── Invertebrates                         [Q2a: Invertebrates]
    ├── Insects: Drosophila melanogaster, honeybee, mosquito, silkworm
    ├── Nematodes: Caenorhabditis elegans
    ├── Molluscs: Aplysia, octopus, snail
    ├── Crustaceans: Daphnia, shrimp
    └── Other: planarian, sea urchin, Hydra
```

### Lookup table

| Animal | Group (Q2a) | Broader class |
|---|---|---|
| Mouse (*Mus musculus*) | Mice | Mammal › Rodent |
| Rat (*Rattus norvegicus*) | Rats | Mammal › Rodent |
| Guinea pig | Other Rodents | Mammal › Rodent |
| Hamster, gerbil | Other Rodents | Mammal › Rodent |
| Rabbit | Other Rodents | Mammal › Lagomorph |
| Rhesus / cynomolgus macaque, marmoset, squirrel monkey, baboon | Non-Human Primates | Mammal › Primate |
| Pig, minipig | Pigs / Swine | Mammal › Ungulate |
| Dog (e.g. beagle) | Dogs / Canines | Mammal › Carnivore |
| Cow, sheep, goat, horse | Livestock | Mammal › Ungulate |
| Cat, ferret | Other | Mammal › Carnivore |
| Chicken, quail, finch | Birds / Avian | Bird |
| Zebrafish, medaka, salmon | Fish | Fish |
| Xenopus, axolotl | Other | Amphibian |
| Lizard, snake, turtle | Other | Reptile |
| *Drosophila*, honeybee, mosquito | Invertebrates | Insect |
| *C. elegans* | Invertebrates | Nematode |
| Planarian, sea urchin, snail, octopus | Invertebrates | Other invertebrate |
| Species named in the abstract that matches none of the above | Other (specify species) | — |
| Animal used, but species not stated | Unclear / Not reported (add keywords) | — |

### Notes on judgement calls
- **Rabbit** sits under *Other Rodents* because the guidelines list it there, although rabbits are taxonomically lagomorphs. This keeps the groups practical rather than strictly phylogenetic.
- **Horse** is placed under *Livestock*; veterinary-clinical horse papers are generally excluded at Q1 as case/clinical studies.
- **Pigs** are their own group, so they are not under Livestock.
- **Horses, cats, amphibians and reptiles** do not have their own group. Use *Other* and enter the species name (required). Several Other entries can be added with the + control, and each gets its own sex entry in Q2b. If any turn up often in the full dataset, they can be collated into groups later.
- Embryonic or larval stages (e.g. zebrafish embryos, *Xenopus* tadpoles) still count as animals under the guidelines.

---

## Part 3. Normalisation notes for the final dataset (Q5)

Annotators may reach the same concept by different routes. Merge as follows when building the final dataset:

| Concept | Accepted annotator routes | Merge to |
|---|---|---|
| Gene / cell therapy | Substance (Nucleic acid therapeutic) and/or Intervention (Genetic modification) | Gene / cell therapy |
| Engineered microorganism as therapy | Substance (Microorganism / probiotic) and/or Intervention (Genetic modification) | Engineered microorganism |
| Purified plant-derived compound | Natural product / extract or Small molecule / drug | Small molecule (name retained) |
