"""Find keywords and make them stand out."""

from pathlib import Path

from pdfdancer import Color, PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        keywords = ["text", "showing"]

        highlighted = 0
        for keyword in keywords:
            for para in pdf.select_paragraphs_matching(keyword):
                para.edit().color(Color(255, 100, 0)).apply()
                highlighted += 1

        pdf.save(Path("output_highlighted_keywords.pdf"))
        print(f"Highlighted {highlighted} matches!")
