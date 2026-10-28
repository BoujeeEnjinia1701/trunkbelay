"""TrunkBelay STEM check calculations (TKB-STM-001, STANDARDS section 20).

Run from the repo root:  python docs/04-calcs/stem_check.py
Imports the calculation note's script (docs/04-calcs/sizing.py, TKB-CAL-001, which imports cad/src/model.py),
so every row is checked against the sizes in the model and closed by the CAL tag it names. Writes
docs/04-calcs/stem_results.csv and the claims table in docs/01b-stem-check.md (between the STM_TABLE markers).
Rows S1 to S32 are option A, the current design; rows B1 to B4 and C1 to C4 are concept options B and C
(TKB-OPT-001). First-order screens only; nothing here replaces a test of the collar on cut trunk sections.
"""
import contextlib
import csv
import io
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "docs" / "04-calcs"), str(ROOT / "cad" / "src")]
from stem_check import Check, G, WITHIN, PLAUSIBLE, FIX  # noqa: E402,F401

with contextlib.redirect_stdout(io.StringIO()):
    import sizing as CAL  # noqa: E402  TKB-CAL-001; builds the model (about 10 s)
import model as M  # noqa: E402

P = M.PARAMS
c = Check(ROOT / "docs/04-calcs/stem_results.csv")
W_proof = CAL.W_proof                     # 2.5 kN, R1 static load (PR-001)
W_work = CAL.W_work                       # 0.99 kN with a 100 kg person held

# ------------------------------------------------------------------ option A: loads
c.order_of_magnitude("S1", "Collar carries about 0.99 kN holding a 100 kg person with the victim set", "Mathematics", "Units and dimensional analysis",
                     claimed=0.99, estimate=(100.0 + 0.96) * G / 1000, unit="kN", law="Weight = m g (100 kg person, 0.96 kg of triangle, sling and carabiner)",
                     closed_by="TKB-CAL-001 [A1]")
# slack drop: the CAL uses 4 % stretch; EN 1891 allows up to 5 % and a new rope may be stiffer. Check the stiffest case (2 %)
EA_stiff = 1.0 / 0.02
peak_stiff = W_work * (1 + math.sqrt(1 + 2 * EA_stiff * 0.03 / (W_work * 1.0)))
frame_limit = W_proof * 1.546                       # the smallest frame factor on welded proof strength (cleat web, [C4])
peak_100 = W_work * (1 + math.sqrt(1 + 2 * EA_stiff * 0.10 / (W_work * 1.0)))
c.cited("S2", "A drop of up to 30 mm onto the rope when the feet are freed stays inside the frame's strength margin", "Physics", "Mechanics and statics",
        "Energy balance of a rigid mass on 1 m of rope, F = W (1 + sqrt(1 + 2 k h / W)); 4 % stretch (CAL) and the stiffest plausible rope, 2 %; frame limit 2.5 kN x 1.36 (the bars' combined factor, [C1b])",
        f"30 mm of slack: 2.6 kN (4 %) to {peak_stiff:.1f} kN (2 %), above the 2.5 kN of R1 but inside {W_proof * 1.36:.1f} kN; 100 mm with 2 % rope: {peak_100:.1f} kN, beyond it. The 30 mm is a drill limit, not physics (independent review); to close: the drill caps slack and the TRL 4 proof load is raised above 3 kN (TKB-DEC-001 O7)",
        PLAUSIBLE, closed_by="")

# ------------------------------------------------------------------ option A: grip
need = CAL.grip[200.0]["need"]
c.cited("S3", "The collar locks on wet bark: combined friction of pads and sleeved chain at least 0.58 on a 200 mm trunk (0.9 assumed)", "Physics", "Mechanics and statics",
        "Self-locking couple: lock if (mu_pad + mu_chain) >= h / e (TKB-CAL-001 section 3); friction of rubber and nylon on wet coconut bark is not published",
        f"needed {need:.2f}, assumed 0.9 (0.5 + 0.4), locking factor {CAL.lock_min:.2f}; no measured value; to close: friction on wet bark measured at TRL 4 (BLD-001 first check 1)", PLAUSIBLE, closed_by="")
