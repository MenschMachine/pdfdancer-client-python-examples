"""Add an image to a page at the specified coordinates."""

from pathlib import Path

from pdfdancer import PDFDancer

PDF_PATH = Path("examples/Showcase.pdf")
IMAGE_PATH = Path("examples/logo.png")
OUTPUT_PATH = Path("output_with_logo.pdf")
PAGE_INDEX = 0
TARGET_X = 72.0
TARGET_Y = 720.0


if __name__ == "__main__":
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF file not found: {PDF_PATH}. Update PDF_PATH to point at a real document.")
    if not IMAGE_PATH.exists():
        raise SystemExit(f"Image file not found: {IMAGE_PATH}. Update IMAGE_PATH to point at an existing asset.")

    with PDFDancer.open(PDF_PATH) as pdf:
        page_count = len(pdf.pages())
        if PAGE_INDEX < 0 or PAGE_INDEX >= page_count:
            raise SystemExit(f"PAGE_INDEX must be between 0 and {page_count - 1}.")

        (
            pdf.new_image()
            .from_file(IMAGE_PATH)
            .at(page=PAGE_INDEX, x=TARGET_X, y=TARGET_Y)
            .add()
        )

        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(OUTPUT_PATH)
        print(f"Placed {IMAGE_PATH} on page {PAGE_INDEX} at ({TARGET_X}, {TARGET_Y}). Saved to {OUTPUT_PATH}.")
