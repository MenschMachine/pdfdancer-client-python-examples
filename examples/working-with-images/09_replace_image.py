"""Working with Images 09 — Replace an image with a new one."""

from pathlib import Path

from pdfdancer import PDFDancer, Image


SHOWCASE_PATH = Path("examples/Showcase.pdf")
REPLACEMENT_IMAGE_PATH = Path("examples/experiment.png")
OUTPUT_PATH = Path("output/working-with-images/replaced_image.pdf")


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    replacement_image_path: Path = REPLACEMENT_IMAGE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    if not replacement_image_path.exists():
        raise FileNotFoundError(f"Replacement image not found: {replacement_image_path}")

    with PDFDancer.open(pdf_path) as pdf:
        images = pdf.page(1).select_images()
        if not images:
            raise ValueError("No images found on page 1 to replace.")

        image = images[0]
        new_image = Image(
            format="PNG",
            data=replacement_image_path.read_bytes(),
        )
        image.replace(new_image)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Replaced first image on page 1 with {replacement_image_path} and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
