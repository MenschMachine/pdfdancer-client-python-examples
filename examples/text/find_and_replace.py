"""Replace text in a paragraph that starts with a specific phrase."""

from pathlib import Path

from pdfdancer import PDFDancer

PDF_PATH = Path("examples/Showcase.pdf")
OUTPUT_PATH = Path("output_find_and_replace.pdf")
PAGE_INDEX = 0
PARAGRAPH_PREFIX = "This line will be replaced"
NEW_TEXT = "Executive Summary\nUpdated with PDFDancer"
APPLY_TO_ALL_MATCHES = False  # set to True to update every paragraph on the page

# Optional formatting tweaks; set to None to keep existing values.
NEW_FONT = "Helvetica"
NEW_FONT_SIZE = 12.0
NEW_LINE_SPACING = 1.1
NEW_POSITION = None  # example: (100.0, 500.0)


if __name__ == "__main__":
    if not PDF_PATH.exists():
        raise SystemExit(f"PDF file not found: {PDF_PATH}. Update PDF_PATH to point at a real document.")
    if NEW_POSITION is not None and len(NEW_POSITION) != 2:
        raise SystemExit("NEW_POSITION should be a tuple like (x, y) or set to None.")

    with PDFDancer.open(PDF_PATH) as pdf:
        page = pdf.page(PAGE_INDEX)
        matches = page.select_paragraphs_starting_with(PARAGRAPH_PREFIX)
        if not matches:
            raise SystemExit(
                f"No paragraphs starting with '{PARAGRAPH_PREFIX}' found on page {PAGE_INDEX}."
            )

        targets = matches if APPLY_TO_ALL_MATCHES else matches[:1]
        for paragraph in targets:
            editor = paragraph.edit().replace(NEW_TEXT)
            if NEW_FONT:
                editor = editor.font(NEW_FONT, NEW_FONT_SIZE)
            if NEW_LINE_SPACING:
                editor = editor.line_spacing(NEW_LINE_SPACING)
            if NEW_POSITION:
                editor = editor.move_to(*NEW_POSITION)

            result = editor.apply()
            if getattr(result, "warning", None):
                print(f"Warning for paragraph {paragraph.internal_id}: {result.warning}")

        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(OUTPUT_PATH)
        print(f"Saved updated PDF to {OUTPUT_PATH}")
