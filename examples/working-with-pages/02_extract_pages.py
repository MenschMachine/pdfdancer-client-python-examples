"""Split specific pages into a new PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Keep only pages 0-2, delete the rest
        total = len(pdf.pages())
        for i in range(total - 1, 2, -1):  # Delete backwards
            pdf.page(i).delete()

        pdf.save(Path("output_first_three.pdf"))
        print(f"Extracted first 3 pages!")
