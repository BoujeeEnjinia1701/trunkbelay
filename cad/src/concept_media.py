"""TrunkBelay concept media (TRL 3, constructable design of TKB-DDR-002), generated from the parametric model.

Run from the repo root:  python cad/src/concept_media.py
Takes the collar, chain and lowering parts from cad/src/model.py as fitted to a 300 mm palm trunk and
renders the media set with .kit/concept.py: media/hero.png, media/exploded.png, media/flow.png,
media/concept-blueprint.png and .pdf (TKB-DWG-010), media/model.glb and media/viewer.html. Every
coloured part carries the BOM line number used in bom/bom.csv. Grey context (the trunk and the
rescuer's forearm on the brake strand) has no BOM number. The chain is drawn as its 20 mm envelope here;
the build plan pictures and the product renders show the links. Figures on the sheet and in the flow
diagram come from docs/04-calcs/sizing.py (TKB-CAL-001). CONCEPT, NOT FOR FABRICATION.
"""
import functools
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build123d as bd  # noqa: E402
from build123d import Pos, Rot  # noqa: E402
from concept import Part, render_all  # noqa: E402
from context_parts import forearm_hand  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
C = M.build_components(P)
D = C["_D"]
LOOP, TA, TB = M.chain_envelope(P, D)     # the chain drawn as its envelope: the concept sheet's hidden-line views stay quick


def hand_on_brake_strand(z=-380.0):
    """Left forearm and hand gripping the brake strand from the far (+Y) side of the frame."""
    from build123d import Location, Vector
    turn = Rot(0, 0, -90) * Rot(90, 0, 0)      # grip axis from Y to Z (vertical rope), hand pointing -Y
    h = turn * forearm_hand(side="left", pose="grip", grip_d=20.0)
    g = (turn * Location(Vector(92, 0, -27))).position
    return Pos(D["xb_strand"] - g.X, 0.0 - g.Y, z - g.Z) * h


def fuse(*keys):
    s = None
    for k in keys:
        s = C[k] if s is None else s + C[k]
    return s


def parts():
    return [
        Part("Spine plate", C["spine"], "#0F766E", 1, (120, 0, 0)),
        Part("Bearing bars (2)", C["bars"], "#64748B", 2, (-60, 0, -120)),
        Part("Eye doubler rings (4)", C["doublers"], "#1D4ED8", 3, (120, 0, -120)),
        Part("Cleat cheeks (2)", C["cheeks"], "#7C3AED", 4, (120, 0, 120)),
        Part("Rubber bark pads (2)", C["pads"], "#111827", 6, (-140, 0, -120)),
        Part("Keeper", C["keeper"], "#B45309", 9, (120, 0, 260)),
        Part("Lock pin", C["pin"], "#DC2626", 10, (120, -160, 200)),
        Part("Chain, grade 80, 6 mm (envelope)", LOOP + TA + TB, "#57534E", 11, (-200, 0, 150)),
        Part("Chain sleeve", C["sleeve"], "#EAB308", 15, (-350, 0, 150)),
        Part("Tether quick link", C["maillon"], "#A16207", 14, (120, 120, -200)),
        Part("Carabiners (load, brake)", fuse("carab_main", "carab_brake"), "#C2410C", 16, (300, 0, -150)),
        Part("Auto-locking descender", C["descender"], "#15803D", 17, (420, 0, -260)),
        Part("Lowering rope, 11 mm", fuse("rope_brake", "rope_load"), "#0E7490", 18, (420, 0, -420)),
    ]


context = [
    Part("Palm trunk, 300 mm (site)", M.trunk(P, None, -720, 420), "#D1D5DB"),
    Part("Rescuer's hand on the brake strand (scale)", hand_on_brake_strand(), "#9CA3AF"),
]

if __name__ == "__main__":
    fine = bd.export_gltf
    bd.export_gltf = functools.partial(fine, linear_deflection=1.0, angular_deflection=0.35)
    try:
        render_all(
            parts(), project="TrunkBelay", title="Palm trunk rescue collar and lowering kit", dwg_no="TKB-DWG-010",
            key_figures=["Steel collar frame: 5 mm spine, two rubber-faced bars in a 120 deg V",
                         "Grade 80 chain, 6 mm, wraps the trunk once; two-slot cleat, keeper and ball-lock pin",
                         "Fits trunks 200 to 450 mm across with no tools",
                         "Load eye 150 mm out: the frame cocks and grips; locking factor 1.54 or more (estimate)",
                         "Held 2.5 kN (R1 load) on paper; bars at 2.1 times yield",
                         "Auto-locking descender, 30 m of 11 mm rope; brake hand about 80 N for 100 kg",
                         "Kit 8.9 kg; about USD 758 (estimate)"],
            cut=False, scale_figure=False, context=context,
            flow={"title": "energy turned to heat lowering a 100 kg person 25 m, kJ (TKB-CAL-001 estimates)",
                  "unit": "kJ",
                  "stages": [("Person lowered 25 m", 24.8), ("Left after the descender", 3.7), ("Held by the brake hand", 2.0)],
                  "losses": [(0, "Heat in the descender (85 %)", 21.1), (1, "Heat in the brake carabiner (7 %)", 1.7)]},
        )
    finally:
        bd.export_gltf = fine
    print("wrote media/hero.png, exploded.png, flow.png, concept-blueprint.png and .pdf, model.glb, viewer.html")
