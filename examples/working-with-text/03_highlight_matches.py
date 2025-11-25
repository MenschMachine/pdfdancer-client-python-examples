"""Working with Text 03 — Highlight matching paragraphs in Showcase.pdf."""

from pathlib import Path

from pdfdancer import Color, PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/highlighted.pdf")
TARGET_PATTERN = r"alignment"
HIGHLIGHT_COLOR = Color(255, 0, 0)


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    pattern: str = TARGET_PATTERN,
    color: Color = HIGHLIGHT_COLOR,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.page(1).select_paragraphs_matching(pattern)
        if not matches:
            raise ValueError(f"No paragraphs matched pattern: {pattern}")

        for paragraph in matches:
            paragraph.edit().color(color).font("Helvetica", 12).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Highlighted {len(matches)} paragraphs and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
