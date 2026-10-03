---
doc_id: TKB-DEC-001
title: TrunkBelay design decisions register
project: TrunkBelay
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Register opened; design decisions made under Amish's 2026-10-03 pre-approvals; requirements not met or at risk posed for Amish
---

# TrunkBelay design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/` or in the review note; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list decisions.

> **Safety:** Several entries below set safety limits (the one-person rating, the proof test, the auto-locking descender, where the collar is placed). Each takes the conservative option and names the evidence that would relax it. Nobody is lowered with this kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.

## Open decisions

Requirements that are not met or at risk on paper are not decided under the pre-approval. Amish, 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on." Each item below is **Proposed, awaiting Amish**. Effects are estimates from TKB-CAL-001.

*Table 1. Open decisions.*

| # | Requirement and state | Options | Recommendation | What it affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| O1 | **R2, at risk.** On paper the collar holds only a downward pull: with one chain at the top, an upward pull on the load eye has no second contact below to hold against. The drill as modelled avoids the case by setting the collar at least 300 mm above the point where the rope meets the victim | **A.** Keep the drill rule; test the upward case at TRL 4 only as a misuse test, and check in the timed drill that a rescuer can reach above the attachment. No cost, no mass; R2 stays unproven for the upward case. **B.** Make the collar double-acting: a second chain round the trunk through two slots in a cheeked block at the frame foot, so it locks either way. R2 expected met on paper; about USD 45 and 1.7 kg more (worsens R7). | **Recommend A**: the upward case never arises if the drill is kept, and B adds 1.7 kg to a kit that is already over its mass target. Fall back to B if the TRL 4 drill shows rescuers cannot reach above the attachment | B adds a foot block, a second chain and a second keeper and pin; drill step 1 | TKB-CAL-001, section 10; TKB-DDR-001, D3 |
| O2 | **R4, at risk.** Rigging is estimated at 4.5 minutes once in position, a thin margin on a rough estimate; fitting the triangle and chest sling (about 2 minutes) is the largest part | **A.** Keep the drill; time it at TRL 4. No cost, no mass. **B.** Pack the victim set pre-rigged: the triangle's three loops and the chest sling already on the victim carabiner with the rope's loop, so one clip is made at height. Saves about 45 s (about 3.8 minutes); no cost, no mass. **C.** Replace the triangle with a quick-fit hip loop. Saves about 60 s; about USD 100 less; holds an unconscious person less securely. | **Recommend B**: it buys back margin at no cost and also offsets the 45 s that O3's tag-line haul would add | B changes step 10 of the build plan: the set is packed already clipped together | TKB-CAL-001, E3 |
| O3 | **R7, not met.** The kit is 8.9 kg if carried up the trunk; the steel frame (2.6 kg), chain set (1.9 kg) and rope (2.3 kg) are the bulk | **A.** The helpers haul the rope bag (rope, triangle, sling) up on a 4 mm tag line the rescuer carries: 5.5 kg carried; about USD 10; adds about 45 s to rigging. **B.** Aluminium frame (6082-T6, 40 % thicker, TIG welded, not galvanised): 7.7 kg carried; about USD 40 more. **C.** Both A and B: 4.4 kg carried; about USD 50 more; adds about 45 s to rigging. | **Recommend C**: the only option that meets the target; with O2-B the rigging time stays at about 4.5 minutes | C changes the frame's material, welding and finish (the steel build plan is replaced by an aluminium one) and adds a tag line to the kit | TKB-CAL-001, F1 to F3 |
| O4 | **R9, not met.** Parts cost USD 758 a kit, over the value-engineering target of R9 by USD 658; the descender (USD 280), triangle (USD 140) and rope (USD 105) are most of it | **A.** Keep the auto-locking descender and the triangle: USD 758; the conservative safety choice. **B.** A hasty seat from two sewn slings in place of the triangle: about USD 642 (USD 116 less), 0.5 kg lighter; holds an unconscious person less securely. **C.** A workshop-made steel bar rack with a friction-hitch backup in place of the descender: about USD 520 (USD 245 less); loses the hands-free lock if the rescuer lets go. | **Recommend A**: B and C trade safety for cost in a rescue of an unconscious person; seek the saving instead through group purchase by the training partner and by sharing one descender and triangle per climber group | None for A | TKB-CAL-001, H2; TKB-DDR-001, D4 and D5 |

## To confirm when parts are bought

