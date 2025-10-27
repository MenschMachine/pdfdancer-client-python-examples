"""Reset all form fields to empty."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Clear every field
        for field in pdf.select_form_fields():
            field.edit().value("").apply()

        pdf.save(Path("output_blank_form.pdf"))
        print("Form cleared!")
