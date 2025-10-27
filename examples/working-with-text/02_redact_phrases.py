"""Working with Text 02 — Redact paragraphs containing forbidden phrases."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/working-with-text/redacted.pdf")
TARGET_PHRASES = ("replaced", "pdfdancer.com")


def run_example(
    pdf_path: Path = SHOWCASE_PATH,
    output_path: Path = OUTPUT_PATH,
    phrases: tuple[str, ...] = TARGET_PHRASES,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    lowered_phrases = tuple(p.lower() for p in phrases)

    with PDFDancer.open(pdf_path) as pdf:
        matches = [
            paragraph
            for paragraph in pdf.select_paragraphs()
            if any(phrase in (paragraph.object_ref().get_text() or "").lower() for phrase in lowered_phrases)
        ]

        if not matches:
            raise ValueError("No matching paragraphs found to redact.")

        for paragraph in matches:
            paragraph.delete()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Deleted {len(matches)} paragraphs. Saved to {output_path}.")


if __name__ == "__main__":
    run_example()
