---
doc_id: TKB-DEC-001
title: TrunkBelay design decisions register
project: TrunkBelay
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; requirements not met or at risk posed for Amish
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's decisions on O1 to O4 recorded (TKB-DDR-003, portfolio decisions 41 to 44); one new open question, O5 (aluminium cleat)"
---

# TrunkBelay design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in the review note; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries below set safety limits (the one-person rating, the proof test, the auto-locking descender, where the collar is placed, the pre-rigged victim set). Each takes the conservative option and names the evidence that would relax it. Nobody is lowered with this kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.

## Open decisions

Amish decided O1 to O4 on 2026-10-03 (TKB-DDR-003; see Decisions made). Carrying decision 43 C into the design raised one new question. It is **Proposed, awaiting Amish**. Effects are estimates.

*Table 1. Open decisions.*

| # | Requirement and state | Options | Recommendation | What it affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O5 | **R1, strength margin of the aluminium cleat.** With the frame in aluminium 6082-T6 (decision 43 C), the 5 mm cleat web beside each slot carries 113 MPa at the R1 load of 2.5 kN. Beside the cheek welds its proof strength is about 125 MPa, a factor of 1.1 (2.3 on unwelded parent metal, 2.8 at the working load); the steel cleat had 3.1. The web cannot be thickened, because a chain link must span it. The steel chain also bears on and slides over the aluminium slot edges, which will wear | **A.** Steel cleat insert: make the slotted top of the spine (about 60 x 45 mm) a separate 5 mm S355 plate, galvanised, bolted to the aluminium spine between the cheeks with two M8 stainless bolts and the lock pin. Cleat factor back to about 3.1 and wear-resistant slots; about 0.1 kg and USD 5 more (4.84 kg carried, R7 still met). **B.** Keep the welded aluminium cleat: factor 1.1 at the R1 load, shown by the TRL 4 proof test; inspect the slot edges for wear before every use. No cost or mass. **C.** Heat-treat the welded frame back to T6 (solution treat and age): factor about 2.3, slots still aluminium; about USD 30 at a heat-treatment shop, and the frame may distort | **Recommend A**: the cleat holds a person, and A restores the steel design's margin and stops the chain wearing the slots for about 0.1 kg and USD 5 | A adds a steel cleat plate, two bolts and a joint to the frame (making sketches 101, 104 and 105, build plan sections 3.1, 3.4 and 3.5) | TKB-CAL-001, C4; TKB-DDR-003 |

Fallback held from decision 41: if the TRL 4 timed drill shows that a rescuer cannot reach to set the collar 300 mm or more above the victim's attachment, the double-acting collar (O1 option B: a second chain through a slot block at the frame foot, about USD 45 and 1.7 kg, estimate) comes back to Amish for decision.

## To confirm when parts are bought

These are facts that can only be settled with real parts, real trunks or the training partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Friction of the rubber pad and of the webbing-sleeved chain on wet coconut bark (0.5 and 0.4 assumed) | The lock needs 0.58 combined on a 200 mm trunk; this is the first test | TKB-CAL-001, B4; TKB-DDR-002, A1 |
| 2 | The chain bought: inner length at least 18 mm and wire 6.0 to 6.3 mm, so a link spans the 5 mm web and fits the 7.5 mm slot; certificate | Cleat geometry | TKB-DWG-101 and 108 |
| 3 | The descender bought: rope range, one-person rating, friction or hand force at 100 kg, and how its brake strand leaves the body | Hand force about 80 N; the brake carabiner's position | TKB-CAL-001, D1; TKB-DDR-002, A3 |
| 4 | The rope bought: breaking strength, stretch and mass per metre | Rope factor, slack-drop load and kit mass | TKB-CAL-001, A2, C6 and F1 |
| 5 | Rubber hardness and the bond of contact adhesive to abraded aluminium | Pad squash and pad security | TKB-CAL-001, B5 |
| 6 | Trunk diameters and shapes in the first partner's area | The 200 to 450 mm range and the 110-link chain | TKB-REQ-001, R3; TKB-DDR-002, A6 |
| 7 | Whether the triangle can be fitted to a head-down dummy in the time estimated | Rigging time | TKB-CAL-001, E3 |
| 8 | That the brake carabiner and the 8 mm quick link sit side by side in the 22 mm spare eye | Spare eye layout | Build plan, Figure 16 |
| 9 | The aluminium 6082-T6 stock bought (plate and RHS 70 x 30 x 5, mill certificate) and a fabricator with AC TIG and an aluminium-qualified welder | The heat-affected strength used in TKB-CAL-001, section C | TKB-DDR-003 |
| 10 | The time to haul the rope's loop end and the victim set up 25 m on the tag line (45 s assumed), and to fit the pre-rigged set (75 s assumed) | Rigging time, R4 | TKB-CAL-001, E3 |
| 11 | The mass of the descender, pouch and tag line bought | R7 is met by 257 g | TKB-CAL-001, F2 |

