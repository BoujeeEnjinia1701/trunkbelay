"""TrunkBelay parametric model (build123d), constructable design (TRL 3, TKB-DDR-002; aluminium frame TKB-DDR-003).

Run from the repo root:
    python cad/src/model.py            export STEP and STL, run the constructability checks
    python cad/src/model.py --check    run the constructability checks only

TrunkBelay is a rescue kit that lets a fellow climber anchor and lower a climber stranded on a
coconut palm. A TIG-welded 6082-T6 aluminium collar frame (a 5 mm spine plate with two rubber-faced
bearing bars set in a 120 deg V at its foot; TKB-DDR-003) is held on the trunk by a 6 mm grade 80 chain that wraps the trunk
once and sits in two slots cut in the top of the spine (the chain cleat, stiffened by a cheek plate
on each face), held there by a sheet-steel keeper and a ball-lock pin. The fixed end is also tethered
to the spare eye with a quick link. The load
hangs from an eye at the outer end of the spine, 140 mm out from the frame, so the frame cocks on
the trunk: the bearing bars press the bark low on the near side and the chain presses it high on
the far side, and the grip rises with the load. An auto-locking rope descender on the eye lowers
the victim, who is fitted with an evacuation triangle and a chest sling, on 30 m of 11 mm
semi-static rope whose spare end runs down to the rope bag on the ground. A second (spare) eye takes a
carabiner for the chain tail or the bag while rigging.

Coordinates in mm. Z up; the trunk axis is the Z axis; the frame sits on the +X side of the trunk,
its foot (the bottom of the bearing bars) at Z = 0. The frame is built in a frame-local system with
the virtual vertex of the V (where the two pad faces would meet) at the origin and then moved out
by q0 = r / sin 60 deg, so the pad faces are tangent to a trunk of radius r.
PRELIMINARY, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from build123d import (Box, Cylinder, Location, Plane, Pos, Rot, Solid, Torus, Compound, Polyline, Helix, Rectangle,
                       make_face, extrude, sweep, export_step, export_stl)

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(Path(__file__).resolve().parent), str(ROOT / ".kit")]

PARAMS = {
    "trunk_d": 300.0,            # trunk used for the model and pictures (range 200 to 450, R3)
    "trunk_range": (200.0, 450.0),
    # bearing V
    "v_half": 60.0,              # angle of each pad face from the frame's centre plane, deg (120 deg V)
    "pad": (155.0, 10.0, 50.0),  # rubber pad: length along the face x thickness x height
    "pad_u0": 15.0,              # pad starts this far along the face from the virtual vertex
    "bar": (50.0, 40.0, 3.0),    # bearing bar RHS, 6082-T6: height x depth (away from the trunk) x wall (TKB-DDR-003)
    "bar_u1": 172.0,             # outer end of the bar along the face (end cap included)
    "cap_t": 3.0,
    # spine
    "spine_t": 5.0,              # also the web of the chain cleat: no thicker than 6 mm (link inner length less two wires)
    "frame_material": "aluminium",   # spine, bars, doublers and cheeks: 6082-T6, TIG welded (TKB-DDR-003)
    "spine_set": 8.0,            # spine front edge behind the virtual vertex
    "spine_pts": ((0, 0), (175, 0), (175, 55), (60, 205), (0, 205)),   # x' (from the front edge), z; top 205: a 55 mm cleat web for all the chain tension on one slot (TKB-DEC-001 D-S2)
    "eye_main": (150.0, 28.0), "eye_bag": (85.0, 28.0), "eye_d": 22.0,   # load eye and spare eye (spare clear of the deeper bars)
    "doubler": (50.0, 4.0),      # eye doubler ring OD x thickness, one each side of each eye
    "light_hole": (85.0, 90.0, 36.0),   # x', z, diameter
    # chain cleat: two slots in the top of the spine, stiffened by a cheek plate on each face
    "slots": (15.0, 43.0), "slot_w": 7.5, "slot_bottom": 150.0,
    "cheek": (60.0, 8.0, 130.0), # x' length x thickness x bottom z (top level with the spine top)
    "notch": (22.0, 148.0),      # notch in each cheek round each slot: width x bottom z
    "pin_xz": (29.0, 139.0), "pin_d": 8.0, "pin_hole": 8.5,
    "keeper": (56.0, 3.0, 6.0, 132.0),  # bridge length (X) x sheet thickness x leg width x leg bottom z
    "tether_hole": (12.0, 112.0, 10.0),  # x' (from the spine front edge), z, diameter: the fixed end's tether link (TKB-DEC-001 D-S1)
    "conn_link": (7.0, 14.0, 9.0), # grade 80 connecting link for 6 mm chain (BOM 13 and 14): wire x straight x bend radius (centre line), opening 11 mm
    # chain, 6 mm grade 80
    "wire": 6.0, "pitch": 18.0, "link_w": 7.8,     # wire dia, inner length, inner width
    "chain_len_links": 110,      # links in the chain, both tails included
    "tail_b_out": -75.0,         # the adjustable tail hangs this far out on -Y, clear of the bar (TKB-DDR-003)
    "sleeve": (600.0, 15.0),     # tubular webbing sleeve length x radius on the chain
    "master": (10.0, 80.0, 45.0),   # master link stock x inner length x inner width
    # load side
    "carab": (10.0, 60.0, 20.0), # carabiner bar dia x straight length x bend radius (centreline)
    "desc": (75.0, 38.0, 150.0), # descender body X x Y x Z
    "rope_d": 11.0,
    "strand_dx": (-15.0, 15.0),  # brake and load strand offsets from the descender centre
    "bag": (200.0, 380.0),       # rope and carry bag diameter x height (kit pictures only)
    "load_end_z": -700.0,        # where the load strand is cut off in the pictures (to the victim)
    # tag line (TKB-DDR-003): 4 mm cord doubled through a micro pulley on the rescuer's harness, both ends on
    # the ground; the helpers tie the bag to one end and haul on the other
    "tag_line": (4.0, 55.0, 0.011),   # cord diameter mm, length m (2 x 25 m plus 5 m), mass kg/m
    "pulley": (30.0, 12.0),           # micro pulley sheave diameter x width (pictures only)
    # ---- concept options B and C (TKB-OPT-001), modelled at D3 for the options picture and the fidelity check
    # option B, constricting wrap anchor: a sewn 45 mm polyester anchor strap wrapped in a tight helix over a
    # rubber bark mat, tied off as a Klemheist, its loop through the top slot of an aluminium rigging plate
    "wrap_turns": 4, "wrap_pitch": 60.0,     # turns and helix pitch, mm
    "webbing": (45.0, 2.0),                  # anchor strap width x thickness, mm
    "mat_t": 3.0,                            # rubber bark mat under the wraps, mm
    "rig_plate": (120.0, 10.0, 140.0),       # rigging plate width (along the trunk face) x thickness x height, mm
    "rig_holes": 65.0,                       # load and brake holes apart, mm (22 mm holes, as the spine eyes)
    "rig_top": -150.0,                       # top of the rigging plate below the wraps, mm
    # option C, screwed stem anchor: a folded 6 mm steel V saddle screwed to the stem with four M10 x 120
    # coach screws, a 10 mm eye lug welded to its ridge
    "saddle": (150.0, 6.0, 200.0),           # V flange length along each face x thickness x height, mm
    "saddle_screw": (10, 120, 60.0, (50.0, 150.0)),   # coach screw d, length; distance along the face; heights
    "lug": (10.0, 125.0, 60.0, 50.0),        # lug thickness; load hole and brake hole out from the ridge; hole height
    "ground_z": -1400.0,                     # ground level for the option and site pictures: a low-height drill, collar foot 1.4 m up
}

DENSITY = {"steel": 7.85e-6, "rubber": 1.5e-6, "aluminium": 2.70e-6}
SIN, COS = math.sin, math.cos


# ----------------------------------------------------------------- helpers
def _add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def _mul(a, k):
    return tuple(x * k for x in a)


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _norm(a):
    n = math.sqrt(_dot(a, a))
    return tuple(x / n for x in a)


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def rod(p0, p1, r, r_in=0.0):
    """Solid cylinder (or tube) between two points."""
    d = _sub(p1, p0)
    L = math.sqrt(_dot(d, d))
    pl = Plane(origin=p0, z_dir=_norm(d))
    s = Solid.make_cylinder(r, L, pl)
    if r_in > 0:
        s = s - Solid.make_cylinder(r_in, L, pl)
    return s


def obox(center, x_dir, z_dir, dx, dy, dz):
    """Box of size dx, dy, dz centred at center, its X along x_dir and Z along z_dir."""
    return Location(Plane(origin=center, x_dir=x_dir, z_dir=z_dir)) * Box(dx, dy, dz)


def fuse_all(shapes):
    out = None
    for s in shapes:
        out = s if out is None else out + s
    return out


def group(shapes):
    return Compound(list(shapes))


def stadium(straight, bend_r, wire_r):
    """Closed ring like a chain link: long axis X, lying in the XY plane, centred at the origin."""
    half = Box(2 * (bend_r + wire_r) + 2, 2 * (bend_r + wire_r) + 2, 2 * wire_r + 2)
    ends = []
    for sgn in (1, -1):
        cut = Pos(sgn * (bend_r + wire_r + 1), 0, 0) * half
        ends.append(Pos(sgn * straight / 2, 0, 0) * (Torus(bend_r, wire_r) & cut))
    sides = [rod((-straight / 2, s * bend_r, 0), (straight / 2, s * bend_r, 0), wire_r) for s in (1, -1)]
    return fuse_all(ends + sides)


def bend_lift(br, wr, half):
    """How far a ring of centre-line bend radius br and wire radius wr must sit back from the edge of an eye or
    hole so that its end bend clears the edge over a plate half-thickness 'half': off the centre plane the bend
    reaches nearer the edge and its section there is an ellipse."""
    worst = 0.0
    for i in range(41):
        y = half * i / 40
        c = math.sqrt(br * br - y * y)
        worst = max(worst, (br - c) + wr * br / c - wr)
    return worst


def place(shape, center, axis, normal):
    """Move a template (long axis X, ring plane XY, normal Z) to center with its long axis along axis
    and its ring-plane normal along normal."""
    return Location(Plane(origin=center, x_dir=_norm(axis), z_dir=_norm(normal))) * shape


# ----------------------------------------------------------------- derived geometry
def derived(P=PARAMS, trunk_d=None):
    D = {}
    r = (trunk_d or P["trunk_d"]) / 2
    a = math.radians(P["v_half"])
    D["r"] = r
    D["q0"] = r / SIN(a)                       # trunk axis to virtual vertex
    D["x_s"] = D["q0"] + P["spine_set"]        # trunk axis to spine front edge
    D["u_contact"] = D["q0"] * COS(a)          # contact point along the pad face from the vertex
    D["w"] = (-COS(a), SIN(a), 0.0)            # +Y face direction, from the vertex toward the trunk side
    D["b"] = (SIN(a), COS(a), 0.0)             # +Y face: behind the face (away from the trunk)
    D["e_main"] = D["x_s"] + P["eye_main"][0]  # load line offset from the trunk axis
    D["slot_z"] = P["slot_bottom"]
    D["z_c"] = P["slot_bottom"] + P["link_w"] / 2 + P["wire"] + 0.05   # chain centre height
    bend = P["link_w"] / 2 + P["wire"] / 2
    D["link_bend"] = bend
    D["link_straight"] = P["pitch"] + P["wire"] - 2 * bend
    D["link_outer_w"] = 2 * (bend + P["wire"] / 2)
    D["R_c"] = r + P["sleeve"][1]              # chain centre-line radius around the trunk
    return D


def _mirror_y(shape):
    return shape.mirror(Plane.XZ)


# ----------------------------------------------------------------- frame (frame-local, vertex at origin)
def _face_box(P, D, u0, u1, t0, t1, z0, z1, side=1):
    w = (D["w"][0], side * D["w"][1], 0.0)
    b = (D["b"][0], side * D["b"][1], 0.0)
    c = _add(_mul(w, (u0 + u1) / 2), _mul(b, (t0 + t1) / 2))
    c = (c[0], c[1], (z0 + z1) / 2)
    # obox: X along w, Z up, so its Y is Z x w; size along Y is the thickness
    return obox(c, w, (0, 0, 1), u1 - u0, t1 - t0, z1 - z0)


def _bar(P, D, side=1):
    """Bearing bar: RHS behind the rubber pad, mitred against the spine face, capped at the outer end."""
    h, dep, wall = P["bar"]
    t0, t1 = P["pad"][1], P["pad"][1] + dep
    outer = _face_box(P, D, -60, P["bar_u1"], t0, t1, 0, h, side)
    inner = _face_box(P, D, -70, P["bar_u1"] - P["cap_t"], t0 + wall, t1 - wall, wall, h - wall, side)
    s = outer - inner
    half = P["spine_t"] / 2
    keep = Pos(0, side * (half + 500), h / 2) * Box(1000, 1000, h + 10)
    return s & keep


def _pad(P, D, side=1):
    L, t, h = P["pad"]
    return _face_box(P, D, P["pad_u0"], P["pad_u0"] + L, 0, t, 0, h, side)


def _pad_screws(P, D, side=1):
    """Two M6 countersunk screws per pad: heads sunk 3 mm below the rubber face, through the bar's front wall."""
    out = []
    w = (D["w"][0], side * D["w"][1], 0.0)
    b = (D["b"][0], side * D["b"][1], 0.0)
    for u in (P["pad_u0"] + 35, P["pad_u0"] + P["pad"][0] - 35):
        p0 = _add(_mul(w, u), _mul(b, 3.0)); p0 = (p0[0], p0[1], P["pad"][2] / 2)
        p1 = _add(_mul(w, u), _mul(b, P["pad"][1] + P["bar"][2] + 4.0)); p1 = (p1[0], p1[1], P["pad"][2] / 2)
        out.append(rod(p0, p1, 3.0) + rod(p0, _add(p0, _mul(b, 3.0)), 5.5))
    return fuse_all(out)


