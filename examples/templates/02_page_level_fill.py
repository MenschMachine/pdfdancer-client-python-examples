"""Working with Templates 02 — Fill placeholders on specific pages."""

from pathlib import Path

from pdfdancer import PDFDancer, TemplateReplacement


TEMPLATE_PATH = Path("examples/templates/MultiPageTemplate.pdf")
OUTPUT_PATH = Path("output/templates/page_level_fill.pdf")


def run_example(
    pdf_path: Path = TEMPLATE_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        # Fill the cover page (page 1) with global replacements
        pdf.apply_replacements([
            TemplateReplacement("{{TITLE}}", "Annual Report 2026"),
            TemplateReplacement("{{SUBTITLE}}", "Financial Overview"),
            TemplateReplacement("{{AUTHOR}}", "Finance Department"),
        ])

        # Fill page-specific placeholders
        # Page 2 gets "Chapter 1" header
        pdf.page(2).apply_replacements([
            TemplateReplacement("{{HEADER}}", "Chapter 1: Introduction"),
            TemplateReplacement("{{FOOTER}}", "Page 1 of 2"),
        ])

        # Page 3 gets "Chapter 2" header
        pdf.page(3).apply_replacements([
            TemplateReplacement("{{HEADER}}", "Chapter 2: Analysis"),
            TemplateReplacement("{{FOOTER}}", "Page 2 of 2"),
        ])

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Filled page-specific placeholders and saved to {output_path}.")


if __name__ == "__main__":
    run_example()
