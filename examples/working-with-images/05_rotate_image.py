"""Working with Images 05 — Rotate an image by a specified angle."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/rotated_image.pdf")
ROTATION_ANGLE = 45


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    angle: float = ROTATION_ANGLE,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to rotate.")

        image = images[0]
        image.rotate(angle)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Rotated first image on page 1 by {angle} degrees and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
