"""Add an image to a page at the specified coordinates."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")
    image_path = Path("examples/logo.png")
    output_path = Path("output_with_logo.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")
    if not image_path.exists():
        raise SystemExit(f"Image file not found: {image_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pdf.new_image().from_file(image_path).at(page=0, x=72.0, y=720.0).add()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Placed {image_path} on page 0 at (72.0, 720.0). Saved to {output_path}.")