def _spine(P, D):
    x0 = P["spine_set"]
    pts = [(x0 + x, z) for x, z in P["spine_pts"]]
    face = make_face(Polyline(*[(x, 0, z) for x, z in pts], close=True).moved(Location((0, 0, 0))))
    # the polyline lies in the XZ plane; extrude along Y
    plate = extrude(face, amount=P["spine_t"] / 2, both=True)
    holes = []
    for ex, ez in (P["eye_main"], P["eye_bag"]):
        holes.append(rod((x0 + ex, -20, ez), (x0 + ex, 20, ez), P["eye_d"] / 2))
    lx, lz, ld = P["light_hole"]
    holes.append(rod((x0 + lx, -20, lz), (x0 + lx, 20, lz), ld / 2))
    top = P["spine_pts"][-1][1]
    for sx in P["slots"]:
        holes.append(Pos(x0 + sx, 0, (P["slot_bottom"] + top + 5) / 2) * Box(P["slot_w"], 20, top + 5 - P["slot_bottom"]))
    px, pz = P["pin_xz"]
    holes.append(rod((x0 + px, -20, pz), (x0 + px, 20, pz), P["pin_hole"] / 2))
    tx, tz, td = P["tether_hole"]
    holes.append(rod((x0 + tx, -20, tz), (x0 + tx, 20, tz), td / 2))
    for hsh in holes:
        plate = plate - hsh
    return plate


def _doublers(P, D):
    x0 = P["spine_set"]
    od, t = P["doubler"]
    out = []
    for ex, ez in (P["eye_main"], P["eye_bag"]):
        for s in (1, -1):
            y0 = s * P["spine_t"] / 2
            y1 = s * (P["spine_t"] / 2 + t)
            out.append(rod((x0 + ex, y0, ez), (x0 + ex, y1, ez), od / 2, P["eye_d"] / 2))
    return out


def _cheeks(P, D):
    """Two 6 mm cheek plates welded on the faces of the spine top, notched round each slot so the chain
    links lie against the 5 mm web, and drilled for the lock pin."""
    x0 = P["spine_set"]
    L, t, zb = P["cheek"]
    top = P["spine_pts"][-1][1]
    out = []
    for sgn in (1, -1):
        yc = sgn * (P["spine_t"] / 2 + t / 2)
        ch = Pos(x0 + L / 2, yc, (zb + top) / 2) * Box(L, t, top - zb)
        nw, nb = P["notch"]
        for sx in P["slots"]:
            ch = ch - Pos(x0 + sx, yc, (nb + top + 5) / 2) * Box(nw, t + 2, top + 5 - nb)
        px, pz = P["pin_xz"]
        ch = ch - rod((x0 + px, -30, pz), (x0 + px, 30, pz), P["pin_hole"] / 2)
        out.append(ch)
    return out


def _keeper(P, D):
    """Keeper: one piece of 3 mm sheet, a bridge lying on the cleat top across both slot mouths and two
    narrow legs bent down outside the cheeks between the notches, drilled for the lock pin."""
    x0 = P["spine_set"]
    Lb, t, lw, lb = P["keeper"]
    top = P["spine_pts"][-1][1]
    half = P["spine_t"] / 2 + P["cheek"][1]          # outside face of a cheek
    px, pz = P["pin_xz"]
    bridge = Pos(x0 + P["cheek"][0] / 2, 0, top + t / 2) * Box(Lb, 2 * (half + t), t)
    legs = []
    for sgn in (1, -1):
        legs.append(Pos(x0 + px, sgn * (half + t / 2), (lb + top) / 2) * Box(lw, t, top - lb))
    k = bridge + legs[0] + legs[1]
    return k - rod((x0 + px, -30, pz), (x0 + px, 30, pz), P["pin_hole"] / 2)


def _pin(P, D):
    """8 mm ball-lock pin, put in from the -Y side; button head outside the keeper leg."""
    x0 = P["spine_set"]
    px, pz = P["pin_xz"]
    half = P["spine_t"] / 2 + P["cheek"][1] + P["keeper"][1]
    body = rod((x0 + px, -half, pz), (x0 + px, half + 3.0, pz), P["pin_d"] / 2)
    head = rod((x0 + px, -half - 6.0, pz), (x0 + px, -half, pz), 8.0)
    return body + head


def frame_parts(P=PARAMS, D=None):
    """Frame parts in frame-local coordinates (virtual vertex at the origin)."""
    D = D or derived(P)
    F = {}
    F["spine"] = _spine(P, D)
    F["bars"] = group([_bar(P, D, 1), _bar(P, D, -1)])
    F["pads"] = group([_pad(P, D, 1), _pad(P, D, -1)])
    F["pad_screws"] = group([_pad_screws(P, D, 1), _pad_screws(P, D, -1)])
    F["doublers"] = group(_doublers(P, D))
    F["cheeks"] = group(_cheeks(P, D))
    F["keeper"] = _keeper(P, D)
    F["pin"] = _pin(P, D)
    return F


