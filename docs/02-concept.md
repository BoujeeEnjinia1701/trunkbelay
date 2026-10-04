---
doc_id: TKB-PRC-001
title: TrunkBelay design precis
project: TrunkBelay
doc_type: Precis
version: "0.4"
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
  change: TRL 2 precis; how it works, components with BOM numbers, key design choices, first-order numbers, safety
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 3; constructable design of TKB-DDR-002 and figures from TKB-CAL-001
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: Round 2 decisions (TKB-DDR-003); aluminium frame, tag-line haul, pre-rigged victim set, figures from TKB-CAL-001 v0.2
---

# TrunkBelay design precis

Lets a fellow climber anchor and lower a climber stranded high on a palm trunk.

![Figure 1. TrunkBelay collar on a 300 mm palm trunk, with the descender and rope](../media/hero.png)

*Figure 1. The collar on a 300 mm trunk, seen from the front right and above. The grey hand on the brake strand gives the scale.*

## How it works

TrunkBelay is an aluminium collar that grips a palm trunk harder the more load hangs from it, with a commodity rope descender clipped to it. The rescuer climbs on their own climbing device to just below the stranded climber, carrying the collar, the descender and a 4 mm tag line in a shoulder pouch (4.74 kg), and works in four stages. The helpers keep the rope bag on the ground.

1. **Fix the collar.** The rescuer holds the collar frame against the trunk, with its two rubber-faced bearing bars touching the bark, passes the chain round the trunk, drops a link into the open slot on top of the frame, pulls the chain snug and slips the keeper and lock pin on. The frame is set at least 300 mm above the point where the rope will meet the victim; this drill rule is what keeps the collar from ever being pulled upward (decision 41 A).
2. **Rig the lowering.** The rescuer drops one end of the tag line to the helpers, who tie on the rope's loop end with the victim set already clipped to it, and hauls it up. The descender is clipped to the load eye at the outer end of the frame and the rope reeved through it. The brake strand turns over a carabiner on the spare eye and runs down to the rope bag on the ground.
3. **Take the weight.** The victim set comes pre-rigged: the triangle's side loops, the chest sling and the rope's end loop are already on the victim carabiner (decision 42 B). The rescuer fits the triangle round the victim's hips and the sling round the chest, makes the one clip left (the triangle's crotch loop), and pulls all slack through the descender, which locks.
4. **Free and lower.** The rescuer frees the victim's feet from the climbing device. The victim turns head up in the triangle and hangs from the collar. The rescuer opens the descender with its handle and lowers the victim to the helpers, holding the brake strand. The rescuer then takes the kit down and descends on their own device.

The load eye sits 150 mm out from the frame. The pull of the rope on the eye tilts the frame on the trunk: the bearing bars press the bark low on the near side and the chain presses it high on the far side. The friction at those two places rises in step with the load, so the collar is self-locking, like a drawer that jams when it is pulled from one corner (TKB-CAL-001, section B).

