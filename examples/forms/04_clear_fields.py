"""Working with Forms 04 — Reset all fields to blank values."""

from pathlib import Path

from pdfdancer import PDFDancer, ObjectType

SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-forms/cleared.pdf")


def run_example(
        pdf_path: Path = SHOWCASE_PATH,
        output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        fields = pdf.select_form_fields()
        for field in fields:
            if field.object_type == ObjectType.CHECK_BOX:
                field.edit().value("Off").apply()
            else:
                field.edit().value("").apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Cleared {len(fields)} fields and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
