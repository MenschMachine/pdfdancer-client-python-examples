"""Redaction 03 — Redact all images on a specific page."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/redaction/redacted_all_images.pdf")
TARGET_PAGE_INDEX = 3


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    page_index: int = TARGET_PAGE_INDEX,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        if page_index >= len(pdf.pages()):
            raise ValueError(f"Page index {page_index} out of range.")

        images = pdf.page(page_index).select_images()
        redacted_count = 0

        for image in images:
            image.redact()
            redacted_count += 1

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Redacted {redacted_count} image(s) on page {page_index}.")
        print(f"Saved to {output_path}")


if __name__ == "__main__":
    run_example()
