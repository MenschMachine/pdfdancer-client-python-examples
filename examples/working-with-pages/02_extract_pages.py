"""Working with Pages 02 — Extract the first N pages."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-pages/first_three_pages.pdf")
PAGES_TO_KEEP = 3


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    pages_to_keep: int = PAGES_TO_KEEP,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pages_to_keep <= 0:
        raise ValueError("pages_to_keep must be positive")

    with PDFDancer.open(pdf_path) as pdf:
        total_pages = len(pdf.pages())
        if pages_to_keep > total_pages:
            raise ValueError(
                f"Document only has {total_pages} pages; cannot keep {pages_to_keep}."
            )

        for index in range(total_pages - 1, pages_to_keep - 1, -1):
            pdf.page(index).delete()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Extracted first {pages_to_keep} pages into {output_path}.")


if __name__ == "__main__":
    run_example()
