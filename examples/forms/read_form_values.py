"""Extract what users filled in."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        fields = pdf.select_form_fields()

        print("Form data:")
        for field in fields:
            value = field.value or "(empty)"
            print(f"  {field.name}: {value}")