# full equilibrium with the contact positions (pads at +-30 deg from the X axis, chain at the back) and two pad normals
r200 = 100.0
D200 = M.derived(P, 200.0)
e, h = D200["e_main"], D200["z_c"]
xf, xb = r200 * math.cos(math.radians(90 - P["v_half"])), D200["R_c"]
mu1, mu2 = 0.5, 0.4
k_pad = 1 / math.cos(math.radians(90 - P["v_half"]))
lock_full = e * (mu1 * k_pad + mu2) / (h + xf * mu1 * k_pad - xb * mu2)
c.claim("S4", "The simplified lock condition h / e in the CAL is on the safe side of the full equilibrium", "Mathematics", "Numerical method",
        "Moments about the trunk axis with the pad contacts at r cos 30 deg, the chain at R_c on the far side and the two pad normals (friction mu N / cos 30 deg); same frictions as S3",
        round(CAL.lock_min, 3), round(lock_full, 3), "", rule="below", closed_by=f"TKB-STM-001 S4 (full equilibrium gives {lock_full:.2f} against {CAL.lock_min:.2f})")
shear = (W_proof * 1000 * 0.5 / 0.9 / 2) / 2000.0 / 1.1 * P["pad"][1]   # each pad's friction share over a 2000 mm2 patch, G 1.1 MPa, 10 mm thick
c.cited("S5", "The frame settles less than the 20 mm of R1 at 2.5 kN", "Physics", "Strength of materials",
        "Pad squash at a 6 MPa compression modulus plus one link of chain seating, levered by e / h (TKB-CAL-001 [B5]); the independent review adds shear of the pads under their share of the vertical friction (G about 1.1 MPa) and tilt of the chain at the back",
        f"{CAL.settle:.0f} mm in the CAL; about {CAL.settle + shear:.0f} mm with pad shear, 14 to 18 mm with chain tilt, against 20 mm; to close: settlement measured in the TRL 4 proof test",
        PLAUSIBLE, closed_by="")

# ------------------------------------------------------------------ option A: strength at the R1 load (welded 6082-T6: HAZ 125 / 185 MPa, EN 1999-1-1)
c.claim("S6", "Bearing bars stay below the welded (heat-affected) proof strength of 6082-T6 at 2.5 kN", "Physics", "Strength of materials",
        "RHS 50 x 40 x 3 from the spine: bending in plan, vertical bending from the pad's friction and torsion from the bottom-edge contact, combined by von Mises (independent review); f0,haz = 125 MPa (EN 1999-1-1 values for welded 6082-T6)",
        round(CAL.s_eq, 0), 125.0, "MPa", closed_by="TKB-CAL-001 [C1b] (factor 1.36; 1.60 in plan bending alone)")
c.claim("S7", "Bar to spine fillet welds stay below the weld metal strength", "Physics", "Strength of materials",
        "Weld group in bending, 5 mm fillets (3.5 mm throat) all round; ER5356 weld metal 210 MPa; about 57 MPa equivalent with the shear (independent review), still factor 3.7",
        round(CAL.s_w, 0), 210.0, "MPa", closed_by="TKB-CAL-001 [C2] (factor 5.3)")
c.claim("S8", "The load eye does not tear out at 2.5 kN", "Physics", "Strength of materials",
        "Two shear planes through the 13 mm eye stack (spine and doubler rings), 14 mm of edge beyond the 22 mm eye, 0.577 x 185 MPa HAZ ultimate",
        round(W_proof, 2), round(CAL.tear, 1), "kN", closed_by="TKB-CAL-001 [C3] (39 kN, 16 times)")
c.claim("S9", "The 5 mm cleat web beside a slot stays below the welded proof strength with all of the chain's pull on one slot (450 mm trunk)", "Physics", "Strength of materials",
        "Ligament in bending beside the slot, web 55 mm deep (D-S2); the two legs need not share the tension (capstan ratio about 6 round the wrap), so the worst case puts it all on one slot; with the old 35 mm web this case gave 162 MPa (factor 0.77) and failed; f0,haz = 125 MPa",
        round(CAL.s_lig_one, 0), 125.0, "MPa", closed_by="TKB-DEC-001 D-S2; TKB-CAL-001 [C4b] (factor 1.21; 2.43 shared equally)")
