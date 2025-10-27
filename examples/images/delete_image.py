"""Remove an image from a specific location."""

from pathlib import Path

from pdfdancer import PDFDancer

if __name__ == "__main__":
    with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
        # Delete all images on page 2
        for img in pdf.page(2).select_images():
            img.delete()

        pdf.save(Path("output_no_images.pdf"))
        print("Deleted all images from page 2!")
