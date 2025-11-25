"""Working with Images 01 — List image positions in Showcase.pdf."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")


def run_example(pdf_path: Path = SHOWCASE_PATH) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.select_images()
        if not images:
            print("No images found in this document.")
            return

        print(f"Found {len(images)} images:\n")
        for image in images:
            position = image.position
            if position.bounding_rect:
                rect = position.bounding_rect
                size = f"{rect.width:.1f}×{rect.height:.1f}" if rect.width and rect.height else "unknown size"
            else:
                rect = None
                size = "unknown size"

            coords = (
                f"({position.x():.1f}, {position.y():.1f})"
                if position.x() is not None and position.y() is not None
                else "(unknown coordinates)"
            )
            print(f"- Page {position.page_number}: {coords} — {size}")


if __name__ == "__main__":
    run_example()