# ----------------------------------------------------------------- chain
_LINK = None


def link_template(P=PARAMS):
    global _LINK
    if _LINK is None:
        D = derived(P)
        _LINK = stadium(D["link_straight"], D["link_bend"], P["wire"] / 2)
    return _LINK


def master_template(P=PARAMS):
    st, L, W = P["master"]
    return stadium(L - W, W / 2 + st / 2, st / 2)


def _tangent_point(Pxy, R, side):
    """Tangent point on a circle (centre origin, radius R) from an outside point; side -1 or +1."""
    d = math.hypot(*Pxy)
    phi = math.atan2(Pxy[1], Pxy[0])
    al = math.acos(R / d)
    th = phi + side * al
    return th, (R * COS(th), R * SIN(th))


def chain_path(P=PARAMS, D=None):
    """Chain centre-line around the trunk in the plane z = z_c, as (points, arc angles).
    Starts at the link standing in slot A (fixed end, loop toward -Y), runs round the back of the
    trunk and ends at the link standing in slot B (adjustable end)."""
    D = D or derived(P)
    xa = D["x_s"] + P["slots"][0]
    xb = D["x_s"] + P["slots"][1]
    sa, sb = (xa, 0.0), (xb, 0.0)
    pa, pb = (xa, -P["pitch"]), (xb, P["pitch"])
    R = D["R_c"]
    tha, ta = _tangent_point(pa, R, -1)
    thb, tb = _tangent_point(pb, R, +1)
    th_end = thb - 2 * math.pi
    arc = []
    n = 72
    for i in range(n + 1):
        th = tha + (th_end - tha) * i / n
        arc.append((R * COS(th), R * SIN(th)))
    pts = [sa, pa] + arc + [pb, sb]
    return pts, (tha, th_end)


def _resample(pts, n):
    """n + 1 points evenly spaced along a 2D polyline."""
    seg = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    L = sum(seg)
    out, acc, j = [], 0.0, 0
    for k in range(n + 1):
        s = L * k / n
        while j < len(seg) - 1 and acc + seg[j] < s:
            acc += seg[j]; j += 1
        f = 0 if seg[j] == 0 else (s - acc) / seg[j]
        out.append((pts[j][0] + f * (pts[j + 1][0] - pts[j][0]), pts[j][1] + f * (pts[j + 1][1] - pts[j][1])))
    return out, L


def loop_length(P=PARAMS, trunk_d=None):
    D = derived(P, trunk_d)
    pts, _ = chain_path(P, D)
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def chain_parts(P=PARAMS, D=None):
    """Links of the loop (those under the sleeve left out), the sleeve, and both tails."""
    D = D or derived(P)
    pts, (th0, th1) = chain_path(P, D)
    L = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    n = int(round(L / P["pitch"]))
    if n % 2:
        n += 1
    centers, _ = _resample(pts, n)
    zc = D["z_c"]
    R = D["R_c"]
    # sleeve: arc centred on the back of the trunk
    th_mid = (th0 + th1) / 2
    half = P["sleeve"][0] / 2 / R
    s0, s1 = th_mid - half, th_mid + half
    link = link_template(P)
    loop_links, n_loop = [], 0
    for k, c in enumerate(centers):
        prev = centers[max(k - 1, 0)]
        nxt = centers[min(k + 1, len(centers) - 1)]
        ax = _norm((nxt[0] - prev[0], nxt[1] - prev[1], 0.0))
        if k in (0, 1, n - 1, n):                 # in and next to the slots the chain runs straight along Y
            ax = (0.0, 1.0, 0.0)
            c = (centers[0][0] if k < 2 else centers[-1][0], (-1 if k < 2 else 1) * (0.0 if k in (0, n) else P["pitch"] - 1.1))
        th = math.atan2(c[1], c[0])
        if th > 0:
            th -= 2 * math.pi
        on_arc = math.hypot(*c) < R + 1 and min(th0, th1) - 0.01 <= th <= max(th0, th1) + 0.01
        n_loop += 1
        if on_arc and s1 - 0.03 <= th <= s0 + 0.03:
            continue                              # inside the sleeve
        normal = _cross(ax, (0, 0, 1)) if k % 2 == 0 else (0, 0, 1)
        loop_links.append(place(link, (c[0], c[1], zc), ax, normal))
    # sleeve as a torus segment
    tor = Pos(0, 0, zc) * (Torus(R, P["sleeve"][1]) - Torus(R, P["sleeve"][1] - 1.5))   # the tubular webbing, the chain inside it
    big = 5 * R
    wedge = extrude(make_face(Polyline((0, 0, 0), (big * COS(s1), big * SIN(s1), 0),
                                       (big * COS((s0 + s1) / 2), big * SIN((s0 + s1) / 2), 0),
                                       (big * COS(s0), big * SIN(s0), 0), close=True)), amount=4 * P["sleeve"][1], both=True)
    sleeve = tor & Pos(0, 0, zc) * wedge
    # tail A (fixed end, +Y side): a flat link in the notch, then links down to the tether quick link
    # in the spare eye, so the fixed end cannot be lost when the keeper is off (exact end interlocks, TKB-DEC-001 D-S1)
    xa = D["x_s"] + P["slots"][0]
    xb = D["x_s"] + P["slots"][1]
    p = P["pitch"]
    tail_a = tail_a_links(P, D, link, zc)
    na_total = len(tail_a)
    # tail B (adjustable end, -Y side): one flat link in the notch, then links hanging down, then a master link
    n_tail = P["chain_len_links"] - n - 1 - na_total
    # the tail first runs out and down, clear of the back of the deeper bearing bar (TKB-DDR-003), then hangs
    tail_b = [place(link, (xb, -p + 1.1, zc), (0, -1, 0), (0, 0, 1))]
    last_link = None
    pos = (xb, -p - 12.0, zc - 6.0)
    y_out = P["tail_b_out"]
    dg = _norm((0.0, -1.0, -1.2))
    zs = []
    for k in range(max(n_tail - 1, 0)):
        if pos[1] > y_out + 0.5:
            normal = _cross(dg, (1, 0, 0)) if k % 2 == 0 else (1, 0, 0)
            tail_b.append(place(link, pos, dg, normal))
            nxt = _add(pos, _mul(dg, p))
            pos = (xb, max(nxt[1], y_out), nxt[2])
        else:
            normal = (1, 0, 0) if k % 2 == 0 else (0, 1, 0)
            tail_b.append(place(link, pos, (0, 0, 1), normal))
            last_link = (pos, normal)
            pos = (xb, pos[1], pos[2] - p)
        zs.append(pos[2] + p)
    hy = pos[1]
    st, ML, MW = P["master"]
    # the master link hangs from a grade 80 connecting link, which threads the last chain link (a 10 mm master
    # link does not pass a 6 mm link's 7.8 mm opening): exact interlocks, each ring at right angles to the last
    (lc, ln) = last_link
    cw, cs, cb = P["conn_link"]
    z_cw_top = lc[2] - (D["link_straight"] / 2 + D["link_bend"]) + P["wire"] / 2 + cw / 2 + 0.05
    cc = (xb, lc[1], z_cw_top - cs / 2 - cb)
    cn = (0, 1, 0) if abs(ln[0]) > 0.5 else (1, 0, 0)
    conn = place(stadium(cs, cb, cw / 2), cc, (0, 0, 1), cn)
    z_m_top = cc[2] - cs / 2 - cb + cw / 2 + st / 2 + 0.05
    mz_b = z_m_top - (ML - MW) / 2 - (MW / 2 + st / 2)
    master = place(master_template(P), (xb, lc[1], mz_b), (0, 0, 1), ln)
    D["loop_links"], D["tail_a_links"] = loop_links, tail_a        # kept for the kit 1.9 components (D3)
    D["tail_b_links"], D["tail_b_conn"], D["tail_b_master"] = tail_b, conn, master
    tail_b = tail_b + [conn, master]
    D["tail_b_y"] = hy
    D["n_tail_a"] = na_total
    D["n_loop_links"] = n + 1
    D["n_tail_b"] = n_tail
    D["loop_len"] = L
    D["tail_b_bottom"] = mz_b - ML / 2 - st
    return {"chain_loop": group(loop_links), "sleeve": sleeve, "chain_tail_a": group(tail_a),
            "chain_tail_b": group(tail_b), "maillon": maillon(P, D)}


NOTCH_SWING = 39.0      # deg: the fixed end's first link swings toward -X over the cleat top, clear of the loop
NOTCH_DROOP = 0.0      # deg: and droops on the slot link's end bend, under the loop coming back into slot B


def tether_pose(P=PARAMS, D=None):
    """The tether link (a grade 80 connecting link, BOM 14; TKB-DEC-001 D-S1) lies flat (ring plane horizontal)
    through the 10 mm tether hole near the spine's front edge, round the strip of web between the hole and the
    edge. Returns its centre (global) and its long axis (+X, toward the hole)."""
    D = D or derived(P)
    tx, tz, td = P["tether_hole"]
    cw, cs, cb = P["conn_link"]
    apex_x = tx + 0.5                                        # hole-side bend inside the hole, just past its centre
    xc = D["x_s"] + apex_x - cb - cs / 2
    return (xc, 0.0, tz), (1.0, 0.0, 0.0)


def maillon_center(P=PARAMS, D=None):
    return tether_pose(P, D)[0]


