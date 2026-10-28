"""TrunkBelay product appearance model for photoreal renders (STANDARDS sections 12 and 24), TRL 3, kit 1.9.

Every product part is components(CHOSEN) from cad/src/model.py as it is, at detail level D3: the spine plate,
bearing bars, rubber pads with their countersunk screws and rivet nuts, eye doubler rings, cleat cheeks, every
weld bead, keeper and lock pin, the 110-link chain with its sleeve, tether link, connecting link and master link,
the load and brake carabiners (body, gate, sleeve, rivet), the descender (plates, cam, handle, axle bolt set,
rivets) and the rope, fitted to the reference 300 mm palm trunk. The whole model is lifted so that ground level
is z = 0 and the collar's foot is 1.4 m up: the low-height drill of the build plan's first checks (TKB-BLD-001).
Only the look and the site are added, as recorded in docs/REVIEW.md: a safe working load label on the spine,
both rope strands carried on down to the rope bag on the ground, the palm trunk and two more palms behind, all
reaching below the ground, and a 1.75 m helper standing on the ground for scale.
APPEARANCE MODEL ONLY. CONCEPT, NOT FOR FABRICATION.

Groups: "shell" (collar, chain and their fixings), "internal" (carabiners, descender, rope, bag), "context"
(site and the helper).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Cylinder, Pos, Rot  # noqa: E402
import model as M  # noqa: E402
import tkb_parts as tk  # noqa: E402
from cad_parts import part, break_edges, label_plate, rope  # noqa: E402

TITLE = "TrunkBelay: palm trunk rescue collar and lowering kit"
LIFT = -M.PARAMS["ground_z"]            # 1400 mm: model z = 0 (the collar foot) becomes 1.4 m above the ground

_SITE = ["--scene=outdoor", "--ground=soil", "--ground-z=0", "--sun=48,-75", "--lens=50"]
RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "internal", "context"], "explode": False, "el": 12, "az": -40, "args": _SITE,
     "note": "Site render in a coconut plantation, from the front right and a little above (about 12 deg elevation): the collar "
             "on a 300 mm palm at drill height (foot 1.4 m up), the descender on the load eye, both rope strands running down "
             "to the rope bag on the ground; a 1.75 m helper standing beside the palm for scale; sun from the camera's side"},
    {"name": "studio", "groups": ["shell", "internal"], "explode": False, "el": 20, "az": -40,
     "note": "Studio render from the front right and above (about 20 deg elevation), trunk hidden: frame weldment with its "
             "weld beads, pads, chain loop and sleeve, keeper and pin, tether link, carabiners, descender and the top of the rope"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 22, "az": -40,
     "note": "Exploded view from the front right and above (about 22 deg elevation): spine plate, bearing bars and pads with "
             "their screws and rivet nuts, eye rings, cleat cheeks, keeper and lock pin, chain, sleeve, tether and connecting "
             "links, master link, carabiners, descender parts and rope; trunk not shown"},
    {"name": "detail", "groups": ["shell"], "explode": False, "el": 35, "az": -125,
     "note": "Detail of the collar from behind and above (about 35 deg elevation), trunk hidden: the two chain links standing in "
             "the slots of the spine top, the cheeks with their weld beads, the keeper over both slots, the ball-lock pin and the "
             "fixed end's tether link at the spine front edge"},
]

_INTERNAL = ("carabiner", "Descender", "rope", "Lowering")


def _lift(s):
    return Pos(0, 0, LIFT) * s


def site():
    """The plantation: the palm the collar is on (300 mm, reaching 0.3 m below the ground and up out of the picture),
    two more palms behind, and the helper on the ground. Ground level is z = 0."""
    out = []
    ctx = lambda n, sh, mat: out.append(part(f"{n} (site)", sh, mat, kind="context", group="context"))
    r = M.PARAMS["trunk_d"] / 2
    ctx("Palm trunk, 300 mm", Pos(0, 0, 2100) * Cylinder(r, 4800), "timber")
    ctx("Palm trunk behind, left", Pos(-2600, 3400, 2100) * Rot(2, -3, 0) * Cylinder(170, 4800), "timber")
    ctx("Palm trunk behind, right", Pos(2900, 4200, 2100) * Rot(-3, 2, 0) * Cylinder(150, 4800), "timber")
    try:
        import context_parts
        man = Pos(700, 850, 0) * Rot(0, 0, 220) * context_parts.mannequin(1750.0, "stand")   # beside the palm, to the right in the hero view
        out.append(part("Helper 1.75 m (scale)", man, "skin", kind="context", group="context"))
    except Exception as e:      # the mannequin is for scale only; never block the product parts
        print("mannequin not added:", e)
    return out


def product_parts():
    parts = [q for q in M.components(M.CHOSEN) if q["kind"] != "context"]
    out = []
    for q in parts:
        d = dict(q)
        d["shape"] = _lift(q["shape"])
        d["group"] = "internal" if any(k in q["name"] for k in _INTERNAL) else "shell"
        out.append(d)
    # safe working load label on the spine's +Y face, between the eyes and the lightening hole
    D = M.build_components(M.PARAMS)["_D"]
    lab = Pos(D["x_s"] + 120, -M.PARAMS["spine_t"] / 2, 66) * label_plate(40, 16, 0.6)
    out.append(dict(part("Safe working load label, one person 100 kg", _lift(lab), "label", kind="bought"), group="shell"))
    # both strands carried on down to the rope bag standing on the ground
    _, info = tk.lowering_set(M.PARAMS, D["carab_main_top"], D["carab_brake_top"])
    end = M.PARAMS["load_end_z"] + LIFT
    bag_c = (info["xl_strand"] - 60.0, 0.0)
    bag_h, bag_d = M.PARAMS["bag"][1], M.PARAMS["bag"][0]
    rd = M.PARAMS["rope_d"]
    for nm, x0 in (("brake", info["xb_strand"]), ("load", info["xl_strand"] + 12.0)):
        pts = [(x0, 0.0, end), (x0, 0.0, end - 150.0), (bag_c[0] + (25 if nm == "load" else -25), 0.0, bag_h + 40.0), (bag_c[0] + (10 if nm == "load" else -10), 0.0, bag_h - 30.0)]
        out.append(dict(part(f"Lowering rope, {nm} strand down to the bag", rope(pts, rd), "rope", kind="bought", bom=18), group="internal"))
    bag = Pos(bag_c[0], 0, bag_h / 2) * Cylinder(bag_d / 2, bag_h)
    bag = break_edges(bag - Pos(bag_c[0], 0, bag_h) * Cylinder(bag_d / 2 - 4, 60), 3.0)
    out.append(dict(part("Rope and carry bag, 35 l, on the ground", bag, "canvas", kind="bought", bom=21), group="internal"))
    return out + site()


if __name__ == "__main__":
    ps = product_parts()
    print(len(ps), "parts;", sum(p["group"] == "shell" for p in ps), "shell,", sum(p["group"] == "internal" for p in ps), "internal,",
          sum(p["group"] == "context" for p in ps), "context")
    for p in ps:
        bb = p["shape"].bounding_box()
        if bb.min.Z < -1 and "(site)" not in p["name"]:
            print("below ground:", p["name"], round(bb.min.Z))
