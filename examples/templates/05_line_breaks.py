"""Working with Templates 05 — Use line breaks in replacement text."""

from pathlib import Path

from pdfdancer import Color, PDFDancer, ReflowPreset


OUTPUT_PATH = Path("output/templates/line_breaks.pdf")


def run_example(output_path: Path = OUTPUT_PATH) -> None:
    # Create a blank PDF with US Letter page size
    with PDFDancer.new(page_size="LETTER") as pdf:
        # Add a title paragraph
        pdf.page(1).new_paragraph() \
            .text("Line Breaks Example") \
            .font("Helvetica-Bold", 20) \
            .color(Color(0, 0, 0)) \
            .at(180, 720) \
            .add()

        # Add a paragraph with a placeholder followed by text on a single line
        pdf.page(1).new_paragraph() \
            .text("{{DESCRIPTION}} This text follows the placeholder on the same line.") \
            .font("Helvetica", 12) \
            .color(Color(0, 0, 0)) \
            .at(50, 650) \
            .add()

        # Replace the placeholder with multi-line text using \n to force line breaks.
        # Without \n the replacement text would try to stay on one line and overflow.
        # With ReflowPreset.NONE the reflow engine respects the explicit line breaks.
        pdf.apply_replacements(
            {"{{DESCRIPTION}}": "PDFDancer supports explicit line breaks in\nreplacement text."},
            reflow_preset=ReflowPreset.NONE,
        )

        # After replacing, adjust line spacing on the resulting multi-line paragraph
        paragraph = pdf.page(1).select_paragraph_starting_with("PDFDancer")
        if paragraph:
            paragraph.edit().line_spacing(2.5).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Created line breaks example at {output_path}.")


if __name__ == "__main__":
    run_example()
