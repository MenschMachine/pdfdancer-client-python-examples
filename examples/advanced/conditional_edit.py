"""Smart edits based on content."""

from pathlib import Path

from pdfdancer import Color, PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # If text contains "Sans", make it bigger and red
        for para in pdf.select_paragraphs():
            text = para.object_ref().get_text() or ""
            if "Sans" in text:
                para.edit().color(Color(200, 0, 0)).font("Helvetica-Bold", 14).apply()

        pdf.save(Path("output_conditional.pdf"))
        print("Conditional edits applied!")
