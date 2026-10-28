---
doc_id: TKB-PRS-001
title: TrunkBelay product requirements and specifications
project: TrunkBelay
doc_type: Product requirements and specifications
version: '0.5'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Status of every requirement on paper at TRL 3 (TKB-CAL-001); targets unchanged
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's decisions 16A, 17B, 18C and 19A carried out (TKB-DDR-003); R9 target restated by Amish; status of R2, R4, R7 and R9 updated
- version: "0.4"
  date: '2026-10-25'
  author: Amish Chadha
  change: "Kit 1.9.1 upgrade: becomes the product requirements and specifications TKB-PRS-001 (replaces TKB-REQ-001); R1 to R10 migrated to PR-001 to PR-010 with targets unchanged, tolerance, units and the user requirement each traces to; PR-011 to PR-018 added for needs the REQ table left implicit; PR-018 records the tether fix TKB-DEC-001 D-S1"
- version: '0.5'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'Amish''s decisions of 2026-10-25 ("i concur with your recommendations"): PR-001 verified by a 3.5 kN proof test and a test to failure of a sample frame (O7); PR-003 lean limit 20 deg and the drill rule for the frame side (O8)'
---

# TrunkBelay product requirements and specifications

What the design must do, each requirement traced to a user need in TKB-URS-001. PR-001 to PR-010 are the requirements R1 to R10 of TKB-REQ-001 with the same targets (R9 as Amish restated it on 2026-10-03); PR-011 to PR-018 make explicit what the design already does. Targets remain proposals for review with a co-design partner. Status comes from the calculation note TKB-CAL-001 v0.3 and the STEM check TKB-STM-001. Method: STANDARDS section 22.

Amish Chadha, 2026-10-03, on the recommendations put to him: "i agree with all the 46 recommendations you provided. please proceed." For TrunkBelay that is decisions 16A (R2: keep the drill rule, double-acting collar as the recorded fallback), 17B (R4: pack the victim set pre-rigged), 18C (R7: the helpers haul the rope bag on a tag line and the collar frame goes to aluminium) and 19A (R9: keep the auto-locking descender and evacuation triangle, seek group purchase, restate the cost target). The design decisions register (TKB-DEC-001) and decision record TKB-DDR-003 hold the detail.

> **Safety:** These requirements describe rope rescue equipment that holds a person at height. Meeting them on paper does not make the kit safe to use. Each is verified by test at TRL 4, and the kit is not used on a person until PR-001 has been proof-tested on cut trunk sections and the drill has been run with a dummy at low height.

