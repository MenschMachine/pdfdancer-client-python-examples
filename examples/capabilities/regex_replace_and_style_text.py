from pathlib import Path
from pdfdancer import PDFDancer, TextReplaceRequest, TextStyleRequest

with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
    replacement = TextReplaceRequest.regex("PDFDancer", "PDFDancer").max_matches(2).build()
    print(pdf.text().replace(replacement).changed)
    style = TextStyleRequest.literal("PDFDancer").font("Helvetica-Bold").size(16).build()
    print(pdf.page(1).text().style(style).changed)
    output = Path("output/capabilities/regex_replaced_and_styled_text.pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(output)
