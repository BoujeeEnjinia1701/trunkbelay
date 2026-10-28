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

## 2026-10-03: Amish's requirement decisions carried out

Amish Chadha, 2026-10-03: "i agree with all the 46 recommendations you provided. please proceed." For TrunkBelay these are decisions 16A (R2), 17B (R4), 18C (R7) and 19A (R9), each the recommended option, recorded in TKB-DDR-003. Not committed or pushed (batch run).

### Changes

- 16A, R2: no hardware change. The drill rule (collar at least 300 mm above the victim's attachment) stays in safety stop S6 and Step 10 of the build plan; the double-acting collar is recorded as the fallback. The TRL 4 first check now treats the upward pull as a misuse test and checks that a rescuer can reach above the attachment.
- 17B, R4: the victim set is packed pre-rigged: the rope's figure-eight loop, the triangle's two waist loops and one end of the chest sling on the victim carabiner, so two clips are left at height. `victim_kit()` in `cad/src/model.py` draws it, with three new checks.
- 18C, R7: the collar frame is 6082-T6 aluminium, TIG welded with ER5356, not galvanised, sized on the welded (heat-affected) strength: bars RHS 50 x 40 x 3; cheeks 8 mm; spine 5 mm with its top raised to 185 mm so the cleat web is 35 mm deep; doubler rings kept 4 mm so the quick link still passes; spare eye moved to 85 mm back, clear of the deeper bars; the adjustable chain tail runs out 75 mm before it hangs, clear of the bar; ball-lock pin grip 27 mm; pad screws into countersunk stainless rivet nuts. The helpers haul the rope bag up on 55 m of 4 mm tag line doubled through a micro pulley on the rescuer's harness. Five new frame checks; 218 of 218 constructability checks pass. STEP and STL regenerated.
- 19A, R9: the auto-locking descender and evacuation triangle stay; R9 restated in `docs/03-requirements.md` (TKB-REQ-001 v0.3, Amish quoted) as parts under USD 850 per kit at single-kit prices, with group purchase sought.
- `bom/bom.csv`: lines 1 to 5, 7 and 10 changed for aluminium, rivet nuts and the 27 mm pin; lines 22 (tag line) and 23 (micro pulley) added; each with a price basis.
- `docs/04-calcs/sizing.py`, `01-sizing.md` (TKB-CAL-001 v0.2) and `results.csv` re-run; `docs/01-problem.md` v0.3 (cost and carry constraints), `docs/02-concept.md` v0.4, README, `project.yaml` (evidence; `budget_usd` unchanged).
- `docs/05-build-plan.md` v0.2: aluminium making and welding text, new section 3.14 (tag line and micro pulley), Step 10 (pre-rigged set and the order at height), first checks, safety stops S1 and S6, tools and skills.
- Pictures: general arrangement TKB-DWG-001 Rev P2; making sketches TKB-DWG-101 to 109; overview (now 18 groups, with the tag line); joints 1 to 8; steps 1 to 10; concept media (hero, exploded, blueprint key figures, `model.glb`, viewer).
- Register `docs/06-design-decisions.md` v0.2: O1 to O4 moved to Decisions made; Open decisions now "None"; four items added to confirm. Decision record `docs/decisions/0003-amish-requirement-decisions.md` (TKB-DDR-003).
- Appearance model `cad/src/product_model.py`: bare aluminium frame colour and names, label moved clear of the moved spare eye; scenes re-exported to `/home/claude/renders/trunkbelay`.

### New results

- R2: at risk for an upward pull, as before; avoided by the drill rule (16A).
- R4: about 4.5 minutes once in position (target under 5): the pre-rigged set saves 45 s and the tag-line haul adds 45 s. Still at risk on a rough estimate; timed at TRL 4.
- R7: 4.55 kg carried up the trunk (target under 5 kg): met on paper. The helpers haul 3.7 kg; the whole kit is 8.3 kg. The decision estimate was about 4.4 kg; the difference is the doubled tag line (0.60 kg) that lets the helpers haul from the ground.
- R9: USD 826 a kit against the restated USD 850 (USD 24 under). Value-engineering target: USD 900. Estimated cost of the constructable design: USD 826 (USD 74 under the target). The changes cost USD 68 against the decision estimate of about USD 50 (aluminium frame about USD 29 net of galvanising, tag line and pulley USD 39).
- Frame strength at the R1 load of 2.5 kN, on the welded proof strength of 6082-T6 (125 MPa): bars 1.60, cleat web 1.55, cleat twist 2.0; welds 5.3 on the weld metal; the steel frame had 2.1 to 3.8 on yield. R1 (locking factor 1.54), R3, R5, R6 and R8 are unchanged.

### For Amish

- Nothing new to decide. Open decisions are "None"; R2 and R4 are settled by the TRL 4 drill and timed trial.
- The photoreal renders (`media/render-*.png`), card and social preview still show the galvanised steel frame; re-render on the Mac from the re-exported scenes.

### Safety

- The aluminium frame has smaller strength margins than the steel one, and aluminium beside a weld is about half as strong as the plate: no added or repair welds, every weld inspected (S1), and the TRL 4 proof test must look for permanent set in the frame.
- The collar holds only a downward pull: the 300 mm drill rule is a safety rule, not a preference (S6). Nobody stands under the bag while it is hauled up.
- The kit is not certified equipment, and nobody is lowered with it before the proof test and a dummy drill at low height.

## 2026-10-04: photoreal renders redone after the round-2 and round-3 decisions

Views: hero, exploded, detail; cards regenerated; image_qc passes and `render.py --check` has no FAIL.

## Session 2026-10-24: kit 1.9.1 upgrade

Run on Amish's instructions of 2026-10-24 ("Kit 1.9.1 rollout - proceed to rollout across the other repos"; "I want detailed TRL3 CAD - and in fact want to ensure the CAD is detailed across all TRLs"; "Detail every option") and his standing fix rule of 2026-10-23. The work was done on 2026-10-25; documents carry that date. Kit 1.9.1 was installed by the coordinator. The repo stays at TRL 3; `stage: P3`.

### What was added

- Pipeline documents: STEM check `docs/01b-stem-check.md` (TKB-STM-001) with `docs/04-calcs/stem_check.py`; concept options `docs/02a-concept-options.md` (TKB-OPT-001) and the selection record `docs/decisions/0004-concept-selection.md` (TKB-DDR-004); users-and-needs and stakeholder tables in `docs/01-problem.md` (v0.4); user requirements `docs/03a-user-requirements.md` (TKB-URS-001, 17 URs); `docs/03-requirements.md` is now the product requirements TKB-PRS-001 v0.4 (R1 to R10 migrated to PR-001 to PR-010, PR-011 to PR-018 added); traceability matrix `docs/03b-traceability.md` (generated, 0 gaps); regulatory register `docs/07-regulatory.md`, feasibility `docs/08-feasibility.md`, risk register with hazard analysis and design FMEA `docs/09-risk.md`, market `docs/10-market.md`, plan `docs/11-plan.md`.
- CAD: `cad/src/model.py` keeps its parametric engine and checks and gains the kit 1.9 interface (`PARAMS`, `OPTIONS`, `PRINCIPLES`, `CHOSEN = "A"`, `OPTION_VIEWS`, `ALLOWED_CONTACTS = []`, `components(option)`), with repo helpers in `cad/src/tkb_parts.py` (weld beads, detailed carabiners and descender, the lowering set). Every option at D3; STEP per made or bought part of option A in `cad/step/A/` (33 files) and `cad/step/{A,B,C}-assembly.step`; `cad/fidelity.json` passes. The chain's end interlocks are now exact (hook link, connecting links), the sleeve is a tube round the chain, every pad screw and rivet nut has its holes.
- Updated: CAL v0.3 (`[C1b]` combined bar stresses, `[C4b]` worst chain split, cited 600 g descender), PRC v0.5, BLD v0.3, DEC v0.3, BOM line 14 and line 1, `sizing.py`, `sheets.py` (TKB-DWG-001 Rev P3), `build_plan_media.py`, `concept_media.py`, `product_model.py` (rebuilt from `components(CHOSEN)` with a site scene), README in the house structure (the broken DOI badge, which contained an error message, is replaced by the concept DOI 10.5281/zenodo.23132240).
- Regenerated: STEP and STL (`python cad/src/model.py`, 0.2 mm tolerance), TKB-DWG-001, build plan pictures and making sketches TKB-DWG-101 to 109, concept media (`media/model.glb` 0.7 MB), and an interim `media/options.png` from `cad/src/options_preview.py`, marked PREVIEW on the picture.

### STEM verdicts and fixes

40 claims: 22 within known science, 17 plausible (to confirm at TRL 4), 1 fails with a fix proposed, 0 fail; `stem_check: open`. Option A: 32 claims, 19 within, 12 plausible, 1 fix proposed (S30). Fixes under the standing instruction (TKB-DEC-001):

- **D-S1** (found by the D3 model): the 8 mm tether quick link cannot pass a 6 mm grade 80 link (7.8 mm opening) and left no place for the hooked chain end beside the brake carabiner. Now a grade 80 connecting link through a new 10 mm tether hole 12 mm behind the spine front edge; the spare eye holds the brake carabiner alone; the fixed end is 6 links, so 15 links remain in the adjustable tail on a 450 mm trunk. BOM +USD 2.
- **D-S2** (found by the independent review): with all of the chain's pull on one slot the 35 mm cleat web reached factor 0.77. The spine top is raised 185 to 205 mm (55 mm web, factor 1.21); cheeks 75 mm high, keeper legs 73 mm; about 0.05 kg.

### Option scores (TKB-OPT-001)

| Option | Score | Parts (fasteners, welds) | Model mass, `cad/fidelity.json` | Carried |
| --- | --- | --- | --- | --- |
| A, self-locking lever collar (current) | 167 | 64 (17, 14) | 3.8 kg | 4.67 kg |
| B, constricting wrap anchor | 175 | 25 (9, 0) | 2.2 kg | about 3.1 kg |
| C, screwed stem anchor | 140 | 34 (17, 2) | 5.4 kg | about 7 kg |

A and B are within 10 % (4.6 %): both go to Amish without a pick. Model masses include the descender, carabiners and about 1.5 m of rope stubs, not the bag items.

### Independent review

A headless Claude session saw only the STEM check, CAL, PRS and `sizing.py`. It upheld the loads, lowering, heat, rope, fit and tether fit; weakened S2, S5, S6, S11, S13, S19, S20, S22 to S24 and S30; refuted S9 for an unequal chain split (fixed, D-S2) and S21 as worded; and added a leaning trunk (S31) and the tether hole (S32). All changes are in TKB-STM-001 Table 3.

### Requirements not met or at risk

- PR-002 (upward pull): at risk; drill rule (16A).
- PR-004 (rigging under 5 minutes): at risk, about 4.5 minutes estimated.
- PR-001 is met on paper only on an unmeasured friction, settlement is 14 to 18 mm with pad shear against 20, and the strength margin is below rescue practice in the worst case (S30).
- PR-008: at risk on green wood at the pads' lower edge (S19).
- PR-010: cannot be shown on paper; PR-013: to verify at TRL 4.
- BOM total USD 828 against `budget_usd` 900 (value-engineering target) and PR-009's USD 850; a branded descender at the cited USD 421 would take the kit to about USD 969.

### Decisions awaiting Amish (TKB-DEC-001)

- **O5** concept selection: A or B (no pick, within 10 %); C not recommended.
- **O6** appearance of the kit 1.9 renders: hero in a coconut plantation at drill height (collar foot 1.4 m up, ground at z = 0, soil), both strands carried down to the rope bag on the ground, two more palms behind, a 1.75 m helper standing on the ground, the safe working load label. Recommended: accept.
- **O7** strength target (safety trade-off): about 5.1:1 (4.5:1 worst split) against the 5:1 to 10:1 of rescue practice; recommended: raise the TRL 4 proof load to 3.5 kN and test a sample frame to failure, with a stronger frame as the fallback.
- **O8** leaning trunks: lean limit of 20 deg in PR-003 and a drill rule for the frame's side; recommended: both.

### Safety concerns

The lock rests on an unmeasured friction on wet bark; the strength margin is thin by rescue standards; a slack drop of 100 mm (4.3 kN) exceeds the frame. Nobody is lowered with the kit before the friction and proof tests and a dummy drill (TRL 4, on hold).

### Renders and checks

Not run, as the rollout asks: `.kit/options.py` without `--export`, `photoreal.py`, `export_views.py`, `cards.py`. The coordinator renders `media/options.png` (replacing the preview) and the `RENDER_VIEWS` hero, studio, exploded and detail; `media/render-studio.png`, linked from the README, does not exist until then, and `render-hero.png`, `render-exploded.png`, `render-detail.png` and the cards are the renders of 2026-10-04 (before D-S1 and D-S2).

### Kit issues met

1. `stem_check.Check.summary()` counts a Plausible row as closed whenever `closed_by` is not empty, so "Open: ..." text reported the check as pass; worked around by leaving `closed_by` empty on open rows.
2. `render.py --check` requires `media/options.png`, which only `.kit/options.py` with Blender writes; worked around with the labelled `cad/src/options_preview.py`.
3. The verdict label "Plausible, to confirm at TRL 3" is fixed in the kit, though in a TRL 3 repo the open rows are confirmed at TRL 4.
4. `cad_check.is_bare()` counts any three-face solid as bare, so a straight rope strand fails; the load strand is drawn with a kink.
5. `trace.py` bumps the RTM version on every run while sources change; the matrix was regenerated from scratch at the end.
6. Repo housekeeping (not kit): two decision records share TKB-DDR-003 (`0003-amish-requirement-decisions.md` and `0003-requirement-decisions-round2.md`); renumbering is left for Amish.

### Recommended next step

Amish decides O5 to O8. The coordinator renders the options picture and product views. TRL 4 stays on hold under the cap; when it opens, the first test is the friction of the pads and sleeved chain on cut, wet trunk sections.

## Session 2026-10-25: decisions

Amish, 2026-10-25 10:19 CT, after a report listing each repo's proposed decisions and recommendations: "i concur with your recommendations". Every decision that carried a recommendation is recorded as decided with the option recommended; every decision without a pick stays open.

### Decided by Amish, 2026-10-25

- **O6, render appearance:** the kit 1.9 departures accepted (site scene at drill height, helper, strands to the rope bag, two more palms, safe working load label). No change.
- **O7, strength target:** option C. The 2.5 kN design load (PR-001) stays; the TRL 4 proof load is raised to **3.5 kN** and a sample frame is tested to failure, with the stronger frame (option B, about 10:1) as the fallback if it shows less than 5:1. PR-001 verification text; build plan first checks (static hold and proof at 2.5 then 3.5 kN; new "frame to failure" check, pass at 5 kN or more); PLN test rig line; RSK H6; STEM S30 from "fails, fix proposed" to **Plausible, to confirm by the test** (`docs/04-calcs/stem_check.py`). No part, dimension or price changed; the estimated breaking load stays about 5.0 kN (5.1:1; 4.5:1 with all the chain's pull on one slot).
- **O8, leaning trunks:** option C. PR-003 gains a **20 deg lean limit**, and the drill rule sets the frame on the favourable side of a leaning trunk (build plan table; RSK H12; STEM S31 closing route; FEA). Locking factor on the adverse side stays 1.21 at 20 deg on the assumed friction, to confirm by test.
- Documents: TKB-DEC-001 v0.4, TKB-PRS-001 v0.5, TKB-STM-001 v0.2 (22 within, 18 plausible, 0 fail across the options; `stem_check` stays open), TKB-BLD-001 v0.4, TKB-RSK-001 v0.2, TKB-PLN-001 v0.2, TKB-FEA-001 v0.2, TKB-OPT-001 v0.2, README.

### Still open (no recommendation to concur with)

- **O5, concept selection:** A (167) and B (175) are within 10 % and went to Amish without a pick; `concept_chosen` stays unset and the repo carries A.

### Checks

Run in this order on 2026-10-25 (no edit to `cad/src/` or `bom/bom.csv` this session):

- `python3 docs/04-calcs/sizing.py`: runs (figures unchanged).
- `python3 docs/04-calcs/stem_check.py`: open, 22 within, 18 plausible, 0 fail.
- `python3 .kit/trace.py`: RTM regenerated, 0 gaps.
- `python3 .kit/cad_check.py --export`: PASS at D3.
- `python3 .kit/render.py` and `python3 .kit/render.py --check`: pass, no FAIL.
- `python3 -m reuse lint`: compliant.
- Em and en dash scan outside `.kit/` and `LICENSES/`: none.
