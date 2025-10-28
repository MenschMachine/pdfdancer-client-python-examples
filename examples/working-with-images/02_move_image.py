"""Working with Images 02 — Move the first page image to new coordinates."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-images/moved_image.pdf")
NEW_POSITION = {"x": 60, "y": 60}


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(0).select_images()
        if not images:
            raise ValueError("No images found on page 0 to move.")

        image = images[0]
        image.move_to(**NEW_POSITION)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(
            f"Moved first image on page 0 to ({NEW_POSITION['x']}, {NEW_POSITION['y']}) and saved to {output_path}."
        )


if __name__ == "__main__":
    run_example()
