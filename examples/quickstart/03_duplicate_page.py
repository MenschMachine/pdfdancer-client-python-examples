"""Quickstart 03 — Duplicate the first page of Showcase.pdf."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/quickstart/duplicated_showcase.pdf")


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pdf.duplicate_page(0)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)

        print(f"Cloned page 0 -> document now has {len(pdf.pages())} pages.")
        print(f"Saved updated PDF to {output_path}")


if __name__ == "__main__":
    run_example()
