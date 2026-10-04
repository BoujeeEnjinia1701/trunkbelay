"""TrunkBelay parametric model (build123d), constructable design (TRL 3, TKB-DDR-002; aluminium frame and
tag-line haul from TKB-DDR-003).

Run from the repo root:
    python cad/src/model.py            export STEP and STL, run the constructability checks
    python cad/src/model.py --check    run the constructability checks only

TrunkBelay is a rescue kit that lets a fellow climber anchor and lower a climber stranded on a
coconut palm. A TIG-welded aluminium 6082-T6 collar frame (a 5 mm spine plate with two rubber-faced
bearing bars set in a 120 deg V at its foot) is held on the trunk by a 6 mm grade 80 chain that wraps the trunk
once and sits in two slots cut in the top of the spine (the chain cleat, stiffened by a cheek plate
on each face), held there by a sheet-steel keeper and a ball-lock pin. The fixed end is also tethered
to the spare eye with a quick link. The load
hangs from an eye at the outer end of the spine, 150 mm out from the frame, so the frame cocks on
the trunk: the bearing bars press the bark low on the near side and the chain presses it high on
the far side, and the grip rises with the load. An auto-locking rope descender on the eye lowers
the victim, who is fitted with an evacuation triangle and a chest sling, on 30 m of 11 mm
semi-static rope whose spare end runs down to the rope bag on the ground. The helpers keep the rope bag
on the ground and the rescuer hauls the rope's loop end, with the victim set pre-rigged on the victim
carabiner, up on a 4 mm tag line (TKB-DDR-003). A second (spare) eye takes the brake carabiner and the
tether quick link of the chain's fixed end.

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

from build123d import (Box, Cylinder, Location, Plane, Pos, Rot, Solid, Torus, Compound, Polyline,
                       make_face, extrude, export_step, export_stl)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = {
    "trunk_d": 300.0,            # trunk used for the model and pictures (range 200 to 450, R3)
    "trunk_range": (200.0, 450.0),
    # bearing V
    "v_half": 60.0,              # angle of each pad face from the frame's centre plane, deg (120 deg V)
    "pad": (155.0, 10.0, 50.0),  # rubber pad: length along the face x thickness x height
    "pad_u0": 15.0,              # pad starts this far along the face from the virtual vertex
    "frame_material": "aluminium",   # 6082-T6, TIG welded, not galvanised (TKB-DDR-003, decision 43 C)
    "bar": (70.0, 30.0, 5.0),    # bearing bar RHS: height x depth (away from the trunk) x wall; sized for the
                                 # heat-affected zone at the weld (TKB-CAL-001, C1); depth 30 at most to clear the spare eye ring
    "bar_u1": 172.0,             # outer end of the bar along the face (end cap included)
    "cap_t": 4.0,
    # spine
    "spine_t": 5.0,              # also the web of the chain cleat: 5 mm, not thickened for aluminium, because a link must
                                 # span it (inner length 18 less two wires of up to 6.3 leaves 5.4 mm)
    "spine_set": 8.0,            # spine front edge behind the virtual vertex
    "spine_pts": ((0, 0), (175, 0), (175, 55), (60, 175), (0, 175)),   # x' (from the front edge), z
    "eye_main": (150.0, 28.0), "eye_bag": (70.0, 28.0), "eye_d": 22.0,   # load eye and spare eye
    "doubler": (50.0, 6.0),      # eye doubler ring OD x thickness, one each side of each eye
    "light_hole": (85.0, 90.0, 36.0),   # x', z, diameter
    # chain cleat: two slots in the top of the spine, stiffened by a cheek plate on each face
    "slots": (15.0, 43.0), "slot_w": 7.5, "slot_bottom": 150.0,
    "cheek": (60.0, 8.0, 130.0), # x' length x thickness x bottom z (top level with the spine top)
    "notch": (22.0, 148.0),      # notch in each cheek round each slot: width x bottom z
    "pin_xz": (29.0, 139.0), "pin_d": 8.0, "pin_hole": 8.5,
    "keeper": (56.0, 3.0, 6.0, 132.0),  # bridge length (X) x sheet thickness x leg width x leg bottom z
    "maillon": (8.0, 30.0, 11.0),  # tether quick link: wire x straight x bend radius (centre line)
    # chain, 6 mm grade 80
    "wire": 6.0, "pitch": 18.0, "link_w": 7.8,     # wire dia, inner length, inner width
    "chain_len_links": 110,      # links in the chain, both tails included
    "sleeve": (600.0, 15.0),     # tubular webbing sleeve length x radius on the chain
    "master": (10.0, 80.0, 45.0),   # master link stock x inner length x inner width
    # load side
    "carab": (10.0, 60.0, 20.0), # carabiner bar dia x straight length x bend radius (centreline)
    "desc": (75.0, 38.0, 150.0), # descender body X x Y x Z
    "rope_d": 11.0,
    "strand_dx": (-15.0, 15.0),  # brake and load strand offsets from the descender centre
    "bag": (200.0, 380.0),       # rope and carry bag diameter x height (kit pictures only)
    "load_end_z": -700.0,        # where the load strand is cut off in the pictures (to the victim)
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
    """Two 8 mm cheek plates welded on the faces of the spine top, notched round each slot so the chain
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
    tor = Pos(0, 0, zc) * Torus(R, P["sleeve"][1])
    big = 5 * R
    wedge = extrude(make_face(Polyline((0, 0, 0), (big * COS(s1), big * SIN(s1), 0),
                                       (big * COS((s0 + s1) / 2), big * SIN((s0 + s1) / 2), 0),
                                       (big * COS(s0), big * SIN(s0), 0), close=True)), amount=4 * P["sleeve"][1], both=True)
    sleeve = tor & Pos(0, 0, zc) * wedge
    # tail A (fixed end, +Y side): a flat link in the notch, then links down to the tether quick link
    # in the spare eye, so the fixed end cannot be lost when the keeper is off
    xa = D["x_s"] + P["slots"][0]
    xb = D["x_s"] + P["slots"][1]
    p = P["pitch"]
    tail_a = [place(link, (xa, p - 1.1, zc), (0, 1, 0), (0, 0, 1))]
    mq = maillon_center(P, D)
    a0 = (xa, p + 12.0, zc - 6.0)
    a1 = (mq[0], mq[1] + P["maillon"][2] + 9.0, mq[2])
    La = math.dist(a0, a1)
    na = max(int(round(La / p)), 1)
    ax = _norm(_sub(a1, a0))
    for k in range(na + 1):
        c = _add(a0, _mul(ax, La * k / na))
        normal = _cross(ax, (1, 0, 0)) if k % 2 == 0 else (1, 0, 0)
        tail_a.append(place(link, c, ax, normal))
    # tail B (adjustable end, -Y side): one flat link in the notch, then links hanging down, then a master link
    n_tail = P["chain_len_links"] - n - 1 - (na + 2)
    tail_b = [place(link, (xb, -p + 1.1, zc), (0, -1, 0), (0, 0, 1))]
    hy = -p - 12.0
    z = zc - 6.0
    zs = []
    for k in range(max(n_tail - 1, 0)):
        normal = (1, 0, 0) if k % 2 == 0 else (0, 1, 0)
        tail_b.append(place(link, (xb, hy, z), (0, 0, 1), normal))
        zs.append(z)
        z -= p
    st, ML, MW = P["master"]
    mz_b = (zs[-1] if zs else zc) - 9.0 - st / 2 - ML / 2 + 3.0
    tail_b.append(place(master_template(P), (xb, hy, mz_b), (0, 0, 1), (0, 1, 0) if len(zs) % 2 == 0 else (1, 0, 0)))
    D["n_tail_a"] = na + 2
    D["n_loop_links"] = n + 1
    D["n_tail_b"] = n_tail
    D["loop_len"] = L
    D["tail_b_bottom"] = mz_b - ML / 2 - st
    return {"chain_loop": group(loop_links), "sleeve": sleeve, "chain_tail_a": group(tail_a),
            "chain_tail_b": group(tail_b), "maillon": maillon(P, D)}


