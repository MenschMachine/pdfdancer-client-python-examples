from pathlib import Path
from pdfdancer import PDFDancer, PdfColorRequest, TextStyleRequest

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/working-with-text/styled_text.pdf")

with PDFDancer.open(INPUT) as pdf:
    response = pdf.text().style(
        TextStyleRequest.literal("PDFDancer")
        .font("Helvetica-Bold")
        .size(18)
        .fill_color(PdfColorRequest.rgb(0.8, 0.1, 0.1))
        .build()
    )
    print(f"Styled {response.changed} text range(s).")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)


