"""Working with Forms 01 — Inspect field names, types, and values."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")


def run_example(pdf_path: Path = SHOWCASE_PATH) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        fields = pdf.select_form_fields()
        print(f"Found {len(fields)} form fields:\n")
        for field in fields:
            value = field.value if field.value not in (None, "") else "(empty)"
            print(f"- {field.name} :: {field.object_type.name} :: {value}")


if __name__ == "__main__":
    run_example()
