from pathlib import Path
from pdfdancer import PDFDancer, TextReplaceRequest

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/working-with-text/replaced_text.pdf")

with PDFDancer.open(INPUT) as pdf:
    response = pdf.text().replace(
        TextReplaceRequest.literal("PDFDancer", "PDFDancer SDK").build()
    )
    print(f"Matched {response.matched} text range(s).")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)


