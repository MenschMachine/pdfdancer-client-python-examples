"""Replace text in a paragraph that starts with a specific phrase."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")
    output_path = Path("output_find_and_replace.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        matches = pdf.page(0).select_paragraphs_starting_with("This line will be replaced")
        if not matches:
            raise SystemExit("No matching paragraphs found on page 0.")

        paragraph = matches[0]
        paragraph.edit().replace("This line was replaced!\nUpdated with PDFDancer").font("Helvetica", 12.0).line_spacing(1.1).apply()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Saved updated PDF to {output_path}")
