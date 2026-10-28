---
doc_id: TKB-PLN-001
title: TrunkBelay project plan
project: TrunkBelay
doc_type: Project plan
version: '0.2'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: First project plan (kit 1.9.1 upgrade) at stage P3
- version: '0.2'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'O6 to O8 decided by Amish (2026-10-25); rig for the 3.5 kN proof load and the test to failure'
---

# TrunkBelay project plan

TrunkBelay is at stage P3 (design outputs, TRL 3): the constructable design of option A, its model at detail level D3, drawings, priced BOM, build plan and the pipeline documents are in place. The next gate, P4 (verification, TRL 4), is on hold while the portfolio cap is P3. Decisions requested from Amish now: the concept selection between options A and B (TKB-DEC-001 O5), the strength target (O7) and the appearance of the new renders (O6). Method: STANDARDS sections 19 and 23.

> **Safety:** P4 work is the first time the kit meets a load and a person. It starts with the friction and proof tests on cut trunk sections and a dummy drill at low height, never with a person (TKB-BLD-001, section 6).

## Workstreams

Table 1. Workstreams.

| Workstream | Owner (role) | Deliverable | Status |
| --- | --- | --- | --- |
| Problem, users and requirements | Project lead | TKB-PRB-001 v0.4, TKB-URS-001, TKB-PRS-001, TKB-RTM-001 | Done at P3; to confirm with a co-design partner |
| STEM check and concept options | Design lead | TKB-STM-001, TKB-OPT-001, TKB-DDR-004 | Done; STEM check open (field data); concept selection awaiting Amish (O5) |
| Design and calculations | Design lead | Model (`cad/src/model.py`, D3), TKB-CAL-001 v0.3, drawings TKB-DWG-001 and 101 to 109, BOM | Done at TRL 3 |
| Build plan | Design lead | TKB-BLD-001 | Done (a plan, not yet built) |
| Regulatory, risk and market | Project lead | TKB-REG-001, TKB-RSK-001, TKB-MKT-001, TKB-FEA-001 | Done at P3; G8 and G9 to assess with the partner |
| Co-design partner | Project lead | Agreement with a training programme, a fire station or a climbers' collective | Not started (none approached) |
| Verification (P4) | Test partner | Friction and proof tests on trunk sections, dummy drill, timed drill | On hold (stage cap P3) |
| Validation (P5) | Co-design partner | Training trial and supervised drills with climbers | On hold |

## Resources needed

Table 2. Resources for P4 (planned, on hold). Costs are estimates and are not added to the value-engineering target.

| Resource | Deliverable | Effort | Estimated cost (USD) |
| --- | --- | --- | --- |
| One prototype kit (BOM) | The kit to test | Fabrication about 2 days | 828 (BOM) |
| Cut coconut trunk sections, 200, 300 and 450 mm, wet and dry | Friction and proof test specimens | 1 day with the partner | To assess |
| Test rig able to apply 2.5 kN, the 3.5 kN proof load and a sample frame's breaking load (about 5 kN or more), and measure slip (CalRig shared block) | Friction, proof, slip and failure tests (O7) | 2 to 3 days | To assess |
| 100 kg test dummy and a 3 m training pole or palm | Dummy drill and timed drill | 1 day | To assess |
| Trainer from the partner programme | Drill card and the half-day session | 1 day | To assess |

## Stage gates

Table 3. Stages (P4 to P6 on hold while the stage cap is P3).

| Stage | Gate criteria | Status |
| --- | --- | --- |
| P0 Proposal | PRB with users and stakeholders, STM, OPT, REG, FEA, PLN | Met (2026-10-25) |
| P1 Definition | URS, PRS draft, RSK with hazard analysis, MKT, REG complete | Met (2026-10-25) |
| P2 Design inputs | PRS with targets and verification, CAL, RTM, concept selection DDR, STM closed, feasibility closed | Met except: STM open (18 plausible rows on field data, S30 among them until the test to failure Amish decided on 2026-10-25, O7) and the concept selection awaiting Amish (O5) |
| P3 Design outputs | Model, STEP, drawings, priced BOM, build plan, DEC, design FMEA, traceability complete | Met (2026-10-25); cad/fidelity.json passes at D3 |
| P4 Verification | Friction and proof tests on trunk sections; dummy drill; timed drill; RSK updated | On hold |
| P5 Validation | Training trial with climbers; field use with a partner | On hold |
| P6 Commercialization | Only with a named deployment partner | On hold |

## Next steps and decision requested

1. Amish decides O5 (option A or B) in TKB-DEC-001; O6, O7 and O8 were decided on 2026-10-25.
2. The coordinator renders `media/options.png` and the product views on the studio machine (Blender Cycles), replacing the labelled preview.
3. When the cap allows P4: approach the Friends of Coconut Tree training programme and a Kerala Fire and Rescue Services station; the first test is the friction of the pads and sleeved chain on wet trunk sections.

## References

Every source cited in this repo's documents, Chicago style.

