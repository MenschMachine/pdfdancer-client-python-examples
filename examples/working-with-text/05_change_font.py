"""Working with Text 05 — Apply a new font to the Showcase title."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/bold_title.pdf")
PARAGRAPH_PREFIX = "PDFDancer"
FONT_NAME = "Helvetica-Bold"
FONT_SIZE = 24


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    paragraph_prefix: str = PARAGRAPH_PREFIX,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.page(1).select_paragraphs_starting_with(paragraph_prefix)
        if not matches:
            raise ValueError(f"No paragraph found starting with '{paragraph_prefix}'.")

        matches[0].edit().font(FONT_NAME, FONT_SIZE).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Updated font to {FONT_NAME} {FONT_SIZE}pt and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
