from pathlib import Path
from pdfdancer import PDFDancer

with PDFDancer.open(Path("examples/Showcase.pdf")) as pdf:
    document = pdf.get_document_snapshot()
    page = pdf.page(1)
    snapshot = page.get_snapshot()
    elements = page.select_elements()
    images = page.select_images_at(60, 60, 10)
    paths = page.select_paths_at(80, 580, 10)
    forms = page.select_forms()
    print(f"Document pages: {len(document.pages)}")
    print(f"Page elements: {len(elements)}, snapshot elements: {len(snapshot.elements)}")
    print(f"Images near (60,60): {len(images)}")
    print(f"Paths near (80,580): {len(paths)}")
    print(f"Form XObjects: {len(forms)}")


