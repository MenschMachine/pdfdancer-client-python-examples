"""Working with Templates 01 — Fill placeholders with dynamic content."""

from pathlib import Path

from pdfdancer import PDFDancer


TEMPLATE_PATH = Path("examples/templates/Template.pdf")
OUTPUT_PATH = Path("output/templates/basic_fill.pdf")


def run_example(
    pdf_path: Path = TEMPLATE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pdf.apply_replacements({
            "{{RECIPIENT_NAME}}": "Jane Smith",
            "{{COURSE_NAME}}": "Introduction to Python",
            "{{DATE}}": "January 7, 2026",
            "{{INSTRUCTOR}}": "Dr. John Doe",
        })

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Filled template and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
