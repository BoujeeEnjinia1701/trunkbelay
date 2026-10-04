"""TrunkBelay general arrangement drawing TKB-DWG-001 (Rev P2).

Run from the repo root:  python cad/src/sheets.py
Builds cad/drawings/TKB-DWG-001.svg, .pdf and .png from the parametric model: the collar frame, pads,
chain (drawn as its envelope so the hidden-line views stay quick), sleeve, keeper and pin, carabiners,
descender and the top of the rope, fitted to a 300 mm palm trunk (a short trunk section is drawn for
reference). The concept sheet in media/ uses TKB-DWG-010. Figures in the notes come from TKB-CAL-001
(python docs/04-calcs/sizing.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(Path(__file__).resolve().parent)]
from build123d import Compound, Pos, Box  # noqa: E402
from drawing import Sheet, project_views  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
D = M.derived(P)
F = {k: Pos(D["q0"], 0, 0) * v for k, v in M.frame_parts(P, D).items()}
CP = M.chain_parts(P, D)                  # also fills D with the tail length
loop, ta, tb = M.chain_envelope(P, D)
L = M.load_side(P, D)
cut = Pos(0, 0, -200) * Box(2000, 2000, 400)          # keep the rope down to 400 mm below the frame foot
rope = (L["rope_brake"] + L["rope_load"]) & cut
tb = tb & Pos(0, 0, -150) * Box(2000, 2000, 500)
trunk = M.trunk(P, None, -400, 320)
asm = Compound([F["spine"], F["bars"], F["doublers"], F["cheeks"], F["pads"], F["keeper"], F["pin"],
                loop, ta, tb, CP["sleeve"], M.maillon(P, D), L["carab_main"], L["carab_brake"], L["descender"], rope, trunk])

work = ROOT / "cad/drawings/_views"
views = project_views(asm, work)
s = Sheet(project="TrunkBelay", title="Palm trunk rescue collar and lowering kit: general arrangement",
          dwg_no="TKB-DWG-001", rev="P2", author="Amish Chadha", date="2026-10-03", concept=True, scale=None,
          material="6082-T6 aluminium plate and RHS, TIG welded; rubber pads; grade 80 chain. See bom/bom.csv",
          revisions=[("P1", "Preliminary GA from the constructable TRL 3 model (TKB-DDR-002)", "2026-10-03", "AC"),
                     ("P2", "Aluminium frame and tag line (TKB-DDR-003)", "2026-10-03", "AC")])
s.add_ortho(views, ["front", "top", "right"])
s.add_svg(views["iso"], 276, 57, 140, 62, label="Isometric view",
          sublabel="Seen from the front right, above; 300 mm trunk section for reference")
s.add_notes("Key dimensions (mm) and data", [
    f"Fits trunks {P['trunk_range'][0]:.0f} to {P['trunk_range'][1]:.0f} across; drawn on a {P['trunk_d']:.0f} trunk",
    f"Spine {P['spine_t']:.0f} aluminium plate, {P['spine_pts'][1][0]:.0f} long x {P['spine_pts'][-1][1]:.0f} high",
    f"Bearing bars RHS {P['bar'][0]:.0f} x {P['bar'][1]:.0f} x {P['bar'][2]:.0f} in a 120 deg V",
    f"Rubber pads {P['pad'][0]:.0f} x {P['pad'][2]:.0f} x {P['pad'][1]:.0f}",
    f"Load eye {P['eye_main'][0]:.0f} out from the spine front edge, {P['eye_main'][1]:.0f} up",
    f"Chain line {D['z_c']:.0f} above the frame foot; slots {P['slot_w']} wide",
    "Chain 6 mm grade 80, 110 links; sleeve 600 tubular webbing",
    f"Cheeks {P['cheek'][1]:.0f}; keeper 3 steel; ball-lock pin 8, grip 27",
    "Locking factor 1.54 or more (TKB-CAL-001, B4)",
    "Sized for 2.5 kN static (R1); one person, 100 kg",
    "Carried 4.55 kg; bag hauled on the tag line",
    "PRELIMINARY, NOT FOR FABRICATION",
], x=276, y=130, width=140)
s.save(ROOT / "cad/drawings/TKB-DWG-001")
shutil.rmtree(work, ignore_errors=True)
print("wrote cad/drawings/TKB-DWG-001.svg, .pdf, .png")
