from pathlib import Path
from pdfdancer import PDFDancer, Color

with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
    images = pdf.select_images()
    if not images:
        raise RuntimeError("No images found.")
    images[0].fill_region(0, 0, 10, 10, Color.WHITE)
    output = Path("output/capabilities/filled_image_region.pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(output)