![Figure 2. The kit's parts pulled apart, with BOM numbers](../media/exploded.png)

*Figure 2. Exploded view; numbers match bom/bom.csv.*

## Components

*Table 1. Components and their BOM lines.*

| BOM | Component | Role |
| --- | --- | --- |
| 1 | Spine plate | 5 mm aluminium 6082-T6 plate in the frame's centre plane: carries the bearing bars at its foot, the chain slots at its top and the load and spare eyes at its outer end |
| 2 | Bearing bars (2) | 70 x 30 x 5 mm aluminium box section set in a 120 deg V at the foot of the spine; they bear on the bark through the pads |
| 3 | Eye doubler rings (4) | 6 mm rings that thicken both eyes to 17 mm so a carabiner bears on a rounded, wide edge |
| 4 | Cleat cheeks (2) | 8 mm plates that stiffen the slotted top of the spine; notched so the chain links bear on the 5 mm web |
| 5 | TIG welding | The frame is one TIG-welded aluminium piece, left bare (no galvanising) |
| 6, 7, 8 | Rubber bark pads (2), screws, adhesive | 10 mm rubber on each bar spreads the load on the bark and adds grip |
| 9, 10 | Keeper and lock pin | Hold both chain links down in their slots |
| 11 to 14 | Chain set | 6 mm grade 80 chain, 110 links, with a master link on the adjustable end and a quick link tethering the fixed end to the spare eye |
| 15 | Chain sleeve | 600 mm of tubular webbing on the chain where it bears on the back of the trunk |
| 16 | Carabiners (3) | Load eye to descender, brake redirect, victim connector |
| 17 | Auto-locking descender | Controls the lowering; locks if the rescuer lets go |
| 18 | Lowering rope | 30 m of 11 mm semi-static rope |
| 19, 20 | Evacuation triangle and chest sling | Hold the victim head up once the feet are freed |
| 21 | Rope and carry bag | Holds the rope, with the pre-rigged victim set on top; stays with the helpers on the ground |
| 22, 23 | Tag line and shoulder pouch | 30 m of 4 mm cord to haul the rope's loop end and the victim set up; the pouch carries the collar, descender, carabiners and tag line hands-free |

## Key design choices

The first were made under Amish's pre-approval of 2026-10-03 and are recorded in TKB-DDR-001 and TKB-DDR-002. Amish decided the requirements that were not met or at risk on 2026-10-03 (TKB-DDR-003). Open questions are in the design decisions register (TKB-DEC-001).

- **Self-locking frame, not a tightened band.** The grip comes from the load's lever on the frame, so it does not depend on how hard the rescuer pulled the chain. The chain only has to be snug.
- **A V of two bars, not a curved saddle.** A 120 deg V touches any trunk from 200 to 450 mm on two lines and centres itself; a curved saddle fits only one size.
- **A generic slotted cleat, no ratchet.** Chain links drop into two plain slots in the spine top and are held by a keeper and pin. This keeps clear of the ratcheting cinch geometry of the 3M DBI-SALA Cynch-Lok (the patent design-around) and has no moving parts to clog with bark.
- **Auto-locking descender.** The conservative choice: if the rescuer is hit, faints or lets go, the descender holds the victim.
- **Brake strand to the ground.** The spare rope goes down to the helpers, so the rescuer does not manage a rope bag at height.
- **Aluminium 6082-T6, TIG welded, with the rope hauled up on a tag line.** Chosen by Amish to meet the 5 kg carried mass of R7 (decision 43 C). Welding halves the strength of 6082-T6 beside the weld, so the bars are larger than first estimated and the cleat has less margin than the steel one (TKB-DEC-001, O5). The frame needs a fabricator with AC TIG and a welder qualified on aluminium, not any village shop.
- **Keep the auto-locking descender and the triangle.** Amish kept the conservative choice over cheaper ones that hold an unconscious person less securely or lose the hands-free lock (decision 44 A); savings are sought through group purchase and one kit per climber group.

## First-order numbers

From TKB-CAL-001; assumptions are stated there.

*Table 2. Key figures (estimates).*

| Quantity | Value |
| --- | --- |
| Trunk range | 200 to 450 mm across, no tools |
| Working load on the collar, 100 kg person | 0.99 kN |
| Static load the collar is sized for (R1) | 2.5 kN |
| Friction needed to lock, 200 mm trunk (worst) | 0.58, against about 0.9 assumed on wet bark; locking factor 1.54 |
| Frame settles under 2.5 kN | About 10 mm |
| Strength at 2.5 kN | Bars 2.0 and cleat web 1.1 times the welded-zone proof strength of the aluminium; chain 8.1 times its breaking force; rope 5.7 times at the knot |
| Hand force on the brake strand, 100 kg | About 80 N |
| Rope | 30 m; 28 m needed for a 25 m lowering |
| Rigging time once in position | About 4.2 minutes (estimate) |
| Mass | 4.74 kg carried by the rescuer (collar 3.6 kg); whole kit 8.5 kg |
| Cost | Value-engineering target: USD 900. Estimated cost of the constructable design: USD 802 (USD 98 under the target) |

## Patent design-arounds

From the preliminary patent, trademark and prior-art screen (not legal advice):

- Generic chain-and-cleat collar; avoid the 3M Cynch-Lok ratcheting cinch geometry and cleated-plate arrangement. The constructable design has no ratchet, no cam and no cleated gripping plate: plain slots, rubber-faced bars and a lever.
- CA2681870C (Bashlin) lapsed in 2015; WO2012131439A1 ceased; neither blocks the concept.

## Shared blocks

- CalRig proof-load (collar slip and proof tests on trunk sections)
- PalmSpan collar data (shelved sibling), for grip across palm sizes

## Safety

> **Safety:** TrunkBelay is rope rescue and work-at-height equipment. A slip of the collar, a wrongly fitted triangle or a lost brake hand can drop a person from 6 to 25 m. It is published as an open engineering reference, not certified rescue or fall-protection equipment.
>
> - Only people trained in the drill use it, and they practise at low height first.
> - Always call emergency services as well; TrunkBelay is for the minutes before they arrive.
> - The collar is not used on a person before it has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height (TRL 4). The build plan's safety stops gate both.
> - The collar is loaded gently. All slack is taken in before the victim's feet are freed, so the victim never drops onto the collar (TKB-CAL-001, A2).
> - The collar is set at least 300 mm above the point where the rope meets the victim, so it is never pulled upward. On paper the collar does not hold an upward pull; the drill rule is the only thing that prevents it.
> - The aluminium frame must be TIG welded only where the drawings show, by a welder qualified on aluminium, and never heated to straighten it.
> - A person hanging head down for a long time needs medical assessment after rescue.

This design is published as an open engineering reference. It is not certified equipment.
