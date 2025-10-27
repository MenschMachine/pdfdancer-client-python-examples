"""Relocate an image to a different spot."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Move first image on page 0 to bottom-left corner
        images = pdf.page(0).select_images()
        if images:
            images[0].move_to(x=50, y=50)
            pdf.save(Path("output_moved_image.pdf"))
            print("Image moved to corner!")
