---
doc_id: TKB-DDR-004
title: TrunkBelay concept selection
project: TrunkBelay
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: Concept selection record for the kit 1.9.1 upgrade; options A and B within 10 %, both put to Amish without a pick
---

# 0004: Concept selection

- **Date:** 2026-10-25
- **Status:** proposed, awaiting Amish (TKB-DEC-001, O5). Options A and B score within 10 % of each other, so both go to Amish without a pick (STANDARDS section 21). Until he decides, the repo carries option A, the constructable design of TKB-DDR-002 and TKB-DDR-003.

## Context

TrunkBelay was designed before kit 1.8, so its design became option A of the concept options record TKB-OPT-001. Kit 1.8 asks for at least two options with different working principles, scored against the user requirements (TKB-URS-001); kit 1.9 asks that every option be modelled to the repo's detail level, here D3 (`cad/src/model.py`, `cad/fidelity.json`: A 64 parts, B 25, C 34, all passing). All three options share the lowering side (auto-locking descender, brake carabiner, 30 m of rope, pre-rigged victim set); they differ in how the anchor holds on the trunk.

## Options considered

*Table 1. Options and scores (TKB-OPT-001, Table 2).*

| Option | Working principle | Weighted score | For | Against |
| --- | --- | --- | --- | --- |
| A, self-locking lever collar | A rigid V frame held by a chain wrap cocks under the load on its 150 mm lever; the grip rises with the load | 167 (95.4 %) | Constructable now, with drawings, priced BOM and build plan; the lock does not depend on how hard the chain was pulled or how a knot is dressed; fails slowly by settling | 4.67 kg carried; breaking load about 5.0 kN, at the low end of rescue practice (O7); needs an AC TIG welder; holds only a downward pull (drill rule); rests on unmeasured friction on wet bark (TKB-STM-001 S3) |
| B, constricting wrap anchor | A strap wrapped four turns and tied off as a Klemheist constricts as it is loaded; capstan friction holds it | 175 (100 %) | About 3.1 kg carried; bought parts only; gentle on the bark (about 0.2 MPa); about USD 100 cheaper | Holding of a friction hitch round a large, wet, tapering trunk under an axial pull is not covered by any cited source (B1); the hitch must be dressed right under stress; rated straps are rated for a pull across a structure, not along it; needs its own TRL 3 design |
| C, screwed stem anchor | A folded steel saddle screwed to the stem with four coach screws | 140 (80 %) | Holds a pull in any direction; familiar tools | About 7 kg carried with the tool; about 12 minutes to rig; four permanent wounds in the palm each use (fails PR-008); pull-out strength in palm tissue unknown (C1) |

## Decision

None yet. Proposed, awaiting Amish: choose between A and B (C is not recommended).

- If Amish keeps **A**, nothing in the repo changes; B's light wrap is recorded as an idea to graft later (a webbing wrap in place of most of the chain loop, with a cleat that keeps clear of the Cynch-Lok ratcheting cinch), to be studied only if he asks.
- If Amish chooses **B**, it becomes a new TRL 3 step for this repo: a constructable design, calculation note, drawings and build plan for the wrap anchor, keeping A's rigid V with rubber pads under the load point if it helps the hitch.

## Consequences

- Either way the first TRL 4 test is the same and is the one that decides whether any option works: friction and slip of the anchor on cut, wet coconut trunk sections at 2.5 kN (PR-001).
- `concept_chosen` in `project.yaml` stays unset until Amish decides; `concept_options` lists A, B and C.

> **Safety:** Each option holds a person at height. Whichever is chosen, nobody is lowered with it before its anchor has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height.