def maillon_center(P=PARAMS, D=None):
    """Tether quick link through the spare eye: long axis Z, ring in the YZ plane, top bar on the eye bottom."""
    D = D or derived(P)
    w, st, br = P["maillon"]
    ex, ez = P["eye_bag"]
    dx = -6.0                                      # shares the spare eye with the brake carabiner
    top = ez - math.sqrt((P["eye_d"] / 2 - w / 2) ** 2 - dx ** 2)
    return (D["x_s"] + ex + dx, 0.0, top - br - st / 2)


def maillon(P=PARAMS, D=None):
    w, st, br = P["maillon"]
    return place(stadium(st, br, w / 2), maillon_center(P, D), (0, 0, 1), (1, 0, 0))


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
    tb = rod((xb, 0, zc), (xb, -P["pitch"] - 12, zc), rr) + rod((xb, -P["pitch"] - 12, zc), (xb, -P["pitch"] - 12, D.get("tail_b_bottom", zc - 400)), rr)
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
    top_m = (x0 + ex, 0.0, ez - off)
    out["carab_main"] = carabiner(P, top_m)
    # descender: body in the XZ plane, hole for the carabiner 15 mm below its top
    dx, dy, dz = P["desc"]
    cb = carab_bottom(P, top_m)
    hole_z = cb[2] + P["carab"][0] / 2 - 9.0          # the carabiner bar rests on the top of the 18 mm hole
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
    cdx = 5.0
    top_s = (x0 + sx + cdx, 0.0, sz - math.sqrt((P["eye_d"] / 2 - P["carab"][0] / 2) ** 2 - cdx ** 2))
    out["carab_brake"] = carabiner(P, top_s)
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
    """Victim connector, evacuation triangle and chest sling, laid out flat, with the rope bag, the shoulder
    pouch and the coiled tag line (for the kit pictures)."""
    ox, oy, oz = origin
    tri = extrude(make_face(Polyline((0, 0, 0), (560, 0, 0), (280, 0, -420), close=True)), amount=7, both=True)
    tri = tri - extrude(make_face(Polyline((180, 0, -40), (380, 0, -40), (280, 0, -190), close=True)), amount=10, both=True)
    loops = [Pos(x, 0, z) * Rot(90, 0, 0) * Torus(28, 6) for x, z in ((20, 10), (540, 10), (280, -430))]
    sling = place(stadium(560, 22, 3), (280, 0, 160), (1, 0, 0), (0, 1, 0))
    conn = place(stadium(P["carab"][1], P["carab"][2], P["carab"][0] / 2), (280, 0, 60), (0, 0, 1), (1, 0, 0))
    bag = Pos(900, 0, -P["bag"][1] / 2) * Cylinder(P["bag"][0] / 2, P["bag"][1])
    coil = Pos(900, 0, -P["bag"][1] - 120) * Torus(140, 30)
    spare = place(stadium(P["carab"][1], P["carab"][2], P["carab"][0] / 2), (420, 0, 60), (0, 0, 1), (1, 0, 0))
    pouch = Pos(1250, 0, -150) * Cylinder(80, 300)                 # 10 l shoulder pouch (TKB-DDR-003)
    tag = Pos(1250, 0, -360) * Torus(90, 6)                         # 4 mm tag line, coiled
    S = Pos(ox, oy, oz)
    return {"triangle": S * (tri + fuse_all(loops)), "chest_sling": S * sling, "carab_victim": S * conn,
            "carab_spare": S * spare, "bag": S * bag, "rope_coil": S * coil, "pouch": S * pouch, "tag_line": S * tag}


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
    """Mass in kg of each item (frame parts from volume; bought items from catalogue class)."""
    C = C or build_components(P)
    m = {}
    for k in ("spine", "bars", "doublers", "cheeks"):
        m[k] = C[k].volume * DENSITY[P["frame_material"]]
    for k in ("keeper", "pad_screws"):
        m[k] = C[k].volume * DENSITY["steel"]
    m["pin"] = 0.04                                          # 8 mm stainless ball-lock pin with lanyard
    m["maillon"] = 0.05                                      # 8 mm steel quick link
    m["pads"] = C["pads"].volume * DENSITY["rubber"]
    m["chain"] = P["chain_len_links"] * P["pitch"] / 1000 * 0.80     # 6 mm grade 80, 0.80 kg/m
    m["master_links"] = 2 * 0.11
    m["sleeve"] = P["sleeve"][0] / 1000 * 0.045
    m["carabiners"] = 3 * 0.085                               # aluminium alloy screw-gate, class B (load, brake, victim)
    m["descender"] = 0.53                                     # auto-locking descender class
    m["rope"] = 30 * 0.078                                    # 11 mm EN 1891 type A, 30 m
    m["bag"] = 0.45                                           # rope bag with shoulder straps
    m["triangle"] = 0.75                                      # evacuation triangle class
    m["chest_sling"] = 0.12                                   # 120 cm sewn sling
    m["tag_line"] = 0.30                                      # 30 m of 4 mm accessory cord, about 10 g/m
    m["pouch"] = 0.15                                         # shoulder pouch for the collar, descender and tag line
    return m


