"""Working with Pages 04 — Append a blank page with custom size."""

from pathlib import Path

from pdfdancer import Orientation, PageSize, PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-pages/extra_page.pdf")
NEW_PAGE_SIZE = PageSize.LETTER
NEW_PAGE_ORIENTATION = Orientation.PORTRAIT


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pdf.new_page().orientation(NEW_PAGE_ORIENTATION).page_size(NEW_PAGE_SIZE).add()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Added blank {NEW_PAGE_SIZE.name.lower()} page. Total pages: {len(pdf.pages())}.")


if __name__ == "__main__":
    run_example()
