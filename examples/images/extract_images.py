"""Find and list all images in a PDF."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        images = pdf.select_images()
        print(f"Found {len(images)} images:")
        for img in images:
            pos = img.position
            print(f"  Page {pos.page_index} at ({pos.x():.1f}, {pos.y():.1f})")
