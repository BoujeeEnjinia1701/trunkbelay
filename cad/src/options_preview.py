"""Interim options picture for TKB-OPT-001: a labelled shaded preview of the D3 option models.

Run from the repo root:  python cad/src/options_preview.py   -> media/options.png
`render.py --check` needs media/options.png, and the Cycles picture is made on the studio machine with
`python .kit/options.py`, which overwrites this file. This preview draws components(option) of every option
from cad/src/model.py with .kit/concept.py's shaded renderer, at one scale, each on the same 300 mm trunk
section, and is marked PREVIEW on the picture so it is never taken for the final render.
CONCEPT OPTIONS, NOT FOR FABRICATION.
"""
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "cad" / "src"), str(ROOT / ".kit")]
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from PIL import Image  # noqa: E402
from build123d import Box, Pos  # noqa: E402
import concept  # noqa: E402
from concept import Part  # noqa: E402
import model as M  # noqa: E402


def panel(opt, path):
    keep = Pos(0, 0, -400) * Box(3000, 3000, 1400)            # trunk section from -1100 to 300 mm
    parts = []
    for p in M.components(opt):
        sh = p["shape"]
        if p["kind"] == "context":
            sh = sh & keep
            parts.append(Part("Palm trunk 300 mm (context)", sh, "#D6C7A1"))
        else:
            parts.append(Part(p["name"], sh, p["color"]))
    concept._render(parts, path, elev=18, azim=-40, size=(5, 6), dpi=150)
    return Image.open(path).convert("RGB")


def main():
    keys = list(M.OPTIONS)
    with tempfile.TemporaryDirectory() as tmp:
        imgs = [panel(k, Path(tmp) / f"opt-{k}.png") for k in keys]
    n = len(keys)
    fig = plt.figure(figsize=(5.2 * n, 7.0), dpi=150)
    fig.text(0.015, 0.975, "TrunkBelay: concept options", fontsize=13, fontweight="bold", color="#111827", va="top")
    fig.text(0.015, 0.94, "PREVIEW: shaded view of the D3 models, to be replaced by the Cycles render (python .kit/options.py). "
             "CONCEPT OPTIONS, NOT FOR FABRICATION. Same 300 mm trunk and scale in every panel.", fontsize=8, color="#B45309", va="top")
    for i, (k, im) in enumerate(zip(keys, imgs)):
        ax = fig.add_axes([i / n + 0.01, 0.2, 1 / n - 0.02, 0.7])
        ax.imshow(im); ax.axis("off")
        fig.text(i / n + 0.02, 0.17, f"Option {k}: {M.OPTIONS[k]}", fontsize=11, fontweight="bold", color="#111827", va="top")
        fig.text(i / n + 0.02, 0.12, textwrap.fill(M.PRINCIPLES[k], 58), fontsize=8, color="#4B5563", va="top")
        if k == M.CHOSEN:
            fig.text((i + 1) / n - 0.02, 0.17, "CURRENT DESIGN", fontsize=8, fontweight="bold", color="#0F766E", va="top", ha="right")
    out = ROOT / "media/options.png"
    fig.savefig(out, facecolor="white")
    plt.close(fig)
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
