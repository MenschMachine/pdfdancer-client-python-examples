"""Insert a fresh blank page."""

from pathlib import Path

from pdfdancer import Orientation, PageSize, PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Add a blank letter-size page at the end
        pdf.new_page().orientation(Orientation.PORTRAIT).page_size(PageSize.LETTER).add()

        pdf.save(Path("output_extra_page.pdf"))
        print(f"Added page! Now has {len(pdf.pages())} pages.")
