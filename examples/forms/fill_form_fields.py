"""List and update AcroForm fields in a PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

PDF_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output_filled.pdf")
FIELD_UPDATES = {
    "firstName": "Ada",
    "lastName": "Lovelace",
}


if __name__ == "__main__":
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF file not found: {PDF_PATH}. Update PDF_PATH to point at a real document.")

    with PDFDancer.open(PDF_PATH) as pdf:
        fields = pdf.select_form_fields()
        print(f"Found {len(fields)} form fields:")
        for field in fields:
            value = field.value if field.value is not None else ""
            print(f"- {field.name} ({field.object_type.name}) -> '{value}'")

        if not FIELD_UPDATES:
            raise SystemExit("\nFIELD_UPDATES is empty; set values to update and re-run.")

        for name, value in FIELD_UPDATES.items():
            matches = pdf.select_form_fields_by_name(name)
            if not matches:
                print(f"Field '{name}' not found; skipping.")
                continue
            for field in matches:
                field.edit().value(value).apply()
            print(f"Updated {len(matches)} field(s) named '{name}' to '{value}'.")

        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(OUTPUT_PATH)
        print(f"\nSaved filled PDF to {OUTPUT_PATH}.")
