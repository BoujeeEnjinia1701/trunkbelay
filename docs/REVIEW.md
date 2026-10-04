# Review note: TrunkBelay

## Session 2026-10-03: round 2 requirement decisions applied

Amish, 2026-10-03: "i approve all of the 47 recommendations provided by you. Execute them." For TrunkBelay these are portfolio decisions 41 to 44, the recommendations on O1 to O4, each decided exactly as worded: 41 A (keep the drill rule that sets the collar 300 mm or more above the victim's attachment; B, the double-acting collar, is the fallback if the TRL 4 drill shows a rescuer cannot reach above the attachment), 42 B (pack the victim set pre-rigged on the victim carabiner), 43 C (haul line plus aluminium 6082-T6 frame), 44 A (keep the auto-locking descender and triangle; savings through group purchase and one kit per climber group). Record: `docs/decisions/0003-requirement-decisions-round2.md` (TKB-DDR-003).

### What changed

- `cad/src/model.py`: frame material aluminium 6082-T6 (`frame_material`); bearing bars RHS 70 x 30 x 5 (was 50 x 25 x 2.5 steel), 4 mm end caps, eye doubler rings 6 mm (was 4), cleat cheeks 8 mm (was 6); spine kept at 5 mm because a chain link must span it; tag line and shoulder pouch in the mass table and the kit pictures; `CARRIED` and `carried_mass()` for R7; new check bars to doubler rings. 213 of 213 constructability checks pass. STEP and STL files re-exported.
- `docs/04-calcs/sizing.py`, `results.csv`, `01-sizing.md` (TKB-CAL-001 v0.2): frame strength in the heat-affected zone of the TIG welds (125 MPa), rigging time with the haul and pre-rigged set, carried mass, cost.
- `bom/bom.csv`: lines 1 to 5 in aluminium with AC TIG welding and no galvanising; lines 7 to 10, 16, 18 and 21 notes; new line 22 (tag line, 30 m of 4 mm cord) and 23 (10 l shoulder pouch). Prices are estimates derived from the steel lines.
- `docs/05-build-plan.md` (TKB-BLD-001 v0.2): aluminium parts, TIG welding and its limits, no galvanising, keeper 28 mm wide, pin 28 mm grip, tag line and pouch, step 10 packs the victim set pre-rigged, first checks for R2 (misuse test), R4 (with the reach check that triggers the fallback) and R7 (pouch under 5 kg), safety stop S1 and tools.
- `cad/src/build_plan_media.py`: making sketches TKB-DWG-101 to 105 and 107 texts, joint 2 and steps 1 to 3 and 10 captions; overview and step 10 show the pouch and tag line. All build plan pictures regenerated.
- `cad/src/sheets.py`: TKB-DWG-001 Rev P2 regenerated. `cad/src/concept_media.py`: key figures; hero, exploded, flow, concept blueprint, `media/model.glb` (linear deflection 1.0, angular 0.35) and viewer regenerated. `cad/src/product_model.py`: frame look changed from galvanised steel to mill-finish aluminium.
- `docs/03-requirements.md` (TKB-REQ-001 v0.3), `docs/02-concept.md` (TKB-PRC-001 v0.4), `README.md`, `docs/06-design-decisions.md` (TKB-DEC-001 v0.2), `project.yaml` (comment and `trl_evidence`; `budget_usd` unchanged at USD 900).

### How decision 43 was sized

The option was costed with every steel part 40 % thicker in aluminium. TIG welding halves the strength of 6082-T6 beside the weld (125 MPa against 260 MPa), and every highly loaded section of this frame lies beside a weld. A 40 % thicker bar (RHS 50 x 25 x 3.5) would carry 135 MPa at its weld at the R1 load, a factor of 0.92: it would yield below 2.5 kN. The bars were therefore sized to keep the steel design's factor of about 2 (RHS 70 x 30 x 5, factor 2.0), held to 30 mm deep to clear the spare eye ring and 70 mm high to clear the chain's fixed-end tail. The aluminium weldment is 1.37 kg against 2.22 kg in steel, a saving of 0.85 kg rather than the 1.2 kg first estimated.

### Requirement status, before and after

| Req. | Before | After |
| --- | --- | --- |
| R1 | Met on paper, friction to confirm | Met on paper, friction to confirm; **aluminium cleat web factor 1.1** on its heat-affected proof strength at the R1 load (2.8 at the working load; 3.1 in steel): new question O5 |
| R2 | At risk | At risk on paper, controlled by the drill rule (41 A); upward case a misuse test only |
| R4 | At risk, 4.5 min | Met on paper (estimate), 4.2 min |
| R7 | Not met, 8.9 kg | **Met on paper, 4.74 kg carried**, a 257 g margin; whole kit 8.5 kg |
| R9 | Not met, USD 758 | Not met, USD 802; accepted by Amish (44 A) |

R3, R5, R6, R8 and R10 unchanged.

### Cost

Value-engineering target: USD 900. Estimated cost of the constructable design: USD 802 (USD 98 under the target), up from USD 758: aluminium parts and TIG welding about USD 29 more than the steel parts, welding and galvanising; tag line and pouch about USD 16 (estimates). `budget_usd` unchanged.

### Decisions proposed and awaiting Amish

**O5, R1 (strength margin of the aluminium cleat).** State: the 5 mm aluminium cleat web carries 113 MPa at the R1 load; beside the cheek welds that is a factor of 1.1 (2.3 on unwelded metal, 2.8 at the working load), against 3.1 for the steel cleat. The web cannot be thickened, and the steel chain will wear the aluminium slot edges.
- A. Steel cleat insert: the slotted top of the spine made as a separate 5 mm S355 galvanised plate, bolted to the aluminium spine between the cheeks with two M8 stainless bolts and the lock pin. Factor back to about 3.1, wear-resistant slots; about 0.1 kg and USD 5 more (4.84 kg carried, R7 still met).
- B. Keep the welded aluminium cleat; the TRL 4 proof test shows it; inspect the slots for wear before every use. No cost or mass.
- C. Heat-treat the welded frame back to T6: factor about 2.3, slots still aluminium; about USD 30, risk of distortion.
- **Recommendation: A**, because the cleat holds a person.

Fallback held from 41: if the TRL 4 drill shows a rescuer cannot reach above the attachment, the double-acting collar comes back to Amish.

### Re-render

The hero geometry changed (bars 70 x 30 instead of 50 x 25, thicker eye rings and cheeks) and the frame finish changed from galvanised steel to bare aluminium, so `media/render-hero.png`, the other photoreal renders, `media/card.png` and `media/social-preview.png` need redoing on Amish's Mac from `cad/src/product_model.py`. They are not made here.

### Safety

- The collar holds only a downward pull on paper. The drill rule (collar 300 mm or more above the victim's attachment) is the only thing that prevents an upward pull; it stays in safety stop S6, the precis, the README and every drill.
- The auto-locking descender and the evacuation triangle stay (44 A): no saving is taken against the security of an unconscious person.
- The pre-rigged victim set is checked before every use: gate screwed shut, loops not twisted, crotch loop free.
- The aluminium frame needs an aluminium-qualified welder; welds only where drawn, never heated to straighten; dye-penetrant check after welding (S1). Its cleat has less margin than the steel one (O5).
- Nobody is lowered with the kit before the 2.5 kN proof test on cut trunk sections and a dummy drill at low height. It is not certified equipment.

### Recommended next step

Amish decides O5. The design then stands at TRL 3; TRL 4 starts only when Amish chooses.

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
