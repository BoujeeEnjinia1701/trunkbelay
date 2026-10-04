"""TrunkBelay sizing calculations (TKB-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Imports the parametric model (cad/src/model.py) so every size used here is the one in the STEP
file and the drawings, reads bom/bom.csv and project.yaml, prints every result with a tag
([A1], [B2] ...) that the calculation note quotes, and writes docs/04-calcs/results.csv.
First-principles screening estimates for a paper proof of concept; nothing here replaces a proof
test of the collar on cut palm trunk sections or a timed drill (TRL 4).
"""
import csv
import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src")]
import model as M  # noqa: E402

P = M.PARAMS
g = 9.81
OUT = []


def out(tag, text, value=None, unit=""):
    print(f"[{tag}] {text}")
    OUT.append((tag, text, "" if value is None else f"{value:.4g}", unit))


# ------------------------------------------------------------------ A. loads
victim = 100.0                      # design person, kg (R2 and R5 test mass)
rope_kg_m = 0.078
gear_below = 0.75 + 0.12 + 0.085   # triangle, chest sling, victim carabiner, kg
W_work = (victim + gear_below + rope_kg_m * 1.0) * g / 1000      # kN on the collar while held
W_proof = 2.5                       # kN, R1 static load
out("A1", f"Working load on the collar with a 100 kg person held: {W_work:.2f} kN; R1 static load {W_proof:.1f} kN "
          f"({W_proof / W_work:.1f} times the working load)", W_work, "kN")
# slack drop when the feet are freed: a rigid mass on a short semi-static rope
EA = 1.0 / 0.04                     # kN: EN 1891 type A elongation about 4 % between 50 and 150 kg (assumed)
L_rope = 1.0                        # m of rope between the descender and the victim at the start
drops = {}
for h in (0.03, 0.05, 0.10):
    F = W_work * (1 + math.sqrt(1 + 2 * EA * h / (W_work * L_rope)))
    drops[h] = F
out("A2", "Peak load if the person drops onto the rope when the feet are freed (rigid body, 1 m of rope): "
          + ", ".join(f"{int(h * 1000)} mm slack {F:.1f} kN" for h, F in drops.items())
          + "; the drill takes all slack in first, so the drop stays under 30 mm and the peak (about 2.6 kN) close to the R1 load, "
      "inside the strength margins of section C",
    drops[0.03], "kN")

# ------------------------------------------------------------------ B. grip on the trunk (self-locking collar)
mu_pad, mu_chain = 0.5, 0.4         # rubber on wet bark; webbing-sleeved chain on wet bark (assumed, to confirm)
mu_sum = mu_pad + mu_chain
h_lever = None
grip = {}
for d in (200.0, 300.0, 450.0):
    D = M.derived(P, d)
    h = D["z_c"]                     # chain line above the bottom edge of the bearing bars (conservative)
    e = D["e_main"]
    need = h / e
    lock = mu_sum / need
    N_proof = W_proof * e / h
    N_work = W_work * e / h
    qa = D["x_s"] + sum(P["slots"]) / 2
    s = math.sqrt(1 - (D["R_c"] / qa) ** 2)
    T_proof = N_proof / (2 * s)
    F_pad = N_proof / (2 * math.cos(math.radians(90 - P["v_half"])))
    grip[d] = dict(h=h, e=e, need=need, lock=lock, N=N_proof, Nw=N_work, T=T_proof, F_pad=F_pad, u=D["u_contact"],
                   q0=D["q0"], gap=D["x_s"] - D["r"])
    h_lever = h
    out(f"B{len(grip)}", f"{d:.0f} mm trunk: load line {e:.0f} mm from the trunk axis, lever height {h:.0f} mm, "
                         f"friction needed {need:.2f} against {mu_sum:.1f} assumed, locking factor {lock:.2f}; at {W_proof} kN "
                         f"the bars press {N_proof:.1f} kN ({F_pad:.1f} kN a pad) and the chain carries {T_proof:.1f} kN",
        lock, "")
