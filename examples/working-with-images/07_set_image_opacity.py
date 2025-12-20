"""Working with Images 07 — Set image opacity/transparency."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/transparent_image.pdf")
OPACITY = 0.5


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    opacity: float = OPACITY,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to adjust opacity.")

        image = images[0]
        image.set_opacity(opacity)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Set first image on page 1 to {opacity * 100:.0f}% opacity and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
