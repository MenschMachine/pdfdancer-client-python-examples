"""Draw lines to connect or underline things."""

from pathlib import Path

from pdfdancer import Color, PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Draw a thick blue underline
        pdf.page(0).new_line().from_point(100, 680).to_point(400, 680).stroke_color(Color(0, 0, 255)).stroke_width(4).add()

        pdf.save(Path("output_with_line.pdf"))
        print("Drew an underline!")