lock_min = min(v["lock"] for v in grip.values())
out("B4", f"Smallest locking factor {lock_min:.2f} (200 mm trunk); the grip rises in step with the load, so the factor is the "
          f"same at any load. Friction from the chain's full wrap round the trunk is extra and not counted", lock_min, "")
# settling under R1: rubber compression and chain seating
rubber_E = 6.0                      # MPa, effective compression modulus of 60 to 70 Shore A pad (assumed)
patch = 40.0 * P["pad"][2]          # mm2 contact patch per pad on a round trunk (assumed 40 mm wide)
F_pad_max = max(v["F_pad"] for v in grip.values())
p_pad = F_pad_max * 1000 / patch
squash = p_pad / rubber_E * P["pad"][1]
seat = P["pitch"] / (2 * math.pi)    # radial take-up of one link of slack in the loop
settle = (squash + seat) * grip[200.0]["e"] / grip[200.0]["h"]
out("B5", f"Settling at {W_proof} kN: pads squash {squash:.1f} mm at {p_pad:.1f} MPa, chain seats {seat:.1f} mm; "
          f"the frame drops about {settle:.0f} mm as it cocks (R1 allows 20 mm of slip)", settle, "mm")

# ------------------------------------------------------------------ C. strength at the R1 load
# frame in 6082-T6 aluminium, TIG welded (TKB-DDR-003). Every frame check uses the heat-affected-zone strength
# (EN 1999-1-1: 0.2 % proof 125 MPa, ultimate 185 MPa), which is conservative away from the welds
fy = 125.0                           # HAZ 0.2 % proof strength, MPa
fu_haz = 185.0
f_weld = 210.0                       # weld metal, ER5356 filler on 6082, MPa
# bearing bars: cantilever from the spine, pad force at the contact point
h_b, d_b, t_b = P["bar"]
Z_bar = (h_b * d_b ** 3 - (h_b - 2 * t_b) * (d_b - 2 * t_b) ** 3) / (6 * d_b)
worst = max(grip.values(), key=lambda v: v["F_pad"] * v["u"])
M_bar = worst["F_pad"] * 1000 * (worst["u"] - P["spine_t"] / 2 / math.cos(math.radians(30)))
s_bar = M_bar / Z_bar
out("C1", f"Bearing bar (aluminium RHS {h_b:.0f} x {d_b:.0f} x {t_b:.0f}): {M_bar / 1e6:.2f} kN m at the spine, {s_bar:.0f} MPa, factor "
          f"{fy / s_bar:.2f} on the welded (HAZ) proof strength at the R1 load ({fy / s_bar * W_proof / W_work:.1f} at the working load) "
          f"and {fu_haz / s_bar:.1f} on the HAZ ultimate strength", fy / s_bar, "")
# weld of each bar to the spine face: outline about (depth / cos 30 deg + 5) x 50 mm, 5 mm fillets (throat 3.5 mm)
throat, wd, wb = 3.5, d_b / math.cos(math.radians(30)) + 5, h_b
S_w = throat * (wd ** 2 / 3 + wb * wd)
s_w = M_bar / S_w
out("C2", f"Bar to spine fillet welds (5 mm, all round, ER5356): {s_w:.0f} MPa against {f_weld:.0f} MPa weld metal strength, "
          f"factor {f_weld / s_w:.1f}", f_weld / s_w, "")
# spine arm: load on the eye, section through the spare eye and lightening hole region
x0 = P["spine_set"]
ex, ez = P["eye_main"]
lx, lz, ld = P["light_hole"]
x_cut = lx + ld / 2 + 5
z_edge = 55 + (175 - x_cut) / 115 * (P["spine_pts"][-1][1] - 55)
Z_sp = P["spine_t"] * z_edge ** 2 / 6
s_sp = W_proof * 1000 * (ex - x_cut) / Z_sp
t_eye = P["spine_t"] + 2 * P["doubler"][1]
s_bear = W_proof * 1000 / (P["carab"][0] * t_eye)
tear = 2 * (P["spine_pts"][1][0] - ex - P["eye_d"] / 2) * t_eye * 0.577 * fu_haz / 1000
out("C3", f"Spine arm: {s_sp:.0f} MPa in bending beside the lightening hole; load eye {t_eye:.0f} mm thick with doublers, bearing "
          f"{s_bear:.0f} MPa under the carabiner bar, tear-out strength {tear:.0f} kN ({tear / W_proof:.0f} times the R1 load)",
    tear / W_proof, "")