CARRIED = ("spine", "bars", "doublers", "cheeks", "keeper", "pad_screws", "pin", "maillon", "pads", "chain",
           "master_links", "sleeve", "descender", "tag_line", "pouch")
"""Items the rescuer carries up the trunk (TKB-DDR-003): the collar, the descender, the load and brake carabiners
(two of the three), the tag line and the pouch. The rope bag, the rope and the victim set (triangle, chest sling and
victim carabiner, pre-rigged on the rope's loop) stay with the helpers and are hauled up on the tag line."""


def carried_mass(m):
    return sum(m[k] for k in CARRIED) + m["carabiners"] * 2 / 3


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
        ("chain_loop", "spine"), ("chain_tail_a", "spine"), ("chain_tail_b", "spine"), ("maillon", "spine"),
        ("maillon", "chain_tail_a"),
        ("carab_main", "doublers"), ("descender", "carab_main"), ("carab_brake", "doublers"),
        ("rope_load", "descender"), ("rope_brake", "descender"), ("rope_brake", "carab_brake"),
    ]
    apart = [
        ("spine", 15), ("bars", 5), ("cheeks", 15), ("keeper", 15), ("pin", 5), ("doublers", 20), ("pad_screws", 2),
        ("maillon", 10),
        ("descender", 50), ("rope_load", 50), ("rope_brake", 30), ("carab_main", 50), ("carab_brake", 20),
        ("chain_tail_a", 10), ("chain_tail_b", 10),
    ]
    pairs_apart = [
        ("chain_tail_b", "doublers", 0.5), ("chain_tail_b", "carab_main", 5), ("chain_tail_b", "keeper", 0.5),
        ("chain_tail_b", "bars", 5), ("chain_tail_b", "descender", 5), ("chain_tail_b", "cheeks", 0.3),
        ("chain_tail_a", "cheeks", 0.3), ("chain_tail_a", "keeper", 0.5), ("chain_tail_a", "doublers", 0.5),
        ("chain_tail_a", "bars", 5), ("chain_loop", "cheeks", 0.3), ("chain_loop", "keeper", 0.5),
        ("chain_loop", "pin", 0.5), ("chain_loop", "bars", 20), ("chain_loop", "pads", 20), ("maillon", "bars", 5),
        ("descender", "spine", 5), ("descender", "doublers", 3), ("pads", "spine", 5),
        ("pin", "chain_tail_a", 0.5), ("pin", "chain_tail_b", 0.5), ("rope_load", "rope_brake", 10),
        ("carab_brake", "maillon", 0.3), ("carab_brake", "chain_tail_a", 0.1), ("carab_brake", "chain_tail_b", 2),
        ("rope_brake", "chain_tail_b", 5), ("rope_brake", "chain_tail_a", 3), ("rope_brake", "spine", 3),
        ("carab_brake", "bars", 5), ("bars", "doublers", 3),
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
        res.append((ov < 1.0 and d >= clr, f"{label}apart  {a:13s} {b:13s} gap {d:6.1f} mm (need {clr:g}), shared {ov:.1f} mm3"))
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


def all_checks(P=PARAMS, verbose=True):
    res = []
    for d in (P["trunk_d"], P["trunk_range"][0], P["trunk_range"][1]):
        res += checks(P, build_components(P, d), verbose, d, label=f"[{d:.0f}] ")
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
