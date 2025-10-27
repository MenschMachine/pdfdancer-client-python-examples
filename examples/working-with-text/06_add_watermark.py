"""Working with Text 06 — Add a DRAFT watermark to every page."""

from pathlib import Path

from pdfdancer import Color, PDFDancer, StandardFonts


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/watermarked.pdf")
WATERMARK_TEXT = "DRAFT"
WATERMARK_FONT = StandardFonts.HELVETICA_BOLD
WATERMARK_SIZE = 72
WATERMARK_COLOR = Color(200, 200, 200, a=128)
WATERMARK_POSITION = {"x": 150, "y": 400}


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        for page in pdf.pages():
            page.new_paragraph().text(WATERMARK_TEXT).font(WATERMARK_FONT, WATERMARK_SIZE).color(
                WATERMARK_COLOR
            ).at(**WATERMARK_POSITION).add()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Watermarked {len(pdf.pages())} pages and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