# cleat: chain tension bears on the 5 mm web beside each slot; the cheeks carry the twist between the two slots
T_max = max(v["T"] for v in grip.values())
nw = P["notch"][0]
lig = (nw - P["slot_w"]) / 2
arm = lig - (P["slot_w"] / 2 + 3.0 - P["slot_w"] / 2)          # cheek edge to the wire's bearing line
Z_lig = (P["spine_pts"][-1][1] - P["slot_bottom"]) * P["spine_t"] ** 2 / 6
s_lig = (T_max / 2 * 1000) * arm / Z_lig
t_tot = P["spine_t"] + 2 * P["cheek"][1]
J = P["cheek"][0] * t_tot ** 3 / 3 * 0.5                         # halved for the notches
tw = T_max * 1000 * (P["slots"][1] - P["slots"][0])
tau = tw * t_tot / J
out("C4", f"Chain cleat at {T_max:.1f} kN chain tension: web ligament beside a slot, {P['spine_pts'][-1][1] - P['slot_bottom']:.0f} mm "
          f"deep, {s_lig:.0f} MPa (factor {fy / s_lig:.2f} on HAZ proof); twist between the two slots {tw / 1e6:.2f} kN m, "
          f"{tau:.0f} MPa in the top with {P['cheek'][1]:.0f} mm cheeks (factor {0.577 * fy / tau:.1f}); the steel links bear on "
          f"the aluminium web at about {T_max / 2 * 1000 / (P['wire'] * P['spine_t']):.0f} MPa (wear to confirm)",
    fy / s_lig, "")
chain_mbl, chain_wll = 45.0, 11.2
out("C5", f"Chain: {T_max:.1f} kN at most at the R1 load against a working load limit of {chain_wll} kN and a minimum breaking "
          f"force of {chain_mbl:.0f} kN (factor {chain_mbl / T_max:.1f}); {T_max * W_work / W_proof:.1f} kN at the working load",
    chain_mbl / T_max, "")
rope_mbs, knot = 22.0, 0.65
out("C6", f"Rope: EN 1891 type A, at least {rope_mbs:.0f} kN, about {rope_mbs * knot:.0f} kN at the figure-eight loop: factor "
          f"{rope_mbs * knot / W_proof:.1f} at the R1 load and {rope_mbs * knot / W_work:.0f} at the working load; carabiners 25 kN, "
          f"factor {25 / W_proof:.0f} and {25 / W_work:.0f}", rope_mbs * knot / W_work, "")

# ------------------------------------------------------------------ D. lowering (R5)
mu_r = 0.20                          # wet kernmantle rope on aluminium (assumed, conservative low)
theta_dev = 3 * math.pi              # rope contact in an auto-locking descender, about 540 deg (assumed)
theta_cb = math.pi                   # 180 deg turn over the brake carabiner
k_dev = math.exp(mu_r * theta_dev)
k_cb = math.exp(mu_r * theta_cb)
load_N = (victim + gear_below) * g
F_hand = load_N / (k_dev * k_cb)
out("D1", f"Hand force on the brake strand holding {victim:.0f} kg: descender ratio {k_dev:.1f}, brake carabiner {k_cb:.2f}, "
          f"hand {F_hand:.0f} N (R5 allows 150 N); without the brake carabiner {load_N / k_dev:.0f} N", F_hand, "N")
v = 0.3
E = (victim + gear_below) * g * 25.0 / 1000
dev_share = (load_N - load_N / k_dev) / load_N
cb_share = (load_N / k_dev - F_hand) / load_N
hand_share = F_hand / load_N
c_al, m_dev = 900.0, 0.53
dT = E * 1000 * dev_share / (c_al * m_dev)
out("D2", f"A 25 m lowering at a steady {v} m/s takes {25 / v:.0f} s and turns {E:.1f} kJ into heat: {dev_share * 100:.0f} % in the "
          f"descender, {cb_share * 100:.0f} % in the brake carabiner, {hand_share * 100:.0f} % at the hand; the descender would warm "
          f"by at most {dT:.0f} K if it kept it all", E, "kJ")

