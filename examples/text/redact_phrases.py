"""Remove paragraphs that contain any of the provided phrases."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")
    output_path = Path("output_redacted.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    target_phrases = ["replaced", "pdfdancer.com"]

    with PDFDancer.open(pdf_path) as pdf:
        matches = [
            p for p in pdf.select_paragraphs()
            if any(phrase in (p.object_ref().get_text() or "").lower() for phrase in target_phrases)
        ]

        if not matches:
            raise SystemExit("No matching paragraphs found.")

        for paragraph in matches:
            paragraph.delete()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Deleted {len(matches)} paragraphs. Saved to {output_path}.")
