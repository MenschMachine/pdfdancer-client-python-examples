"""Process multiple PDFs in one go."""

from pathlib import Path

from pdfdancer import Color, PDFDancer, StandardFonts

if __name__ == "__main__":
    # Simulate batch processing
    input_files = [Path("examples/Showcase.pdf")]

    for pdf_file in input_files:
        with PDFDancer.open(pdf_file) as pdf:
            # Add "PROCESSED" stamp to every page
            for page in pdf.pages():
                page.new_paragraph().text("PROCESSED").font(StandardFonts.HELVETICA_BOLD, 36).color(Color(255, 0, 0, a=100)).at(x=200, y=200).add()

            output = Path(f"output_batch_{pdf_file.stem}.pdf")
            pdf.save(output)
            print(f"Processed {pdf_file.name} → {output}")
