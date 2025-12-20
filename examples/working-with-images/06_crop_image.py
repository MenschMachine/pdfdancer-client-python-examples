"""Working with Images 06 — Crop an image by removing pixels from edges."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/cropped_image.pdf")
CROP_PIXELS = {"left": 20, "top": 20, "right": 20, "bottom": 20}


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    crop_left: int = CROP_PIXELS["left"],
    crop_top: int = CROP_PIXELS["top"],
    crop_right: int = CROP_PIXELS["right"],
    crop_bottom: int = CROP_PIXELS["bottom"],
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to crop.")

        image = images[0]
        image.crop(left=crop_left, top=crop_top, right=crop_right, bottom=crop_bottom)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(
            f"Cropped first image on page 1 (left={crop_left}, top={crop_top}, "
            f"right={crop_right}, bottom={crop_bottom}) and saved to {output_path}."
        )


if __name__ == "__main__":
    run_example()
