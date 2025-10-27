"""List and update AcroForm fields in a PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")
    output_path = Path("output_filled.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        fields = pdf.select_form_fields()
        print(f"Found {len(fields)} form fields:")
        for field in fields:
            value = field.value if field.value is not None else ""
            print(f"- {field.name} ({field.object_type.name}) -> '{value}'")

        field_updates = {"Name": "Ada Lovelace", "Email": "ada@example.com", "Subscribe": "Yes"}

        for name, value in field_updates.items():
            matches = pdf.select_form_fields_by_name(name)
            if not matches:
                print(f"Field '{name}' not found; skipping.")
                continue
            for field in matches:
                field.edit().value(value).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"\nSaved filled PDF to {output_path}.")
