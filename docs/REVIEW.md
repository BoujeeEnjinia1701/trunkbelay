# Review note: TrunkBelay

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (TKB-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (TKB-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (TKB-REQ-001 v0.1): 10 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate)

Run as the first half of `/to-trl3` in Batch 2, under Amish's pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost." and his instruction of the same day: "Proceed with the remaining 15 scaffolds". Kit 1.7.0 installed.

### What was done

- `docs/01-problem.md` (TKB-PRB-001 v0.2): constraints restated with the value-engineering target, open questions answered on paper, first co-design candidates, safety section.
- `docs/02-concept.md` (TKB-PRC-001 v0.2, then v0.3 at TRL 3): how it works in four stages, components with BOM numbers, key design choices, first-order numbers, design-arounds kept, safety.
- `docs/03-requirements.md` (TKB-REQ-001 v0.2): targets unchanged; status on paper for all ten requirements.
- Concept media from `cad/src/concept_media.py`: `media/hero.png` (300 mm trunk and the rescuer's hand for scale), `media/concept-blueprint.png`, `.pdf` and `.svg` (TKB-DWG-010), `media/model.glb` (4.2 MB) and `media/viewer.html`, `media/exploded.png` with BOM callouts, `media/flow.png` (energy of a 25 m lowering, estimates). No cutaway: nothing inside matters to the concept. The chain is drawn as its envelope in the concept media.
- `bom/bom.csv`: 21 priced lines.

### Results

- The collar works on paper as a self-locking frame: the load on a lever makes the grip rise with the load.
- The open question of the load turning direction is avoided by the drill, not by the hardware; this is posed to Amish (R2, O1).

### Decisions made under the pre-approvals

TKB-DDR-001, D1 to D10: self-locking frame; V of rubber-faced bars; collar above the victim's attachment in the drill as modelled; auto-locking descender with a brake carabiner; evacuation triangle and chest sling; spare rope to the ground; one-person 100 kg rating at 2.5 kN; first co-design candidates (not approached); steel, welded and galvanised; pitch, problem, design-arounds and budget unchanged.

### Safety concerns

- A failure drops a person from up to 25 m. The kit is not certified equipment, and no one is lowered with it before a proof test and a dummy drill (TRL 4).

## Session 2026-10-03: TRL 3 (advance and build plan)

Run as the second half of `/to-trl3` under the same pre-approvals, which count as the TRL 2 approval.

### What was done

- `cad/src/model.py`: parametric build123d model of the constructable kit on 200, 300 and 450 mm trunks; 210 of 210 constructability checks pass (contacts, clearances to the trunk and between parts, chain links in the slots, pad contact point, chain length). Exports `cad/step/trunkbelay-assembly.step`, `cad/step/trunkbelay-frame-weldment.step` and two STL files in `cad/stl/`.
- `docs/04-calcs/01-sizing.md` (TKB-CAL-001 v0.1) with `docs/04-calcs/sizing.py` and `results.csv`: loads, grip and locking factor, strength, lowering, fit and rigging, mass, bark pressure, cost, and a results table against every requirement.
- `cad/src/sheets.py`: general arrangement `cad/drawings/TKB-DWG-001` (SVG, PDF, PNG) at Rev P1.
- `cad/src/build_plan_media.py`: `docs/05-build-plan/overview.png`, 9 making sketches `cad/drawings/TKB-DWG-101` to `109`, 8 joint close-ups and 10 step pictures.
- `docs/05-build-plan.md` (TKB-BLD-001 v0.1), `docs/06-design-decisions.md` (TKB-DEC-001 v0.1), `docs/decisions/0001-trl2-review-decisions.md` (TKB-DDR-001) and `docs/decisions/0002-design-for-construction.md` (TKB-DDR-002).
- `cad/src/product_model.py` (appearance model) and render scenes exported with `.kit/export_views.py` to `/home/claude/renders/trunkbelay` for hero, exploded and detail views; photoreal renders and cards are made on Amish's Mac.
- `project.yaml`: trl 3, trl_target 3, `design_state: constructable`, evidence listed; `budget_usd` unchanged. README leads with `media/render-hero.png` and has a "Building the prototype" section.

### Results

- Locking factor 1.54 on a 200 mm trunk, 1.86 on 300 mm and 2.35 on 450 mm, against an assumed combined friction of 0.9 on wet bark (0.58 needed at worst). The frame settles about 10 mm at 2.5 kN.
- At 2.5 kN: bearing bars 2.1 times yield, welds 3.5, cleat web 3.1, chain 8.1 on breaking force, rope 5.7 at the knot, carabiners 10.
- Brake hand force about 80 N for 100 kg with the brake carabiner (about 150 N without it).
- A slack drop of 30 mm when the feet are freed gives about 2.6 kN; the drill takes in all slack first.
- Rope 28 m needed of 30 m; rigging about 4.5 minutes once in position (estimate).
- Mass: collar 4.4 kg, kit 8.9 kg.
- Value-engineering target: USD 900. Estimated cost of the constructable design: USD 758 (USD 142 under the target).

### Requirements not met

- R7: 8.9 kg carried (not met).
- R9: USD 758 a kit, over the value-engineering target of R9 by USD 658 (not met).
- R2: at risk; the single top chain holds only a downward pull.
- R4: at risk; about 4.5 minutes on a rough estimate.
- R10 cannot be shown on paper (training trial at TRL 4). R1, R5 and R8 are met on paper subject to the items to confirm.

### Decisions for Amish

Proposed, awaiting Amish (also in TKB-DEC-001, Open decisions).

**O1, R2 (load passing the collar).** State: on paper the collar holds only a downward pull; with one chain at its top, an upward pull on the load eye has no second contact below to hold against. The drill as modelled avoids the case by setting the collar 300 mm or more above the victim's attachment.
- A. Keep the drill rule; test the upward case only as a misuse test and check in the timed drill that a rescuer can reach above the attachment. No cost or mass; the upward case stays unproven.
- B. Double-acting collar: a second chain through a cheeked slot block at the frame foot, so it locks either way. R2 expected met on paper; about USD 45 and 1.7 kg more (worsens R7).
- **Recommendation: A**, with B as the fallback if the TRL 4 drill shows a rescuer cannot reach above the attachment.

**O2, R4 (rigging time).** State: about 4.5 minutes once in position, a thin margin on a rough estimate; fitting the triangle and chest sling (about 2 minutes) is the largest part.
- A. Keep the drill and time it at TRL 4. No cost or mass.
- B. Pack the victim set pre-rigged (triangle loops and chest sling already on the victim carabiner with the rope's loop): about 45 s saved, about 3.8 minutes; no cost or mass.
- C. A quick-fit hip loop in place of the triangle: about 60 s saved, about USD 100 less; holds an unconscious person less securely.
- **Recommendation: B**; it also absorbs the 45 s that O3's tag line adds.

**O3, R7 (kit mass).** State: 8.9 kg carried; steel frame 2.6 kg, chain set 1.9 kg and rope 2.3 kg are the bulk.
- A. Helpers haul the rope bag (rope, triangle, sling) up on a 4 mm tag line: 5.5 kg carried, about USD 10, about 45 s more rigging.
- B. Aluminium frame (6082-T6, 40 % thicker, TIG welded): 7.7 kg carried, about USD 40 more.
- C. Both: 4.4 kg carried, about USD 50 more, about 45 s more rigging.
- **Recommendation: C**, the only option that meets the target.

**O4, R9 (cost per kit).** State: USD 758 a kit, over the value-engineering target of R9 by USD 658; descender USD 280, triangle USD 140 and rope USD 105 dominate.
- A. Keep the auto-locking descender and triangle: USD 758; the conservative safety choice.
- B. Two-sling hasty seat in place of the triangle: about USD 642 and 0.5 kg lighter; less secure for an unconscious person.
- C. Workshop bar rack with a friction-hitch backup in place of the descender: about USD 520; loses the hands-free lock.
- **Recommendation: A**, with savings sought through group purchase and one kit per climber group.

### Decisions made under the pre-approvals

- TKB-DDR-002: design for construction, changes C1 to C11 and assumptions A1 to A6.
- No use on a person before a proof test of the collar at 2.5 kN on cut trunk sections and a dummy drill at low height.
- Appearance model departures (renders only): a safe working load label on the spine, a 400 mm trunk with leaf-scar rings (inside the 200 to 450 mm range), the rope cut 450 mm below the frame, and a clay forearm and hand holding the brake strand from the far side for scale.

### Build plan findings

- Design changes for construction (2026-10-03), all in TKB-DDR-002: V of box-section bearing bars with bonded and screwed rubber pads; one 5 mm spine plate; the cleat as two slots in the spine top with notched 6 mm cheeks (the web must be 6 mm or thinner for a 6 mm link to span it, and the cheeks carry the twist); a bent sheet keeper and ball-lock pin; the fixed chain end in a slot and tethered to the spare eye with a quick link; eyes thickened with doubler rings; the lever geometry; a 110-link chain with a master link and painted slot links; the chain sleeve; the brake carabiner; galvanising and marking.
- The pad screws' nuts sit inside the box bars; the plan offers rivet nuts if they cannot be reached.
- The concept media draw the chain as its envelope to keep the hidden-line views quick; the build plan pictures and the product model show the links.
- Items to confirm with real parts (friction on wet bark, chain dimensions, descender data, rope, rubber bond, trunk survey, triangle fitting time, spare eye layout) are in TKB-DEC-001.

### Safety concerns

- Rope rescue at height: a slipping collar, a lost brake hand or a badly fitted triangle can drop a person up to 25 m. The kit is not certified equipment. Safety stops S1 to S6 in TKB-BLD-001 gate galvanising, first load, the proof test, work at height and every use.
- The lock rests on an assumed friction on wet bark; measuring it on cut trunk sections is the first TRL 4 task.
- The victim must never drop onto the collar: all slack is taken in before the feet are freed.
- A person who has hung head down needs medical assessment after the rescue; emergency services are always called.

### Recommended next step

Amish decides O1 to O4. The design then looks ready for TRL 4 once Amish chooses to start it: build one collar, measure friction and run the 2.5 kN hold on wet cut trunk sections with CalRig, then a timed dummy drill at 3 m with the first co-design candidate.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
