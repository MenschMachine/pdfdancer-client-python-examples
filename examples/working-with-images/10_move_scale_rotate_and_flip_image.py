from pathlib import Path
from pdfdancer import PDFDancer

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/working-with-images/moved_scaled_rotated_flipped_image.pdf")

with PDFDancer.open(INPUT) as pdf:
    images = pdf.select_images()
    if not images:
        raise RuntimeError("No images found.")
    image = images[0]
    image.move_to(80, 80)
    image.scale(0.8)
    image.rotate(15)
    image.set_opacity(0.8)
    image.flip_horizontal()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)


