"""Inspect the high-level structure of a PDF document."""

from pathlib import Path
from textwrap import shorten

from pdfdancer import PDFDancer

if __name__ == "__main__":
    pdf_path = Path("examples/Showcase.pdf")

    if not pdf_path.exists():
        raise SystemExit(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        pages = pdf.pages()
        print("Document Summary")
        print("================")
        print(f"Total pages: {len(pages)}")
        print(f"Total paragraphs: {len(pdf.select_paragraphs())}")
        print(f"Total text lines: {len(pdf.select_text_lines())}")
        print(f"Total images: {len(pdf.select_images())}")
        print(f"Total form fields: {len(pdf.select_form_fields())}")

        if not pages:
            raise SystemExit("This PDF does not contain any pages.")

        first_page = pages[0]
        print("\nFirst Page Details")
        print("------------------")
        print(f"Page index: {first_page.page_index}")
        print(f"Paragraphs on page: {len(first_page.select_paragraphs())}")
        print(f"Images on page: {len(first_page.select_images())}")
        print(f"Form fields on page: {len(first_page.select_form_fields())}")

        sample = first_page.select_paragraphs()[:5]
        if not sample:
            print("\nNo paragraphs found on the first page.")
        else:
            print("\nSample paragraphs:")
            for para in sample:
                position = para.position
                coord = "(?, ?)" if position is None else f"({position.x():.1f}, {position.y():.1f})"
                raw_text = para.object_ref().get_text() or ""
                text = shorten(raw_text.replace("\n", " "), width=80, placeholder="…") if raw_text else ""
                print(f"- {coord} :: {text}")
