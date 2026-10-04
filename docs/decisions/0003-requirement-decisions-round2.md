---
doc_id: TKB-DDR-003
title: TrunkBelay requirement decisions, round 2
project: TrunkBelay
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish's decisions on open items O1 to O4 (portfolio decisions 41 to 44) carried into the design
---

# 0003: Requirement decisions, round 2

- **Date:** 2026-10-03
- **Status:** decided by Amish Chadha, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For TrunkBelay these are portfolio decisions 41 to 44, the recommendations on open items O1 to O4 of TKB-DEC-001 v0.1, each taken exactly as recommended.

## Context

At TRL 3 (TKB-CAL-001 v0.1) four requirements were not met or at risk on paper: R2 (the collar holds only a downward pull), R4 (rigging about 4.5 minutes against 5), R7 (8.9 kg carried against 5 kg) and R9 (USD 758 a kit against USD 100). Each was posed to Amish with options and a recommendation in TKB-DEC-001. Three of the four (O1, O2 and O4) concern holding a person, so the safety notes below stay conservative.

## Options considered

*Table 1. Options.*

| # | Requirement | Options |
| --- | --- | --- |
| 41 (O1) | R2, load passing the collar | **A.** Keep the drill rule (collar 300 mm or more above the victim's attachment) and test the upward case only as a misuse test: no cost or mass, upward case stays unproven. **B.** Double-acting collar, a second chain through a slot block at the frame foot: R2 expected met on paper, about USD 45 and 1.7 kg more |
| 42 (O2) | R4, rigging time | **A.** Keep the drill and time it at TRL 4. **B.** Pack the victim set pre-rigged on the victim carabiner: about 45 s saved, no cost or mass. **C.** A quick-fit hip loop in place of the triangle: about 60 s saved and USD 100 less, but holds an unconscious person less securely |
| 43 (O3) | R7, kit mass | **A.** Helpers haul the rope bag up on a 4 mm tag line. **B.** Aluminium frame (6082-T6, 40 % thicker, TIG welded). **C.** Both A and B |
| 44 (O4) | R9, cost per kit | **A.** Keep the auto-locking descender and triangle. **B.** Two-sling hasty seat in place of the triangle. **C.** Workshop bar rack with a friction-hitch backup in place of the descender |

## Decision

*Table 2. Decisions and what changed.*

| # | Decision | What changed in the design |
| --- | --- | --- |
| 41 | **A**, with **B** as the fallback if the TRL 4 drill shows a rescuer cannot reach above the attachment | No hardware change. The drill rule stays: the collar is set 300 mm or more above the point where the rope meets the victim, so it is only ever pulled downward. The TRL 4 upward-pull test is a misuse test whose result is recorded but does not relax the rule. The timed drill at TRL 4 records whether the rescuer could reach above the attachment; if not, the double-acting collar (about USD 45 and 1.7 kg, estimate) is brought back to Amish. R2 stays at risk on paper, controlled by procedure |
| 42 | **B** | No new parts. The victim set is packed pre-rigged: the rope's figure-eight loop, the triangle's two side loops and one end of the chest sling are on the victim carabiner, and the triangle's crotch loop is the one clip made at height. Build plan step 10 and figure 28 changed. Fitting falls from about 120 s to about 75 s (estimate) |
| 43 | **C** | The frame is aluminium 6082-T6, TIG welded with ER5356 and left bare (no galvanising). The helpers keep the rope bag on the ground; the rescuer carries the collar, descender, load and brake carabiners and a 30 m, 4 mm tag line in a 10 l shoulder pouch (new BOM lines 22 and 23), and hauls the rope's loop end with the pre-rigged victim set up on the tag line. Sizes, see below |
| 44 | **A**, with savings sought through group purchase and one kit per climber group | No change to the parts. The auto-locking descender with anti-panic and the evacuation triangle stay. R9 stays not met by Amish's choice; the savings route is recorded in TKB-DEC-001 |

### How the aluminium frame was sized (decision 43)

The option was costed as each steel part 40 % thicker in aluminium. Checking that against strength showed two limits, and the parts were sized to the decision's intent (an aluminium frame that holds the R1 load) rather than to the 40 % figure:

- **Welding softens 6082-T6.** Beside a TIG weld the 0.2 % proof strength falls from 260 MPa to about 125 MPa, over about 30 mm (EN 1999-1-1). Every highly loaded section of this small frame is that close to a weld. A 40 % thicker bar (RHS 50 x 25 x 3.5) would carry 135 MPa at its weld at the R1 load of 2.5 kN, a factor of 0.92: it would yield below R1. The bars are therefore aluminium RHS **70 x 30 x 5**, 61 MPa, factor 2.0 at the R1 load (the steel bar had 2.1). The section is held to 30 mm deep to clear the spare eye's doubler ring and to 70 mm high to clear the chain's fixed-end tail; both clearances are new constructability checks.
- **The spine cannot be thickened.** The spine top is the web of the chain cleat, and a 6 mm grade 80 link (inner length 18 mm, wire up to 6.3 mm) must span it, which leaves 5.4 mm at most. The spine stays **5 mm**. The doubler rings go from 4 to **6 mm** and the cleat cheeks from 6 to **8 mm** (stock plate thicknesses at or above 40 % thicker). The keeper's bridge widens from 23 to 28 mm and the lock pin's grip from 23 to 28 mm.

*Table 3. Results (TKB-CAL-001 v0.2).*

| Item | Before | After |
| --- | --- | --- |
| R1 | Met on paper, friction to confirm | Met on paper, friction to confirm; the 5 mm aluminium cleat web has a factor of 1.1 on its heat-affected proof strength at the R1 load (2.3 on the parent metal, 2.8 at the working load), against 3.1 in steel. New open question O5 |
| R2 | At risk | At risk on paper, controlled by the drill rule (decision 41 A) |
| R4 | At risk, about 4.5 min | Met on paper (estimate), about 4.2 min: haul 45 s added, fitting 45 s saved, lowering the bag (20 s) no longer needed |
| R7 | Not met, 8.9 kg carried | Met on paper, 4.74 kg carried (257 g margin); whole kit 8.5 kg |
| R9 | Not met, USD 758 | Not met, USD 802 (accepted, decision 44 A) |
| Frame weldment | 2.22 kg steel, galvanised | 1.37 kg aluminium, bare (bars 0.92 kg) |
| Collar | 4.4 kg | 3.6 kg |
| Cost | USD 758 | USD 802: aluminium parts and TIG welding about USD 29 more than the steel parts, welding and galvanising; tag line and pouch about USD 16 (estimates) |
| Model | 210 constructability checks pass | 213 checks pass (bars to doubler rings added; chain tail to bars now the binding clearance at 6.7 mm) |
| Drawings | TKB-DWG-001 Rev P1 | TKB-DWG-001 Rev P2; making sketches TKB-DWG-101 to 107 and the build plan pictures regenerated |

## Consequences

- The frame now needs a fabricator with an AC TIG welder and a welder qualified on aluminium; "any village fabrication shop" no longer applies (TKB-DDR-001, D9, is superseded on material by this record).
- Galvanising is gone. Stainless screws in the aluminium bars are fitted with anti-seize; the zinc-plated keeper and quick link are compatible with aluminium.
- The grade 80 steel chain bears on and slides over aluminium slot edges, which will wear faster than steel. This is part of O5.
- The rescuer's carried mass meets R7 by only 257 g; any heavier descender or pouch would use it up.
- The rescuer depends on the helpers to send the rope up. If no helper is on the ground, the rescuer must carry the rope bag as well (8.5 kg, R7 not met for that case).

> **Safety:** TrunkBelay holds a person at height. These decisions keep the conservative choices: the auto-locking descender and the evacuation triangle stay (44 A), and the collar is used only with the drill rule that sets it 300 mm or more above the victim's attachment (41 A), because on paper it does not hold an upward pull. If a rescuer cannot reach above the attachment, the collar is not used that way; the double-acting collar is the fallback. The pre-rigged victim set must be checked before every use: carabiner gate screwed shut, loops not twisted, crotch loop free. The aluminium frame has less margin at the cleat than the steel one (O5). Nobody is lowered with the kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height. It is not certified equipment.