## Value engineering

Value-engineering target: USD 900 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 802 (USD 98 under the target); USD 758 before the round 2 decisions. Against R9's per-kit figure the kit is over its value-engineering target by USD 702; Amish has accepted this to keep the descender and triangle (decision 44 A). Main cost drivers and savings worth trying:

- The bought rescue gear is about 80 % of the cost: the auto-locking descender (USD 280), the evacuation triangle (USD 140), the rope (USD 105), the bag (USD 45) and three carabiners (USD 45). The made aluminium frame, including TIG welding, is about USD 71.
- Savings sought (decision 44 A): group purchase of descenders, triangles and rope by the training partner for many kits, and one kit per climber group rather than per climber. Also worth trying: rope bought by the reel; a plain stuff sack in place of a rope bag (about USD 30); frames welded in batches.
- One kit per climber group, rather than per climber, spreads the cost of the descender and triangle.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: self-locking frame with the load eye on a lever; two rubber-faced bars in a 120 deg V; the drill places the collar above the victim's attachment (the R2 question stays open as O1); auto-locking descender with anti-panic and a brake carabiner; evacuation triangle with chest sling; spare rope lowered to the ground; one-person 100 kg rating sized for 2.5 kN; first co-design candidates (a climber training programme under the Coconut Development Board's Friends of Coconut Tree scheme in Kerala, a Kerala Fire and Rescue Services station in Kasaragod or Kannur, a climbers' collective in the same district; none approached yet); steel, welded and galvanised (material superseded by TKB-DDR-003: aluminium 6082-T6); pitch, problem, design-arounds and budget unchanged | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds" | TKB-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C11: V of box bars with bonded and screwed pads, 5 mm spine plate, slotted cleat with notched cheeks, keeper and ball-lock pin, fixed end in a slot tethered to the spare eye, eyes with doubler rings, lever geometry, 110-link grade 80 chain with master link, chain sleeve, brake carabiner, galvanising and marking (thicknesses, material and finish of the frame superseded by TKB-DDR-003) | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | Assumptions A1 to A6: friction on wet bark, pad rubber, descender friction, rope stretch, bark limits, trunk range; each to be confirmed (Table 2) | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | No use on a person before a proof test of the collar at 2.5 kN on cut trunk sections and a dummy drill at low height (conservative; this is a gate, not relaxed) | Amish, same pre-approvals | TKB-BLD-001, section 6 |
| 2026-10-03 | Appearance model departures for the renders only: a safe working load label on the spine, a 400 mm trunk with leaf-scar rings, the rope cut below the frame, and a clay forearm and hand on the brake strand | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
| 2026-10-03 | O1, R2 (portfolio decision 41): **A**, keep the drill rule that sets the collar 300 mm or more above the victim's attachment; the upward case is tested only as a misuse test; **B**, the double-acting collar, is the fallback if the TRL 4 drill shows a rescuer cannot reach above the attachment | Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." | TKB-DDR-003 |
| 2026-10-03 | O2, R4 (decision 42): **B**, pack the victim set pre-rigged on the victim carabiner | Amish, same instruction | TKB-DDR-003 |
| 2026-10-03 | O3, R7 (decision 43): **C**, haul line plus aluminium 6082-T6 frame, TIG welded, not galvanised; bars sized for the heat-affected zone (RHS 70 x 30 x 5), spine kept at 5 mm, rings 6 mm, cheeks 8 mm | Amish, same instruction | TKB-DDR-003 |
| 2026-10-03 | O4, R9 (decision 44): **A**, keep the auto-locking descender and triangle; savings through group purchase and one kit per climber group | Amish, same instruction | TKB-DDR-003 |

## Change log

- 2026-10-03, v0.2: O1 to O4 decided by Amish and moved from "Proposed, awaiting Amish" to Decisions made (TKB-DDR-003); O5 (aluminium cleat) added as Proposed, awaiting Amish; items to confirm 9 to 11 added; value engineering updated to USD 802.
