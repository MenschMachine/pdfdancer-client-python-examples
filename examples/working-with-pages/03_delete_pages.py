"""Remove unwanted pages."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Delete page 3
        pdf.page(3).delete()

        pdf.save(Path("output_deleted_page.pdf"))
        print(f"Now has {len(pdf.pages())} pages!")
