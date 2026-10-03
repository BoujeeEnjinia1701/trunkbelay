"""TrunkBelay prototype build plan pictures (TKB-BLD-001, STANDARDS section 18).

Run from the repo root:
    python cad/src/build_plan_media.py                       everything (heavy: better one group per process)
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py, so the pictures and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/TKB-DWG-101 to 109        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
import model as m  # noqa: E402
from model import PARAMS as P  # noqa: E402
from build123d import Box, Pos, Rot, Compound  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
_C = None

COL = {"spine": "#0F766E", "bars": "#64748B", "doublers": "#1D4ED8", "cheeks": "#7C3AED", "pads": "#111827",
       "pad_screws": "#9CA3AF", "keeper": "#B45309", "pin": "#DC2626", "chain": "#57534E", "sleeve": "#EAB308",
       "maillon": "#A16207", "carab": "#C2410C", "descender": "#15803D", "rope": "#0E7490", "triangle": "#F97316",
       "sling": "#2563EB", "bag": "#475569", "trunk": "#D6C7A1"}


def comps():
    global _C
    if _C is None:
        _C = m.build_components(P)
    return _C


def D():
    return comps()["_D"]


def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def win(shape, x0, x1, y0, y1, z0, z1):
    """The part of a shape inside a box (for close-ups)."""
    w = bx(x0, x1, y0, y1, z0, z1)
    try:
        sols = list(shape.solids()) or [shape]
    except Exception:
        sols = [shape]
    kept = []
    for s_ in sols:
        bb = s_.bounding_box()
        if bb.max.X < x0 or bb.min.X > x1 or bb.max.Y < y0 or bb.min.Y > y1 or bb.max.Z < z0 or bb.min.Z > z1:
            continue
        try:
            r = s_ & w
            if r is not None and r.volume > 1e-3:
                kept.append(r)
        except Exception:
            pass
    return Compound(kept) if kept else None


def part(name, shape, color, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, color, None, tuple(explode), alpha)


def K(key, name, explode=(0, 0, 0), col=None):
    return part(name, comps()[key], COL.get(col or key, "#64748B"), explode)


def W(key, name, box, explode=(0, 0, 0), col=None):
    s = win(comps()[key], *box)
    return None if s is None else part(name, s, COL.get(col or key, "#64748B"), explode)


def keep(ps):
    return [p for p in ps if p is not None]


def xs():
    return D()["x_s"]


def chain_all():
    c = comps()
    return c["chain_loop"] + c["chain_tail_a"] + c["chain_tail_b"]


def trunk(z0=-250, z1=320):
    return part("Palm trunk, 300 mm (or a test post)", m.trunk(P, None, z0, z1), COL["trunk"])


def kit(origin=(0.0, 0.0, 0.0)):
    return m.victim_kit(P, origin)


# ----------------------------------------------------------------- single components, laid square
def local():
    return m.frame_parts(P, m.derived(P))


def bar_flat():
    return Rot(0, 0, -120) * m._bar(P, m.derived(P), 1)


def pad_flat():
    return Rot(0, 0, -120) * m._pad(P, m.derived(P), 1)


def one_ring():
    return m._doublers(P, m.derived(P))[0]


def one_cheek():
    return m._cheeks(P, m.derived(P))[0]


def chain_sample(n=8):
    """A short straight piece of the chain with the master link and connecting link on its end."""
    lk = m.link_template(P)
    out = []
    for k in range(n):
        out.append(m.place(lk, (k * P["pitch"], 0, 0), (1, 0, 0), (0, 0, 1) if k % 2 else (0, 1, 0)))
    cl = m.place(m.stadium(14.0, 7.5, 4.0), (n * P["pitch"] + 2, 0, 0), (1, 0, 0), (0, 0, 1))
    st, ML, MW = P["master"]
    ml = m.place(m.master_template(P), (n * P["pitch"] + 18 + ML / 2, 0, 0), (1, 0, 0), (0, 1, 0))
    return m.fuse_all(out + [cl, ml])


def sleeve_flat():
    return m.rod((0, 0, 0), (P["sleeve"][0], 0, 0), P["sleeve"][1], P["sleeve"][1] - 1.5)


# ----------------------------------------------------------------- overview
def overview():
    c = comps()
    K_ = kit(origin=(xs() + 420, 380, 120))
    rope = (c["rope_brake"] + c["rope_load"]) & bx(-2000, 2000, -2000, 2000, -320, 200)
    parts = [
        part("Spine plate", c["spine"], COL["spine"], (0, 0, 0)),
        part("Eye doubler rings (4)", c["doublers"], COL["doublers"], (0, 0, -220)),
        part("Bearing bars (2)", c["bars"], COL["bars"], (-120, 0, -220)),
        part("Cleat cheeks (2)", c["cheeks"], COL["cheeks"], (0, 0, 220)),
        part("Rubber bark pads (2) and screws", c["pads"] + c["pad_screws"], COL["pads"], (-300, 0, -220)),
        part("Keeper", c["keeper"], COL["keeper"], (0, 0, 380)),
        part("Lock pin, ball-lock 8 mm", c["pin"], COL["pin"], (0, -250, 330)),
        part("Chain, grade 80, 110 links, with master link", chain_all(), COL["chain"], (-450, 0, 250)),
        part("Chain sleeve, tubular webbing", c["sleeve"], COL["sleeve"], (-650, 0, 250)),
        part("Tether quick link", c["maillon"], COL["maillon"], (0, 250, -250)),
        part("Carabiners (load and brake)", c["carab_main"] + c["carab_brake"], COL["carab"], (250, 0, -300)),
        part("Auto-locking descender", c["descender"], COL["descender"], (450, 0, -350)),
        part("Lowering rope, 30 m (top shown)", rope, COL["rope"], (450, 0, -450)),
        part("Victim carabiner", K_["carab_victim"], COL["carab"], (0, 0, 0)),
        part("Evacuation triangle", K_["triangle"], COL["triangle"], (0, 0, 0)),
        part("Chest sling", K_["chest_sling"], COL["sling"], (0, 0, 0)),
        part("Rope and carry bag", K_["bag"], COL["bag"], (0, 0, 0)),
    ]
    return bv.overview(parts, OUT / "overview.png", "TrunkBelay: the kit pulled apart, in build order",
                       "Numbered in build order; made parts first, then the bought chain, rigging and rescue gear",
                       elev=22, azim=-55, size=(11, 8), key=True)


# ----------------------------------------------------------------- making sketches
def sheet(n, shape, name, color, neighbours, title, material, notes, view_shape=None, inset=(24, -58)):
    p = part(name, shape, color)
    return bv.component_sheet(p, keep(neighbours), "TrunkBelay", f"TKB-DWG-{n}", f"TrunkBelay: {title}", material,
                              notes, DATE, out_dir=str(DWG), view_shape=view_shape, inset_view=inset)


def grey(name, shape):
    return part(name, shape, "#D1D5DB")


def sheets(which=None):
    c = comps()
    L = local()
    x0 = P["spine_set"]
    S = {}
    S[101] = lambda: sheet(101, c["spine"], "Spine plate", COL["spine"],
        [grey("bars", c["bars"]), grey("cheeks", c["cheeks"]), grey("doublers", c["doublers"])],
        "spine plate (make 1)", "S355 steel plate 5 mm",
        ["One piece of 5 mm S355 plate, profile cut. Outline from the",
         "  front edge (the edge toward the trunk): 175 long at the",
         "  bottom, 175 high at the front; 55 high at the back end; the",
         "  top runs 60 back from the front edge, then slopes down.",
         "Holes: load eye 22 at 150 back, 28 up; spare eye 22 at 70",
         "  back, 28 up; lightening hole 36 at 85 back, 90 up.",
         "Chain slots: two, 7.5 wide, 25 deep from the top edge,",
         "  centred 15 and 43 back from the front edge. Cut them",
         "  square and file every edge smooth; no burr may touch chain.",
         "Lock pin hole 8.5 at 29 back, 139 up (drill after the cheeks",
         "  are welded on, through all three plates).",
         "Do not thicken the plate: a link must span it (6 mm at most).",
         "Round the eye edges to 2 mm radius after the rings go on."],
        inset=(20, -60))
    S[102] = lambda: sheet(102, one_ring(), "Eye doubler ring", COL["doublers"],
        [grey("spine", c["spine"])], "eye doubler ring (make 4)", "S275 steel plate 4 mm",
        ["Make four. 4 mm steel, 50 outside diameter, 22 bore.",
         "Cut from plate or buy as heavy washers and open the bore.",
         "One ring each side of each eye, the bores in line with the",
         "  22 eye hole within 0.5 mm (use a 22 pin to line them up).",
         "Weld all round the outside, 3 mm fillet; no weld in the bore.",
         "After welding, round the bore edges to 2 mm radius, so a",
         "  carabiner bears on a smooth curve, never a sharp edge.",
         "Finished eye: 13 thick (4 + 5 + 4)."],
        inset=(20, -60))
    S[103] = lambda: sheet(103, c["bars"], "Bearing bar", COL["bars"],
        [grey("spine", c["spine"]), grey("pads", c["pads"])], "bearing bar (make 2, opposite hands)",
        "S355 rectangular hollow section 50 x 25 x 2.5 mm",
        ["Make two, one a mirror image of the other. RHS 50 x 25 x 2.5,",
         "  the 50 face vertical; the 25 depth runs away from the trunk.",
         "Length 175 along the trunk-side face; the inner end is cut",
         "  at 30 deg so it lies flat on the spine face.",
         "Weld a 3 mm cap on the outer end. Drill an 8 vent hole in",
         "  the bottom face near each end before galvanising.",
         "Drill two 6.5 holes through the trunk-side face only, 53 and",
         "  138 from the inner end on the centre line, for the pad screws.",
         "The two bars meet the spine at its foot and form a V with",
         "  120 deg between their trunk-side faces."],
        view_shape=bar_flat(), inset=(20, -60))
    S[104] = lambda: sheet(104, c["cheeks"], "Cleat cheek", COL["cheeks"],
        [grey("spine", c["spine"]), grey("keeper", c["keeper"])], "cleat cheek (make 2)", "S355 steel plate 6 mm",
        ["Make two. 6 mm plate, 60 long x 45 high.",
         "Two notches from the top edge, 22 wide and 27 deep, centred",
         "  15 and 43 from the front end, so they sit round the two",
         "  chain slots in the spine with 7.25 of web showing each side.",
         "Weld one on each face of the spine, top edges flush with the",
         "  spine top, front ends flush with its front edge: 4 mm fillets",
         "  along the bottom and the back end only (keep the notches",
         "  and the top clean).",
         "Then drill the 8.5 lock pin hole through cheek, spine and",
         "  cheek together, 29 from the front, 139 up from the frame foot."],
        view_shape=one_cheek(), inset=(20, -60))
    S[105] = lambda: sheet(105, m.frame_weldment(c), "Frame weldment", COL["spine"],
        [grey("pads", c["pads"]), grey("keeper", c["keeper"])], "collar frame weldment (make 1)",
        "S355 steel parts above, welded, then hot-dip galvanised",
        ["Weld the bars to the spine foot first, in a jig that holds",
         "  their trunk-side faces at 120 deg and 50 high from the foot.",
         "  4 mm fillets all round each bar end; the bar ends must not",
         "  stand proud of the spine's front edge.",
         "Then the four eye rings, then the two cheeks.",
         "Check: the V faces meet (if extended) 8 in front of the spine",
         "  front edge; both bar faces flat within 1 mm.",
         "Grind spatter off the bar faces and slots. Galvanise the whole",
         "  frame; afterwards run a 7 mm bar through both slots and the",
         "  8 pin through its hole to clear the zinc.",
         "Stamp SWL 100 kg ONE PERSON and the frame number on the spine."],
        inset=(20, -60))
    S[106] = lambda: sheet(106, c["pads"], "Rubber bark pad", COL["pads"],
        [grey("bars", c["bars"]), grey("spine", c["spine"])], "rubber bark pad (make 2)",
        "Natural rubber sheet with one fabric ply, 10 mm, 60 to 70 Shore A",
        ["Make two. Cut 155 x 50 from 10 mm fabric-ply rubber sheet.",
         "Drill two 6.5 holes on the centre line, 35 from each end, and",
         "  counterbore them 13 diameter, 4 deep from the trunk side, so",
         "  the screw heads sit 3 below the rubber face.",
         "Bond to the bar's trunk-side face with contact adhesive, the",
         "  inner end 15 from where the two pad faces would meet.",
         "Fit M6 x 30 countersunk screws through pad and bar face with",
         "  a washer and nyloc nut inside the bar (reach in from the",
         "  inner end before the bar is capped, or use rivet nuts).",
         "Replace a pad that is torn, glazed or soaked in oil."],
        view_shape=pad_flat(), inset=(20, -60))
    S[107] = lambda: sheet(107, c["keeper"], "Keeper", COL["keeper"],
        [grey("spine", c["spine"]), grey("cheeks", c["cheeks"]), grey("pin", c["pin"])], "keeper (make 1)",
        "S275 steel sheet 3 mm, zinc plated",
        ["Cut a cross from 3 mm sheet: a bridge 56 long (front to back)",
         "  x 23 wide, with a leg 6 wide and 43 long at the middle of",
         "  each long side.",
         "Bend both legs down 90 deg so they sit 17 apart inside: they",
         "  slide over the two cheeks between the notches.",
         "Drill 8.5 through both legs, 39 below the bridge's top face.",
         "The bridge lies on the cleat top across both slot mouths, so a",
         "  chain link cannot lift out of its slot.",
         "Tie the lock pin's lanyard to one leg."],
        inset=(30, -60))
    S[108] = lambda: sheet(108, chain_sample(), "Chain set", COL["chain"],
        [grey("frame", m.frame_weldment(c))], "chain set (assemble 1)",
        "Bought: grade 80 alloy chain 6 mm, master link, connecting link",
        ["Buy 110 links of 6 mm grade 80 chain (about 1.98 m) with its",
         "  certificate, cut to length by the supplier. Count the links.",
         "Never weld, heat, grind or bend the chain.",
         "One end (the adjustable end): fit the master link with a",
         "  6 mm grade 80 connecting link and peen its pin.",
         "Other end (the fixed end): leave plain; it goes into the front",
         "  slot and a quick link ties its tail to the spare eye.",
         "Paint the 56th, 72nd and 100th links from the fixed end: the",
         "  link that drops into the rear slot on 200, 300 and 450 trunks.",
         "Drawn: eight links, the connecting link and the master link."],
        inset=(30, -60))
    S[109] = lambda: sheet(109, c["sleeve"], "Chain sleeve", COL["sleeve"],
        [grey("chain", c["chain_loop"])], "chain sleeve (make 1)", "50 mm (2 in) tubular nylon webbing",
        ["Cut 600 of 50 mm tubular webbing with a hot knife so the",
         "  ends are sealed. Mark its middle.",
         "Feed the chain's adjustable end through it before the master",
         "  link is fitted, and slide it to the middle of the loop.",
         "It lies on the bark at the back of the trunk, opposite the",
         "  frame, where the chain presses hardest.",
         "On a 200 trunk it covers almost the whole loop; on bigger",
         "  trunks the chain each side of it is bare.",
         "Replace it when it is cut through to the chain."],
        view_shape=sleeve_flat(), inset=(40, -60))
    for n in sorted(S):
        if which and n not in which:
            continue
        print(n, "->", S[n]())


# ----------------------------------------------------------------- joints
def joints(which=None):
    c = comps()
    x = xs()
    J = {}

    def jt(n, parts, title, sub, **kw):
        return bv.joint(keep(parts), OUT / f"joint-{n:02d}.png", f"Joint {n}: {title}", sub, **kw)

    foot = (x - 160, x + 60, -180, 180, -5, 60)
    J[1] = lambda: jt(1, [W("spine", "Spine plate", foot), K("bars", "Bearing bars (2)"), K("pads", "Rubber pads"),
                          K("pad_screws", "Pad screws", col="pad_screws")],
                      "bearing bars welded to the spine foot",
                      "The two bars form a 120 deg V; 4 mm fillets all round each bar end on the spine faces",
                      elev=55, azim=-150)
    eye = (x + 120, x + 180, -20, 20, -5, 60)
    J[2] = lambda: jt(2, [W("spine", "Spine plate (cut)", eye), W("doublers", "Doubler rings (cut)", eye),
                          W("carab_main", "Load carabiner", (x + 120, x + 180, -40, 40, -100, 60), col="carab")],
                      "load eye with its doubler rings, cut open",
                      "Ring, 5 mm spine, ring: 13 mm of rounded steel under the carabiner bar", cut="+X", elev=20, azim=-60)
    top = (x - 10, x + 75, -45, 45, 120, 185)
    J[3] = lambda: jt(3, [W("spine", "Spine top with two slots", top), K("cheeks", "Cheeks (2)"), part("Keeper, lifted to show the slots", Pos(0, 0, 70) * c["keeper"], COL["keeper"]),
                          K("pin", "Lock pin"), W("chain_loop", "Chain links in the slots", top, col="chain"),
                          W("chain_tail_a", "Fixed end tail", top, col="chain"), W("chain_tail_b", "Adjustable end tail", top, col="chain")],
                      "the chain cleat: two links standing in the slots",
                      "Links stand in 7.5 mm slots; their neighbours bear on the 5 mm web in the cheek notches",
                      elev=45, azim=-125)
    J[4] = lambda: jt(4, [K("bars", "Bearing bar"), K("pads", "Rubber pad"), K("pad_screws", "Countersunk screws", col="pad_screws")],
                      "rubber pad on a bearing bar, cut open",
                      "Bonded, plus two M6 screws with heads 3 mm below the rubber face", cut="-Y", elev=30, azim=-100)
    back = (-200, -60, -140, 140, 120, 200)
    J[5] = lambda: jt(5, [part("Trunk (bark)", win(m.trunk(P, None, 100, 220), -200, -100, -160, 160, 100, 220), COL["trunk"]),
                          W("sleeve", "Chain sleeve", back), W("chain_loop", "Chain", (-200, 40, -175, 175, 120, 200), col="chain")],
                      "the chain sleeve at the back of the trunk",
                      "600 mm of tubular webbing on the chain where it presses hardest on the bark", elev=30, azim=150)
    spare = (x + 35, x + 110, -40, 60, -60, 70)
    J[6] = lambda: jt(6, [W("spine", "Spine (spare eye)", spare), W("doublers", "Doubler rings", spare),
                          K("maillon", "Tether quick link"), W("carab_brake", "Brake carabiner", (x + 40, x + 110, -40, 40, -110, 60), col="carab"),
                          W("chain_tail_a", "Fixed end tail", (x + 20, x + 110, 0, 60, -60, 160), col="chain")],
                      "spare eye: tether quick link and brake carabiner",
                      "The fixed end of the chain is tied to the frame, so it cannot be dropped; the brake carabiner shares the eye",
                      elev=20, azim=-35)
    low = (x + 40, x + 290, -60, 60, -330, 60)
    J[7] = lambda: jt(7, [W("spine", "Spine", (x + 40, x + 200, -20, 20, -5, 60)), K("carab_main", "Load carabiner", col="carab"),
                          K("descender", "Auto-locking descender"), K("carab_brake", "Brake carabiner", col="carab"),
                          W("rope_brake", "Brake strand", low, col="rope"), W("rope_load", "Load strand, to the victim", low, col="rope")],
                      "descender and brake carabiner",
                      "Load strand straight down to the victim; brake strand turns 180 deg over the brake carabiner, then down",
                      elev=15, azim=-80)
    J[8] = lambda: jt(8, [part("Trunk, 300 mm", m.trunk(P, None, -60, 230), COL["trunk"]), K("bars", "Bearing bars"),
                          K("pads", "Rubber pads"), K("spine", "Spine"), K("cheeks", "Cheeks"), K("keeper", "Keeper"),
                          part("Chain", chain_all() & bx(-400, 600, -400, 400, 100, 200), COL["chain"]), K("sleeve", "Sleeve")],
                      "the collar on the trunk, seen from above",
                      "Pads touch the bark on two lines; the chain wraps the trunk once at 160 mm above the frame foot",
                      elev=70, azim=-90, size=(7, 5.5))
    for n in sorted(J):
        if which and n not in which:
            continue
        print(n, "->", J[n]())


# ----------------------------------------------------------------- steps
def steps(which=None):
    c = comps()
    E = {}

    def st(n, done, new, title, sub, **kw):
        return bv.step(keep(done), keep(new), OUT / f"step-{n:02d}.png", f"Step {n}: {title}", sub, **kw)

    spine = K("spine", "Spine plate")
    bars = K("bars", "Bearing bars")
    rings = K("doublers", "Doubler rings")
    cheeks = K("cheeks", "Cheeks")
    pads = K("pads", "Pads")
    frame = [spine, bars, rings, cheeks]
    tr = trunk()
    E[1] = lambda: st(1, [spine], [K("bars", "Bearing bars (2)", (-150, 0, -120))], "weld the bearing bars to the spine",
                      "In a jig: the bar faces at 120 deg, their bottoms level with the spine foot; 4 mm fillets all round",
                      elev=30, azim=-120)
    E[2] = lambda: st(2, [spine, bars], [K("doublers", "Doubler rings (4)", (0, 0, -150))], "weld the eye rings",
                      "A 22 mm pin through each eye lines the rings up; 3 mm fillets round the outside only",
                      elev=20, azim=-60)
    E[3] = lambda: st(3, [spine, bars, rings], [K("cheeks", "Cleat cheeks (2)", (0, 0, 160))], "weld the cheeks, drill the pin hole",
                      "Cheeks flush with the spine top and front; then drill 8.5 mm through all three; then galvanise the frame",
                      elev=25, azim=-60)
    E[4] = lambda: st(4, frame, [K("pads", "Rubber pads (2)", (-160, 0, 0)), K("pad_screws", "M6 screws (4)", (-160, 0, 0), col="pad_screws")],
                      "bond and screw the pads",
                      "Contact adhesive on both faces, press on, then two countersunk screws each, nuts inside the bars",
                      elev=30, azim=-120)
    E[5] = lambda: st(5, frame + [pads], [K("chain_tail_a", "Fixed end of the chain", (0, 150, 120), col="chain"),
                                          K("maillon", "Tether quick link", (0, 150, -100))],
                      "fit the fixed end and its tether",
                      "Fixed end's link down into the front slot; its tail tied to the spare eye with the quick link, gate screwed shut",
                      elev=25, azim=40)
    E[6] = lambda: st(6, frame + [pads, K("chain_tail_a", "Fixed end", col="chain")],
                      [K("chain_loop", "Chain round the trunk", (-250, 0, 0), col="chain"), K("sleeve", "Sleeve", (-250, 0, 0))],
                      "wrap the chain round the trunk (a 300 mm test post at the bench)",
                      "Bar pads on the bark, chain once round with the sleeve at the back, pulled snug by hand",
                      context=[part(tr.name, tr.shape, "#E5E7EB")], elev=35, azim=-60, label_done=False)
    E[7] = lambda: st(7, frame + [pads, K("chain_tail_a", "Fixed end", col="chain"), K("chain_loop", "Chain", col="chain"), K("sleeve", "Sleeve")],
                      [K("chain_tail_b", "Adjustable end into the rear slot", (0, -120, 120), col="chain"),
                       K("keeper", "Keeper", (0, 0, 120)), K("pin", "Lock pin", (0, -150, 0))],
                      "drop the adjustable end in, keeper on, pin in",
                      "Pull the tail hard, drop the nearest link into the rear slot, keeper over both slots, pin through until it clicks",
                      context=[part(tr.name, tr.shape, "#E5E7EB")], elev=30, azim=-125, label_done=False)
    collar = frame + [pads, K("chain_loop", "Chain", col="chain"), K("chain_tail_a", "Fixed end", col="chain"),
                      K("chain_tail_b", "Tail", col="chain"), K("sleeve", "Sleeve"), K("keeper", "Keeper"), K("pin", "Pin"),
                      K("maillon", "Quick link")]
    E[8] = lambda: st(8, collar, [K("carab_main", "Load carabiner", (250, 0, 0), col="carab"),
                                  K("descender", "Auto-locking descender", (250, 0, -100))],
                      "clip on the descender",
                      "Load carabiner through the load eye, gate screwed shut, descender on it, handle outward",
                      context=[part(tr.name, tr.shape, "#E5E7EB")], elev=20, azim=-60, label_done=False)
    E[9] = lambda: st(9, collar + [K("carab_main", "Load carabiner", col="carab"), K("descender", "Descender")],
                      [K("carab_brake", "Brake carabiner", (0, 0, -150), col="carab"),
                       K("rope_load", "Rope: load strand", (200, 0, -150), col="rope"),
                       K("rope_brake", "Rope: brake strand", (0, 0, -150), col="rope")],
                      "reeve the rope and the brake carabiner",
                      "As the descender's maker shows; brake strand up over the brake carabiner in the spare eye, then down",
                      context=[part(tr.name, tr.shape, "#E5E7EB")], elev=15, azim=-70, label_done=False)
    K_ = kit()
    E[10] = lambda: st(10, [], [part("Victim carabiner", K_["carab_victim"], COL["carab"], (0, 0, 150)),
                               part("Evacuation triangle", K_["triangle"], COL["triangle"], (0, 0, 0)),
                               part("Chest sling", K_["chest_sling"], COL["sling"], (0, 0, 120)),
                               part("Rope bag (rope inside)", K_["bag"] + K_["rope_coil"], COL["bag"], (0, 0, 0))],
                       "make up the victim set and pack",
                       "Victim carabiner on the rope's end loop; rope, triangle, chest sling and collar packed in the bag",
                       elev=25, azim=-70)
    for n in sorted(E):
        if which and n not in which:
            continue
        print(n, "->", E[n]())


if __name__ == "__main__":
    args = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    what, nums = args[0], [int(a) for a in args[1:]]
    if what == "overview":
        print("overview ->", overview())
    elif what == "sheets":
        sheets(nums or None)
    elif what == "joints":
        joints(nums or None)
    elif what == "steps":
        steps(nums or None)
    else:
        for w in args:
            {"overview": overview, "sheets": sheets, "joints": joints, "steps": steps}[w]()
