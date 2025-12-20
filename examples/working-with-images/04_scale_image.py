"""Working with Images 04 — Scale/resize an image."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/scaled_image.pdf")
SCALE_FACTOR = 0.5


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    scale_factor: float = SCALE_FACTOR,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to scale.")

        image = images[0]
        image.scale(scale_factor)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Scaled first image on page 1 by factor {scale_factor} and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
