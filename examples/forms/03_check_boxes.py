"""Working with Forms 03 — Toggle checkbox widgets."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-forms/checked.pdf")
CHECKBOX_NAME = "Subscribe"
CHECKED_VALUE = "Yes"


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    checkbox_name: str = CHECKBOX_NAME,
    checked_value: str = CHECKED_VALUE,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.select_form_fields_by_name(checkbox_name)
        if not matches:
            raise ValueError(f"No checkbox found with name '{checkbox_name}'.")

        for field in matches:
            field.edit().value(checked_value).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Checked '{checkbox_name}' and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
