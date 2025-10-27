"""Remove all vector graphics from a page."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Clear all paths/shapes from page 1
        for path in pdf.page(1).select_paths():
            path.delete()

        pdf.save(Path("output_no_shapes.pdf"))
        print("Removed all shapes!")
