"""Draw a colored box around content."""

from pathlib import Path

from pdfdancer import Color, PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Draw a red rectangle border
        pdf.page(0).new_path().add_rectangle(x=100, y=600, width=200, height=100).stroke_color(
            Color(255, 0, 0)).stroke_width(3).add()

        pdf.save(Path("output_with_box.pdf"))
        print("Drew a red box!")