def maillon(P=PARAMS, D=None):
    """The tether link: a 6 mm grade 80 connecting link (two halves and a pin, drawn as one ring with the pin
    boss on its -Y side) through the tether hole, round the web strip at the spine's front edge."""
    cw, cs, cb = P["conn_link"]
    c, u = tether_pose(P, D)
    tmpl = stadium(cs, cb, cw / 2) + rod((-2.0, cb, 0), (2.0, cb, 0), cw / 2 + 1.6, cw / 2)   # template +y is global -Y
    return place(tmpl, c, u, (0.0, 0.0, 1.0))


def tail_a_links(P, D, link, zc):
    """Links of the fixed end (tail A), with exact interlocks: a flat link on the +Y end of the link standing in
    slot A, swung toward -X clear of the chain loop that comes back into slot B over the cleat; a short run
    hanging from it; and a link that hooks the tether link's +Y straight wire in front of the spine's front edge.
    Interlocked links are one pitch apart along the chain and at right angles."""
    p = P["pitch"]
    xa = D["x_s"] + P["slots"][0]
    ends = D["link_straight"] / 2 + D["link_bend"]          # centre to end-wire centre, 12 mm
    sw, dr = math.radians(NOTCH_SWING), math.radians(NOTCH_DROOP)
    a0 = (-SIN(sw) * COS(dr), COS(sw) * COS(dr), -SIN(dr))
    s_end = (xa, ends, zc)                                   # +Y end wire of the link standing in slot A, along Z
    c0 = _add(s_end, _mul(a0, ends - P["wire"] - 0.05))
    out = [place(link, c0, a0, _norm(_sub((0, 0, 1), _mul(a0, a0[2]))))]
    l0_end = _add(c0, _mul(a0, ends))                        # its far end wire, horizontal
    cw, cs, cb = P["conn_link"]
    tc, _ = tether_pose(P, D)
    wire = (tc[0] - cs / 2 + 2.0, tc[1] + cb, tc[2])          # on the tether link's +Y straight wire, along X
    gap = P["wire"] / 2 + cw / 2 + 0.05
    hc = (wire[0], wire[1], wire[2] + ends - gap)
    hook = place(link, hc, (0, 0, 1), (1, 0, 0))
    h_top = (hc[0], hc[1], hc[2] + ends)                     # its top end wire, along Y
    A = _add(l0_end, (0.0, 0.0, -(ends - P["wire"] - 0.05)))   # the run's first link hangs from the notch link
    B = _add(h_top, (0.0, 0.0, ends - P["wire"] - 0.05))     # the run's last link stands on the hook link
    d = math.dist(A, B)
    m = max(2, int(math.ceil(d / p)) + 1)
    if m % 2 == 1:                                           # first and last run links: the first hangs at right
        m += 1                                               # angles to the flat notch link, the last at right
    L = (m - 1) * p                                          # angles to the hook link
    mid = _mul(_add(A, B), 0.5)
    lo, hi = 0.0, L
    for _ in range(80):                                       # the slack bows out to +Y and -X, clear of the cheek
        sg = (lo + hi) / 2
        K = (mid[0] - 0.5 * sg, mid[1] + sg, mid[2])
        if math.dist(A, K) + math.dist(K, B) > L:
            hi = sg
        else:
            lo = sg
    K = (mid[0] - 0.5 * lo, mid[1] + lo, mid[2])
    pts = [A, K, B]
    run = []
    for i in range(m):
        c, a = _along(pts, i * p)
        if i == 0:
            c = A
        if i == m - 1:
            c = B
        nA = _norm(_sub((1.0, 0.0, 0.0), _mul(a, a[0]))) if abs(a[0]) < 0.95 else _norm(_sub((0.0, 1.0, 0.0), _mul(a, a[1])))
        n_ = nA if i % 2 == 1 else _norm(_cross(a, nA))
        run.append(place(link, c, a, n_))
    return out + run + [hook]


def _along(pts, s):
    """Point and unit direction at arc length s along a 3D polyline."""
    acc = 0.0
    for a, b in zip(pts, pts[1:]):
        L = math.dist(a, b)
        if s <= acc + L + 1e-9 or b is pts[-1]:
            d = _norm(_sub(b, a))
            return _add(a, _mul(d, s - acc)), d
        acc += L


def chain_envelope(P=PARAMS, D=None):
    """Light stand-in for the chain on drawing sheets: a 20 mm round envelope along the chain's centre line
    (loop, both tails), so hidden-line views stay quick. The pictures and checks use the real links."""
    D = D or derived(P)
    pts, (th0, th1) = chain_path(P, D)
    zc, R, rr = D["z_c"], D["R_c"], D["link_outer_w"] / 2
    p3 = [(x, y, zc) for x, y in pts]
    segs = [rod(p3[0], p3[1], rr), rod(p3[1], p3[2], rr), rod(p3[-3], p3[-2], rr), rod(p3[-2], p3[-1], rr)]
    lo, hi = min(th0, th1), max(th0, th1)
    big = 5 * R
    mids = [lo + (hi - lo) * k / 6 for k in range(7)]
    wedge = extrude(make_face(Polyline((0, 0, 0), *[(big * COS(t), big * SIN(t), 0) for t in mids], close=True)),
                    amount=4 * rr, both=True)
    arc = (Pos(0, 0, zc) * Torus(R, rr)) & (Pos(0, 0, zc) * wedge)
    xa = D["x_s"] + P["slots"][0]
    xb = D["x_s"] + P["slots"][1]
    mq = maillon_center(P, D)
    ta = rod((xa, 0, zc), (xa, P["pitch"] + 12, zc), rr) + rod((xa, P["pitch"] + 12, zc - 6), (mq[0], mq[1] + 20, mq[2]), rr)
    y0 = -P["pitch"] - 12
    yo = P["tail_b_out"]
    z_out = zc - 6 - (y0 - yo) * 1.2
    tb = rod((xb, 0, zc), (xb, y0, zc), rr) + rod((xb, y0, zc), (xb, yo, z_out), rr) + \
        rod((xb, yo, z_out), (xb, yo, D.get("tail_b_bottom", zc - 400)), rr)
    return fuse_all(segs + [arc]), ta, tb


# ----------------------------------------------------------------- load side (global coordinates)
def carabiner(P, top, normal=(1, 0, 0)):
    """Locking carabiner as a closed ring (gate not drawn): long axis Z, its top bar centre at top."""
    d, st, br = P["carab"]
    c = (top[0], top[1], top[2] - br - st / 2)
    return place(stadium(st, br, d / 2), c, (0, 0, 1), normal)


def carab_bottom(P, top):
    d, st, br = P["carab"]
    return (top[0], top[1], top[2] - st - 2 * br)


def load_side(P=PARAMS, D=None):
    D = D or derived(P)
    x0 = D["x_s"]
    out = {}
    ex, ez = P["eye_main"]
    off = P["eye_d"] / 2 - P["carab"][0] / 2          # the bar bears on the bottom of the eye
    # the carabiner's end bend bears on the eye at the outer faces of the doubler rings, not at its middle
    lift = bend_lift(P["carab"][2], P["carab"][0] / 2, P["spine_t"] / 2 + P["doubler"][1]) + 0.05
    top_m = (x0 + ex, 0.0, ez - off + lift)
    out["carab_main"] = carabiner(P, top_m)
    # descender: body in the XZ plane, hole for the carabiner 15 mm below its top
    dx, dy, dz = P["desc"]
    cb = carab_bottom(P, top_m)
    hole_z = cb[2] + P["carab"][0] / 2 - 9.0 + bend_lift(P["carab"][2], P["carab"][0] / 2, 11.6) + 0.1   # the 18 mm hole bears on the bar at the plate faces
    body = Pos(cb[0], 0, hole_z + 15 - dz / 2) * Box(dx, dy, dz)
    body = body - rod((cb[0], -dy, hole_z), (cb[0], dy, hole_z), 9.0)
    handle = rod((cb[0] + dx / 2 - 10, 0, hole_z - 25), (cb[0] + dx / 2 + 85, 0, hole_z + 5), 7.0)
    out["descender"] = body + handle
    d_bot = hole_z + 15 - dz
    D["desc_bottom"] = d_bot
    # brake carabiner in the spare eye, beside the tether quick link; the brake strand leaves the side of
    # the descender, turns 180 deg over the carabiner's bottom bar and runs down to the rope bag, which is
    # lowered to the helpers on the ground before the lowering starts; the load strand runs down to the victim
    sx, sz = P["eye_bag"]
    cdx = 0.0                                  # the spare eye holds the brake carabiner alone (TKB-DEC-001 D-S1)
    top_s = (x0 + sx + cdx, 0.0, sz - math.sqrt((P["eye_d"] / 2 - P["carab"][0] / 2) ** 2 - cdx ** 2) + lift)
    out["carab_brake"] = carabiner(P, top_s)
    D["carab_main_top"], D["carab_brake_top"] = top_m, top_s          # kept for the kit 1.9 components (D3)
    cbs = carab_bottom(P, top_s)
    rr = P["rope_d"] / 2
    R = P["carab"][0] / 2 + rr
    xl = cb[0] + P["strand_dx"][1]
    side = (cb[0] - dx / 2, 0.0, hole_z - 55)
    up = (cbs[0] + R, 0.0, cbs[2])
    down = (cbs[0] - R, 0.0, cbs[2])
    half = (Pos(cbs[0], 0, cbs[2]) * Rot(90, 0, 0) * Torus(R, rr)) & (Pos(cbs[0], 0, cbs[2] + 50) * Box(100, 100, 100))
    out["rope_brake"] = rod(side, up, rr) + half + rod(down, (down[0], 0, P["load_end_z"]), rr)
    out["rope_load"] = rod((xl, 0, d_bot + 10), (xl, 0, P["load_end_z"]), rr)
    D["xb_strand"], D["xl_strand"] = down[0], xl
    return out


