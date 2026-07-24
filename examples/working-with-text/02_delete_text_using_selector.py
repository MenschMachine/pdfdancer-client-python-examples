from pathlib import Path
from pdfdancer import PDFDancer, TextDeleteRequest

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/working-with-text/deleted_text.pdf")

with PDFDancer.open(INPUT) as pdf:
    response = pdf.text().delete(TextDeleteRequest.literal("PDFDancer").build())
    print(f"Deleted {response.changed} text range(s).")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)


