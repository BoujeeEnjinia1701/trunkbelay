---
doc_id: TKB-RSK-001
title: TrunkBelay risk register and hazard analysis
project: TrunkBelay
doc_type: Risk register and hazard analysis
version: '0.2'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-25'
  author: Amish Chadha
  change: First risk register, preliminary hazard analysis and first-pass design FMEA (kit 1.9.1 upgrade, stage P3)
- version: '0.2'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'H6 and H12 controls as decided by Amish (O7, O8), 2026-10-25'
---

# TrunkBelay risk register and hazard analysis

The top risks are a collar that slides on a wet trunk because the friction is lower than assumed, a person dropped by a wrongly rigged or misplaced collar, and a strength margin at the low end of rescue practice; the top project risk is that no co-design partner runs the friction and drill tests that decide all three. Method: STANDARDS section 23. Likelihood, impact, severity and occurrence are scored 1 (low) to 5 (high); detection 1 (sure to be found before use) to 5 (not found).

> **Safety:** Every hazard below can drop a person from 6 to 25 m. Nobody is lowered with this kit before the collar has been proof-tested at 2.5 kN on cut trunk sections and the drill has been run with a dummy at low height (TKB-BLD-001, section 6). Emergency services are always called as well.

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | No co-design partner runs the TRL 4 tests | None of the first candidates (training scheme, fire station, climbers' collective) approached yet | The design stays on paper; the deciding unknown (friction) is never measured | 3 | 5 | Project lead | Approach the Friends of Coconut Tree training programme and a Kasaragod or Kannur fire station first (TKB-PLN-001) |
| P2 | Wet-bark friction below 0.58 on small trunks | Rubber and nylon on wet, fibrous, possibly algae-covered bark | Option A does not lock on 200 mm trunks; redesign of the lever geometry or pads | 2 | 5 | Design lead | Friction test first (BLD first check 1); recorded fallback: longer lever arm, higher-friction pad compound |
| P3 | Concept choice delayed | Options A and B within 10 % (TKB-DEC-001 O5) | Effort split between two anchors | 3 | 2 | Project lead | Put O5 to Amish with this upgrade; test both anchors' slip on the same trunk sections if he wishes |
| P4 | Bought rescue gear dearer than the BOM | The BOM's USD 280 descender is a class price; a cited branded device lists at USD 421 | PR-009 (USD 850) exceeded | 3 | 3 | Project lead | Group purchase by the training partner; one kit per climber group (19A) |
| P5 | Aluminium welding not available near the partner | AC TIG is less common than stick welding in rural workshops | Frames made far away or poorly welded | 3 | 3 | Fabrication partner | Find a shop with AC TIG before the build; weld test pieces first |
| P6 | Users take the open design as certified equipment | Published drawings and a working-looking kit | Use without training or proof testing | 2 | 5 | Project lead | "Not certified equipment" on every document, drawing and the spine marking; drill card with the gates |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Collar slides down the trunk under load | Friction on wet bark below what the lock needs; slack chain; bark sloughing off | Victim and rescuer dropped or jerked; fall from height | 5 | 2 | Self-locking geometry (factor 1.54 on assumed friction); pads and sleeve; friction and proof tests before any use on a person | Medium until the friction is measured |
| H12 | Collar slips on a leaning trunk | Frame on the adverse side of a trunk leaning 20 to 30 deg | Collar slides (as H1) | 5 | 2 | Lean limit of 20 deg (PR-003) and a drill rule that sets the frame on the favourable side (TKB-DEC-001 O8, decided 2026-10-25); friction test on a leaning section | Medium |
| H2 | Collar loaded upward | Collar set below the victim's attachment, or the victim swung above it | Single top chain lifts out of grip; collar slips | 5 | 2 | Drill rule: collar at least 300 mm above the attachment (16A); training; misuse test at TRL 4 | Medium |
| H3 | Shock load when the victim's feet are freed | Slack left in the rope | 2.6 to 3.0 kN at 30 mm of slack, 4.3 kN at 100 mm | 5 | 2 | Drill: take all slack through the descender first; frame covers a 30 mm drop (TKB-STM-001 S2); higher proof load (O7) | Medium |
| H4 | Rescuer loses the brake strand | Fatigue, a blow, fainting | Uncontrolled descent | 5 | 2 | Auto-locking descender with anti-panic function (PR-011); brake carabiner keeps the hand force near 80 N | Low |
| H5 | Victim slips out of the triangle or hangs head down | Wrong fitting; unconscious victim | Fall; airway risk | 5 | 2 | Pre-rigged triangle and chest sling on one carabiner (PR-012); drill with a dummy | Medium |
| H6 | Frame member or weld breaks | Poor TIG weld; overload beyond about 5.0 kN (4.5 kN with an unequal chain split); a slack drop of 100 mm (4.3 kN); fatigue after many uses | Fall | 5 | 2 | Welding procedure and inspection (BLD-001); proof test of every frame at 3.5 kN and a sample frame tested to failure, the stronger frame the fallback below 5:1 (TKB-DEC-001 O7, decided 2026-10-25); 55 mm cleat web (D-S2) | Medium (strength below the low end of practice in the worst case) |
| H7 | Chain or keeper released at height | Pin not fully in; keeper not over both slots | Collar released | 5 | 2 | Ball-lock pin through keeper, cheeks and web; fixed end tethered (PR-018); buddy check in the drill | Low |
| H8 | Dropped kit or tool strikes helpers | Parts dropped while rigging; the bag hauled up | Head injury below | 3 | 3 | Tethered fixed end, lanyarded pin; helpers stand clear while the bag moves; helmets | Low |
| H9 | Harm to the palm | Bare chain links on soft bark; over-tight wrap | Bark marks; permanent wounds (palms do not heal) | 2 | 2 | Pads at 1.9 MPa, sleeve 0.6 MPa, links mark about 0.3 mm; no spikes or screws (PR-008) | Low |
| H10 | Heat at the hand | Long fast lowering | Burn to the brake hand | 2 | 1 | Brake strand warms well under 1 K; gloves; lower at about 0.3 m/s (TKB-STM-001 S29) | Low |
| H11 | Victim's condition after hanging head down | Long suspension before help | Medical harm | 5 | 3 | Kit shortens the wait to minutes; emergency services always called; medical assessment after every rescue (soft, non-clinical wording) | Medium |

## Design FMEA (first pass, P3)

Table 3. Failure modes of option A. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Rubber bark pads | Grip and spread the load on the bark | Slip on wet bark | Collar slides (H1) | Friction lower than 0.5 assumed; glazed or oily rubber | 5 | 3 | 4 | 60 | Friction test on wet trunk sections (BLD first check 1); pad compound to choose from test; replace glazed pads |
| F2 | Chain sleeve | Grip at the back of the trunk, protect the bark | Slides or wears through | Lower grip; bark marked | Friction lower than 0.4; abrasion | 4 | 2 | 3 | 24 | Include in the friction test; replace when cut through (TKB-DWG-109) |
| F3 | Cleat web (spine top) | Hold the chain links in the slots | Ligament yields; slot faces wear or dent | Chain link slips out of its slot | All of the chain's pull on one slot (11.1 kN at 2.5 kN); steel on aluminium bearing at 92 MPa | 5 | 2 | 3 | 30 | 55 mm web (D-S2, factor 1.21 in the worst split); proof test on a 450 mm section with the chain pulled snug from one end; inspect slot faces (TKB-STM-001 S9, S10); O7 |
| F4 | Bar to spine welds | Carry the pad force into the spine | Crack in the weld or heat-affected zone | Bar bends or breaks | Poor AC TIG weld; porosity | 5 | 2 | 3 | 30 | Weld test pieces; visual and dye check of every frame; proof test |
| F5 | Keeper and lock pin | Keep the links in the slots | Pin not fully home, or lost | Link lifts out under a shock | Bark debris in the pin hole; lanyard cut | 5 | 2 | 2 | 20 | Buddy check; pin click; lanyard to the keeper |
| F6 | Tether link and tether hole (D-S1) | Keep the fixed end on the frame | Web strip bent; connecting link pin lost | Fixed end free when the keeper is off | Dropped frame; unpeened pin | 2 | 2 | 2 | 8 | Peen the pin; inspect the strip (TKB-DEC-001 item 14) |
| F7 | Load eye and doubler rings | Carry the load carabiner | Tear-out or wear of the eye | Load released | Overload far beyond 2.5 kN (factor 16 on tear-out) | 5 | 1 | 2 | 10 | Round the bore edges; inspect for grooves |
| F8 | Auto-locking descender (bought) | Control and stop the lowering | Fails to lock; wrong reeving | Uncontrolled descent | Wrong rope diameter; reeved backwards | 5 | 2 | 2 | 20 | Buy for 10.5 to 11.5 mm rope; maker's reeving check in the drill card |
| F9 | Brake carabiner (bought) | Turn the brake strand, lower the hand force | Gate open, cross-loaded | Higher hand force; carabiner damage | Gate not screwed shut | 3 | 2 | 2 | 12 | Buddy check of every gate |
| F10 | Rope (bought) | Carry and lower the person | Cut or abraded | Fall | Rope over a sharp edge; UV aged | 5 | 2 | 2 | 20 | Rope runs clear of the frame edges (model checks); retire on the maker's rules (TKB-STM-001 S26) |
| F11 | Evacuation triangle and chest sling (bought) | Hold the victim head up | Wrongly fitted; victim slips out | Victim falls or hangs badly | Haste at height | 5 | 2 | 3 | 30 | Pre-rigged set (17B); dummy drill; training |
| F12 | Frame (bare 6082-T6) | Whole-kit structure | Corrosion at steel contacts | Loss of section over years | Galvanic contact with steel chain, wet storage | 3 | 2 | 3 | 18 | Store dry; barrier paste at the rivet nuts; inspect after each season (TKB-STM-001 S25) |

The highest RPN (F1, 60) is the friction of the pads on wet bark, the same unknown that leads the STEM check (S3) and the feasibility assessment; it is the first TRL 4 test.
