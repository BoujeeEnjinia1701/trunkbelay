---
doc_id: TKB-REQ-001
title: TrunkBelay requirements
project: TrunkBelay
doc_type: Requirements
version: "0.3"
status: Draft
date: '2026-10-03'
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
  change: Status after Amish's round 2 decisions (TKB-DDR-003); targets unchanged
---

# TrunkBelay requirements

Requirements with their status on paper at TRL 3. The targets are unchanged from version 0.1; they are to be confirmed with the co-design partner. The status column comes from the calculation note TKB-CAL-001 (v0.2). Amish decided how each requirement that was not met or at risk is handled on 2026-10-03 (TKB-DDR-003); open questions are in the design decisions register (TKB-DEC-001).

Table 1. Requirements

| ID | Requirement | Target | Verification (TRL 3 or later) | Status on paper (TRL 3) |
| --- | --- | --- | --- | --- |
| R1 | Collar holds on a palm trunk | No slip greater than 20 mm under a 2.5 kN (562 lbf) static downward load on wet trunk sections | Proof test on CalRig with cut trunk sections at TRL 3 | Met on paper; the friction on wet bark is to be confirmed (locking factor 1.54, settles about 10 mm). The aluminium cleat web has a factor of 1.1 on its heat-affected proof strength at this load (TKB-DEC-001, O5) |
| R2 | Collar holds when load direction changes | No slip greater than 50 mm when a 100 kg (220 lb) test mass passes the collar during lowering | Drop and transition tests on trunk sections | At risk on paper: the single top chain cannot hold an upward pull. Controlled by the drill rule (decision 41 A): the collar is set 300 mm or more above the victim's attachment, so the case does not arise; the upward case is tested at TRL 4 only as a misuse test. Fallback: the double-acting collar, if the TRL 4 drill shows a rescuer cannot reach above the attachment |
| R3 | Fits common palms | Trunk diameters 200 to 450 mm (8 to 18 in) without tools | Fit trials on surveyed palms | Met: the V and the 110-link chain fit the whole range |
| R4 | Quick to rig | Collar fixed and victim clipped in under 5 minutes by a trained climber | Timed drills at 3 m height | Met on paper (estimate): about 4.2 minutes with the victim set pre-rigged (decision 42 B) and the rope hauled up on the tag line (decision 43 C); to be timed at TRL 4 |
| R5 | Controlled lowering | Descent speed held under 0.5 m/s with hand force under 150 N (34 lbf) for a 100 kg (220 lb) load | Lowering tests with test mass | Met on paper: about 80 N at the hand with the brake carabiner |
| R6 | Rope length | Lowers from 25 m (82 ft) | Measured | Met: 30 m of rope, 28 m needed |
| R7 | Portable | Kit mass under 5 kg (11 lb); carried hands-free while climbing | Weighing and climbing trial | Met on paper, thin margin: 4.74 kg carried by the rescuer with the aluminium frame and the rope bag and victim set hauled up on a tag line (decision 43 C); whole kit 8.5 kg |
| R8 | No damage to the palm | No bark cuts deeper than 5 mm after a full test lowering | Inspection after trials | Met on paper; to confirm by test (pads 1.9 MPa, sleeve 0.6 MPa at 2.5 kN) |
| R9 | Cost | Parts under USD 100 per kit | Costed bill of materials | Not met: USD 802 per kit. Amish kept the auto-locking descender and triangle (decision 44 A); savings are sought through group purchase and one kit per climber group |
| R10 | Teachable | Climbers new to the kit complete a supervised rescue drill after a half-day session | Training trial with partner programme | Cannot be shown on paper; training trial at TRL 4 |

## Assumptions

- A second climber is often on site or nearby when a climber is stranded, as in the reported cases.
- The rescuer can reach and work just below the victim using their own climbing device.
- Coconut bark and fibre can carry a collar load without crushing, if the load is spread.
- Victims can be fitted with a sling while hanging head down.

## Safety

> **Safety:** These requirements describe rope rescue equipment that holds a person at height. Meeting them on paper does not make the kit safe to use. Each is verified by test at TRL 4, and the kit is not used on a person until R1 has been proof-tested on cut trunk sections and the drill has been run with a dummy at low height.