bear = CAL.T_max / 2 * 1000 / (P["wire"] * P["spine_t"])
c.cited("S10", "Steel chain links bearing on the aluminium slot faces do not wear or dent the cleat in service", "Engineering and technology", "Manufacturing tolerances",
        "Projected bearing of a 6 mm link on the 5 mm web against about 1.5 x f0,haz; local line contact and repeated use make wear the open question",
        f"projected bearing {bear:.0f} MPa against about 190 MPa; wear and denting not calculable on paper; to close: inspect the slot faces after the TRL 4 proof tests (TKB-DEC-001 item 11)", PLAUSIBLE, closed_by="")
c.claim("S11", "The 6 mm grade 80 chain holds the largest chain tension with a wide margin", "Physics", "Strength of materials",
        "Grade 80, 6 mm: minimum breaking force 45.2 kN, working load limit 1.12 t (S3i, EN 818-2 class); checked with all of the pull in one leg (independent review); a link bearing on a flat web is not the link-on-link case of the rating, a reason the factor is kept large",
        round(2 * CAL.T_max, 1), 45.2, "kN", closed_by="TKB-CAL-001 [C5] (factor 4.1 in one leg, 8.1 shared)")
wet = 0.85
c.claim("S12", "The rope at its figure-eight loop holds 2.5 kN wet, with margin", "Chemistry", "Materials and polymer chemistry",
        "Basis here: EN 1891 type A holds 15 kN for 3 minutes with figure-eight terminations, less 15 % wet (the CAL's [C6] uses 22 kN x 0.65 knot efficiency, 14.3 kN dry); new-rope values, so abrasion and descender bends are left to the retirement rules (S26)",
        round(W_proof, 2), round(15.0 * wet, 1), "kN", closed_by="TKB-CAL-001 [C6] (14 kN dry at the knot)")

# ------------------------------------------------------------------ option A: lowering
c.claim("S13", "Brake hand force for a 100 kg person stays under the 150 N of R5", "Physics", "Mechanics and statics",
        "Capstan friction T1/T2 = exp(mu theta): rope on aluminium mu 0.2 over 540 deg in the descender and 180 deg over the brake carabiner; cross-check: EN 341 limits the holding force to 200 N at the device's maximum rated load (150 kg for the cited class), about 135 N at 101 kg, 72 N with the brake carabiner. Within for a certified device on dry rope: the capstan estimate reaches 150 N at a friction of 0.15 and 282 N at 0.10 (independent review)",
        round(CAL.F_hand, 0), 150.0, "N", closed_by="TKB-CAL-001 [D1]")
heat = {"descender": CAL.E * CAL.dev_share, "brake carabiner": CAL.E * CAL.cb_share, "hand": CAL.E * CAL.hand_share}
c.balance("S14", "Lowering 100 kg through 25 m turns 24.8 kJ into heat; the descender warms by 44 K at most", "Physics", "Thermodynamics",
          inputs={"potential energy": (100.0 + 0.96) * G * 25.0 / 1000}, outputs=heat, unit="kJ",
          law="Energy balance m g h = heat in the descender, brake carabiner and hand; dT = Q / (m c), 0.53 kg of aluminium, c 900 J/(kg K): bulk rise 44 K, the body near 79 C from 35 C ambient, hotter at the rope contact; the hand holds only the handle and the brake strand (S29); EN 341 class A allows 7.5 x 10^6 J of descent energy",
          closed_by="TKB-CAL-001 [D2]")
c.claim("S15", "30 m of rope lowers from 25 m", "Mathematics", "Orders of magnitude",
        "Rope used = 25 m drop + 1 m to the person + 1.5 m of knots + 0.5 m round the brake carabiner",
        round(CAL.rope_need, 1), 30.0, "m", closed_by="TKB-CAL-001 [E1]")

# ------------------------------------------------------------------ option A: fit, time, mass
D450 = CAL.D450
c.claim("S16", "The 110-link chain fits every trunk from 200 to 450 mm and leaves at least 4 links in the adjustable tail", "Mathematics", "Numerical method",
        f"Chain path round the trunk from the model: loop links + fixed end + tail = 110; links counted on the 450 mm trunk; on a 200 mm trunk {int(M.build_components(P, 200.0)['_D']['n_tail_b'])} links (about 1.1 m) hang free and are stowed in the bag's clip loop",
        int(D450["n_tail_b"]), 4, "links", rule="above", closed_by="TKB-CAL-001 [E2]; cad/src/model.py checks")