These are facts that can only be settled with real parts, real trunks or the training partner. None changes a decision; each may change a size or a limit.

*Table 2. Items to confirm.*

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Friction of the rubber pad and of the webbing-sleeved chain on wet coconut bark (0.5 and 0.4 assumed) | The lock needs 0.58 combined on a 200 mm trunk; this is the first test | TKB-CAL-001, B4; TKB-DDR-002, A1 |
| 2 | The chain bought: inner length at least 18 mm and wire 6.0 to 6.3 mm, so a link spans the 5 mm web and fits the 7.5 mm slot; certificate | Cleat geometry | TKB-DWG-101 and 108 |
| 3 | The descender bought: rope range, one-person rating, friction or hand force at 100 kg, and how its brake strand leaves the body | Hand force about 80 N; the brake carabiner's position | TKB-CAL-001, D1; TKB-DDR-002, A3 |
| 4 | The rope bought: breaking strength, stretch and mass per metre | Rope factor, slack-drop load and kit mass | TKB-CAL-001, A2, C6 and F1 |
| 5 | Rubber hardness and the bond of contact adhesive to galvanised steel | Pad squash and pad security | TKB-CAL-001, B5 |
| 6 | Trunk diameters and shapes in the first partner's area | The 200 to 450 mm range and the 110-link chain | TKB-REQ-001, R3; TKB-DDR-002, A6 |
| 7 | Whether the triangle can be fitted to a head-down dummy in the time estimated | Rigging time | TKB-CAL-001, E3 |
| 8 | That the brake carabiner and the 8 mm quick link sit side by side in the 22 mm spare eye | Spare eye layout | Build plan, Figure 16 |

## Value engineering

Value-engineering target: USD 900 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 758 (USD 142 under the target). Against R9's per-kit figure the kit is over its value-engineering target by USD 658 (open decision O4). Main cost drivers and savings worth trying:

- The bought rescue gear is 85 % of the cost: the auto-locking descender (USD 280), the evacuation triangle (USD 140), the rope (USD 105), the bag (USD 45) and three carabiners (USD 45). The made frame, including welding and galvanising, is about USD 50.
- Savings worth trying: group purchase of descenders, triangles and rope by the training partner for many kits; rope bought by the reel; a plain stuff sack in place of a rope bag (about USD 30); galvanising frames in batches.
- One kit per climber group, rather than per climber, spreads the cost of the descender and triangle.

## Decisions made

*Table 3. Decisions made.*

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | TRL 2 review items D1 to D10: self-locking frame with the load eye on a lever; two rubber-faced bars in a 120 deg V; the drill places the collar above the victim's attachment (the R2 question stays open as O1); auto-locking descender with anti-panic and a brake carabiner; evacuation triangle with chest sling; spare rope lowered to the ground; one-person 100 kg rating sized for 2.5 kN; first co-design candidates (a climber training programme under the Coconut Development Board's Friends of Coconut Tree scheme in Kerala, a Kerala Fire and Rescue Services station in Kasaragod or Kannur, a climbers' collective in the same district; none approached yet); steel, welded and galvanised; pitch, problem, design-arounds and budget unchanged | Amish, pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and, for this batch, "Proceed with the remaining 15 scaffolds" | TKB-DDR-001 |
| 2026-10-03 | Design for construction, changes C1 to C11: V of box bars with bonded and screwed pads, 5 mm spine plate, slotted cleat with notched cheeks, keeper and ball-lock pin, fixed end in a slot tethered to the spare eye, eyes with doubler rings, lever geometry, 110-link grade 80 chain with master link, chain sleeve, brake carabiner, galvanising and marking | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | Assumptions A1 to A6: friction on wet bark, pad rubber, descender friction, rope stretch, bark limits, trunk range; each to be confirmed (Table 2) | Amish, same pre-approvals | TKB-DDR-002 |
| 2026-10-03 | No use on a person before a proof test of the collar at 2.5 kN on cut trunk sections and a dummy drill at low height (conservative; this is a gate, not relaxed) | Amish, same pre-approvals | TKB-BLD-001, section 6 |
| 2026-10-03 | Appearance model departures for the renders only: a safe working load label on the spine, a 400 mm trunk with leaf-scar rings, the rope cut below the frame, and a clay forearm and hand on the brake strand | Amish, same pre-approvals | docs/REVIEW.md, TRL 3 section |
