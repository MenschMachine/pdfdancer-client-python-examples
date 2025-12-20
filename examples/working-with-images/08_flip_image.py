"""Working with Images 08 — Flip an image horizontally or vertically."""

from pathlib import Path

from pdfdancer import PDFDancer, ImageFlipDirection


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/flipped_image.pdf")
FLIP_DIRECTION = ImageFlipDirection.HORIZONTAL


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    direction: ImageFlipDirection = FLIP_DIRECTION,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to flip.")

        image = images[0]
        image.flip(direction)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Flipped first image on page 1 {direction.value} and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
