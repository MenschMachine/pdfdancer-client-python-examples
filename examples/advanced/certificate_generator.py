"""Create personalized certificates."""

from pathlib import Path

from pdfdancer import Color, Orientation, PageSize, PDFDancer, StandardFonts

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]

    for name in names:
        with PDFDancer.new(page_size=PageSize.LETTER, orientation=Orientation.LANDSCAPE, initial_page_count=1) as pdf:
            # Border
            pdf.page(0).new_path().rectangle(x=50, y=50, width=700, height=500).stroke_color(Color(0, 100, 200)).stroke_width(5).add()

            # Title
            pdf.new_paragraph().text("Certificate of Achievement").font(StandardFonts.TIMES_BOLD, 36).color(Color(0, 50, 100)).at(0, 200, 450).add()

            # Name
            pdf.new_paragraph().text(f"Awarded to {name}").font(StandardFonts.TIMES_ITALIC, 28).color(Color(50, 50, 50)).at(0, 250, 350).add()

            # Date
            pdf.new_paragraph().text("January 2025").font(StandardFonts.HELVETICA, 14).color(Color(100, 100, 100)).at(0, 320, 150).add()

            pdf.save(Path(f"output_certificate_{name}.pdf"))
            print(f"Certificate for {name} created!")