Table 1. Product requirements and specifications.

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status | Was |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Collar holds on a palm trunk | The anchor shall hold a 2.5 kN (562 lbf) static downward load on wet trunk sections without slipping more than 20 mm | 2.5 | Slip 20 mm max | kN | Analysis (TKB-CAL-001 B, C), TRL 3; proof test on cut trunk sections at 3.5 kN and a test to failure of a sample frame, TRL 4 (TKB-DEC-001 O7, decided by Amish 2026-10-25) | Met on paper; the friction on wet bark, settlement (10 mm, 14 to 18 mm with pad shear) and the strength margin (about 5.1:1, 4.5:1 with an unequal chain split; the stronger frame is the fallback if the test to failure shows less than 5:1, O7) are to verify at TRL 4 (locking factor 1.54) | R1 |
| PR-002 | UR-002 | Safety | Holds when the load direction changes | The anchor shall not slip more than 50 mm when a 100 kg (220 lb) test mass passes the collar during lowering | 50 | Max | mm | Drop and transition tests on trunk sections, the upward case as a misuse test only, TRL 4 | At risk for an upward pull: the single top chain cannot hold it. Decided by Amish (16A): the drill rule stays (collar at least 300 mm above the victim's attachment); the double-acting collar is the recorded fallback | R2 |
| PR-003 | UR-003 | Physical architecture | Fits common palms | The anchor shall fit trunks 200 to 450 mm (8 to 18 in) across, leaning no more than 20 deg from vertical, with no tools; on a leaning trunk the frame is set on the favourable side by the drill rule (lean limit and drill rule decided by Amish, 2026-10-25, TKB-DEC-001 O8) | 200 to 450; lean 20 max | Full range, no tools | mm; deg | Analysis of the model on 200, 300 and 450 mm trunks (TKB-CAL-001 E2) and of the lock on a leaning trunk (TKB-STM-001 S31), TRL 3; fit trials on surveyed palms and the drill on a leaning palm, TRL 4 | Met by design for diameter: the V and the 110-link chain fit the range, 15 links to spare on 450 mm; lean: locking factor 1.21 at 20 deg on the adverse side on the assumed friction, to confirm by test | R3 |
| PR-004 | UR-004 | Usability | Quick to rig | A trained climber shall fix the collar and clip the victim in within 5 minutes once in position | 5 | Max | min | Analysis (TKB-CAL-001 E3), TRL 3; timed drills at 3 m height, TRL 4 | At risk: about 4.5 minutes estimated, a thin margin | R4 |
| PR-005 | UR-005 | Performance | Controlled lowering | The kit shall hold the descent of a 100 kg (220 lb) load under 0.5 m/s with a hand force under 150 N (34 lbf) | 150 | Max; speed 0.5 m/s max | N | Analysis (TKB-CAL-001 D1), TRL 3; lowering tests with a test mass, TRL 4 | Met on paper: about 80 N at the hand with the brake carabiner | R5 |
| PR-006 | UR-006 | Performance | Rope length | The rope shall lower a person from 25 m (82 ft) | 25 | Min | m | Inspection and analysis (TKB-CAL-001 E1), TRL 3; measured, TRL 4 | Met: 30 m of rope, 28 m needed | R6 |
| PR-007 | UR-007 | Physical architecture | Portable | What the rescuer carries up the trunk shall weigh under 5 kg (11 lb) and hang from the harness, hands-free | 5 | Max | kg | Analysis (TKB-CAL-001 F2), TRL 3; weighing and climbing trial, TRL 4 | Met on paper: 4.67 kg carried; the 3.7 kg bag is hauled up on the tag line (18C); whole kit 8.4 kg | R7 |
| PR-008 | UR-008 | Safety | No damage to the palm | After a full test lowering no bark cut shall be deeper than 5 mm | 5 | Max | mm | Analysis (TKB-CAL-001 G1; TKB-STM-001 S19, S20), TRL 3; inspection after trials, TRL 4 | Met on paper, at risk on green wood: pads 1.9 MPa mean (about 3.8 MPa at the lower edge) against 9.3 MPa air dry, 4.6 to 5.6 MPa green; bare links mark about 0.3 to 1.3 mm (TKB-STM-001 S19 to S21) | R8 |
| PR-009 | UR-009 | Cost | Cost | Parts shall cost under USD 850 per kit at single-kit prices, keeping the auto-locking descender and the evacuation triangle; group purchase by the training partner to lower it, one kit per climber group | 850 | Max | USD | Costed bill of materials (TKB-CAL-001 H2), TRL 3 | Met on paper: USD 828 per kit (USD 22 under) | R9 |
| PR-010 | UR-010 | Usability | Teachable | Climbers new to the kit shall complete a supervised rescue drill after a half-day session | 0.5 | Max | day | Training trial with the partner programme, TRL 4 | To verify at TRL 4: cannot be shown on paper | R10 |
| PR-011 | UR-011 | Safety | Holds if the rescuer lets go | The lowering device shall lock and hold the load when the rescuer releases the handle or the brake strand, and when the handle is pulled too far (anti-panic) | 100 | Held hands-off, min | kg | Inspection of the bought descender's rating and certificate (BOM line 17; EN 341 class A or EN 12841 type C), TRL 3; dummy drill, TRL 4 | Met by design | |
| PR-012 | UR-012 | Safety | Head up once freed | The victim set shall hold the person head up once the feet are freed: an evacuation triangle (EN 1498 class B) round the hips and a chest sling on one victim carabiner | 1 | Person, 100 kg | person | Inspection (BOM lines 16, 19, 20; TKB-STM-001 S22), TRL 3; dummy drill, TRL 4 | Met by design; fitting time on a head-down dummy to verify at TRL 4 | |
| PR-013 | UR-013 | Materials | Survives the climate | No part shall corrode through or lose strength in two years of use and humid storage: bare 6082-T6 frame, stainless fixings in rivet nuts with barrier paste, zinc-plated keeper, soft goods stored in the bag | 2 | Min | years | Analysis (TKB-STM-001 S25, S26), TRL 3; inspection after the trial season, TRL 4 | To verify at TRL 4 (corrosion and ageing are plausible, not shown) | |
| PR-014 | UR-014 | Maintenance | Wear parts replaceable | The pads, sleeve, keeper, lock pin, rope and soft goods shall be inspectable by eye and replaceable with hand tools | 0 | Special tools | tools | Inspection of the build plan (TKB-BLD-001), TRL 3 | Met by design | |
| PR-015 | UR-015 | Safety | Recognised rescue gear | The bought rescue gear shall meet EN 341 class A or EN 12841 type C (descender), EN 362 class B (carabiners), EN 1891 type A (rope) and EN 1498 class B (triangle) or equal; the kit shall be marked as not certified equipment | 4 | All four items | items | Inspection of the BOM and the marking on the spine (TKB-BLD-001 sheet TKB-DWG-105), TRL 3 | Met by design | |
| PR-016 | UR-016 | Physical architecture | Made locally | The made parts shall be cut from plate, sheet, tube and rubber sheet, drilled and AC TIG welded, with no casting, machining or special tooling | 0 | Special processes | processes | Inspection of the build plan (TKB-BLD-001), TRL 3 | Met by design (an AC TIG welder is needed) | |
| PR-017 | UR-017 | Physical architecture | Patent design-around | The collar shall have no ratcheting cinch, cam or cleated gripping plate (3M DBI-SALA Cynch-Lok geometry) | 0 | Such features | features | Inspection of the drawings and the precis (TKB-PRC-001), TRL 3 | Met by design | |
| PR-018 | UR-004 | Safety | Fixed end captive | The chain's fixed end shall stay attached to the frame when the keeper is off, without crowding the brake carabiner in the spare eye | 1 | Tether, min | tether | Inspection of the model (cad/fidelity.json, no interference) and the build plan step 5, TRL 3 | Met by design: grade 80 connecting link through the 10 mm tether hole (TKB-DEC-001 D-S1) | |

Categories: physical architecture, performance, materials, usability, safety, maintenance, cost. Status: met on paper, met by design, at risk, not met, over target, withdrawn, to verify at TRL 4.

## Assumptions

- A second climber is often on site or nearby when a climber is stranded, as in the reported cases.
- The rescuer can reach and work just below the victim using their own climbing device.
- Coconut bark and fibre can carry a collar load without crushing, if the load is spread (TKB-STM-001 S19).
- Victims can be fitted with a sling while hanging head down.
