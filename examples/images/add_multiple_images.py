"""Add the same image to multiple pages."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        logo = Path("examples/logo.png")

        # Add logo to top-right of every page
        for i, page in enumerate(pdf.pages()):
            page.new_image().from_file(logo).at(x=500, y=750).add()

        pdf.save(Path("output_logos_everywhere.pdf"))
        print(f"Added logo to {len(pdf.pages())} pages!")
