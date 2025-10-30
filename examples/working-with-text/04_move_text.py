"""Working with Text 04 — Move a paragraph to new coordinates."""

from pathlib import Path

from pdfdancer import PDFDancer

SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/moved_text.pdf")
PARAGRAPH_PREFIX = "This is regular"


def run_example(
        pdf_path: Path = SHOWCASE_PATH,
        output_path: Path = OUTPUT_PATH,
        paragraph_prefix: str = PARAGRAPH_PREFIX,
) -> None:
    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.page(0).select_paragraphs_starting_with(paragraph_prefix)
        if not matches:
            raise ValueError(f"No paragraph found starting with '{paragraph_prefix}'.")

        print(matches[0].object_ref().get_text())
        matches[0].edit().move_to(50, 750).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Moved paragraph to (50,750) and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