c.cited("S17", "A trained climber fixes the collar and clips the victim in under 5 minutes once in position", "Biology", "Ergonomics",
        "Task time estimate summed step by step (TKB-CAL-001 [E3]); work at height on a climbing device, hot and possibly wet",
        f"estimate {CAL.t_rig / 60:.1f} min against 5 min; a thin margin, no timed drill yet; to close: timed drill at 3 m at TRL 4 (BLD-001 first checks; PR-004)", PLAUSIBLE, closed_by="")
c.claim("S18", "The rescuer carries under 5 kg up the trunk", "Engineering and technology", "Mass budget",
        "Sum of the carried items from the model and catalogue masses, with the cited descender at 600 g (Petzl I'D S class) and the 55 mm cleat web of D-S2",
        round(CAL.carried, 2), 5.0, "kg", closed_by="TKB-CAL-001 [F2]")

# ------------------------------------------------------------------ option A: bark and palm
c.cited("S19", "The rubber pads do not crush the bark at 2.5 kN", "Biology", "Plant and animal biology",
        "Pad pressure from the CAL against the compressive strength of coconut stem wood, 9.28 MPa air dry at 400 kg/m3 average density (Rana et al. 2015; grain direction as reported); green or wet wood is typically 40 to 50 % weaker, and a cocked pad bears on a strip near its lower edge (independent review)",
        f"{CAL.p_pad:.1f} MPa mean, about {2 * CAL.p_pad:.1f} MPa at the lower edge, against about 4.6 to 5.6 MPa green; no margin left at the edge; to close: crush test on green stem sections at TRL 4",
        PLAUSIBLE, closed_by="")
q_line = CAL.T_max * 1000 / D450["R_c"]                      # N/mm of chain pressing the bark per unit length, 450 mm trunk
w_cont = q_line / 9.28                                       # contact width that brings the bark to its crushing strength
depth = 3.0 - math.sqrt(9.0 - (w_cont / 2) ** 2)
w_wet = q_line / 4.6
depth_wet = 3.0 - math.sqrt(max(9.0 - (w_wet / 2) ** 2, 0.0)) if w_wet < 6 else 3.0
c.claim("S20", "Bare chain links outside the sleeve mark the bark less than the 5 mm of R8 (static)", "Physics", "Strength of materials",
        f"Line load T / R = {q_line:.0f} N/mm on a 6 mm wire; the wire sinks until the contact width w = q / 9.28 MPa ({w_cont:.1f} mm); depth = r - sqrt(r^2 - (w/2)^2); static only: dragging while tightening is not included; about {depth_wet:.1f} mm on green wood at 4.6 MPa",
        round(depth, 2), 5.0, "mm", closed_by="TKB-CAL-001 [G1] (bare links may mark, R8)")
c.cited("S21", "The collar does not penetrate the stem and leaves no mark deeper than 5 mm", "Biology", "Plant and animal biology",
        "Palms have no vascular cambium, so any mark is permanent (Broschat 2019): the shallow static marks of S20 stay; the collar has no spikes, screws or cleats; pad crushing depends on S19 (reworded after the independent review)",
        "no penetrating part; marks about 0.3 to 1.3 mm static; to close: bark inspection after the TRL 4 lowerings (PR-008)", PLAUSIBLE, closed_by="")
c.cited("S22", "The victim turns head up in the triangle once the feet are freed", "Biology", "Human physiology and biomechanics",
        "Statics: a hanging body settles with its centre of mass below the attachment; the triangle and chest sling attach at the hips and chest, above the centre of mass when head up",
        "attachment above the centre of mass when head up, but hanging head down from the hips is also a stable state; that the body passes from one to the other unaided is not shown by statics (independent review); to close: dummy drill at TRL 4", PLAUSIBLE, closed_by="")
t_total = CAL.t_rig / 60 + 25.0 / 0.3 / 60 + 3.0
c.cited("S23", "The kit brings a stranded climber down in minutes, against the 30 to 150 minutes reported", "Mathematics", "Orders of magnitude",
        "Rigging (S17) + lowering 25 m at 0.3 m/s + about 3 minutes to climb to the victim (not timed); reported waits from the PRB sources",
        f"about {t_total:.0f} min against 30 to 150 min; rests on S17 and an untimed climb; to close: timed drill at TRL 4", PLAUSIBLE, closed_by="")
