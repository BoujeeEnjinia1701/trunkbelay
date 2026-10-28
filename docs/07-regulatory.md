---
doc_id: TKB-REG-001
title: TrunkBelay regulatory and standards register
project: TrunkBelay
doc_type: Regulatory and standards register
version: "0.1"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: First register (kit 1.9.1 upgrade), complete for stages P0 to P3
---

# TrunkBelay regulatory and standards register

TrunkBelay is published as an open engineering reference, not as certified rescue or fall-protection equipment, and it is not placed on any market. Its bought rescue gear is specified to recognised standards (G3 to G6), and those certificates are what a user relies on. The made collar is an anchor for a rescue, and no certification route for a home-built palm anchor is known: on paper it would not pass the 12 kN static test of EN 795 (G2), which is the main gap if a partner ever wants a certified product. In India, where the first co-design partner is sought, no mandatory standard for rope rescue equipment was found; that is to assess with the partner and a qualified reviewer (G8, G9). Not legal advice; anything marked "to assess" needs a qualified reviewer before any product claim. Method: STANDARDS section 23.

Table 1. Regulatory and standards register.

| # | Standard or regulation | Jurisdiction | What it covers | Applicability to this design | Owner (role) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Regulation (EU) 2016/425 on personal protective equipment | European Union | Placing PPE on the EU market: risk categories, conformity assessment and CE marking | Only if a kit were ever sold or supplied in the EU; an open design shared without being placed on the market is outside it | Project lead | To assess (does not apply while nothing is placed on the market) |
| G2 | EN 795:2012, protection against falls from a height, anchor devices | European Union; reference elsewhere | Anchor devices for one or more users, types A to E; static strength test at 12 kN (metallic) or 18 kN (textile without a service-life marking), plus dynamic tests | The collar acts as a transportable anchor (type B class). Sized for 2.5 kN static (PR-001) with an estimated breaking load of about 5.7 kN, it would not pass the 12 kN static test | Design lead | Certification needed later; on paper not met (TKB-STM-001 S30; TKB-DEC-001 O7) |
| G3 | EN 341:2011, descender devices for rescue | European Union; reference elsewhere | Rescue descenders: classes A to D by descent energy (class A 7.5 MJ), descent speed 0.5 to 2 m/s, holding force at most 200 N, touch surfaces at most 48 C | The bought auto-locking descender (BOM line 17) is specified as EN 341 class A or EN 12841 type C or equal | Design lead | Applies when bought (ask for the declaration of conformity; PR-011, PR-015) |
| G4 | EN 362:2004, connectors | European Union; reference elsewhere | Carabiners and connectors for fall protection; class B (basic) connectors | The three locking carabiners (BOM line 16) | Design lead | Applies when bought (PR-015) |
| G5 | EN 1891:1998, low stretch kernmantle ropes | European Union; reference elsewhere | Type A ropes 8.5 to 16 mm: at least 22 kN, 15 kN for 3 minutes with figure-eight terminations, elongation and sheath slippage limits | The 11 mm lowering rope (BOM line 18) | Design lead | Applies when bought (PR-015; TKB-STM-001 S12) |
| G6 | EN 1498:2006, rescue equipment, rescue loops | European Union; reference elsewhere | Rescue loops and evacuation triangles, classes A to C | The evacuation triangle, class B (BOM line 19) | Design lead | Applies when bought (PR-012, PR-015) |
| G7 | EN 818-2, short link chain for lifting purposes, grade 8 | European Union; reference elsewhere | Dimensions, working load limits and test forces of grade 8 lifting chain | The 6 mm grade 80 chain and its connecting and master links (BOM lines 11 to 14): 7.8 mm minimum link opening, 45.2 kN minimum breaking force (TKB-STM-001 S11, S27) | Design lead | Applies when bought (ask for the certificate; TKB-DEC-001 item 2) |
| G8 | Indian Standards for fall protection equipment, for example IS 3521 (industrial safety belts and harnesses) | India | Bureau of Indian Standards specifications for safety harnesses and belts | Whether any Indian Standard or Quality Control Order covers a rescue anchor, descender or kit used by coconut climbers is not known | Co-design partner | To assess |
| G9 | Occupational safety law for agricultural and plantation work, and the Coconut Development Board's climber training and insurance schemes | India (Kerala and Tamil Nadu first) | Duties of employers and schemes for climbers; training content of the Friends of Coconut Tree scheme | Whether the drill could be added to the training scheme, and whether the scheme's insurance has conditions on rescue equipment | Co-design partner | To assess |
| G10 | NFPA 2500, operations and training for technical search and rescue incidents and life safety rope and equipment for emergency services | United States; reference elsewhere | Life safety rope, harnesses and auxiliary equipment for emergency services (it absorbed the former NFPA 1983) | The bought descender class is also listed to NFPA 2500 (Petzl catalogue); a reference for fire services elsewhere | Design lead | Does not apply (reference only) |
| G11 | ANSI/ASSP Z359 family, fall protection, including Z359.4 assisted-rescue and self-rescue systems | United States; reference elsewhere | Rescue systems and components for work at height | Reference for rescue practice; the kit is not marketed in the United States | Design lead | Does not apply (reference only) |
| G12 | Patents: 3M DBI-SALA Cynch-Lok ratcheting cinch geometry; CA2681870C (Bashlin, lapsed 2015); WO2012131439A1 (ceased) | International | Freedom to operate | Design-around kept (PR-017): no ratchet, cam or cleated gripping plate (TKB-PRB-001, TKB-PRC-001) | Project lead | Met by design (preliminary screen, not legal advice) |

Status: to assess, applies, does not apply, met by design, certification needed later.

## Sources

- SATRA. "EN 341:2011 Descender Devices for Rescue." https://www.satra.com/spotlight/article.php?id=439 (checked 2026-10-25) (G3).
- Vandernet. "EN 795 Standard Explained." https://www.vandernet.com/tuotetiedostot/EK-FPPFM30x/EN_795_standard_explained.pdf (checked 2026-10-25) (G2).
- Vandernet. "EN 1891 Standard Explained." https://vandernet.com/tuotetiedostot/EK-FPPFM20x/EN_1891_standard_explained.pdf (checked 2026-10-25) (G5).
- S3i. "Lifting Chain, Grade 80, Alloy Steel." https://www.s3i.co.uk/lifting-chain-grade-80.php (checked 2026-10-25) (G7).
- Petzl. "Professional catalogue 2026: I'D S certifications." https://catalogs.petzl.com/Petzl-pro-catalog-2026/en/68-Rope-Clamps.html (checked 2026-10-25) (G3, G10).
- Piatt, Lance. "Rope Rescue Safety Factors." Rigging Lab Academy, July 3, 2023. https://rigginglabacademy.com/rope-rescue-safety-factors/ (checked 2026-10-25) (G2, safety factor practice).
- Regulation (EU) 2016/425, EN 362:2004, EN 1498:2006, IS 3521, NFPA 2500 and ANSI/ASSP Z359.4 are cited by number and title only; their texts were not consulted for this register, and each applicability is to be confirmed by the role named.
- Patent references as screened in TKB-PRB-001 (G12).
