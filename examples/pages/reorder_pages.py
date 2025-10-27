"""Move a page from one position to another inside a PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")
    output_path = Path("output_reordered.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pdf.move_page(0, 2)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Moved page 0 to position 2. Saved PDF to {output_path}.")
