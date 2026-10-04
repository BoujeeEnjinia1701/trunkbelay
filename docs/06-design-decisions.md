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
  change: Open decisions O1 to O4 decided by Amish (16A, 17B, 18C, 19A) and moved to Decisions made; items to confirm and value engineering updated
---

# TrunkBelay design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in the review note; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries below set safety limits (the one-person rating, the proof test, the auto-locking descender, where the collar is placed). Each takes the conservative option and names the evidence that would relax it. Nobody is lowered with this kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.

## Open decisions

None. Amish decided the four open decisions (O1 to O4) on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." They are recorded under Decisions made and in TKB-DDR-003. R2 and R4 remain at risk on paper and are settled by the TRL 4 drill and timed trial (items 9 and 10 below); nothing in carrying out the decisions needs a new decision from Amish.

## To confirm when parts are bought

These are facts that can only be settled with real parts, real trunks or the training partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Friction of the rubber pad and of the webbing-sleeved chain on wet coconut bark (0.5 and 0.4 assumed) | The lock needs 0.58 combined on a 200 mm trunk; this is the first test | TKB-CAL-001, B4; TKB-DDR-002, A1 |
| 2 | The chain bought: inner length at least 18 mm and wire 6.0 to 6.3 mm, so a link spans the 5 mm web and fits the 7.5 mm slot; certificate | Cleat geometry | TKB-DWG-101 and 108 |
| 3 | The descender bought: rope range, one-person rating, friction or hand force at 100 kg, and how its brake strand leaves the body | Hand force about 80 N; the brake carabiner's position | TKB-CAL-001, D1; TKB-DDR-002, A3 |
| 4 | The rope bought: breaking strength, stretch and mass per metre | Rope factor, slack-drop load and kit mass | TKB-CAL-001, A2, C6 and F1 |
| 5 | Rubber hardness and the bond of contact adhesive to bare 6082 aluminium | Pad squash and pad security | TKB-CAL-001, B5 |
| 6 | Trunk diameters and shapes in the first partner's area | The 200 to 450 mm range and the 110-link chain | TKB-REQ-001, R3; TKB-DDR-002, A6 |
| 7 | Whether the triangle can be fitted to a head-down dummy in the time estimated | Rigging time | TKB-CAL-001, E3 |
| 8 | That the brake carabiner and the 8 mm quick link sit side by side in the 22 mm spare eye | Spare eye layout | Build plan, Figure 16 |
| 9 | In the timed drill, that a rescuer can reach to set the collar at least 300 mm above the victim's attachment | If not, the recorded fallback for R2 (the double-acting collar) is built | TKB-DDR-003, 16A |
| 10 | The timed drill with the bag hauled on the doubled tag line and the victim set pre-rigged | R4 estimate of 4.5 minutes; whether the doubled line tangles while the rescuer climbs | TKB-DDR-003, 17B and 18C |
| 11 | Wear of the aluminium cleat web where the steel links bear (about 92 MPa at 2.5 kN), and no permanent set of the frame after the 2.5 kN proof test | The aluminium frame's smaller strength margins (1.55 on the welded proof strength) | TKB-CAL-001, C1 and C4 |
| 12 | Quotes for 6082-T6 plate and tube and AC TIG welding near the first partner | Cost of the aluminium frame (about USD 69 with welding) | bom/bom.csv, lines 1 to 5 |

## Value engineering

Value-engineering target: USD 900 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 826 (USD 74 under the target). Against R9 as restated by Amish (USD 850 per kit at single-kit prices) the kit is USD 24 under. Main cost drivers and savings worth trying:

- The bought rescue gear is most of the cost: the auto-locking descender (USD 280), the evacuation triangle (USD 140), the rope (USD 105), the bag (USD 45) and three carabiners (USD 45). Amish kept the descender and triangle for safety (19A). The aluminium frame, including TIG welding, is about USD 69; the tag line and micro pulley about USD 39.
- Savings worth trying: group purchase of descenders, triangles and rope by the training partner for many kits; rope and cord bought by the reel; a plain stuff sack in place of a rope bag (about USD 30); welding frames in batches.
- One kit per climber group, rather than per climber, spreads the cost of the descender and triangle.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: self-locking frame with the load eye on a lever; two rubber-faced bars in a 120 deg V; the drill places the collar above the victim's attachment (the R2 question, O1, later decided as 16A); auto-locking descender with anti-panic and a brake carabiner; evacuation triangle with chest sling; spare rope lowered to the ground; one-person 100 kg rating sized for 2.5 kN; first co-design candidates (a climber training programme under the Coconut Development Board's Friends of Coconut Tree scheme in Kerala, a Kerala Fire and Rescue Services station in Kasaragod or Kannur, a climbers' collective in the same district; none approached yet); steel, welded and galvanised (superseded for the frame by aluminium, TKB-DDR-003); pitch, problem, design-arounds and budget unchanged | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds" | TKB-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C11: V of box bars with bonded and screwed pads, 5 mm spine plate, slotted cleat with notched cheeks, keeper and ball-lock pin, fixed end in a slot tethered to the spare eye, eyes with doubler rings, lever geometry, 110-link grade 80 chain with master link, chain sleeve, brake carabiner, galvanising (superseded by the bare aluminium frame, TKB-DDR-003) and marking | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | Assumptions A1 to A6: friction on wet bark, pad rubber, descender friction, rope stretch, bark limits, trunk range; each to be confirmed (Table 2) | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | No use on a person before a proof test of the collar at 2.5 kN on cut trunk sections and a dummy drill at low height (conservative; this is a gate, not relaxed) | Amish, same pre-approvals | TKB-BLD-001, section 6 |
| 2026-10-03 | O1 to O4 on the requirements not met or at risk. 16A (R2): keep the drill rule, collar at least 300 mm above the victim's attachment; double-acting collar recorded as the fallback. 17B (R4): pack the triangle and chest sling pre-rigged on the victim carabiner (45 s saved). 18C (R7): the helpers haul the rope bag up on a tag line and the collar frame goes to aluminium (4.55 kg carried, met). 19A (R9): keep the auto-locking descender and evacuation triangle, seek group purchase, R9 restated to USD 850 per kit (USD 826, met) | Amish, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." | TKB-DDR-003 |
| 2026-10-03 | Appearance model departures for the renders only: a safe working load label on the spine, a 400 mm trunk with leaf-scar rings, the rope cut below the frame, and a clay forearm and hand on the brake strand | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
