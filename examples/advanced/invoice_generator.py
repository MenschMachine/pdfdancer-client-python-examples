"""Generate a professional invoice from scratch."""

from pathlib import Path

from pdfdancer import Color, Orientation, PageSize, PDFDancer, StandardFonts

if __name__ == "__main__":
    with PDFDancer.new(page_size=PageSize.LETTER, orientation=Orientation.PORTRAIT, initial_page_count=1) as pdf:
        # Header
        pdf.new_paragraph().text("INVOICE").font(StandardFonts.HELVETICA_BOLD, 32).color(Color(0, 0, 128)).at(0, 72, 720).add()
        pdf.new_paragraph().text("Invoice #12345\nDate: 2025-01-15").font(StandardFonts.HELVETICA, 10).at(0, 400, 720).add()

        # Divider line
        pdf.page(0).new_line().from_point(72, 700).to_point(540, 700).stroke_color(Color(200, 200, 200)).stroke_width(1).add()

        # Items
        pdf.new_paragraph().text("Item: Professional Services\nQuantity: 10 hours\nRate: $150/hour").font(StandardFonts.COURIER, 11).at(0, 72, 600).add()

        # Total box
        pdf.page(0).new_path().rectangle(x=400, y=450, width=140, height=40).fill_color(Color(230, 230, 255)).add()
        pdf.new_paragraph().text("TOTAL: $1,500.00").font(StandardFonts.HELVETICA_BOLD, 14).at(0, 410, 460).add()

        pdf.save(Path("output_invoice.pdf"))
        print("Invoice generated!")
