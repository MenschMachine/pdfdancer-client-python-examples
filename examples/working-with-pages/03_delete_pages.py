"""Working with Pages 03 — Delete a specific page."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-pages/deleted_page.pdf")
PAGE_INDEX = 4


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    page_index: int = PAGE_INDEX,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        if page_index >= len(pdf.pages()):
            raise ValueError(f"Page index {page_index} out of range.")

        pdf.page(page_index).delete()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Deleted page {page_index}. Document now has {len(pdf.pages())} pages.")


if __name__ == "__main__":
    run_example()
