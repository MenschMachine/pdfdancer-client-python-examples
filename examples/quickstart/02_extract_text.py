"""Quickstart 02 — Export Showcase.pdf text to a plaintext file."""

from pathlib import Path

from pdfdancer import PDFDancer


SHOWCASE_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output/quickstart/extracted_text.txt")


def run_example(pdf_path: Path = SHOWCASE_PATH, output_path: Path = OUTPUT_PATH) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    paragraphs: list[str] = []
    with PDFDancer.open(pdf_path) as pdf:
        for para in pdf.select_paragraphs():
            text = (para.object_ref().get_text() or "").strip()
            if text:
                paragraphs.append(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(paragraphs), encoding="utf-8")

    print(f"Exported {len(paragraphs)} paragraphs to {output_path}")
    preview = "\n".join(paragraphs[:3])
    if preview:
        print("\nPreview:\n" + preview)


if __name__ == "__main__":
    run_example()