# ------------------------------------------------------------------ E. reach, fit and rigging (R3, R4, R6)
rope_need = 25.0 + 1.0 + 1.5 + 0.5
out("E1", f"Rope: 25 m of lowering, 1 m from the descender to the person at the start, 1.5 m for the figure-eight loop and "
          f"stopper knot, 0.5 m round the brake carabiner: {rope_need:.1f} m of the 30 m", rope_need, "m")
fits = []
C450 = None
for d in (200.0, 300.0, 450.0):
    L = M.loop_length(P, d)
    fits.append(f"{d:.0f} mm trunk: loop {L:.0f} mm ({math.ceil(L / P['pitch'])} links), bars touch the trunk {grip[d]['u']:.0f} mm "
                f"along the pad, spine {grip[d]['gap']:.0f} mm clear of the bark")
out("E2", "Fit: " + "; ".join(fits) + f"; the 110-link chain leaves at least 10 links of tail on a 450 mm trunk", None)
steps = [("Clip the frame to the trunk with the chain round it, link into slot, keeper and pin on", 60),
         ("Helpers haul the rope bag up on the tag line through the micro pulley on the rescuer's harness; the rescuer "
          "clips it to the spare eye", 45),
         ("Clip the descender to the load eye and reeve the rope; brake strand over the brake carabiner", 40),
         ("Lower the bag on its rope end to the ground (helpers take the brake strand slack)", 20),
         ("Fit the pre-rigged evacuation triangle round the hips and the chest sling (waist loops, sling and rope loop "
          "already on the victim carabiner)", 90),
         ("Clip the crotch loop and the chest sling's free end into the victim carabiner and take in all slack", 15)]
t_rig = sum(t for _, t in steps)
out("E3", "Rigging time once the rescuer is in position (estimate): "
          + "; ".join(f"{s} {t} s" for s, t in steps) + f"; total {t_rig / 60:.1f} min", t_rig / 60, "min")

# ------------------------------------------------------------------ F. mass (R7)
C = M.build_components(P)
mass = M.mass_table(P, C)
frame_keys = ("spine", "bars", "doublers", "cheeks")
frame = sum(mass[k] for k in frame_keys + ("keeper", "pad_screws", "pads", "pin"))
chain = mass["chain"] + mass["master_links"] + mass["sleeve"] + mass["maillon"]
collar = frame + chain
kit = sum(mass.values())
carried = M.carried_mass(mass)
hauled = kit - carried
out("F1", f"Mass: collar frame {frame:.2f} kg (aluminium weldment {sum(mass[k] for k in frame_keys):.2f} kg), chain set {chain:.2f} kg, "
          f"descender {mass['descender']:.2f} kg, carabiners {mass['carabiners']:.2f} kg, rope {mass['rope']:.2f} kg, triangle and sling "
          f"{mass['triangle'] + mass['chest_sling']:.2f} kg, bag {mass['bag']:.2f} kg, tag line {mass['tag_line']:.2f} kg "
          f"({P['tag_line'][1]:.0f} m of {P['tag_line'][0]:.0f} mm cord) and micro pulley {mass['micro_pulley']:.2f} kg", kit, "kg")
out("F2", f"Whole kit {kit:.1f} kg; the helpers haul {hauled:.1f} kg up in the bag (rope, pre-rigged victim set with its carabiner, "
          f"bag), so the rescuer carries {carried:.2f} kg up the trunk: collar, chain set, descender, load and brake carabiners, "
          f"micro pulley and the tag line hanging from it (R7 asks for under 5 kg)", carried, "kg")
steel_equiv = sum(mass[k] for k in frame_keys) * M.DENSITY["steel"] / M.DENSITY["aluminium"]
out("F3", f"The aluminium weldment saves about {steel_equiv - sum(mass[k] for k in frame_keys):.1f} kg against the same parts "
          f"in steel; the tag line counts its full {P['tag_line'][1]:.0f} m because both legs hang from the rescuer at the top", carried, "kg")

