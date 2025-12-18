"""Redaction 04 — Batch redaction of multiple object types."""

from pathlib import Path

from pdfdancer import Color, PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/redaction/batch_redacted.pdf")


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        objects_to_redact = []

        # Collect paragraphs containing "PDFDancer"
        paragraphs = pdf.select_paragraphs_matching(r"PDFDancer")
        objects_to_redact.extend(paragraphs)

        # Collect images from page 3
        images = pdf.page(3).select_images()
        objects_to_redact.extend(images)

        if not objects_to_redact:
            print("No objects found to redact.")
            return

        # Batch redact all collected objects
        result = pdf.redact(
            objects_to_redact,
            replacement="[REDACTED]",
            placeholder_color=Color(0, 0, 0),
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Batch redacted {result.count} object(s).")
        print(f"Success: {result.success}")
        print(f"Saved to {output_path}")


if __name__ == "__main__":
    run_example()