c.claim("S24", "The upward pull of R2 does not arise when the collar is at least 300 mm above the victim's attachment", "Physics", "Mechanics and statics",
        "The load strand runs from the descender down to the attachment point below it, so the force on the load eye points down; the upward case needs the attachment above the collar (the drill rule, decision 16A). A victim 0.3 m to the side on 1 m of rope adds about 0.3 W sideways, not counted in the lock analysis (independent review)",
        -1.0, 0.0, "(vertical component of the rope pull, up positive, per unit load)", rule="below", closed_by="TKB-DDR-003 16A; R2 stays at risk on the drill, not on the physics")

# ------------------------------------------------------------------ option A: chemistry
c.cited("S25", "Bare 6082-T6 frame in contact with steel chain, zinc-plated keeper and stainless screws survives humid coastal use", "Chemistry", "Electrochemistry and batteries",
        "Aluminium is anodic to steel and stainless steel in a wet joint; the pad screws sit in stainless rivet nuts with barrier paste, the chain touches the slots only while rigged, and the kit is stored dry in its bag",
        "galvanic attack needs a standing electrolyte; the controls are in the build plan; the rate on bare 6082 in sea air is not calculated; to close: inspect the frame after the TRL 4 trial season (TKB-RSK-001 FMEA)", PLAUSIBLE, closed_by="")
c.cited("S26", "Rope, webbing and rubber pads keep their properties in tropical sun and heat for their service life", "Chemistry", "Materials and polymer chemistry",
        "Polyamide and natural rubber degrade in UV and ozone; the kit is stored in its bag out of the sun, and rope, slings and pads are retired on the makers' inspection rules",
        "time-dependent; controlled by storage and inspection, not by a margin; to close: makers' retirement rules adopted in the drill card at TRL 4 (TKB-RSK-001)", PLAUSIBLE, closed_by="")

# ------------------------------------------------------------------ option A: engineering detail found by the D3 model (fix rule)
cw = P["conn_link"][0]
c.claim("S27", "The tether link threads the chain's end link: wire diameter inside the 6 mm grade 80 link's 7.8 mm opening", "Engineering and technology", "Manufacturing tolerances",
        "Inner width of 6 mm grade 80 chain at least 7.8 mm (S3i, EN 818-2 class); the BOM's 8 mm quick link failed this check and was replaced by a 6 mm grade 80 connecting link (7 mm at the chain end) through a 10 mm tether hole",
        cw, P["link_w"] - 0.5, "mm", closed_by="TKB-DEC-001 D-S1 (fix under the standing instruction)")
import json  # noqa: E402
fid = json.loads((ROOT / "cad/fidelity.json").read_text()) if (ROOT / "cad/fidelity.json").exists() else {}
ov_a = sum(v for a_, b_, v in fid.get("options", {}).get("A", {}).get("interference", []))
c.claim("S28", "The brake carabiner has the 22 mm spare eye to itself, clear of the tether", "Engineering and technology", "Manufacturing tolerances",
        "D3 model interference check (cad/fidelity.json) after D-S1: the tether link and the fixed end of the chain sit in front of the spine, the brake carabiner alone in the spare eye",
        ov_a, 5.0, "mm3 of overlap", closed_by="TKB-DEC-001 D-S1; cad/fidelity.json")
rope_dT = CAL.E * 1000 * CAL.hand_share / (0.078 * 25.0 * 1700.0)     # the 8 % at the hand spread over the 25 m of rope that runs through it (polyamide, c about 1.7 kJ/(kg K))
c.claim("S29", "The brake strand the rescuer holds stays far below the 48 C touch limit of EN 341", "Physics", "Heat transfer",
        "8 % of the 24.8 kJ goes into the hand and the brake strand running through it; spread over the 1.95 kg of rope that passes the hand (c about 1.7 kJ/(kg K)) it warms the rope by about this much; limit: 48 C less 35 C ambient. The descender body (85 %, up to 44 K) is held only by its handle",
        round(rope_dT, 2), 13.0, "K", closed_by="TKB-CAL-001 [D2]")