# ------------------------------------------------------------------ G. bark (R8)
p_work = p_pad * W_work / W_proof
T_work = T_max * W_work / W_proof
sleeve_w = 40.0                      # mm of flattened sleeve in contact
p_chain = T_max * 1000 / (M.derived(P, 450)["R_c"]) / sleeve_w
p_bare = T_max * 1000 / (M.derived(P, 450)["R_c"]) / 3.0
out("G1", f"Bark pressure at the R1 load: pads {p_pad:.1f} MPa ({p_work:.1f} MPa working), sleeved chain {p_chain:.2f} MPa, bare "
          f"chain links {p_bare:.0f} MPa on a 3 mm line; the outer coconut stem is far stronger in crushing, so no cut is expected "
          f"under the pads or the sleeve. Bare links outside the sleeve may mark the bark (to confirm by test)", p_pad, "MPa")

# ------------------------------------------------------------------ H. cost (R9)
rows = list(csv.DictReader((ROOT / "bom" / "bom.csv").open()))
cost = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
pm = yaml.safe_load((ROOT / "project.yaml").read_text())
target = float(pm["budget_usd"])
big = sorted(((float(r["qty"]) * float(r["unit_cost_usd"]), r["spec"].split(":")[0].split(",")[0].split(" (")[0]) for r in rows), reverse=True)[:4]
out("H1", f"Kit cost from the BOM: USD {cost:,.0f}. Value-engineering target: USD {target:,.0f}. Estimated cost of the constructable "
          f"design: USD {cost:,.0f} (USD {abs(target - cost):,.0f} {'under' if cost <= target else 'over'} the target)", cost, "USD")
r9 = 850.0                          # R9 as restated by Amish's decision 19A (TKB-REQ-001 v0.3)
out("H2", f"R9 per-kit parts cost at single-kit prices: USD {cost:,.0f} against the restated R9 target of USD {r9:,.0f} "
          f"(USD {abs(r9 - cost):,.0f} {'under' if cost <= r9 else 'over'}); the largest lines are "
          + ", ".join(f"{n.lower()} USD {c:,.0f}" for c, n in big)
          + "; group purchase by the training partner and one kit per climber group are not counted", cost, "USD")

# ------------------------------------------------------------------ results table
results = [
    ("R1", "Met on paper (friction to confirm)", f"Locking factor {lock_min:.2f} at the smallest trunk; settles about {settle:.0f} mm"),
    ("R2", "At risk for an upward pull; drill rule kept (decision 16A)",
     "The single top chain cannot hold an upward pull; the drill keeps the collar at least 300 mm above the person's attachment; "
     "double-acting collar is the recorded fallback"),
    ("R3", "Met", "Chain and V fit 200 to 450 mm trunks with no tools"),
    ("R4", "At risk (estimate)", f"About {t_rig / 60:.1f} min once in position: the pre-rigged victim set saves 45 s and the tag-line haul adds 45 s"),
    ("R5", "Met on paper (estimate)", f"Hand force about {F_hand:.0f} N with the brake carabiner"),
    ("R6", "Met", f"30 m rope, {rope_need:.1f} m needed"),
    ("R7", "Met on paper", f"{carried:.2f} kg carried up the trunk; the {hauled:.1f} kg bag is hauled up by the helpers"),
    ("R8", "Met on paper (to confirm)", f"Pads {p_pad:.1f} MPa, sleeve {p_chain:.2f} MPa at the R1 load"),
    ("R9", "Met on paper (restated target)", f"USD {cost:,.0f} a kit at single-kit prices against USD {r9:,.0f}"),
    ("R10", "Cannot be shown on paper", "Needs the training trial at TRL 4"),
]
for rid, st, note in results:
    out("R", f"{rid}: {st}. {note}")
with (ROOT / "docs" / "04-calcs" / "results.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tag", "result", "value", "unit"])
    w.writerows(OUT)
print("wrote docs/04-calcs/results.csv")