def victim_kit(P=PARAMS, origin=(0.0, 0.0, 0.0)):
    """Victim set packed pre-rigged (TKB-DDR-003), laid out flat for the kit pictures: the victim carabiner
    already holds the rope's figure-eight loop, the triangle's two waist loops (drawn as their straps pulled
    to the carabiner) and one end of the chest sling, so at height only the crotch loop and the sling's free
    end are clipped. Also the rope bag and coil, and the tag line coil with its micro pulley."""
    ox, oy, oz = origin
    tri = extrude(make_face(Polyline((0, 0, 0), (560, 0, 0), (280, 0, -420), close=True)), amount=7, both=True)
    tri = tri - extrude(make_face(Polyline((180, 0, -40), (380, 0, -40), (280, 0, -190), close=True)), amount=10, both=True)
    loops = [Pos(x, 0, z) * Rot(90, 0, 0) * Torus(28, 6) for x, z in ((20, 10), (540, 10), (280, -430))]
    d, st, br = P["carab"]
    cc = (280.0, 0.0, 110.0)                                   # victim carabiner centre
    conn = place(stadium(st, br, d / 2), cc, (0, 0, 1), (1, 0, 0))
    c_bot = (cc[0], 0.0, cc[2] - st / 2 - br)                 # inside of the bottom bar
    c_top = (cc[0], 0.0, cc[2] + st / 2 + br)
    straps = [rod((x, 0, 30), (cc[0] + sx, 0, c_bot[2]), 5.0) for x, sx in ((40, -6), (520, 6))]
    sling = rod((cc[0] + 4, 0, c_bot[2] - 2), (cc[0] + 300, 0, c_bot[2] + 40), 3.0) + \
        place(stadium(260, 18, 3), (cc[0] + 440, 0, c_bot[2] + 40), (1, 0, 0), (0, 1, 0))
    rl = 22.0
    rope_end = Pos(c_top[0], 0, c_top[2] + rl - 6) * Rot(90, 0, 0) * Torus(rl, P["rope_d"] / 2) + \
        rod((c_top[0], 0, c_top[2] + 2 * rl - 8), (c_top[0], 0, c_top[2] + 260), P["rope_d"] / 2)
    bag = Pos(900, 0, -P["bag"][1] / 2) * Cylinder(P["bag"][0] / 2, P["bag"][1])
    coil = Pos(900, 0, -P["bag"][1] - 120) * Torus(140, 30)
    tag = Pos(-380, 0, -300) * Torus(110, 14)
    pd, pw = P["pulley"]
    pulley = Pos(-380, 0, -120) * Rot(90, 0, 0) * Cylinder(pd / 2, pw) + rod((-380, 0, -105), (-380, 0, -60), 4.0)
    S = Pos(ox, oy, oz)
    return {"triangle": S * (tri + fuse_all(loops) + fuse_all(straps)), "chest_sling": S * sling, "carab_victim": S * conn,
            "rope_end": S * rope_end, "bag": S * bag, "rope_coil": S * coil, "tag_line": S * tag, "micro_pulley": S * pulley}


def prerig_checks(P=PARAMS):
    """The pre-rigged victim set: straps, sling and rope loop meet the victim carabiner."""
    K = victim_kit(P)
    res = []
    for a in ("triangle", "chest_sling", "rope_end"):
        d = _gap(K[a], K["carab_victim"])
        res.append((d <= 1.0, f"prerig touch {a:13s} carab_victim  gap {d:6.2f} mm"))
    return res


# ----------------------------------------------------------------- whole kit
def build_components(P=PARAMS, trunk_d=None):
    """Every component of the kit as fitted to a trunk, in global coordinates (trunk axis = Z)."""
    D = derived(P, trunk_d)
    F = frame_parts(P, D)
    C = {k: Pos(D["q0"], 0, 0) * v for k, v in F.items()}
    C.update(chain_parts(P, D))
    C.update(load_side(P, D))
    C["_D"] = D
    return C


def comps_only(C):
    return {k: v for k, v in C.items() if not k.startswith("_")}


def assembly(P=PARAMS, C=None):
    C = C or build_components(P)
    return Compound(list(comps_only(C).values()))


def trunk(P=PARAMS, trunk_d=None, z0=-800.0, z1=500.0):
    r = (trunk_d or P["trunk_d"]) / 2
    return Pos(0, 0, (z0 + z1) / 2) * Cylinder(r, z1 - z0)


def frame_weldment(C):
    return C["spine"] + C["bars"] + C["doublers"] + C["cheeks"]


def mass_table(P=PARAMS, C=None):
    """Mass in kg of each carried item (steel parts from volume; bought items from catalogue class)."""
    C = C or build_components(P)
    m = {}
    for k in ("spine", "bars", "doublers", "cheeks"):                # the frame weldment, 6082-T6 (TKB-DDR-003)
        m[k] = C[k].volume * DENSITY[P.get("frame_material", "steel")]
    for k in ("keeper", "pad_screws"):
        m[k] = C[k].volume * DENSITY["steel"]
    m["pin"] = 0.04                                          # 8 mm stainless ball-lock pin with lanyard
    m["maillon"] = 0.05                                      # tether: grade 80 connecting link for 6 mm chain (TKB-DEC-001 D-S1)
    m["pads"] = C["pads"].volume * DENSITY["rubber"]
    m["chain"] = P["chain_len_links"] * P["pitch"] / 1000 * 0.80     # 6 mm grade 80, 0.80 kg/m
    m["master_links"] = 2 * 0.11
    m["sleeve"] = P["sleeve"][0] / 1000 * 0.045
    m["carabiners"] = 3 * 0.085                               # aluminium alloy screw-gate, class B (load, brake, victim)
    m["descender"] = 0.60                                     # auto-locking descender class, at the cited Petzl I'D S mass (TKB-STM-001 S18)
    m["rope"] = 30 * 0.078                                    # 11 mm EN 1891 type A, 30 m
    m["bag"] = 0.45                                           # rope bag with shoulder straps
    m["triangle"] = 0.75                                      # evacuation triangle class
    m["chest_sling"] = 0.12                                   # 120 cm sewn sling
    m["tag_line"] = P["tag_line"][1] * P["tag_line"][2]       # 4 mm accessory cord, doubled from the ground (TKB-DDR-003)
    m["micro_pulley"] = 0.05                                  # micro pulley for the tag line, on the rescuer's harness
    return m


HAULED = ("rope", "bag", "triangle", "chest_sling", "carab_victim")   # hauled up in the bag on the tag line (TKB-DDR-003)


def carried_mass(m):
    """Mass the rescuer carries up the trunk: everything except the bag the helpers haul up on the tag line.
    The victim carabiner (one of the three) travels in the bag with the pre-rigged victim set."""
    per_carab = m["carabiners"] / 3
    return sum(m.values()) - sum(m[k] for k in HAULED if k in m) - per_carab


# ----------------------------------------------------------------- constructability checks
def _gap(a, b):
    return a.distance_to(b)


def _shared(a, b):
    try:
        return (a & b).volume
    except Exception:
        return 0.0


