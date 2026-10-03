"""TrunkBelay product appearance model (build123d), TRL 3, constructable design (TKB-DDR-002).

Finished-product look for photoreal renders, built from the constructable model: every component of
cad/src/model.py build_components() is used as it is (spine with its slots and eyes, the two bearing
bars, eye doubler rings, cleat cheeks, rubber pads and screws, keeper and lock pin, the 110-link chain
with its master link, the sleeve, the tether quick link, both carabiners, the descender and the rope),
fitted to a 400 mm palm trunk, inside the 200 to 450 mm range. Only the look is added, as recorded in
docs/REVIEW.md: a safe working load label on the spine, a bark texture band (the trunk is a plain
cylinder with leaf-scar rings), the rope cut 450 mm below the frame foot, and the rescuer's left
forearm and hand (clay) holding the brake strand from the far side, for scale.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: Z up, the trunk axis on Z, the frame on the +X side, its foot at Z = 0.
Groups: "shell" (frame, pads, cleat, chain), "internal" (carabiners, descender, rope),
"context" (trunk, forearm and hand).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Box, Cylinder, Location, Pos, Rot, Torus, Vector  # noqa: E402
import model as M  # noqa: E402

TITLE = "TrunkBelay: palm trunk rescue collar and lowering kit"
TRUNK_D = 400.0
ROPE_CUT = -450.0

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 18, "az": -40,
     "note": "Product render from the front right, about 18 deg above: the collar fitted to a 400 mm palm trunk, "
             "the auto-locking descender on the load eye and the brake strand held by the rescuer's hand, "
             "reaching in from the far side (forearm and hand for scale)"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 22, "az": -40,
     "note": "Exploded view from the front right and above (about 22 deg elevation): spine plate, bearing bars and pads, "
             "eye rings, cleat cheeks, keeper and lock pin, chain and sleeve, tether quick link, carabiners, "
             "descender and rope; trunk not shown"},
    {"name": "detail", "groups": ["shell"], "explode": False, "el": 35, "az": -125,
     "note": "Detail of the collar from behind and above (about 35 deg elevation), trunk hidden: the two chain links "
             "standing in the slots of the spine top, the cheeks, the keeper over both slots and the ball-lock pin"},
]

C_GALV = "#A9B0B8"      # hot-dip galvanised steel
C_ACCENT = "#0F766E"    # teal paint stripe on the keeper and pin lanyard
C_RUBBER = "#1F2328"
C_CHAIN = "#5B6168"
C_SLEEVE = "#E2A90F"
C_ALU = "#C2410C"       # orange anodised carabiners
C_DESC = "#2F7D32"
C_ROPE = "#0E7490"
C_LABEL = "#F4F4F2"
C_BARK = "#8A6F4E"
C_CLAY = "#B9B4AC"

# model key: (display name, colour, material, group, BOM line, explode offset)
LOOK = {
    "spine": ("Spine plate, galvanised steel", C_GALV, "metal", "shell", 1, (150, 0, 0)),
    "bars": ("Bearing bars, galvanised steel", C_GALV, "metal", "shell", 2, (-60, 0, -200)),
    "doublers": ("Eye doubler rings, galvanised", C_GALV, "metal", "shell", 3, (150, 0, -150)),
    "cheeks": ("Cleat cheeks, galvanised", C_GALV, "metal", "shell", 4, (150, 0, 150)),
    "pads": ("Rubber bark pads", C_RUBBER, "rubber", "shell", 6, (-200, 0, -200)),
    "pad_screws": ("Pad screws, stainless", C_GALV, "metal", "shell", 7, (-200, 0, -200)),
    "keeper": ("Keeper, painted steel", C_ACCENT, "painted", "shell", 9, (150, 0, 300)),
    "pin": ("Lock pin, stainless", "#D9DDE1", "metal", "shell", 10, (150, -200, 260)),
    "chain_loop": ("Chain, grade 80, 6 mm", C_CHAIN, "metal", "shell", 11, (-250, 0, 200)),
    "chain_tail_a": ("Chain fixed end", C_CHAIN, "metal", "shell", 11, (150, 150, 0)),
    "chain_tail_b": ("Chain adjustable end with master link", C_CHAIN, "metal", "shell", 11, (150, -200, 0)),
    "sleeve": ("Chain sleeve, tubular webbing", C_SLEEVE, "fabric", "shell", 15, (-400, 0, 200)),
    "maillon": ("Tether quick link, galvanised", C_GALV, "metal", "shell", 14, (150, 200, -250)),
    "carab_main": ("Load carabiner, aluminium", C_ALU, "metal", "internal", 16, (350, 0, -250)),
    "carab_brake": ("Brake carabiner, aluminium", C_ALU, "metal", "internal", 16, (200, 0, -350)),
    "descender": ("Auto-locking descender", C_DESC, "painted", "internal", 17, (500, 0, -350)),
}


def _rope(C):
    keep = Pos(0, 0, (ROPE_CUT + 200) / 2) * Box(3000, 3000, 200 - ROPE_CUT)
    return (C["rope_brake"] & keep), (C["rope_load"] & keep)


def _label(D):
    """Safe working load label on the spine's +Y face, between the eyes and the lightening hole."""
    P = M.PARAMS
    x = D["x_s"] + 112
    return Pos(x, -P["spine_t"] / 2 - 0.4, 62) * Box(44, 0.8, 16)


def _trunk(D):
    r = TRUNK_D / 2
    z0, z1 = -520.0, 420.0
    body = Pos(0, 0, (z0 + z1) / 2) * Cylinder(r, z1 - z0)
    rings = None
    for z in (-430, -250, -70, 330):
        ring = Pos(0, 0, z) * Torus(r, 4.0)
        rings = ring if rings is None else rings + ring
    return body + rings


def _hand(D):
    from context_parts import forearm_hand
    turn = Rot(0, 0, -90) * Rot(90, 0, 0)         # grip axis vertical, hand pointing -Y, forearm toward +Y (the far side)
    h = turn * forearm_hand(side="left", pose="grip", grip_d=20.0)
    g = (turn * Location(Vector(92, 0, -27))).position
    return Pos(D["xb_strand"] - g.X, -g.Y, -300.0 - g.Z) * h


def product_parts(p=M.PARAMS):
    C = M.build_components(p, TRUNK_D)
    D = C["_D"]
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append({"name": name, "shape": shape, "color": color, "material": material, "bom": bom,
                    "group": group, "explode": tuple(explode)})

    for key, (name, color, mat, group, bom, ex) in LOOK.items():
        add(name, C[key], color, mat, bom, group, ex)
    rb, rl = _rope(C)
    add("Lowering rope, brake strand", rb, C_ROPE, "fabric", 18, "internal", (200, 0, -500))
    add("Lowering rope, load strand to the victim", rl, C_ROPE, "fabric", 18, "internal", (500, 0, -500))
    add("Safe working load label, one person 100 kg", _label(D), C_LABEL, "paper", None, "shell", (150, 0, 0))
    add("Palm trunk, 400 mm, bark", _trunk(D), C_BARK, "wood", None, "context")
    add("Rescuer's forearm and hand (scale)", _hand(D), C_CLAY, "clay", None, "context")
    return out


if __name__ == "__main__":
    for q in product_parts():
        s = q["shape"]
        print(f"{q['name']:50s} {q['group']:9s} {q['material']:8s} vol={s.volume / 1000:10.1f} cm3")
