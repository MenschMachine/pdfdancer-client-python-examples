"""Working with Text 01 — Replace the first matching paragraph."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/find_and_replace.pdf")
PARAGRAPH_PREFIX = "This line will be replaced"


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    paragraph_prefix: str = PARAGRAPH_PREFIX,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.page(0).select_paragraphs_starting_with(paragraph_prefix)
        if not matches:
            raise ValueError(f"No paragraphs found starting with '{paragraph_prefix}'.")

        matches[0].edit().replace(
            "This line was replaced!\nUpdated with PDFDancer",
        ).font("Helvetica", 12.0).line_spacing(1.1).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Saved updated PDF to {output_path}")


if __name__ == "__main__":
    run_example()
