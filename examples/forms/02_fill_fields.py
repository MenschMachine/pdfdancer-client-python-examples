"""Working with Forms 02 — Populate common fields by name."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-forms/filled.pdf")
FIELD_UPDATES = {
    "Name": "Ada Lovelace",
    "Email": "ada@example.com",
    "Subscribe": "Yes",
}


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    updates: dict[str, str] | None = None,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    updates = updates or FIELD_UPDATES

    with PDFDancer.open(pdf_path) as pdf:
        for name, value in updates.items():
            matches = pdf.select_form_fields_by_name(name)
            if not matches:
                print(f"Skipping '{name}' — field not found")
                continue
            for field in matches:
                field.edit().value(value).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Filled {len(updates)} fields and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