def checks(P=PARAMS, C=None, verbose=True, trunk_d=None, label=""):
    """Parts that must touch do touch (gap <= 0.6 mm); parts that must not touch are apart."""
    C = C or build_components(P, trunk_d)
    D = C["_D"]
    T = trunk(P, trunk_d or P["trunk_d"], -900, 600)
    touch = [
        ("pads", "bars"), ("bars", "spine"), ("doublers", "spine"), ("cheeks", "spine"), ("keeper", "cheeks"),
        ("keeper", "spine"), ("pin", "keeper"), ("pin", "cheeks"), ("pad_screws", "pads"), ("pad_screws", "bars"),
        ("chain_loop", "spine"), ("chain_tail_b", "spine"), ("chain_tail_a", "chain_loop"),
        ("maillon", "chain_tail_a"),
        ("carab_main", "doublers"), ("descender", "carab_main"), ("carab_brake", "doublers"),
        ("rope_load", "descender"), ("rope_brake", "descender"), ("rope_brake", "carab_brake"),
    ]
    apart = [
        ("spine", 15), ("bars", 5), ("cheeks", 15), ("keeper", 15), ("pin", 5), ("doublers", 20), ("pad_screws", 2),
        ("maillon", 0.3),
        ("descender", 50), ("rope_load", 50), ("rope_brake", 30), ("carab_main", 50), ("carab_brake", 20),
        ("chain_tail_a", 3), ("chain_tail_b", 10),
    ]
    pairs_apart = [
        ("chain_tail_b", "doublers", 0.5), ("chain_tail_b", "carab_main", 5), ("chain_tail_b", "keeper", 0.5),
        ("chain_tail_b", "bars", 5), ("chain_tail_b", "descender", 5), ("chain_tail_b", "cheeks", 0.3),
        ("chain_tail_a", "cheeks", 0.0), ("chain_tail_a", "keeper", 0.5), ("chain_tail_a", "doublers", 0.5),
        ("chain_tail_a", "bars", 5), ("chain_loop", "cheeks", 0.3), ("chain_loop", "keeper", 0.5),
        ("chain_loop", "pin", 0.5), ("chain_loop", "bars", 20), ("chain_loop", "pads", 20), ("maillon", "bars", 5),
        ("descender", "spine", 5), ("descender", "doublers", 3), ("pads", "spine", 5),
        ("pin", "chain_tail_a", 0.5), ("pin", "chain_tail_b", 0.5), ("rope_load", "rope_brake", 10),
        ("carab_brake", "maillon", 0.3), ("carab_brake", "chain_tail_a", 0.1), ("carab_brake", "chain_tail_b", 2),
        ("rope_brake", "chain_tail_b", 5), ("rope_brake", "chain_tail_a", 3), ("rope_brake", "spine", 3),
        ("carab_brake", "bars", 5), ("chain_tail_a", "chain_loop", 0.0), ("chain_tail_a", "chain_tail_b", 0.0),
        ("maillon", "doublers", 5.0), ("maillon", "cheeks", 0.5), ("maillon", "spine", 0.0), ("maillon", "chain_tail_b", 0.0),
        ("chain_tail_a", "pads", 2.0), ("carab_brake", "spine", 0.0), ("carab_brake", "doublers", 0.0),
    ]
    res = []
    for a, b in touch:
        d = _gap(C[a], C[b])
        res.append((d <= 0.6, f"{label}touch  {a:13s} {b:13s} gap {d:6.2f} mm"))
    for a, clr in apart:
        d = _gap(C[a], T)
        ov = _shared(C[a], T)
        res.append((ov < 1.0 and d >= clr, f"{label}apart  {a:13s} trunk         gap {d:6.1f} mm (need {clr:g}), shared {ov:.1f} mm3"))
    for a, b, clr in pairs_apart:
        d = _gap(C[a], C[b])
        ov = _shared(C[a], C[b])
        tol = 6.0 if (a, b) == ("chain_tail_a", "chain_loop") else 1.0     # slack links resting on each other
        res.append((ov < tol and d >= clr, f"{label}apart  {a:13s} {b:13s} gap {d:6.1f} mm (need {clr:g}), shared {ov:.1f} mm3"))
    # pads bear on the trunk; the sleeve lies on it
    for a in ("pads", "sleeve"):
        d = _gap(C[a], T)
        res.append((d <= 0.6, f"{label}touch  {a:13s} trunk         gap {d:6.2f} mm"))
    u = D["u_contact"]
    res.append((P["pad_u0"] + 10 <= u <= P["pad_u0"] + P["pad"][0] - 10,
                f"{label}contact {u:.0f} mm along the pad face (pad runs {P['pad_u0']:.0f} to {P['pad_u0'] + P['pad'][0]:.0f})"))
    res.append((D["n_tail_b"] >= 4 and D["n_loop_links"] + D["n_tail_a"] + D["n_tail_b"] == P["chain_len_links"], f"{label}chain: {D['n_loop_links']} links in the loop, {D['n_tail_b']} left in the adjustable tail (need 4)"))
    res.append((D["tail_b_bottom"] > -2500, f"{label}tail bottom at {D['tail_b_bottom']:.0f} mm"))
    if verbose:
        for ok, txt in res:
            print(("pass " if ok else "FAIL ") + txt)
    return res


def frame_checks(P=PARAMS, C=None):
    """Checks added with the aluminium frame (TKB-DDR-003): the cleat web still lets a link span it, the
    lock pin's grip matches the thicker stack, the quick link still passes round the spare eye, the deeper
    bars leave room to weld beside the spare eye's rings, and the cleat web is deeper than before."""
    C = C or build_components(P)
    res = []
    span = P["pitch"] - 2 * P["wire"]
    res.append((P["spine_t"] <= span - 0.5, f"frame cleat web {P['spine_t']:.1f} mm inside a link's span of {span:.1f} mm (0.5 mm clearance)"))
    stack = P["spine_t"] + 2 * P["cheek"][1] + 2 * P["keeper"][1]
    res.append((abs(stack - 27.0) <= 0.5, f"frame lock pin stack {stack:.1f} mm against a 27 mm ball-lock pin grip"))
    cw, cs, cb = P["conn_link"]
    inner = 2 * (cb - cw / 2)
    res.append((P["spine_t"] <= inner - 0.5, f"frame tether link opening {inner:.1f} mm round the {P['spine_t']:.1f} mm web (0.5 mm clearance)"))
    tx, tz, td = P["tether_hole"]
    res.append((cw <= td - 2.0 and tx - td / 2 >= 5.0, f"frame tether hole {td:.0f} mm for the {cw:.0f} mm link wire; web strip to the front edge {tx - td / 2:.0f} mm (need 5)"))
    res.append((cw <= P["link_w"] - 0.5, f"frame tether link wire {cw:.1f} mm through the chain link's {P['link_w']:.1f} mm opening"))
    d = _gap(C["bars"], C["doublers"])
    res.append((d >= 8.0, f"frame bars to eye rings {d:.1f} mm (need 8 for the welds)"))
    depth = P["spine_pts"][-1][1] - P["slot_bottom"]
    res.append((depth >= 35.0, f"frame cleat web {depth:.0f} mm deep above the slot bottoms (need 35)"))
    return res


def all_checks(P=PARAMS, verbose=True):
    res = []
    for d in (P["trunk_d"], P["trunk_range"][0], P["trunk_range"][1]):
        res += checks(P, build_components(P, d), verbose, d, label=f"[{d:.0f}] ")
    extra = frame_checks(P) + prerig_checks(P)
    if verbose:
        for ok, txt in extra:
            print(("pass " if ok else "FAIL ") + txt)
    res += extra
    n_ok = sum(1 for ok, _ in res if ok)
    if verbose:
        print(f"{n_ok} of {len(res)} constructability checks pass")
    return res


def export(P=PARAMS, C=None):
    C = C or build_components(P)
    step_dir, stl_dir = ROOT / "cad" / "step", ROOT / "cad" / "stl"
    step_dir.mkdir(parents=True, exist_ok=True); stl_dir.mkdir(parents=True, exist_ok=True)
    export_step(assembly(P, C), str(step_dir / "trunkbelay-assembly.step"))
    F = frame_parts(P)
    export_step(Compound([F["spine"], F["bars"], F["doublers"], F["cheeks"]]), str(step_dir / "trunkbelay-frame-weldment.step"))
    export_stl(Compound([F["spine"], F["bars"], F["doublers"], F["cheeks"]]), str(stl_dir / "trunkbelay-frame-weldment.stl"),
               tolerance=0.2, angular_tolerance=0.3)
    export_stl(F["pads"], str(stl_dir / "trunkbelay-pads.stl"), tolerance=0.2, angular_tolerance=0.3)
    print("wrote cad/step/trunkbelay-assembly.step, trunkbelay-frame-weldment.step and cad/stl/*.stl")


# ================================================================== kit 1.9 interface (STANDARDS section 24), D3
import cad_parts as cp  # noqa: E402
import tkb_parts as tk  # noqa: E402

TITLE = "TrunkBelay"
OPTIONS = {"A": "Self-locking lever collar", "B": "Constricting wrap anchor", "C": "Screwed stem anchor"}
PRINCIPLES = {
    "A": "A rigid V frame held by a chain wrap cocks under the load on its 150 mm lever arm; the grip at the pads "
         "and the chain rises in step with the load (self-locking couple).",
    "B": "A webbing strap wrapped four turns round the trunk and tied off as a Klemheist constricts as it is "
         "loaded; friction over the wrapped length holds it (capstan friction).",
    "C": "A folded steel saddle is screwed to the stem with four coach screws; the screws carry the load in "
         "bearing and bending in the stem wood (mechanical fastening).",
}
CHOSEN = "A"          # the current design (option A, TKB-OPT-001); the choice between options is awaiting Amish
_GZ = PARAMS["ground_z"]
OPTION_VIEWS = {k: {"el": 18, "az": -40, "scale": "person", "keep_context": True, "ground_z": _GZ} for k in OPTIONS}
ALLOWED_CONTACTS = []

_AL, _ST = "aluminium", "stainless"


def _spine_prism(P, D):
    """The spine outline extruded 40 mm each side: weld beads on the spine faces are trimmed to it."""
    x0 = P["spine_set"]
    pts = [(x0 + x, z) for x, z in P["spine_pts"]]
    face = make_face(Polyline(*[(x, 0, z) for x, z in pts], close=True))
    return extrude(face, amount=40, both=True)


def _frame_welds(P, D):
    """Fillet weld beads (r 2.5 mm, about a 5 mm leg) of the frame weldment, frame-local: each bearing bar to
    the spine (top edge and both walls), each eye ring all round, each cheek along its bottom and rear edges."""
    r = 2.5
    hs = P["spine_t"] / 2
    h, dep, wall = P["bar"]
    t0, t1 = P["pad"][1], P["pad"][1] + dep
    bx, by = D["b"][0], D["b"][1]
    out = []
    for s in (1, -1):
        b = (bx, s * by, 0.0)
        xf = (t0 - hs * by) / bx
        xb = (t1 - hs * by) / bx
        side = "right" if s > 0 else "left"
        out.append((f"Weld, bearing bar {side} to spine, top", tk.bead((xf, s * hs, h), (xb, s * hs, h), (0, 0, 1), (0, s, 0), r)))
        out.append((f"Weld, bearing bar {side} to spine, front wall", tk.bead((xf, s * hs, 0.5), (xf, s * hs, h), (0, s, 0), tuple(-c for c in b), r)))
        out.append((f"Weld, bearing bar {side} to spine, rear wall", tk.bead((xb, s * hs, 0.5), (xb, s * hs, h), (0, s, 0), b, r)))
        x0 = P["spine_set"]
        od, t = P["doubler"]
        for nm, (ex, ez) in (("load eye", P["eye_main"]), ("spare eye", P["eye_bag"])):
            out.append((f"Weld, {nm} ring {side} to spine", tk.ring_bead((x0 + ex, s * hs, ez), (0, s, 0), od / 2, 2.0)))
        L, ct, zb = P["cheek"]
        top = P["spine_pts"][-1][1]
        out.append((f"Weld, cleat cheek {side} to spine, bottom", tk.bead((x0 + 0.5, s * hs, zb), (x0 + L, s * hs, zb), (0, 0, -1), (0, s, 0), r)))
        out.append((f"Weld, cleat cheek {side} to spine, rear", tk.bead((x0 + L, s * hs, zb), (x0 + L, s * hs, top), (1, 0, 0), (0, s, 0), r)))
    prism = _spine_prism(P, D)
    return [(n, sh & prism) for n, sh in out]


