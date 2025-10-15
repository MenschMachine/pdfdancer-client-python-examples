"""Create a brand-new PDF and add branded content."""

from pathlib import Path

from pdfdancer import Color, Orientation, PageSize, PDFDancer, StandardFonts

OUTPUT_PATH = Path("generated.pdf")
PAGE_SIZE = PageSize.LETTER
ORIENTATION = Orientation.PORTRAIT
INITIAL_PAGE_COUNT = 1
HEADLINE_TEXT = "PDFDancer Generated PDF"
BODY_TEXT = "This PDF was assembled using the pdfdancer-client-python SDK."


if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with PDFDancer.new(
        page_size=PAGE_SIZE,
        orientation=ORIENTATION,
        initial_page_count=INITIAL_PAGE_COUNT,
    ) as pdf:
        (
            pdf.new_paragraph()
            .text(HEADLINE_TEXT)
            .font(StandardFonts.HELVETICA_BOLD, 18)
            .color(Color(34, 34, 34))
            .at(0, 72, 700)
            .add()
        )

        (
            pdf.new_paragraph()
            .text(BODY_TEXT)
            .font(StandardFonts.HELVETICA, 12)
            .color(Color(80, 80, 80))
            .line_spacing(1.3)
            .at(0, 72, 660)
            .add()
        )

        (
            pdf.page(0)
            .new_line()
            .from_point(72, 640)
            .to_point(523, 640)
            .stroke_color(Color(0, 120, 215))
            .stroke_width(2.0)
            .add()
        )

        pdf.save(OUTPUT_PATH)
        print(f"Created a {len(pdf.pages())}-page PDF at {OUTPUT_PATH}.")
