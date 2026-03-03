"""Working with Paths 01 — List all paths on page 1."""

from pathlib import Path

from pdfdancer import PDFDancer


BASIC_PATHS_PATH = Path("examples/basic-paths.pdf")


def run_example(pdf_path: Path = BASIC_PATHS_PATH) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        paths = pdf.page(1).select_paths()
        if not paths:
            print("No paths found on page 1.")
            return

        print(f"Found {len(paths)} paths on page 1:\n")
        for p in paths:
            position = p.position
            if position.x() is not None and position.y() is not None:
                coords = f"({position.x():.1f}, {position.y():.1f})"
            else:
                coords = "(unknown coordinates)"

            if position.bounding_rect:
                rect = position.bounding_rect
                size = f"{rect.width:.1f}×{rect.height:.1f}" if rect.width and rect.height else "unknown size"
            else:
                size = "unknown size"

            print(f"- ID: {p.internal_id} at {coords} — {size}")


if __name__ == "__main__":
    run_example()
