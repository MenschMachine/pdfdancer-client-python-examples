"""Working with Text 04 — Move a paragraph to new coordinates."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/moved_text.pdf")
PARAGRAPH_PREFIX = "This is regular"
NEW_POSITION = {"x": 50, "y": 750}


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
            raise ValueError(f"No paragraph found starting with '{paragraph_prefix}'.")

        matches[0].edit().move_to(**NEW_POSITION).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Moved paragraph to ({NEW_POSITION['x']}, {NEW_POSITION['y']}) and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
