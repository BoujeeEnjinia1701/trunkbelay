---
doc_id: TKB-CAL-001
title: TrunkBelay sizing calculations
project: TrunkBelay
doc_type: Calculation note
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue at TRL 3, on the constructable design of TKB-DDR-002
---

# TrunkBelay sizing calculations

On paper, the constructable TrunkBelay collar locks on every trunk from 200 to 450 mm with a locking factor of 1.54 or more, holds the 2.5 kN load of R1 with every steel part at 2.1 times yield or better, and lets one rescuer lower a 100 kg person 25 m with about 80 N at the brake hand. Its weak points are friction, mass and cost: the lock rests on an assumed friction on wet bark that must be measured first, the kit weighs 8.9 kg against a 5 kg target, and it costs USD 758 against a USD 100 per-kit target. Every figure below comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are the sizes in the STEP file, the drawings and the build plan. Tags in square brackets ([A1], [B4] ...) match the script output and `results.csv`.

These are first-principles screening estimates for a paper proof of concept. They do not replace a proof test of the collar on cut palm trunk sections or a timed drill, which are TRL 4 work.

> **Safety:** TrunkBelay holds and lowers a person at height. These numbers are for a design review only. The kit is not certified rescue or fall-protection equipment, and nobody is lowered with it before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.

## 1. Assumptions

*Table 1. Assumptions.*

| # | Assumption | Value | Basis |
| --- | --- | --- | --- |
| 1 | Design person | 100 kg, plus 0.96 kg of triangle, sling and carabiner | TKB-REQ-001, R2 and R5 |
| 2 | Static load the collar is sized for | 2.5 kN (R1) | TKB-REQ-001, R1 |
| 3 | Friction on wet coconut bark | Rubber pad 0.5; webbing-sleeved chain 0.4 | Judgement for rubber and nylon on wet fibrous wood; first item to measure (TKB-DDR-002, A1) |
| 4 | Lever height | The chain line above the bottom edge of the bars, 160 mm (conservative: the bars bear at their bottom edge as the frame cocks) | Model |
| 5 | Pad rubber | 60 to 70 Shore A, compression modulus 6 MPa, contact patch 40 mm wide on a round trunk | Rubber class |
| 6 | Steel | S355, yield 355 MPa; fillet welds 290 MPa allowed (E7018) | BOM lines 1 to 5 |
| 7 | Chain | 6 mm grade 80: working load limit 11.2 kN, minimum breaking force 45 kN, 0.80 kg/m | Catalogue class |
| 8 | Rope | 11 mm EN 1891 type A: at least 22 kN, 65 % at a figure-eight loop, 4 % stretch from 50 to 150 kg, 78 g/m | Standard minimum and catalogue class |
| 9 | Descender | Rope friction 0.2 over 540 deg of contact (ratio 6.6) | Conservative; confirm with the maker's data |
| 10 | Carabiners | Aluminium, class B, 25 kN on the long axis, 85 g | EN 362 class |
| 11 | Bark | No cut below 2 MPa under rubber; the outer coconut stem is far stronger in crushing | Judgement; inspected at TRL 4 (R8) |

## 2. Loads [A]

- [A1] Holding a 100 kg person, the collar carries 0.99 kN. The R1 load of 2.5 kN is 2.5 times that.
- [A2] If slack is left when the feet are freed, the person drops onto the rope. On 1 m of rope a 30 mm drop gives about 2.6 kN, 50 mm 2.9 kN and 100 mm 3.4 kN. The drill takes all slack through the descender first, so the drop stays under 30 mm; the strength factors in section 4 cover the small excess over 2.5 kN.

## 3. Grip on the trunk [B]

The collar is self-locking. The load hangs from the load eye at a distance e from the trunk axis; the chain holds the frame at a height h above the bottom of the bars. Taking moments, the bars press the bark with a force N = W e / h and the chain presses the far side with the same force. Friction at both places holds the frame if (friction at the pads + friction at the chain) x N is at least W, that is if the combined friction is at least h / e. The ratio of the friction available to the friction needed is the locking factor. It does not depend on the load: the grip rises in step with it.

*Table 2. Grip at the R1 load of 2.5 kN.*

| Trunk | Load line from the axis | Friction needed | Locking factor | Bars press (each pad) | Chain tension |
| --- | --- | --- | --- | --- | --- |
| 200 mm [B1] | 273 mm | 0.58 | 1.54 | 4.3 kN (2.5 kN) | 3.3 kN |
| 300 mm [B2] | 331 mm | 0.48 | 1.86 | 5.2 kN (3.0 kN) | 4.2 kN |
| 450 mm [B3] | 418 mm | 0.38 | 2.35 | 6.5 kN (3.8 kN) | 5.5 kN |

- [B4] The smallest locking factor is 1.54, on the smallest trunk. The friction of the chain's full wrap round the trunk is extra and is not counted.
- [B5] Under 2.5 kN the pads squash about 3.1 mm (1.9 MPa) and the chain seats up to 2.9 mm; the frame drops about 10 mm as it cocks, inside the 20 mm of R1.

The lock depends on assumption 3. If the combined friction on a wet 200 mm trunk were below 0.58, the collar would slide. Measuring it is the first TRL 4 task.

