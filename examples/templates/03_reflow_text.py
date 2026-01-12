"""Working with Templates 03 — Use text reflow for longer replacements."""

from pathlib import Path

from pdfdancer import PDFDancer, ReflowPreset


TEMPLATE_PATH = Path("examples/templates/Template.pdf")
OUTPUT_PATH = Path("output/templates/reflow_text.pdf")


def run_example(
    pdf_path: Path = TEMPLATE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        # Use BEST_EFFORT reflow to handle longer replacement text
        # This automatically adjusts text to fit available space
        pdf.apply_replacements(
            {
                "{{RECIPIENT_NAME}}": "Dr. Alexandra Elizabeth Montgomery-Harrington",
                "{{COURSE_NAME}}": "Advanced Machine Learning and Neural Network Architecture Design",
                "{{DATE}}": "January 7, 2026",
                "{{INSTRUCTOR}}": "Prof. Williams",
            },
            reflow_preset=ReflowPreset.BEST_EFFORT,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Filled template with reflow and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
