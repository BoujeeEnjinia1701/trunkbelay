"""TrunkBelay repo-specific CAD helpers for the kit 1.9 model (cad/src/model.py), detail level D3.

Kept here, not in .kit/, because they describe this kit's bought rescue hardware and its weld beads:

    bead(p0, p1, n1, n2, r)        fillet weld bead along a corner line, tangent to both faces
    ring_bead(c, axis, ro, r)      fillet weld bead round a ring welded flat on a plate
    carabiner_d3(...)              locking carabiner: body, gate, locking sleeve and gate rivet
    descender_d3(...)              auto-locking descender: two side plates, cam, handle, axle bolt set,
                                   handle pivot and two spacer rivets, at the catalogue envelope
    lowering_set(P, top_m, top_s)  load carabiner, descender, brake carabiner and both rope strands, from
                                   the two attachment points (the same geometry as model.load_side)

Coordinates in mm. PRELIMINARY, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math

from build123d import Box, Cylinder, Location, Plane, Pos, Rot, Solid, Torus

import cad_parts as cp


def _v(a):
    return tuple(float(x) for x in a)


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


def rod(p0, p1, r, r_in=0.0):
    """Solid cylinder (or tube) between two points."""
    d = _sub(p1, p0)
    L = math.sqrt(_dot(d, d))
    pl = Plane(origin=_v(p0), z_dir=_norm(d))
    s = Solid.make_cylinder(r, L, pl)
    if r_in > 0:
        s = s - Solid.make_cylinder(r_in, L, pl)
    return s


def bead(p0, p1, n1, n2, r):
    """Fillet weld bead along the corner line p0 to p1. n1 and n2 are the unit normals of the two faces,
    pointing into the open corner (away from the metal). The bead is a round of radius r tangent to both
    faces, so it touches the parts and does not overlap them."""
    n1, n2 = _norm(n1), _norm(n2)
    phi = math.pi - math.acos(max(-1.0, min(1.0, _dot(n1, n2))))      # opening angle of the corner
    bis = _norm(_add(n1, n2))
    off = _mul(bis, r / math.sin(phi / 2) + 0.02)
    return rod(_add(p0, off), _add(p1, off), r)


def ring_bead(c, axis, ro, r):
    """Fillet weld bead round the outside of a ring (outer radius ro) welded flat on a plate; c is the centre
    of the ring face on the plate and axis points from the plate into the ring."""
    axis = _norm(axis)
    cc = _add(c, _mul(axis, r + 0.02))
    return Location(Plane(origin=_v(cc), z_dir=axis)) * Torus(ro + r + 0.02, r)


def place(shape, center, axis, normal):
    """Move a template (long axis X, ring plane XY, normal Z) to center, long axis along axis."""
    return Location(Plane(origin=_v(center), x_dir=_norm(axis), z_dir=_norm(normal))) * shape


def _stadium(straight, bend_r, wire_r):
    half = Box(2 * (bend_r + wire_r) + 2, 2 * (bend_r + wire_r) + 2, 2 * wire_r + 2)
    out = None
    for sgn in (1, -1):
        cut = Pos(sgn * (bend_r + wire_r + 1), 0, 0) * half
        e = Pos(sgn * straight / 2, 0, 0) * (Torus(bend_r, wire_r) & cut)
        out = e if out is None else out + e
    for s in (1, -1):
        out = out + rod((-straight / 2, s * bend_r, 0), (straight / 2, s * bend_r, 0), wire_r)
    return out


def carabiner_d3(P, top, normal=(1, 0, 0), label="Load carabiner", bom=16, explode=(0, 0, 0)):
    """Locking carabiner, D3: the body (a stadium of 10 mm bar with the gate opening cut out of one long
    side), the gate, the screw-lock sleeve on the gate and the gate pivot rivet in holes through the body
    and the gate. top is the centre of the top bar (as model.carabiner); long axis Z."""
    d, st, br = P["carab"]
    r = d / 2
    body = _stadium(st, br, r)
    xh, xn = -st / 2 + 6.0, st / 2 - 6.0                 # hinge and nose ends of the gate opening
    body = body - Pos((xh + xn) / 2, br, 0) * Box(xn - xh, 2 * r + 2, 2 * r + 2)
    gate = rod((xh - 4.5, br, 0), (xn - 0.4, br, 0), r * 0.85)        # the heel (first 4.9 mm) sits in a slot in the body
    sleeve = rod((xn - 20.0, br, 0), (xn - 2.0, br, 0), r * 0.85 + 1.6, r * 0.85)
    rv = rod((xh - 2.5, br, -r - 0.6), (xh - 2.5, br, r + 0.6), 1.4)
    slot = Pos(xh - 2.0, br, 0) * Box(5.0, 2 * r * 0.85 + 0.4, 2 * r * 0.85 + 0.4)
    body = (body - slot) - rv
    gate = gate - rv
    c = (top[0], top[1], top[2] - br - st / 2)
    mv = lambda s: place(s, c, (0, 0, 1), normal)
    al = "aluminium"
    return [
        cp.part(f"{label}, body (EN 362 class B, aluminium)", mv(body), al, kind="bought", bom=bom, explode=explode),
        cp.part(f"{label}, gate", mv(gate), al, kind="bought", bom=bom, explode=explode),
        cp.part(f"{label}, screw-lock sleeve", mv(sleeve), al, kind="bought", bom=bom, explode=explode),
        cp.part(f"{label}, gate rivet", mv(rv), "stainless", kind="fastener", explode=explode),
    ]


def bend_drop(P, y):
    """How far the carabiner's crown must sit back from the edge of an eye or hole so that its end bend
    (centre-line radius br, bar radius d / 2) clears the edge over a plate half-thickness y: off the centre
    plane the bend reaches nearer the edge and its section is an ellipse."""
    d, st, br = P["carab"]
    wr = d / 2
    worst = 0.0
    for i in range(41):
        yy = y * i / 40
        c = math.sqrt(br * br - yy * yy)
        worst = max(worst, (br - c) + wr * br / c - wr)
    return worst


def carab_bottom(P, top):
    d, st, br = P["carab"]
    return (top[0], top[1], top[2] - st - 2 * br)


def descender_d3(P, cb, hole_z, bom=17, explode=(0, 0, 0)):
    """Auto-locking descender at the catalogue envelope of the BOM class (75 x 38 x 150 mm), D3: two 4 mm side
    plates with the attachment hole, the cam between them, the handle, an M6 axle bolt set through the plates
    and the cam, the handle pivot pin and two spacer rivets. Built in the frame of model.load_side: the
    attachment hole axis along Y at (cb[0], hole_z), the rope channel between the plates at y = 0."""
    dx, dy, dz = P["desc"]
    x0 = cb[0]
    zt = hole_z + 15.0
    zb = zt - dz
    gap, t = 7.6, 4.0                                      # half-width of the rope channel, plate thickness
    holes = [((x0, hole_z), 9.0), ((x0 - 8.0, hole_z - 60.0), 3.1), ((x0 + 31.0, hole_z - 24.0), 2.6),
             ((x0 - 22.0, zb + 22.0), 2.6), ((x0 + 24.0, zb + 40.0), 2.6)]

    def plate(sgn):
        y0 = sgn * (gap + t / 2)
        pl = Pos(x0, y0, (zt + zb) / 2) * Box(dx, t, dz)
        try:
            pl = pl.fillet(7.0, pl.edges().filter_by(lambda e: abs(e.tangent_at(0.5).Y) > 0.9))
        except Exception:
            pass
        for (hx, hz), hr in holes:
            pl = pl - rod((hx, -30, hz), (hx, 30, hz), hr)
        return cp.break_edges(pl, 0.6)

    cam = rod((x0 - 8.0, -gap + 0.6, hole_z - 60.0), (x0 - 8.0, gap - 0.6, hole_z - 60.0), 16.0)
    cam = cam - Pos(x0 - 8.0 + 24.0, 0, hole_z - 60.0) * Box(20.0, 30.0, 40.0)    # flat brake face of the cam
    cam = cam - rod((x0 - 8.0, -30, hole_z - 60.0), (x0 - 8.0, 30, hole_z - 60.0), 3.1)
    handle = rod((x0 + dx / 2 - 10, 0, hole_z - 25), (x0 + dx / 2 + 85, 0, hole_z + 5), 7.0)
    handle = handle - rod((x0 + 31.0, -30, hole_z - 24.0), (x0 + 31.0, 30, hole_z - 24.0), 2.6)
    h0, h1 = (x0 + dx / 2 - 10, hole_z - 25), (x0 + dx / 2 + 85, hole_z + 5)
    f = 0.45
    grip = rod((h0[0] + f * (h1[0] - h0[0]), 0, h0[1] + f * (h1[1] - h0[1])), (h1[0], 0, h1[1]), 9.0, 7.0)
    out = [
        cp.part("Descender, fixed side plate", plate(-1), "aluminium", kind="bought", bom=bom, explode=explode),
        cp.part("Descender, moving side plate", plate(1), "aluminium", kind="bought", bom=bom, explode=explode),
        cp.part("Descender, cam", cam, "stainless", kind="bought", bom=bom, explode=explode),
        cp.part("Descender, handle", handle, "aluminium", kind="bought", bom=bom, explode=explode),
        cp.part("Descender, handle grip", grip, "matte_black", kind="bought", bom=bom, explode=explode),
    ]
    # M6 axle bolt set through both plates and the cam, along Y (grip = the plate pack)
    grip_t = 2 * (gap + t)
    axle = Location(Plane(origin=(x0 - 8.0, gap + t, hole_z - 60.0), z_dir=(0, 1, 0)))
    for nm, sh in cp.hex_bolt_set(6, grip_t):
        out.append(cp.part(f"Descender axle, {nm}", axle * sh, "stainless", kind="fastener", explode=explode))
    for nm, (hx, hz) in (("handle pivot pin", (x0 + 31.0, hole_z - 24.0)), ("spacer rivet, rear", (x0 - 22.0, zb + 22.0)),
                         ("spacer rivet, front", (x0 + 24.0, zb + 40.0))):
        pin = rod((hx, -(gap + t + 0.8), hz), (hx, gap + t + 0.8, hz), 2.6)
        head = rod((hx, -(gap + t + 1.6), hz), (hx, -(gap + t), hz), 4.0) + rod((hx, gap + t, hz), (hx, gap + t + 1.6, hz), 4.0)
        out.append(cp.part(f"Descender {nm}", pin + head, "stainless", kind="fastener", explode=explode))
    return out


def lowering_set(P, top_m, top_s, load_end_z=None, explode=True):
    """Load carabiner at top_m, the descender hanging from it, the brake carabiner at top_s and the two rope
    strands: the brake strand leaves the side of the descender, turns 180 deg over the brake carabiner's
    bottom bar and runs down to the rope bag; the load strand runs down to the victim. The same geometry as
    model.load_side, for any pair of attachment points with top_s on the -X side of top_m."""
    end_z = P["load_end_z"] if load_end_z is None else load_end_z
    out = carabiner_d3(P, top_m, label="Load carabiner", explode=(300, 0, -150) if explode else (0, 0, 0))
    dx, dy, dz = P["desc"]
    cb = carab_bottom(P, top_m)
    # the descender's hole bears on the carabiner's bottom bend at the outer faces of its plates
    hole_z = cb[2] + P["carab"][0] / 2 - 9.0 + bend_drop(P, 7.6 + 4.0) + 0.1
    out += descender_d3(P, cb, hole_z, explode=(420, 0, -260) if explode else (0, 0, 0))
    d_bot = hole_z + 15 - dz
    out += carabiner_d3(P, top_s, label="Brake carabiner", explode=(200, 0, -300) if explode else (0, 0, 0))
    cbs = carab_bottom(P, top_s)
    rr = P["rope_d"] / 2
    R = P["carab"][0] / 2 + rr
    xl = cb[0] + P["strand_dx"][1]
    side = (cb[0] - dx / 2, cb[1], hole_z - 55)
    up = (cbs[0] + R, cbs[1], cbs[2])
    down = (cbs[0] - R, cbs[1], cbs[2])
    half = (Pos(cbs[0], cbs[1], cbs[2]) * Rot(90, 0, 0) * Torus(R, rr)) & (Pos(cbs[0], cbs[1], cbs[2] + 50) * Box(100, 100, 100))
    brake = rod(side, up, rr) + half + rod(down, (down[0], down[1], end_z), rr)
    # the load strand hangs straight, then kinks a little where the victim's weight swings it off the trunk
    load = cp.rope([(xl, cb[1], d_bot + 10), (xl, cb[1], end_z + 120.0), (xl + 12.0, cb[1], end_z)], P["rope_d"])
    out.append(cp.part("Lowering rope, brake strand (11 mm, EN 1891 type A)", brake, "rope", kind="bought", bom=18, explode=(200, 0, -500) if explode else (0, 0, 0)))
    out.append(cp.part("Lowering rope, load strand to the victim", load, "rope", kind="bought", bom=18, explode=(500, 0, -500) if explode else (0, 0, 0)))
    return out, dict(cb=cb, hole_z=hole_z, d_bot=d_bot, xb_strand=down[0], xl_strand=xl)