def _pad_fixings(P, D, side):
    """Two M6 x 30 countersunk screws per pad, each in a rivet nut set in the bearing bar's front wall:
    returns the screws, the rivet nuts and the cutters for the pad and bar holes (frame-local)."""
    w = (D["w"][0], side * D["w"][1], 0.0)
    b = (D["b"][0], side * D["b"][1], 0.0)
    pt, wall = P["pad"][1], P["bar"][2]
    zc = P["pad"][2] / 2
    at_ = lambda u, t: (w[0] * u + b[0] * t, w[1] * u + b[1] * t, zc)
    screws, nuts, pad_cut, bar_cut = [], [], [], []
    for u in (P["pad_u0"] + 35, P["pad_u0"] + P["pad"][0] - 35):
        head = Solid.make_cone(6.0, 3.0, 3.3, Plane(origin=at_(u, 3.0), z_dir=b))
        shank = tk.rod(at_(u, 6.2), at_(u, 33.0), 3.0)
        screws.append(head + shank)
        nuts.append(tk.rod(at_(u, pt), at_(u, pt + wall + 10.0), 4.5, 3.0) + tk.rod(at_(u, pt + wall + 10.0), at_(u, pt + wall + 11.0), 4.5, 3.0))
        pad_cut.append(Solid.make_cone(6.0, 3.0, 3.3, Plane(origin=at_(u, 3.0), z_dir=b)) + tk.rod(at_(u, -1.0), at_(u, 3.0), 6.0)
                       + tk.rod(at_(u, 0.0), at_(u, pt + 0.5), 3.25))
        bar_cut.append(tk.rod(at_(u, pt - 0.5), at_(u, pt + wall + 0.5), 4.5))
    return screws, nuts, pad_cut, bar_cut


def _keeper_d3(P, D):
    """The keeper as one bent piece of 3 mm sheet: legs run up into the bridge so the part is one solid."""
    x0 = P["spine_set"]
    Lb, t, lw, lb = P["keeper"]
    top = P["spine_pts"][-1][1]
    half = P["spine_t"] / 2 + P["cheek"][1]
    px, pz = P["pin_xz"]
    k = Pos(x0 + P["cheek"][0] / 2, 0, top + t / 2) * Box(Lb, 2 * (half + t), t)
    for sgn in (1, -1):
        k = k + Pos(x0 + px, sgn * (half + t / 2), (lb + top + t) / 2) * Box(lw, t, top + t - lb)
    k = k - rod((x0 + px, -30, pz), (x0 + px, 30, pz), P["pin_hole"] / 2)
    return cp.break_edges(k, 0.5)


def _trunk_part(P, r, z0=None, z1=900.0):
    z0 = PARAMS["ground_z"] - 200.0 if z0 is None else z0
    return cp.part(f"Palm trunk, {2 * r:.0f} mm (site)", Pos(0, 0, (z0 + z1) / 2) * Cylinder(r, z1 - z0), "timber", kind="context", group="context")


def option_a(P=PARAMS, trunk_d=None):
    """Option A, the self-locking lever collar: the constructable design of TKB-DDR-002 and TKB-DDR-003, as
    build_components() fits it to the trunk, with the D3 detail added (holes for every fixing, rivet nuts,
    weld beads, edge breaks, the master link on its own, and detailed carabiners and descender)."""
    C = build_components(P, trunk_d)
    D = C["_D"]
    mv = lambda s: Pos(D["q0"], 0, 0) * s
    out = []
    add = lambda name, shape, mat, kind="made", bom=None, ex=(0, 0, 0): out.append(cp.part(name, shape, mat, kind=kind, bom=bom, explode=ex))
    add("Spine plate, 6082-T6 aluminium 5 mm", cp.break_edges(mv(_spine(P, D)), 0.5), _AL, bom=1, ex=(120, 0, 0))
    for s, side in ((1, "right"), (-1, "left")):
        screws, nuts, pad_cut, bar_cut = _pad_fixings(P, D, s)
        bar = cp.break_edges(_bar(P, D, s), 0.5)
        pad = cp.break_edges(_pad(P, D, s), 1.0)
        for c_ in bar_cut:
            bar = bar - c_
        for c_ in pad_cut:
            pad = pad - c_
        add(f"Bearing bar {side}, 6082-T6 RHS 50 x 40 x 3", mv(bar), _AL, bom=2, ex=(-60, 0, -120))
        add(f"Rubber bark pad {side}, 10 mm", mv(pad), "epdm", bom=6, ex=(-140, 0, -120))
        for i, (sc, nu) in enumerate(zip(screws, nuts), 1):
            add(f"Pad screw {side} {i}, M6 x 30 countersunk, A2", mv(sc), _ST, kind="fastener", ex=(-180, 0, -120))
            add(f"Rivet nut {side} {i}, M6 countersunk, stainless", mv(nu), _ST, kind="fastener", ex=(-100, 0, -120))
    for i, ring in enumerate(_doublers(P, D), 1):
        add(f"Eye doubler ring {i}, 6082-T6 4 mm", cp.break_edges(mv(ring), 0.4), _AL, bom=3, ex=(120, 0, -120))
    for i, ch in enumerate(_cheeks(P, D), 1):
        add(f"Cleat cheek {i}, 6082-T6 8 mm", cp.break_edges(mv(ch), 0.5), _AL, bom=4, ex=(120, 0, 120))
    for name, sh in _frame_welds(P, D):
        add(name + " (TIG, ER5356)", mv(sh), _AL, kind="weld", bom=None, ex=(120, 0, 0))
    add("Keeper, 3 mm steel sheet, zinc plated", mv(_keeper_d3(P, D)), "zinc_plated", bom=9, ex=(120, 0, 260))
    add("Lock pin, ball-lock 8 mm, stainless", mv(_pin(P, D)), _ST, kind="bought", bom=10, ex=(120, -160, 200))
    add("Chain loop, grade 80, 6 mm", group(D["loop_links"]), "mild_steel", kind="bought", bom=11, ex=(-200, 0, 150))
    add("Chain fixed end", group(D["tail_a_links"]), "mild_steel", kind="bought", bom=11, ex=(150, 150, 0))
    add("Chain adjustable end", group(D["tail_b_links"]), "mild_steel", kind="bought", bom=11, ex=(150, -200, 0))
    add("Master link, grade 80", D["tail_b_master"], "mild_steel", kind="bought", bom=12, ex=(150, -260, -60))
    add("Chain sleeve, 50 mm tubular nylon webbing", C["sleeve"], "canvas", bom=15, ex=(-350, 0, 150))
    add("Tether link, grade 80 connecting link, 6 mm", C["maillon"], "mild_steel", kind="bought", bom=14, ex=(-120, 120, 0))
    add("Connecting link, grade 80, 6 mm", D["tail_b_conn"], "mild_steel", kind="bought", bom=13, ex=(150, -260, -30))
    ls, _ = tk.lowering_set(P, D["carab_main_top"], D["carab_brake_top"])
    out += ls
    out.append(_trunk_part(P, D["r"]))
    return out


