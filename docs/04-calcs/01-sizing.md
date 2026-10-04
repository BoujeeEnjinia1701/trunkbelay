---
doc_id: TKB-CAL-001
title: TrunkBelay sizing calculations
project: TrunkBelay
doc_type: Calculation note
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: First issue at TRL 3, on the constructable design of TKB-DDR-002
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: Re-run for Amish's decisions 16A, 17B, 18C and 19A (TKB-DDR-003); aluminium frame, tag-line haul, pre-rigged victim set, restated R9
---

# TrunkBelay sizing calculations

On paper, the constructable TrunkBelay collar locks on every trunk from 200 to 450 mm with a locking factor of 1.54 or more, holds the 2.5 kN load of R1 with every aluminium frame part at 1.55 times its welded (heat-affected) proof strength or better, and lets one rescuer lower a 100 kg person 25 m with about 80 N at the brake hand. Version 0.2 carries out Amish's decisions of 2026-10-03 (TKB-DDR-003): the frame is TIG-welded 6082-T6 aluminium, the helpers haul the rope bag up on a tag line, and the victim set is packed pre-rigged, so the rescuer carries 4.55 kg against the 5 kg target; the kit costs USD 826 against the restated R9 target of USD 850. Its weak points are friction and the drill: the lock rests on an assumed friction on wet bark that must be measured first, and the upward pull of R2 is avoided by the drill rule, not by the hardware. Every figure below comes from `docs/04-calcs/sizing.py`, which imports the parametric model (`cad/src/model.py`), so the sizes here are the sizes in the STEP file, the drawings and the build plan. Tags in square brackets ([A1], [B4] ...) match the script output and `results.csv`.

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
| 6 | Frame metal | 6082-T6 aluminium, TIG welded with ER5356 filler. Every frame check uses the heat-affected-zone strength (0.2 % proof 125 MPa, ultimate 185 MPa); weld metal 210 MPa. Keeper and fixings stay steel | EN 1999-1-1 values; BOM lines 1 to 5 (TKB-DDR-003) |
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

- [C1] Bearing bars, aluminium RHS 50 x 40 x 3: 0.48 kN m at the spine on the 450 mm trunk, 78 MPa, factor 1.60 on the welded proof strength (4.0 at the working load) and 2.4 on the welded ultimate strength. The bars are 15 mm deeper than the steel ones; that is why the spare eye moved 15 mm back (to 85 mm) and the adjustable chain tail now runs out 75 mm before it hangs.
- [C2] Bar-to-spine fillet welds, 5 mm all round: 40 MPa, factor 5.3 on the weld metal.
- [C3] Spine arm: 7 MPa beside the lightening hole. The load eye is 13 mm thick with its doubler rings (kept at 4 mm so the 8 mm quick link still passes round the spare eye); bearing under the carabiner bar is 19 MPa and the tear-out strength 39 kN, 16 times the R1 load.
- [C4] Chain cleat at 5.5 kN of chain tension: the 5 mm web beside a slot, loaded by the next link, now 35 mm deep (the spine top was raised 10 mm to 185 mm), 81 MPa, factor 1.55 on the welded proof strength; the twist between the two slots, 0.16 kN m, gives 35 MPa in the top with 8 mm cheeks (factor 2.0 in shear). The web stays 5 mm because a chain link must span it. The steel links bear on the aluminium web at about 92 MPa; wear of the slot faces is to be confirmed.
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
- [E3] Rigging time once the rescuer is in position (estimate): collar 60 s; the helpers haul the bag up on the tag line 45 s; descender and rope 40 s; bag to the ground 20 s; the pre-rigged triangle and chest sling 90 s (was 120 s); clip the crotch loop and the sling's free end and take in slack 15 s (was 30 s): 4.5 minutes. The pre-rigged set saves the 45 s the haul adds, so the estimate is unchanged.

## 7. Mass [F]

- [F1] Collar frame 1.31 kg (the aluminium weldment 0.97 kg), chain set 1.88 kg, descender 0.53 kg, carabiners 0.26 kg, rope 2.34 kg, triangle and sling 0.87 kg, bag 0.45 kg, tag line 0.60 kg (55 m of 4 mm cord) and micro pulley 0.05 kg: 8.3 kg in all.
- [F2] The helpers haul 3.7 kg up in the bag (the rope, the pre-rigged victim set with its carabiner, and the bag). The rescuer carries 4.55 kg: the collar, chain set, descender, load and brake carabiners, the micro pulley and the tag line hanging from it. R7 asks for under 5 kg: met on paper with 0.45 kg to spare. The decision estimate was about 4.4 kg; the difference is the tag line, which runs doubled from the ground (both legs hang from the rescuer at the top) so the helpers can haul.
- [F3] The aluminium weldment saves about 1.9 kg against the same parts in steel.

## 8. Bark [G]

- [G1] At 2.5 kN the pads press 1.9 MPa (0.7 MPa at the working load) and the sleeved chain 0.6 MPa: no cut is expected. Bare links outside the sleeve press about 8 MPa on a 3 mm line and may mark the bark; R8 is confirmed by inspection after the TRL 4 tests.

## 9. Cost [H]

- [H1] Value-engineering target: USD 900. Estimated cost of the constructable design: USD 826 (USD 74 under the target). The aluminium frame adds about USD 29 (material, TIG welding and rivet nuts, less the galvanising) and the tag line and micro pulley USD 39, USD 68 in all against the decision estimate of about USD 50.
- [H2] Against R9 as restated by Amish's decision 19A (USD 850 per kit at single-kit prices), the kit is USD 24 under. The largest lines are the auto-locking descender (USD 280), the evacuation triangle (USD 140), the rope (USD 105) and the TIG welding (USD 45). Group purchase by the training partner and one kit per climber group are savings to seek and are not counted.

## 10. Results against the requirements

*Table 3. Requirements on paper.*

| ID | Status on paper | Basis |
| --- | --- | --- |
| R1 | Met on paper; friction to confirm | Locking factor 1.54 at the smallest trunk; settles about 10 mm [B4, B5] |
| R2 | **At risk** for an upward pull; drill rule kept (decision 16A) | The single top chain cannot hold an upward pull on paper; the drill keeps the collar at least 300 mm above the person's attachment so the case does not arise; the double-acting collar is the recorded fallback |
| R3 | Met | 200 to 450 mm, no tools [E2] |
| R4 | **At risk** (estimate) | About 4.5 minutes: the pre-rigged set saves 45 s and the tag-line haul adds 45 s [E3]; timed at TRL 4 |
| R5 | Met on paper (estimate) | About 80 N at the hand [D1] |
| R6 | Met | 28 m needed of 30 m [E1] |
| R7 | Met on paper | 4.55 kg carried, 0.45 kg under the target; the 3.7 kg bag is hauled up [F2] |
| R8 | Met on paper; to confirm | Pads 1.9 MPa, sleeve 0.6 MPa [G1] |
| R9 | Met on paper (restated target) | USD 826 a kit against USD 850 [H2] |
| R10 | Cannot be shown on paper | Needs the training trial at TRL 4 |

Amish decided R2, R4, R7 and R9 on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." (decisions 16A, 17B, 18C and 19A, TKB-DDR-003). R2 and R4 stay at risk on paper and are settled by the TRL 4 drill and timed trial.