## 4. Strength at the R1 load [C]

- [C1] Bearing bars, RHS 50 x 25 x 2.5: 0.48 kN m at the spine on the 450 mm trunk, 171 MPa, factor 2.1 on yield (5.3 at the working load).
- [C2] Bar-to-spine fillet welds, 4 mm all round: 82 MPa, factor 3.5.
- [C3] Spine arm: 8 MPa beside the lightening hole. The load eye is 13 mm thick with its doubler rings; bearing under the carabiner bar is 19 MPa and the tear-out strength 75 kN, 30 times the R1 load.
- [C4] Chain cleat at 5.5 kN of chain tension: the 5 mm web beside a slot, loaded by the next link, 113 MPa (factor 3.1); the twist between the two slots, 0.16 kN m, gives 54 MPa in the cheeked top (factor 3.8 in shear).
- [C5] Chain: 5.5 kN at most, factor 8.1 on its breaking force and under half its working load limit; 2.2 kN at the working load.
- [C6] Rope: about 14 kN at the figure-eight loop, factor 5.7 at the R1 load and 14 at the working load. Carabiners: factor 10 and 25.

## 5. Lowering [D]

- [D1] The descender's friction ratio of 6.6 and the 180 deg turn over the brake carabiner (1.87) leave about 80 N at the brake hand for a 100 kg person, inside the 150 N of R5. Without the brake carabiner the hand would hold about 150 N, at the limit, which is why the brake carabiner is part of the design.
- [D2] A 25 m lowering at 0.3 m/s takes 83 s and turns 24.8 kJ into heat: 85 % in the descender, 7 % in the brake carabiner and 8 % at the hand. If the descender kept it all it would warm by at most 44 K.

![Figure 1. Where the energy of a 25 m lowering goes](../../media/flow.png)

*Figure 1. Energy turned to heat lowering a 100 kg person 25 m (estimates).*

## 6. Fit, reach and rigging [E]

- [E1] Rope: 25 m of lowering, 1 m from the descender to the person at the start, 1.5 m for the knots and 0.5 m round the brake carabiner: 28 m of the 30 m.
- [E2] Fit: on a 200 mm trunk the chain loop is 769 mm, the pads touch 58 mm along their faces and the spine is 23 mm clear of the bark; on 300 mm, 1,086 mm, 87 mm and 31 mm; on 450 mm, 1,563 mm, 130 mm and 43 mm. The 110-link chain leaves at least 10 links of tail on a 450 mm trunk.
- [E3] Rigging time once the rescuer is in position (estimate): collar 60 s, descender and rope 40 s, bag to the ground 20 s, triangle and chest sling 120 s, clip in and take in slack 30 s: 4.5 minutes.

## 7. Mass [F]

- [F1] Collar frame 2.55 kg (2.26 kg of it steel), chain set 1.88 kg, descender 0.53 kg, carabiners 0.26 kg, rope 2.34 kg, triangle and sling 0.87 kg, bag 0.45 kg.
- [F2] The whole kit is 8.9 kg if carried up the trunk.
- [F3] If the helpers haul the rope, bag, triangle and sling up on a 4 mm tag line, the rescuer carries 5.5 kg; an aluminium frame (6082-T6, 40 % thicker) saves about 1.2 kg; both together leave 4.4 kg.

## 8. Bark [G]

- [G1] At 2.5 kN the pads press 1.9 MPa (0.7 MPa at the working load) and the sleeved chain 0.6 MPa: no cut is expected. Bare links outside the sleeve press about 8 MPa on a 3 mm line and may mark the bark; R8 is confirmed by inspection after the TRL 4 tests.

## 9. Cost [H]

- [H1] Value-engineering target: USD 900. Estimated cost of the constructable design: USD 758 (USD 142 under the target).
- [H2] Against R9 (parts per kit) the kit is over the value-engineering target of R9 by USD 658. The largest lines are the auto-locking descender (USD 280), the evacuation triangle (USD 140), the rope (USD 105) and the bag (USD 45).

## 10. Results against the requirements

*Table 3. Requirements on paper.*

| ID | Status on paper | Basis |
| --- | --- | --- |
| R1 | Met on paper; friction to confirm | Locking factor 1.54 at the smallest trunk; settles about 10 mm [B4, B5] |
| R2 | **At risk** | The single top chain cannot hold an upward pull on paper; the drill keeps the collar above the person's attachment so the case does not arise |
| R3 | Met | 200 to 450 mm, no tools [E2] |
| R4 | **At risk** | About 4.5 minutes, a thin margin on a rough estimate [E3] |
| R5 | Met on paper (estimate) | About 80 N at the hand [D1] |
| R6 | Met | 28 m needed of 30 m [E1] |
| R7 | **Not met** | 8.9 kg carried [F2] |
| R8 | Met on paper; to confirm | Pads 1.9 MPa, sleeve 0.6 MPa [G1] |
| R9 | **Not met** | USD 758 a kit [H2] |
| R10 | Cannot be shown on paper | Needs the training trial at TRL 4 |

The requirements not met or at risk (R2, R4, R7 and R9) are set out with options and a recommendation for Amish in the design decisions register (TKB-DEC-001).