def option_b(P=PARAMS, trunk_d=None):
    """Option B, the constricting wrap anchor: rubber bark mat, anchor strap wrapped in a helix and tied off
    as a Klemheist (the top tail runs down over the wraps through the bottom eye), its sewn loop through the
    top slot of an aluminium rigging plate; the same carabiners, descender and rope as option A, turned so the
    rope hangs in the plane of the plate."""
    r = (trunk_d or P["trunk_d"]) / 2
    n, pitch = P["wrap_turns"], P["wrap_pitch"]
    ww, wt = P["webbing"]
    mt = P["mat_t"]
    H = n * pitch
    out = []
    # rubber bark mat: a slit sleeve under the wraps
    z0m, z1m = -ww / 2 - 15, H + ww / 2 + 15
    mat = Pos(0, 0, (z0m + z1m) / 2) * (Cylinder(r + mt, z1m - z0m) - Cylinder(r, z1m - z0m))
    mat = mat - Pos(r + mt, 0, (z0m + z1m) / 2) * Box(30, 20, z1m - z0m + 2)
    out.append(cp.part("Rubber bark mat, 3 mm, slit sleeve", cp.break_edges(mat, 0.8), "epdm", explode=(-200, 0, 0)))
    # strap: helix of n turns at the mid-plane of the webbing
    rh = r + mt + wt / 2
    hx = Helix(pitch, H, rh)
    pl = Plane(origin=hx.position_at(0), z_dir=hx.tangent_at(0), x_dir=(1, 0, 0))
    wrap = sweep(pl * Rectangle(wt, ww), hx, is_frenet=True)
    xt = r + mt + wt + 0.3                       # inner face of the top tail lying over the wraps
    zt0, zt1 = -70.0, H + ww / 2
    tail1 = Pos(xt + 1.1, 0, (zt0 + zt1) / 2) * Box(2.2, ww, zt1 - zt0)
    pw, pt_, ph = P["rig_plate"]
    xp = r + 32.0                                # mid-plane of the rigging plate and of the rope
    zp = P["rig_top"]
    a0, a1 = (xt + 1.1, 0.0, zt0), (xp, 0.0, zp + 1.3)
    d = (a1[0] - a0[0], 0.0, a1[2] - a0[2])
    tail2 = Location(Plane(origin=((a0[0] + a1[0]) / 2, 0, (a0[2] + a1[2]) / 2), x_dir=(0, 1, 0), z_dir=d)) * Box(ww, 2.2, math.hypot(d[0], d[2]) + 2.0)
    eye = (Pos(xt + 1.1, 0, -50) * Box(2.2 + 4.4, ww + 4.4, 18)) - (Pos(xt + 1.1, 0, -50) * Box(2.4, ww + 0.4, 20))
    bridge_lo = zp - 12.0
    xo0, xo1 = xp - pt_ / 2 - 2.4, xp + pt_ / 2 + 2.4
    loop = (Pos(xp, 0, (bridge_lo - 2.4 + zp + 2.4) / 2) * Box(xo1 - xo0, ww, zp + 2.4 - (bridge_lo - 2.4))) - \
        (Pos(xp, 0, (bridge_lo - 0.2 + zp + 0.2) / 2) * Box(pt_ + 0.4, ww + 2, zp + 0.2 - (bridge_lo - 0.2)))
    strap = wrap + tail1 + tail2 + eye + loop
    out.append(cp.part("Anchor strap, 45 mm polyester webbing, sewn loop, Klemheist", strap, "canvas", kind="bought", explode=(-120, 0, 0)))
    # rigging plate in the YZ plane: top slot for the strap loop, load and brake holes below
    hz = zp - ph + 30.0
    hsep = P["rig_holes"]
    plate = Pos(xp, 0, zp - ph / 2) * Box(pt_, pw, ph)
    try:
        plate = plate.fillet(12.0, plate.edges().filter_by(lambda e: abs(e.tangent_at(0.5).X) > 0.9))
    except Exception:
        pass
    plate = plate - Pos(xp, 0, zp - 18.0) * Box(pt_ + 2, 50.0, 12.0)
    for y in (hsep / 2, -hsep / 2):
        plate = plate - rod((xp - 20, y, hz), (xp + 20, y, hz), P["eye_d"] / 2)
    out.append(cp.part("Rigging plate, aluminium, 3 holes and a strap slot", cp.break_edges(plate, 0.6), _AL, kind="bought", explode=(150, 0, -150)))
    # lowering set built in option A's frame (hole axes along Y, brake on -X), then turned 90 deg about Z
    off = P["eye_d"] / 2 - P["carab"][0] / 2
    lift = tk.bend_drop(P, pt_ / 2) + 0.05
    ls, _ = tk.lowering_set(P, (hsep / 2, 0.0, hz - off + lift), (-hsep / 2, 0.0, hz - off + lift), load_end_z=-900.0)
    T = Pos(xp, 0, 0) * Rot(0, 0, 90)
    for q in ls:
        q["shape"] = T * q["shape"]
        out.append(q)
    out.append(_trunk_part(P, r))
    return out


def _saddle(P, D):
    """Folded V saddle of 6 mm plate, frame-local (virtual vertex at the origin, faces as option A's pads)."""
    L, t, h = P["saddle"]
    w, b = D["w"], D["b"]
    wm, bm = (w[0], -w[1]), (b[0], -b[1])
    p1 = (w[0] * L, w[1] * L)
    p3 = (wm[0] * L, wm[1] * L)
    p4 = (p3[0] + bm[0] * t, p3[1] + bm[1] * t)
    p5 = (t / b[0], 0.0)                              # the ridge: both back faces meet on the centre plane
    p6 = (p1[0] + b[0] * t, p1[1] + b[1] * t)
    poly = Polyline((p1[0], p1[1], 0), (0, 0, 0), (p3[0], p3[1], 0), (p4[0], p4[1], 0), (p5[0], p5[1], 0), (p6[0], p6[1], 0), close=True)
    v = extrude(make_face(poly), amount=h)
    try:
        v = v.fillet(4.0, v.edges().filter_by(lambda e: abs(e.tangent_at(0.5).Z) > 0.9 and abs(e.center().Y) < 1e-3))
    except Exception:
        pass
    return v, p5[0]


def option_c(P=PARAMS, trunk_d=None):
    """Option C, the screwed stem anchor: a folded 6 mm steel V saddle (the same 120 deg V as option A) held
    by four M10 x 120 coach screws with washers driven into the stem, a 10 mm eye lug welded to the ridge
    with two fillet welds; the same carabiners, descender and rope as option A."""
    D = derived(P, trunk_d)
    mv = lambda s: Pos(D["q0"], 0, 0) * s
    L, t, h = P["saddle"]
    sd, sl, su, szs = P["saddle_screw"]
    v, xr = _saddle(P, D)
    out = []
    fix = []
    for s in (1, -1):
        w = (D["w"][0], s * D["w"][1], 0.0)
        b = (D["b"][0], s * D["b"][1], 0.0)
        for zz in (szs if s > 0 else tuple(z + 30.0 for z in szs)):      # staggered: the screws must not meet in the stem
            pt = (w[0] * su + b[0] * t, w[1] * su + b[1] * t, zz)
            v = v - tk.rod((pt[0] - b[0] * 20, pt[1] - b[1] * 20, zz), (pt[0] + b[0] * 5, pt[1] + b[1] * 5, zz), (sd + 1) / 2)
            fix.append((s, zz, pt, b))
    out.append(cp.part("Saddle, folded 6 mm steel V, galvanised", mv(cp.break_edges(v, 0.8)), "galvanised", explode=(-120, 0, 0)))
    lt, lm, ls_, lz = P["lug"]
    x0 = xr - 3.5
    prof = [(x0, 0), (xr + 150, 0), (xr + 150, 80), (x0, 190)]
    lug = extrude(make_face(Polyline(*[(x, 0, z) for x, z in prof], close=True)), amount=lt / 2, both=True)
    lug = Pos(0, 0, 5) * lug
    lug = lug - v
    for xx in (lm, ls_):
        lug = lug - rod((xr + xx, -20, 5 + lz), (xr + xx, 20, 5 + lz), P["eye_d"] / 2)
    lug = cp.break_edges(lug, 0.6)
    out.append(cp.part("Eye lug, 10 mm steel plate, galvanised", mv(lug), "galvanised", explode=(150, 0, 0)))
    bx_, by_ = D["b"][0], D["b"][1]
    xw = (t - (lt / 2) * by_) / bx_
    for s in (1, -1):
        bd = tk.bead((xw, s * lt / 2, 6.0), (xw, s * lt / 2, 6.0 + 180.0), (0, s, 0), (bx_, s * by_, 0), 3.0)
        bd = bd & Pos(0, 0, h / 2) * Box(2000, 2000, h - 1)
        out.append(cp.part(f"Weld, eye lug to saddle {'right' if s > 0 else 'left'}", mv(bd), "galvanised", kind="weld", explode=(150, 0, 0)))
    for i, (s, zz, pt, b) in enumerate(fix, 1):
        loc = Location(Plane(origin=pt, z_dir=b))
        out.append(cp.part(f"Coach screw {i}, M{sd} x {sl}, DIN 571, galvanised", mv(Location(Plane(origin=(pt[0] + b[0] * cp.ISO[sd][4], pt[1] + b[1] * cp.ISO[sd][4], zz), z_dir=b)) * cp.coach_screw(sd, sl)),
                           "galvanised", kind="fastener", explode=(-200, 0, 0)))
        out.append(cp.part(f"Washer {i}, M{sd}, ISO 7089", mv(loc * cp.washer(sd)), "galvanised", kind="fastener", explode=(-160, 0, 0)))
    off = P["eye_d"] / 2 - P["carab"][0] / 2
    lift = tk.bend_drop(P, lt / 2) + 0.05
    xq = D["q0"] + xr
    ls, _ = tk.lowering_set(P, (xq + lm, 0.0, 5 + lz - off + lift), (xq + ls_, 0.0, 5 + lz - off + lift))
    out += ls
    out.append(_trunk_part(P, D["r"]))
    return out


def components(option=CHOSEN):
    """kit 1.9: every part of one concept option as cad_parts.part() dicts, fitted to the reference 300 mm trunk."""
    return {"A": option_a, "B": option_b, "C": option_c}[option]()


if __name__ == "__main__":
    D = derived()
    print(f"trunk {PARAMS['trunk_d']:.0f} mm: vertex {D['q0']:.1f} mm out, load line {D['e_main']:.1f} mm from the axis, "
          f"chain centre {D['z_c']:.1f} mm up; loop {loop_length():.0f} mm")
    for d in (200, 300, 450):
        print(f"  loop length on a {d} mm trunk: {loop_length(trunk_d=d):.0f} mm")
    res = all_checks()
    if "--check" not in sys.argv:
        export()
    if not all(ok for ok, _ in res):
        sys.exit(1)
