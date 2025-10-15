"""Move a page from one position to another inside a PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

PDF_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output_reordered.pdf")
SOURCE_INDEX = 0       # zero-based index of the page to move
DESTINATION_INDEX = 2  # new zero-based index for the page


if __name__ == "__main__":
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF file not found: {PDF_PATH}. Update PDF_PATH to point at a real document.")

    with PDFDancer.open(PDF_PATH) as pdf:
        page_count = len(pdf.pages())
        if SOURCE_INDEX < 0 or SOURCE_INDEX >= page_count:
            raise SystemExit(f"SOURCE_INDEX must be between 0 and {page_count - 1}.")
        if DESTINATION_INDEX < 0 or DESTINATION_INDEX >= page_count:
            raise SystemExit(f"DESTINATION_INDEX must be between 0 and {page_count - 1}.")
        if SOURCE_INDEX == DESTINATION_INDEX:
            raise SystemExit("SOURCE_INDEX and DESTINATION_INDEX are the same. Nothing to do.")

        pdf.move_page(SOURCE_INDEX, DESTINATION_INDEX)
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(OUTPUT_PATH)
        print(f"Moved page {SOURCE_INDEX} to position {DESTINATION_INDEX}. Saved PDF to {OUTPUT_PATH}.")