# the frame's estimated breaking load (weakest member at the heat-affected ultimate strength) over the working load
fu_haz = 185.0
F_break_sym = min(W_proof * fu_haz / CAL.s_lig, W_proof * fu_haz / CAL.s_eq)
F_break = min(F_break_sym, W_proof * fu_haz / CAL.s_lig_one)
c.cited("S30", "The collar's static system safety factor on a one-person load sits within the 5:1 to 10:1 that rope rescue teams aim for", "Engineering and technology", "Standards practice",
        "Breaking load estimated from the weakest frame member at the welded ultimate strength, over the 0.99 kN working load; rescue practice ratios 5:1 to 10:1, 15:1 once common (Piatt 2023); EN 795 tests anchor devices statically at 12 kN",
        f"{F_break_sym:.1f} kN with the chain's pull shared ({F_break_sym / W_work:.1f}:1, the bars govern), {F_break:.1f} kN with all of it on one slot ({F_break / W_work:.1f}:1): below 5:1 in the worst case. Amish decided on 2026-10-25 (TKB-DEC-001 O7, option C): keep the 2.5 kN design load, raise the TRL 4 proof load to 3.5 kN and decide after a test to failure of a sample frame, with the stronger frame (option B) as the recorded fallback if it shows less than 5:1",
        PLAUSIBLE, closed_by="Test to failure of a sample frame and the 3.5 kN proof test, TRL 4 (TKB-DEC-001 O7)")
# leaning trunk (independent review)
lean = {}
for th in (15.0, 20.0, 30.0):
    t_ = math.radians(th)
    lean[th] = (mu1 + mu2) / (h * math.cos(t_) / (e * math.cos(t_) - h * math.sin(t_)))
c.cited("S31", "The collar locks on a trunk leaning up to 20 deg with the frame on either side", "Physics", "Mechanics and statics",
        "Self-locking condition on a leaning trunk, frame on the adverse side: need = h cos t / (e cos t - h sin t) (independent review), 200 mm trunk, the same assumed friction 0.9",
        f"locking factor {lean[15.0]:.2f} at 15 deg, {lean[20.0]:.2f} at 20 deg, {lean[30.0]:.2f} at 30 deg on the adverse side; Amish decided on 2026-10-25 (TKB-DEC-001 O8, option C): a 20 deg lean limit in PR-003 and a drill rule that sets the frame on the favourable side of a leaning trunk; to close: friction test and the drill on a leaning palm",
        PLAUSIBLE, closed_by="")
tx, tz, td = P["tether_hole"]
strip = tx - td / 2
tear_t = 2 * strip * P["spine_t"] * 0.577 * fu_haz / 1000
c.claim("S32", "The tether hole holds the fixed end's share of the chain tension if the keeper is unseated", "Physics", "Strength of materials",
        f"Two shear planes of the {strip:.0f} mm web strip beside the 10 mm tether hole, 5 mm thick, 0.577 x 185 MPa HAZ ultimate, against the chain tension at the R1 load (2.2 kN at the working load); the tether is not a working load path",
        round(CAL.T_max, 1), round(tear_t, 1), "kN", closed_by="TKB-DEC-001 D-S1 (factor 1.4 at the R1 load, 3.4 at the working load)")

# ------------------------------------------------------------------ option B: constricting wrap anchor (TKB-OPT-001)
n_t, mu_w = P["wrap_turns"], 0.3
hold_ratio = math.pi * n_t * mu_w                            # holding force over load, band tension at least W / 2 in each wrap
c.cited("B1", "Option B: a strap wrapped 4 turns and tied off as a Klemheist holds 2.5 kN along a vertical 300 mm trunk", "Physics", "Mechanics and statics",
        "Capstan friction over the wrapped length: axial holding about 2 pi n mu T with the band tension T at least W / 2 in each wrap (mu 0.3 assumed, polyester on wet bark); friction hitches round large trunks under axial load are not covered by a cited source",
        f"holding about {hold_ratio:.1f} times the load on paper; the self-tightening of the hitch round a large, wet, tapering trunk is the open question; not carried forward (option B is not carried forward unless Amish chooses it)", PLAUSIBLE, closed_by="")
c.claim("B2", "Option B: the 45 mm polyester anchor strap holds 2.5 kN with margin", "Physics", "Strength of materials",
        "EN 795 anchor devices are tested statically at 12 kN (metallic) or 18 kN (textile, no service-life marking) for one user (EN 795 summary, Vandernet)",
        round(W_proof, 1), 18.0, "kN", closed_by="Catalogue class; TKB-OPT-001")
ww = P["webbing"][0]
p_wrap = (W_proof * 1000 / 2) / (150.0 * ww)
c.claim("B3", "Option B: the wraps press the bark far below its crushing strength", "Biology", "Plant and animal biology",
        "Band pressure p = T / (R w) at T = W / 2 on a 300 mm trunk, 45 mm webbing, against 9.28 MPa (Rana et al. 2015)",
        round(p_wrap, 2), 9.28, "MPa", closed_by="TKB-OPT-001")
