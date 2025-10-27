"""Toggle a checkbox on."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Check the "Subscribe" checkbox
        checkboxes = pdf.select_form_fields_by_name("Subscribe")
        if checkboxes:
            checkboxes[0].edit().value("Yes").apply()

            pdf.save(Path("output_checked.pdf"))
            print("Checkbox checked!")
