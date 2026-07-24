import os
from pathlib import Path
from pdfdancer import PDFDancer

with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
    matches = pdf.find_fonts("Helvetica", 12)
    print(f"Matching fonts: {len(matches)}")
    font_path = os.getenv("PDFDANCER_FONT_PATH")
    if font_path:
        print(f"Registered font: {pdf.register_font(Path(font_path))}")


