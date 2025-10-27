"""Create a brand-new PDF and add branded content."""

from pathlib import Path

from pdfdancer import Color, Orientation, PageSize, PDFDancer, StandardFonts

if __name__ == "__main__":
    output_path = Path("generated.pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with PDFDancer.new(page_size=PageSize.LETTER, orientation=Orientation.PORTRAIT, initial_page_count=1) as pdf:
        pdf.new_paragraph().text("PDFDancer Generated PDF").font(StandardFonts.HELVETICA_BOLD, 18).color(Color(34, 34, 34)).at(0, 72, 700).add()
        pdf.new_paragraph().text("This PDF was assembled using the pdfdancer-client-python SDK.").font(StandardFonts.HELVETICA, 12).color(Color(80, 80, 80)).line_spacing(1.3).at(0, 72, 660).add()
        pdf.page(0).new_line().from_point(72, 640).to_point(523, 640).stroke_color(Color(0, 120, 215)).stroke_width(2.0).add()

        pdf.save(output_path)
        print(f"Created a {len(pdf.pages())}-page PDF at {output_path}.")
