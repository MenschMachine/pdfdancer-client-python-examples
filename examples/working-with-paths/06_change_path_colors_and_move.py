from pathlib import Path
from pdfdancer import Color, PDFDancer

INPUT = Path("examples/basic-paths.pdf")
OUTPUT = Path("output/working-with-paths/changed_path_colors_and_position.pdf")

with PDFDancer.open(INPUT) as pdf:
    paths = pdf.page(1).select_paths()
    if not paths:
        raise RuntimeError("No paths found.")
    path = paths[0]
    path.edit().stroke_color(Color.RED).fill_color(Color(255, 255, 0)).apply()
    path.move_to(180, 500)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)