- Beam Dimensions. "6082 Alloy Aluminium Properties, EN 1999 (Welded)." Accessed October 25, 2026. https://beamdimensions.com/materials/Aluminium/EN_1999_2007_Welded/6082.
- Broschat, T. K. "Palm Morphology and Anatomy." ENH1212. Gainesville: University of Florida IFAS Extension, 2019. https://edis.ifas.ufl.edu/pdf/EP/EP47300.pdf.
- Buckingham Manufacturing. "SuperSqueeze Pole Top Rescue 488P." Accessed September 30, 2026. https://buckinghammfg.com/products/supersqueeze-pole-top-rescue-488p/.
- FAO. "Coconut Wood: Basic Density." Accessed October 25, 2026. https://www.fao.org/4/w7731e/w7731e07.htm.
- George, J., et al. Survey of coconut tree climbers in Kerala and Tamil Nadu. *Journal of Clinical and Diagnostic Research*, 2012. https://www.jcdr.net/article_fulltext.asp?id=1829.
- Haness Supply. "Petzl D020AA00 I'D S Descender/Belay Device." Accessed October 25, 2026. https://www.hanessupply.com/petzl-d020aa00.
- *International Journal of Emergency Medicine*. Coconut-related trauma at a southern Indian tertiary centre, 2021 to 2023. 2025. https://link.springer.com/article/10.1186/s12245-025-00816-4.
- *Medical Journal of Australia*. "Barking Up the Wrong Tree: Injuries Due to Falls from Trees in Solomon Islands." 2014. https://www.mja.com.au/journal/2014/201/11/barking-wrong-tree-injuries-due-falls-trees-solomon-islands.
- Oliunid. "Petzl Pitagor Evacuation Triangle." Accessed October 25, 2026. https://www.oliunid.com/petzl-pitagor-evacuation-triangle.
- Onmanorama. Reports of suspended coconut climbers rescued in Kerala, October 2, 2025; January 31, 2026; February 8, 2026. https://www.onmanorama.com/news/kerala/2025/10/02/coconut-plucker-hanging-upside-down-rescued-by-friend-firefighters.html; https://www.onmanorama.com/news/kerala/2026/01/31/coconut-tree-man-trapped-fire-rescue.html; https://www.onmanorama.com/news/kerala/2026/02/08/fire-officials-save-60-year-old-man-hanging-upside-down-coco.html.
- Petzl. *Professional Catalogue 2026*, "Rope Clamps" and descenders. Accessed October 25, 2026. https://catalogs.petzl.com/Petzl-pro-catalog-2026/en/68-Rope-Clamps.html.
- Piatt, Lance. "Rope Rescue Safety Factors." Rigging Lab Academy, July 3, 2023. https://rigginglabacademy.com/rope-rescue-safety-factors/.
- Press Information Bureau, Government of India. Coconut Development Board insurance scheme for climbers. 2022. https://www.pib.gov.in/PressReleasePage.aspx?PRID=1880306&reg=3&lang=2.
- Rana, M., A. Das, and M. Ashaduzzaman. "Physical and Mechanical Properties of Coconut Palm (*Cocos nucifera*) Stem." *Bangladesh Journal of Scientific and Industrial Research* 50, no. 1 (2015): 39 to 46. https://banglajol.info/index.php/BJSIR/article/view/23808.
- S3i. "Lifting Chain, Grade 80, Alloy Steel." Accessed October 25, 2026. https://www.s3i.co.uk/lifting-chain-grade-80.php.
- Saftgard. "3M DBI-SALA 1204075 Cynch-Lok Pole Climbing Device." Accessed September 30, 2026. https://www.saftgard.com/products/3m-dbi-sala-1204075-cynch-lok-pole-climbing-device-1204075/.
- SATRA. "EN 341:2011 Descender Devices for Rescue." Accessed October 25, 2026. https://www.satra.com/spotlight/article.php?id=439.
- Skyland Equipment. "CT Sparrow 200 R Rescue Descender." Accessed October 25, 2026. https://skylandequipment.com/products/ct-sparrow-200.
- Vandernet. "EN 795 Standard Explained" and "EN 1891 Standard Explained." Accessed October 25, 2026. https://www.vandernet.com/tuotetiedostot/EK-FPPFM30x/EN_795_standard_explained.pdf; https://vandernet.com/tuotetiedostot/EK-FPPFM20x/EN_1891_standard_explained.pdf.
- *World Neurosurgery*. Spinal injuries after coconut tree falls at a Tanzanian referral institute. 2023. https://www.sciencedirect.com/science/article/abs/pii/S1878875023004023.
- Patents CA2681870C and WO2012131439A1, as screened in TKB-PRB-001. https://patents.google.com/patent/CA2681870C/en; https://patents.google.com/patent/WO2012131439A1/en.
- Standards cited by number and title only (text not consulted): Regulation (EU) 2016/425; EN 341:2011; EN 362:2004; EN 795:2012; EN 818-2; EN 1498:2006; EN 1891:1998; EN 1995-1-1; EN 1999-1-1; IS 3521; NFPA 2500; ANSI/ASSP Z359.4.
