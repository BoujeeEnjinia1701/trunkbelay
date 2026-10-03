---
doc_id: TKB-PRB-001
title: TrunkBelay problem statement
project: TrunkBelay
doc_type: Problem statement
version: "0.2"
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
  change: TRL 2 and 3 update; constraints restated with the value-engineering target, open questions answered, first co-design candidates, safety section
---

# TrunkBelay problem statement

When a climber is stranded on a palm, the first person able to help is usually another climber, not a fire crew. That person can reach the victim but has nothing to anchor them to and no way to lower them.

## The problem

The reported rescues follow a pattern. A climber blacks out or slips, the climbing device holds the feet, and the person hangs head down. A bystander or fellow climber goes up and improvises with cloth and rope to stop a fall ([Onmanorama, 2025](https://www.onmanorama.com/news/kerala/2025/10/02/coconut-plucker-hanging-upside-down-rescued-by-friend-firefighters.html); [Onmanorama, 2026](https://www.onmanorama.com/news/kerala/2026/01/31/coconut-tree-man-trapped-fire-rescue.html)). Fire crews then arrive, use ladders and rescue nets, and in some cases an officer climbs the trunk directly ([Onmanorama, 2026](https://www.onmanorama.com/news/kerala/2026/02/08/fire-officials-save-60-year-old-man-hanging-upside-down-coco.html)). Each rescue is improvised on the spot.

Utility workers have purpose-built answers. The Buckingham SuperSqueeze is a pole-top rescue strap with an adjustable web grab, rated to 350 lb and sold at about USD 1,576 ([Buckingham](https://buckinghammfg.com/products/supersqueeze-pole-top-rescue-488p/)). The 3M DBI-SALA Cynch-Lok grips a wooden pole with a cleated plate and carabiner and is rated to 310 lb for poles from 5.5 to 18.5 in diameter ([Saftgard](https://www.saftgard.com/products/3m-dbi-sala-1204075-cynch-lok-pole-climbing-device-1204075/)). These are sized for smooth utility poles, priced for utilities and not designed for the fibrous, tapering and often curved trunk of a coconut palm.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Coconut climbers (the rescuer) | Anchor and lower a stranded colleague quickly and safely | Plantations and home gardens, often working in pairs or small groups |
| The stranded climber | Be supported, freed from the climbing device and lowered without a fall | Head down or slumped, possibly unconscious, 6 to 25 m up |
| Fire and rescue services | A light anchor to secure a victim before ladders or nets are set | Rural stations called to palm rescues |
| Coconut Development Board and climber training schemes | A standard kit and drill to teach | Climber training and insurance programmes |

## Operating environment

- Coconut palm trunks roughly 200 to 450 mm (8 to 18 in) diameter (estimate, to be surveyed), fibrous, often wet, sometimes curved or leaning.
- Working heights from about 6 m to 25 m (20 to 82 ft).
- Hot humid climate, monsoon rain; kit stored in the open or in a shed.
- Rescuer is already on the trunk using a mechanical climbing device or traditional rope loop.
- No anchor points other than the trunk itself.

## Constraints

- Value-engineering target: USD 900 for the first prototype kit (a control target for value engineering, not a spending limit; STANDARDS section 18).
- Kit parts cost target under USD 100 (R9), well below utility pole-rescue kits.
- Carried up the trunk by one climber: total kit mass under 5 kg (11 lb) (target).
- Collar must fit the full trunk range without special tools.
- Must not use the ratcheting cinch geometry of the 3M Cynch-Lok (IP screen design-around).
- Open hardware under CERN-OHL-S-2.0.

## Out of scope

- Replacing or redesigning climbing devices.
- Fall arrest for routine climbing (a separate problem).
- Rescue of a climber who has already fallen.
- Medical care beyond getting the person to the ground.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Buckingham SuperSqueeze pole-top rescue (488P) | Adjustable web-grab strap for lowering an injured lineman from a utility pole | Priced for utilities (about USD 1,576) and sized for smooth poles, not fibrous palm trunks | [link](https://buckinghammfg.com/products/supersqueeze-pole-top-rescue-488p/) |
| 3M DBI-SALA Cynch-Lok pole climbing device | Fall-restriction strap gripping the pole with a cleated plate and carabiner | Fall restriction for the climber, not a rescue anchor; proprietary cinch geometry | [link](https://www.saftgard.com/products/3m-dbi-sala-1204075-cynch-lok-pole-climbing-device-1204075/) |
| CA2681870C, Bashlin pole climbing and fall restraint device (lapsed 2015) | Belt and lanyard with a locking device for pole climbing | Personal restraint, not a rescue anchor | [link](https://patents.google.com/patent/CA2681870C/en) |
| WO2012131439A1, safety tree climbing device (ceased) | Engine-powered wheeled drum that climbs single-stem palms with a brake and safety cable | Climbing machine, not a rescue kit; never entered national phase | [link](https://patents.google.com/patent/WO2012131439A1/en) |
| Fire service improvised rescue with ladders, ropes and nets | Current practice in Kerala palm rescues | Arrives late; relies on ladders that do not reach tall palms | [link](https://www.onmanorama.com/news/kerala/2025/10/02/coconut-plucker-hanging-upside-down-rescued-by-friend-firefighters.html) |

## Co-design

A climber training programme or climbers' collective in Kerala, working with a local Fire and Rescue Services station that has done palm rescues, so the kit and drill fit both the climbers who will use it first and the crews who arrive later.

First candidates to approach (none approached yet; recorded in TKB-DDR-001, D8):

1. A coconut climber training programme run under the Coconut Development Board's "Friends of Coconut Tree" scheme in Kerala, for the drill and the training trial (R10).
2. A Kerala Fire and Rescue Services station in a district with recorded palm rescues (Kasaragod or Kannur), for the drill and for adoption by crews.
3. A climbers' collective or labour bank in the same district, for fit trials on real palms (R3) and the kit's carry and rigging (R4, R7).

## Questions answered at TRL 2 and 3

The open questions of version 0.1 were settled on paper under Amish's pre-approval of 2026-10-03 (TKB-DDR-001). Each answer is checked at TRL 4.

| Question (version 0.1) | Answer on paper | Record |
| --- | --- | --- |
| Can the collar hold the load turning from upward to downward as the victim passes it? | Not with the single top chain. The drill sets the collar at least 300 mm above the point where the rope meets the victim, so the pull is always downward. Whether that drill is workable is a decision for Amish (R2) | TKB-DDR-001, D3; TKB-DEC-001 |
| How much does grip vary with moisture, age and curvature? | The collar is self-locking: it needs a combined friction of 0.58 or less on a 200 mm trunk against about 0.9 assumed for rubber and sleeved chain on wet bark. Friction on real trunks is the first thing to confirm | TKB-CAL-001, section B |
| Which friction device is simplest to learn? | An auto-locking descender with an anti-panic function, plus a carabiner the brake strand turns over. It stops if the rescuer lets go | TKB-DDR-001, D4 |
| How is an unconscious, head-down person fitted with a sling? | An evacuation triangle round the hips and a chest sling, both clipped to the rope's victim carabiner, so the person turns head up when the feet are freed | TKB-DDR-001, D5 |
| Would fire services adopt the kit, and would that change the rating? | Unknown until the first co-design candidates are approached. The rating stays at one person (100 kg design mass, 2.5 kN static) | TKB-DDR-001, D8 |

## Safety

> **Safety:** TrunkBelay is a rope rescue and work-at-height kit. A mistake can drop a person from 6 to 25 m. It is published as an open engineering reference, not certified rescue or fall-protection equipment, and is not used on a person before a proof test of the collar on cut trunk sections and a supervised drill at low height (TRL 4). Emergency services are always called as well. A person who has hung head down for any length of time needs medical assessment after the rescue.
