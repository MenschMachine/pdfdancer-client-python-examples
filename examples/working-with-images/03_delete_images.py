"""Working with Images 03 — Remove all images from a specific page."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/no_images_page.pdf")
TARGET_PAGE_INDEX = 2


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
        if not images:
            raise ValueError(f"No images found on page {page_index} to delete.")

        for image in images:
            image.delete()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Deleted {len(images)} images from page {page_index} and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
