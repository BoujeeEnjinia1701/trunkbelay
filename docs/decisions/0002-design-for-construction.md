---
doc_id: TKB-DDR-002
title: TrunkBelay design for construction
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
  change: Concept made constructable; changes C1 to C11 and assumptions A1 to A6 decided under Amish's 2026-10-03 pre-approvals
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day: "Proceed with the remaining 15 scaffolds". Design-for-construction rule, Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible."

## Context

The TRL 2 concept (TKB-DDR-001) named the parts but not how each is made or joined: a "chain collar", a "slotted cleat", a "padded bearing plate" and a friction device "on the collar". STANDARDS section 18 requires every part to be makeable by a stated process and to fit and fasten to its neighbours. The parametric model (`cad/src/model.py`) was built part by part, and its 210 constructability checks (contact, clearance, the trunk, the chain in its slots and the pad contact point, each on 200, 300 and 450 mm trunks) all pass. None of the changes alters what the kit does, its pitch or its safety case; each is the simplest physically sound way to make a concept part.

## Changes

*Table 1. Changes from the concept to the constructable design.*

| # | Component | The concept had | The constructable design has | Why |
| --- | --- | --- | --- | --- |
| C1 | Bark bearing | A padded curved plate | Two 50 x 25 x 2.5 mm steel box bars in a 120 deg V, each faced with a 10 mm rubber pad, bonded and held by two countersunk M6 screws | Fits 200 to 450 mm trunks; a box bar carries the pad force with a factor of 2.1 on yield at 2.5 kN (TKB-CAL-001, C1) |
| C2 | Frame | Not defined | One 5 mm steel spine plate carrying the bars at its foot, the chain slots at its top and two eyes at its outer end | One plate ties every load together; 5 mm because a 6 mm chain link must span the web |
| C3 | Cleat | A slotted cleat | Two 7.5 mm slots cut in the spine top, with a 6 mm cheek welded on each face, notched round each slot | The chain pulls across the plate; the cheeks stop the thin top twisting (C4 factor 3.1 and 3.8) and the notches let the links bear on the web |
| C4 | Lock | Not defined | A keeper bent from 3 mm sheet, its bridge over both slot mouths, held by an 8 mm ball-lock pin through its legs, the cheeks and the web | A link cannot lift out of its slot; one pin to check |
| C5 | Fixed chain end | Not defined | Also in a slot (the front one), its tail tied to the spare eye with an 8 mm quick link | The chain can be adjusted from either end and cannot be dropped when the keeper is off |
| C6 | Eyes | "On the collar" | Two 22 mm eyes with a 4 mm doubler ring welded each side, edges rounded: 13 mm of rounded steel under a carabiner | A carabiner must never bear on a thin plate edge |
| C7 | Lever | Not defined | The load eye 150 mm out from the spine's front edge; the chain line 160 mm above the frame foot | Gives a locking factor of 1.54 or more on every trunk (TKB-CAL-001, B4) |
| C8 | Chain | "Short length of alloy chain" | 6 mm grade 80, 110 links, master link and connecting link on the adjustable end; painted links mark the slot link for 200, 300 and 450 mm trunks | Fits the full trunk range with at least 10 links of tail; factor 8.1 on breaking force |
| C9 | Chain padding | The plate "stops the chain biting in" | 600 mm of 50 mm tubular webbing on the chain at the back of the trunk | Spreads the chain's pressure where it is highest (0.6 MPa at 2.5 kN) |
| C10 | Brake | A friction device | Auto-locking descender on the load eye, brake strand turned 180 deg over a carabiner in the spare eye | Brings the hand force from about 150 N to about 80 N (TKB-CAL-001, D1) |
| C11 | Finish | Not defined | Frame hot-dip galvanised after welding, vent holes in the bars, slots and pin hole cleared afterwards; load and one-person marking stamped on the spine | Rust-proof in the open in a monsoon climate |

## Assumptions decided

*Table 2. Assumptions behind the constructable design.*

| # | Assumption | Value | Relaxed or tightened by |
| --- | --- | --- | --- |
| A1 | Friction on wet coconut bark | Rubber pad 0.5, webbing-sleeved chain 0.4, together 0.9 | Slip tests on cut trunk sections at TRL 4; the design needs 0.58 on a 200 mm trunk |
| A2 | Pad rubber | 60 to 70 Shore A, effective compression modulus 6 MPa | The rubber bought |
| A3 | Descender | Rope friction 0.2 over 540 deg of contact, ratio 6.6 | The maker's data for the descender bought |
| A4 | Rope stretch | 4 % between 50 and 150 kg (EN 1891 type A class) | The rope bought |
| A5 | Bark | No cut at 2 MPa under rubber or 0.6 MPa under webbing; bare links may mark it | Inspection after the TRL 4 tests (R8) |
| A6 | Trunk range | 200 to 450 mm, round enough for a V to touch on two lines | A survey of palms with the first co-design candidate |

## Consequences

- Every part is cut, drilled, bent or welded from plate, box section and sheet, or bought; the frame is one welded, galvanised piece of about 2.3 kg of steel.
- The collar (frame and chain set) weighs 4.4 kg and the kit 8.9 kg; the kit mass is open in TKB-DEC-001, O3.
- The general arrangement TKB-DWG-001, the making sketches TKB-DWG-101 to 109 and the build plan TKB-BLD-001 show this design.

> **Safety:** These changes make the collar buildable; they do not make it safe to use on a person. The build plan's safety stops require a proof test of the collar at 2.5 kN on cut trunk sections and a dummy drill at low height before anyone is lowered with it.