c.cited("B4", "Option B: a climber ties the 4-turn wrap at height in about 90 s", "Biology", "Ergonomics",
        "Task time estimate: four wraps and a Klemheist with a 4 m strap, one hand on the trunk",
        "estimate 90 s against 60 s for the collar; not timed; not carried forward (option B)", PLAUSIBLE, closed_by="")

# ------------------------------------------------------------------ option C: screwed stem anchor (TKB-OPT-001)
d_s = float(P["saddle_screw"][0])
rho_k = 400.0                                                # average coconut stem density (Rana et al. 2015); dermal zone up to 900
f_h = 0.082 * (1 - 0.01 * d_s) * rho_k                       # embedment strength, EN 1995-1-1 eq. 8.32 form (timber, not palm)
My = 0.3 * 400 * d_s ** 2.6                                  # yield moment of a 400 MPa screw, EN 1995-1-1 eq. 8.30 form
t1 = P["saddle_screw"][1] - P["saddle"][1] - 10.0
F1 = min(f_h * t1 * d_s * (math.sqrt(2 + 4 * My / (f_h * d_s * t1 ** 2)) - 1), 2.3 * math.sqrt(My * f_h * d_s)) / 1000
c.cited("C1", "Option C: four M10 x 120 coach screws hold 2.5 kN in the stem", "Physics", "Strength of materials",
        f"Johansen steel-plate-to-timber estimate per screw with timber formulas (EN 1995-1-1 form) at 400 kg/m3: {F1:.1f} kN each; palm stem wood is fibre bundles in soft tissue, not timber, so the embedment strength is unknown",
        f"about {4 * F1:.0f} kN for four screws on timber formulas against 2.5 kN; not valid for palm wood without a test; not carried forward (option C is not carried forward unless Amish chooses it)", PLAUSIBLE, closed_by="")
c.cited("C2", "Option C: four 10 mm holes 110 mm deep do not seriously harm the palm", "Biology", "Plant and animal biology",
        "Palm stem wounds are permanent (Broschat 2019); every use leaves four more holes, an entry for pests and rot; R8 limits marks to 5 mm",
        "the holes are permanent and fail R8 by design; harm to the palm is not quantified; not carried forward (option C); fails PR-008 by design", PLAUSIBLE, closed_by="")
lt = P["lug"][0]
lug_tear = 2 * 39.0 * lt * 0.577 * 410 / 1000                 # S275-class lug, 39 mm below the 22 mm hole, two shear planes
c.claim("C3", "Option C: the 10 mm steel eye lug does not tear out at 2.5 kN", "Physics", "Strength of materials",
        "Two shear planes of the 10 mm lug below the 22 mm hole (39 mm of material), 0.577 x 410 MPa ultimate (S275 class)",
        round(W_proof, 1), round(lug_tear, 0), "kN", closed_by="TKB-OPT-001")
c.cited("C4", "Option C: driving four coach screws by hand at height fits the 5 minutes of R4", "Biology", "Ergonomics",
        "Pilot drilling and driving 4 x 120 mm screws with a ratchet while hanging on a climbing device, estimate 2 min a screw",
        "estimate about 8 min for the screws alone against 5 min for the whole rig; not carried forward (option C); at risk against PR-004", PLAUSIBLE, closed_by="")

state = c.write()

# ------------------------------------------------------------------ claims table into the STM document
doc = ROOT / "docs/01b-stem-check.md"
if doc.exists():
    rows = list(csv.DictReader((ROOT / "docs/04-calcs/stem_results.csv").open()))
    head = "| # | Claim | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
    body = "".join(f"| {r['id']} | {r['claim']} | {r['field']} | {r['branch']} | {r['law']} | {r['check']} | {r['verdict']} | {r['closed_by']} |\n" for r in rows)
    text = doc.read_text()
    a, b = text.find("<!-- STM_TABLE -->"), text.find("<!-- /STM_TABLE -->")
    if a >= 0 and b > a:
        doc.write_text(text[:a] + "<!-- STM_TABLE -->\n" + head + body + text[b:])
        print("updated the claims table in docs/01b-stem-check.md")
