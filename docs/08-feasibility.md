---
doc_id: TKB-FEA-001
title: TrunkBelay feasibility assessment
project: TrunkBelay
doc_type: Feasibility assessment
version: '0.2'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: First assessment (kit 1.9.1 upgrade) of the TRL 3 design, option A
- version: '0.2'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'O8 decided (2026-10-25)'
---

# TrunkBelay feasibility assessment

Feasible on paper, with one deciding unknown: the collar (option A) is constructable from plate, tube and bought rigging, its lowering numbers hold with margin, and its parts are easy to buy, but whether it locks on a wet palm depends on a friction nobody has measured, and its strength margin is below the low end of rescue practice in the worst case, a safety trade-off Amish decided on 2026-10-25: a 3.5 kN proof load and a test to failure of a sample frame at TRL 4, with a stronger frame as the fallback (O7). Method: STANDARDS section 23.

> **Safety:** Feasible on paper is not safe to use. Nobody is lowered with this kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.

Table 1. Feasibility by aspect.

| Aspect | Assessment | Rating | Risks and notes | Evidence |
| --- | --- | --- | --- | --- |
| Design: grip on the trunk | The self-locking couple is sound physics; the full equilibrium gives a locking factor of 1.63 against 1.54 in the simplified method, both on an assumed combined friction of 0.9; settlement 14 to 18 mm with pad shear against 20 | Medium | Friction of rubber and sleeved chain on wet coconut bark is unmeasured; if it were below 0.58 the collar would slide on a 200 mm trunk | TKB-STM-001 S3, S4; TKB-CAL-001 [B1] to [B5] |
| Design: strength | Every frame part at 1.21 times its welded proof strength or better at 2.5 kN, even with all of the chain's pull on one slot (D-S2); chain 4.1 in one leg, rope 5.7 at the knot | Low | Estimated breaking load about 5.0 kN, 5.1:1 on the one-person load, 4.5:1 in the worst chain split: below the 5:1 to 10:1 of rescue practice (TKB-STM-001 S30, plausible until the TRL 4 test to failure; TKB-DEC-001 O7, decided 2026-10-25) | TKB-STM-001 S6 to S12, S30; TKB-CAL-001 [C1] to [C6], [C1b], [C4b] |
| Design: lowering | 80 N at the brake hand; 25 m lowering turns 24.8 kJ into heat, within a class A descender's rating | High | The bought descender's own data replaces the assumed rope friction | TKB-STM-001 S13, S14, S29; TKB-CAL-001 [D1], [D2] |
| Design: use at height | Rigging about 4.5 minutes against 5; collar must be set at least 300 mm above the victim's attachment; on a leaning trunk the lock falls toward 1.0 at 30 deg | Medium | Thin time margin; whether a rescuer can reach above the attachment is only shown by a drill; 20 deg lean limit and frame-side drill rule decided by Amish on 2026-10-25 (O8) | TKB-STM-001 S17, S24, S31; PR-002, PR-004 |
| Materials | 6082-T6 plate and RHS, natural rubber, grade 80 chain, polyamide rope and webbing | Medium | Galvanic contact of steel and aluminium, polymer ageing in sun and heat (plausible, not shown) | TKB-STM-001 S25, S26 |
| Manufacturing and assembly | Profile cutting, drilling, AC TIG welding, rubber bonding, rivet nuts; ten assembly steps | Medium | An AC TIG welder and a welder who knows aluminium are needed; weld quality decides the frame's strength | TKB-BLD-001; TKB-DWG-101 to 109 |
| Power and controls | None: a passive mechanism worked by hand | High | Not applicable | TKB-PRC-001 |
| Supply of parts | Chain, carabiners, descender, rope, triangle and slings are catalogue items | High | Certified rescue gear is most of the cost (USD 280 descender, USD 140 triangle in the BOM; a cited branded descender lists at USD 421) | bom/bom.csv; TKB-MKT-001 |
| Model and checks | Detailed D3 model of every option passes the fidelity check; 244 constructability checks pass on 200, 300 and 450 mm trunks | High | The D3 model found one fit failure (tether quick link, D-S1) and the independent review one strength failure (cleat web, D-S2), both fixed | cad/fidelity.json; `python cad/src/model.py --check` |

Ratings: High, Medium, Low.
