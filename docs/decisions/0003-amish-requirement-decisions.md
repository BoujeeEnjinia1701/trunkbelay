---
doc_id: TKB-DDR-003
title: TrunkBelay requirement decisions R2, R4, R7 and R9
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
  change: Amish's decisions 16A, 17B, 18C and 19A on open decisions O1 to O4 recorded and carried out
---

# 0003: Requirement decisions R2, R4, R7 and R9

- **Date:** 2026-10-03
- **Status:** decided by Amish Chadha on 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For TrunkBelay these are decisions 16A (O1, R2), 17B (O2, R4), 18C (O3, R7) and 19A (O4, R9), each the recommended option.

## Context

At TRL 3 the calculation note (TKB-CAL-001 v0.1) left four requirements not met or at risk on paper: R2 (the single top chain holds only a downward pull), R4 (about 4.5 minutes to rig, a thin margin), R7 (8.9 kg carried against 5 kg) and R9 (USD 758 a kit against USD 100). They were posed to Amish as open decisions O1 to O4 in the register (TKB-DEC-001) with options and a recommendation.

## Decisions

*Table 1. Decisions and how they were carried out.*

| # | Requirement | Decision | Carried out as | New result (TKB-CAL-001 v0.2) |
| --- | --- | --- | --- | --- |
| 16A | R2, load passing the collar | Keep the drill rule: the collar at least 300 mm above the victim's attachment. The double-acting collar (a second chain through a cheeked block at the frame foot, about 1.7 kg in steel and USD 45) is the recorded fallback | No hardware change. The rule is in the build plan's safety stop S6 and Step 10; the TRL 4 first checks test the upward case only as a misuse test and check in the timed drill that a rescuer can reach above the attachment | At risk for an upward pull, as before; avoided by the drill. If the TRL 4 drill shows a rescuer cannot reach above the attachment, the fallback is built |
| 17B | R4, rigging time | Pack the evacuation triangle and chest sling pre-rigged on the victim carabiner | The rope's figure-eight loop, the triangle's two waist loops and one end of the chest sling are packed on the victim carabiner; at height only the crotch loop and the sling's free end are clipped. Model: `victim_kit()` and three new checks that the straps, sling and rope loop meet the carabiner | Fitting 90 s (was 120 s), clipping in 15 s (was 30 s): 45 s saved, no cost, no mass |
| 18C | R7, kit mass | The helpers haul the rope bag up on a tag line, and the collar frame goes to aluminium | Frame weldment in 6082-T6, TIG welded with ER5356, not galvanised, sized on the heat-affected-zone strength (125 MPa): bars RHS 50 x 40 x 3 (were 50 x 25 x 2.5 steel); cheeks 8 mm (were 6); spine kept 5 mm (a link must span the cleat web) with its top raised 10 mm to 185 mm so the web beside each slot is 35 mm deep; doubler rings kept 4 mm (the quick link must pass round the spare eye); spare eye moved from 70 to 85 mm back, clear of the deeper bars; the adjustable chain tail runs out 75 mm before it hangs, clear of the bar; ball-lock pin grip 27 mm (was 23); pad screws into countersunk stainless rivet nuts. Tag line: 55 m of 4 mm cord doubled through a micro pulley on the rescuer's harness, both ends on the ground, so the helpers haul. Five new frame checks in the model | The rescuer carries 4.55 kg (target under 5 kg): met on paper. The helpers haul 3.7 kg. The haul adds about 45 s to rigging, offset by 17B, so R4 stays at about 4.5 minutes. Frame factors at the R1 load on the welded proof strength: bars 1.60, cleat web 1.55, cleat twist 2.0, welds 5.3 on the weld metal |
| 19A | R9, cost per kit | Keep the auto-locking descender and the evacuation triangle; seek savings by group purchase; restate the cost target | R9 restated in TKB-REQ-001 v0.3 as "parts under USD 850 per kit at single-kit prices, keeping the auto-locking descender and the evacuation triangle; group purchase by the training partner sought to lower it, one kit per climber group" (was USD 100) | USD 826 a kit, USD 24 under the restated target. Value-engineering target: USD 900. Estimated cost of the constructable design: USD 826 (USD 74 under the target) |

## Differences from the estimates put to Amish

- **Mass, 4.55 kg against about 4.4 kg.** The option assumed a 30 m tag line of 0.3 kg. To let the helpers haul from the ground (rather than the rescuer hauling at height), the line runs doubled through a micro pulley, so 55 m (0.60 kg) hangs from the rescuer at the top, plus a 0.05 kg pulley. The aluminium frame also came out lighter than the option's rough "40 % thicker" estimate, because only the parts that needed it were thickened.
- **Cost, USD 68 more against about USD 50.** The aluminium frame adds about USD 29 (6082 plate and tube, AC TIG welding and rivet nuts, less the galvanising) and the tag line and micro pulley about USD 39.
- **Frame strength.** The steel frame had factors of 2.1 to 3.8 on yield at the R1 load; the aluminium frame has 1.55 to 2.0 on the welded proof strength (2.3 or more on the welded ultimate strength). That is adequate for the 2.5 kN proof load, which is 2.5 times the working load, but the margins are smaller, and the proof test at TRL 4 must check for permanent set in the frame.

## Consequences

- The steel build plan is replaced by an aluminium one: a fabricator with an AC TIG welder is needed rather than a stick or MIG welder and a galvaniser. No weld may be added or repaired beyond the plan.
- The steel chain bears on the aluminium cleat web at about 92 MPa; wear of the slot faces is a new item to confirm at TRL 4. Stainless fixings sit in rivet nuts with barrier paste against galvanic corrosion.
- The kit gains a tag line and micro pulley (BOM lines 22 and 23); the victim carabiner travels in the bag.
- R2 and R4 remain at risk on paper and are settled by the TRL 4 drill and timed trial.

## Evidence

- `cad/src/model.py` (218 of 218 constructability checks pass), `docs/04-calcs/sizing.py` and `01-sizing.md` (TKB-CAL-001 v0.2), `bom/bom.csv`, `docs/03-requirements.md` (TKB-REQ-001 v0.3), `docs/05-build-plan.md` (TKB-BLD-001 v0.2), general arrangement TKB-DWG-001 Rev P2.
