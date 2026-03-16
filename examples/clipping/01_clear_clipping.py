"""Clipping 01 - Remove clipping so hidden content becomes visible again."""

from pathlib import Path

from pdfdancer import PDFDancer


CLIPPED_PDF_PATH = Path("examples/clipping/invisible-content-clipping-test.pdf")
OUTPUT_PATH = Path("output/clipping/cleared_clipping.pdf")


def run_example(
    pdf_path: Path = CLIPPED_PDF_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        page = pdf.page(1)
        images = page.select_images()
        if not images:
            raise ValueError("No images found on page 1 to clear clipping from.")

        paths = page.select_paths()
        if len(paths) < 2:
            raise ValueError(
                f"Need at least 2 paths on page 1 to create a path group, found {len(paths)}."
            )

        image = images[0]
        image.clear_clipping()

        path_group = page.group_paths([path.internal_id for path in paths])
        path_group.clear_clipping()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(
            f"Cleared clipping from 1 image and a path group with {path_group.path_count} "
            f"paths on page 1, then saved to {output_path}."
        )


if __name__ == "__main__":
    run_example()
