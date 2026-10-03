---
doc_id: TKB-DDR-001
title: TrunkBelay TRL 2 review decisions
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
  change: TRL 2 review items decided under Amish's 2026-10-03 pre-approvals
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** decided, except where noted. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day for this batch: "Proceed with the remaining 15 scaffolds". Requirements that are not met or at risk are not decided here; they are open in the design decisions register (TKB-DEC-001), as Amish asked on 2026-10-03: "A simple statement doesn't add value - ensure you are identifying a state and posing it as a clear recommendation for me to decide on."

## Context

The scaffold (TKB-PRB-001, TKB-PRC-001 and TKB-REQ-001, all v0.1) described a chain collar with a slotted cleat, a padded bearing plate, a commodity friction device, a rope, a victim sling and a bag. It left five open questions: the load turning from upward to downward as the victim passes the collar, grip on wet and curved trunks, which friction device to use, how to fit a sling to an unconscious person hanging head down, and whether fire services would adopt the kit. Populating the concept to TRL 2 meant settling these on paper. Items that touch safety take the conservative option and say what evidence would relax it. Partners are the first candidates to approach, not agreements.

## Options considered

*Table 1. Options.*

| # | Item | Options |
| --- | --- | --- |
| D1 | How the collar grips | (a) a band tightened hard round the trunk (grip set by the rescuer's pull); (b) a self-locking frame, the load hung on a lever so the grip rises with the load |
| D2 | Bearing on the bark | (a) a curved padded plate; (b) two rubber-faced bars in a V |
| D3 | Where the collar goes | (a) level with the rescuer, below the victim, and loaded upward at first; (b) at least 300 mm above the point where the rope meets the victim, always loaded downward |
| D4 | Friction device | (a) a figure-eight descender; (b) a bar rack; (c) a Munter hitch on a carabiner; (d) an auto-locking descender with anti-panic, plus a brake carabiner |
| D5 | Victim attachment | (a) one sewn sling as a hasty seat; (b) an evacuation triangle with a chest sling |
| D6 | Rope and spare rope | (a) all rope in a bag hung on the collar; (b) the bag lowered to the helpers and the brake strand run to the ground |
| D7 | Rating | (a) a two-person load for fire crews; (b) one person, 100 kg design mass, sized for a 2.5 kN static load (R1) |
| D8 | First co-design candidates | Climber training programme, fire station, climbers' collective |
| D9 | Material | (a) steel, welded and hot-dip galvanised; (b) aluminium |

## Decision

*Table 2. Decisions.*

| # | Decision | Why |
| --- | --- | --- |
| D1 | (b) Self-locking frame. The load eye sits 150 mm out from the frame and the chain line 160 mm above its foot, so the frame cocks on the trunk | Grip does not depend on how hard a tired rescuer pulls; it rises with the load (TKB-CAL-001, B1 to B4) |
| D2 | (b) Two rubber-faced bearing bars in a 120 deg V | Touches every trunk from 200 to 450 mm on two lines and centres the frame; a curved plate fits one size |
| D3 | (b) for the drill as modelled. Whether this answers R2 or the collar is made to hold both ways is open: TKB-DEC-001, O1 | The single top chain cannot hold an upward pull on paper |
| D4 | (d) Auto-locking descender with anti-panic, brake strand over a carabiner on the spare eye | Conservative: it holds the victim if the rescuer lets go or pulls too hard. Relaxed only by a training trial showing that rescuers control a manual device reliably |
| D5 | (b) Evacuation triangle round the hips and a chest sling on the same victim carabiner | Turns the victim head up once the feet are freed and holds an unconscious person |
| D6 | (b) Bag lowered, brake strand to the ground | The rescuer handles one strand at height; the helpers manage the spare rope |
| D7 | (b) One person, 100 kg, 2.5 kN static. No use on a person before a proof test at 2.5 kN on cut trunk sections and a dummy drill at low height | Conservative gate; the rating is raised only by a test programme with a fire service partner |
| D8 | First candidates to approach (none approached yet): a coconut climber training programme under the Coconut Development Board's Friends of Coconut Tree scheme in Kerala; a Kerala Fire and Rescue Services station in Kasaragod or Kannur; a climbers' collective or labour bank in the same district | They teach, rescue and climb |
| D9 | (a) Steel, welded and galvanised, for the prototype. An aluminium frame is one of the options for R7 in TKB-DEC-001, O3 | Any village fabrication shop can make it |
| D10 | Pitch, problem, patent design-arounds and `budget_usd` unchanged | Scope rule |

## Consequences

- The cleat is a pair of plain slots with a keeper and pin, not a ratchet, which keeps the design-around of the 3M Cynch-Lok.
- The kit carries more than its 5 kg target and costs more than its USD 100 target; both are open decisions for Amish (TKB-DEC-001, O3 and O4).
- The drill's placement rule (D3) and rigging time are open decisions for Amish (TKB-DEC-001, O1 and O2).

> **Safety:** D3, D4 and D7 set safety limits. Each takes the conservative option and names the evidence that would relax it. Nobody is lowered with this kit until the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.
