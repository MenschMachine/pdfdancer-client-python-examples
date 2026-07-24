from pathlib import Path
from pdfdancer import BoundingRect, PDFDancer

with PDFDancer.open(Path("examples/basic-paths.pdf")) as pdf:
    page = pdf.page(1)
    group = page.group_paths_in_region(BoundingRect(0, 0, 600, 800))
    group.resize(300, 300)
    output = Path("output/capabilities/grouped_paths_in_region_and_resized.pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(output)

