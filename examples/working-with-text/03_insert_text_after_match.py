from pathlib import Path
from pdfdancer import PDFDancer, TextInsertRequest

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/working-with-text/inserted_text.pdf")

with PDFDancer.open(INPUT) as pdf:
    response = pdf.text().insert(
        TextInsertRequest.after("PDFDancer", " — current SDK").build()
    )
    print(f"Inserted at {response.changed} target(s).")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)


