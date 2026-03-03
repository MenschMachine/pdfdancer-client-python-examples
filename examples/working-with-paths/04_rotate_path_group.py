"""Working with Paths 04 — Group first 2 paths and rotate 45 degrees."""

from pathlib import Path

from pdfdancer import PDFDancer


BASIC_PATHS_PATH = Path("examples/basic-paths.pdf")
OUTPUT_PATH = Path("output/working-with-paths/rotated_group.pdf")
ROTATION_DEGREES = 45.0


def run_example(
    pdf_path: Path = BASIC_PATHS_PATH,
    output_path: Path = OUTPUT_PATH,
    rotation_degrees: float = ROTATION_DEGREES,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        paths = pdf.page(1).select_paths()
        if len(paths) < 2:
            raise ValueError(f"Need at least 2 paths on page 1, found {len(paths)}.")

        path_ids = [p.internal_id for p in paths[:2]]
        group = pdf.page(1).group_paths(path_ids)
        group.rotate(rotation_degrees)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Grouped {group.path_count} paths, rotated {rotation_degrees} degrees, saved to {output_path}.")


if __name__ == "__main__":
    run_example()
