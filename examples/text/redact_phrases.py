"""Remove paragraphs that contain any of the provided phrases."""

from pathlib import Path

from pdfdancer import PDFDancer

PDF_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output_redacted.pdf")
TARGET_PHRASES = ["replaced", "pdfdancer.com"]
CASE_SENSITIVE = False


if __name__ == "__main__":
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF file not found: {PDF_PATH}. Update PDF_PATH to point at a real document.")

    phrases = TARGET_PHRASES if CASE_SENSITIVE else [p.lower() for p in TARGET_PHRASES]

    with PDFDancer.open(PDF_PATH) as pdf:
        matches = []
        for paragraph in pdf.select_paragraphs():
            text = paragraph.object_ref().get_text() or ""
            haystack = text if CASE_SENSITIVE else text.lower()
            if any(phrase in haystack for phrase in phrases):
                matches.append(paragraph)

        if not matches:
            raise SystemExit("No matching paragraphs found. Adjust TARGET_PHRASES and try again.")

        for paragraph in matches:
            paragraph.delete()

        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(OUTPUT_PATH)
        print(f"Deleted {len(matches)} paragraphs. Saved sanitized PDF to {OUTPUT_PATH}.")
