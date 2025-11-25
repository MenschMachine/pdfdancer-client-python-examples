"""Working with Pages 01 — Move a page to a new index."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-pages/reordered.pdf")
SOURCE_INDEX = 1
DEST_INDEX = 3


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    source_index: int = SOURCE_INDEX,
    dest_index: int = DEST_INDEX,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        if source_index >= len(pdf.pages()):
            raise ValueError(f"Source index {source_index} out of range.")

        pdf.move_page(source_index, dest_index)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(
            f"Moved page {source_index} to position {dest_index}. Saved PDF to {output_path}."
        )


if __name__ == "__main__":
    run_example()
