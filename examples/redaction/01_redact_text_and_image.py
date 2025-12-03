"""Redaction 01 — Redact text and an image from Showcase.pdf."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/redaction/redacted_text_and_image.pdf")


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        # Redact text: find and redact the "PDFDancer Showcase" title on page 1
        paragraphs = pdf.page(1).select_paragraphs_starting_with("PDFDancer Showcase")
        text_redacted = 0
        for para in paragraphs:
            para.redact(replacement="[REDACTED]")
            text_redacted += 1

        # Redact first image on page 3 (the "Transparent PNG" image)
        images = pdf.page(3).select_images()
        image_redacted = 0
        if images:
            images[0].redact()
            image_redacted += 1

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Redacted {text_redacted} text paragraph(s) and {image_redacted} image(s).")
        print(f"Saved to {output_path}")


if __name__ == "__main__":
    run_example()
