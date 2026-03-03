"""Working with Paths 05 — Group a path and remove it from the PDF."""

from pathlib import Path

from pdfdancer import PDFDancer


BASIC_PATHS_PATH = Path("examples/basic-paths.pdf")
OUTPUT_PATH = Path("output/working-with-paths/removed_group.pdf")


def run_example(
    pdf_path: Path = BASIC_PATHS_PATH,
    output_path: Path = OUTPUT_PATH,
) -> None:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    with PDFDancer.open(pdf_path) as pdf:
        paths = pdf.page(1).select_paths()
        if not paths:
            raise ValueError("No paths found on page 1 to remove.")

        path_ids = [paths[0].internal_id]
        group = pdf.page(1).group_paths(path_ids)
        group.remove()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pdf.save(output_path)
        print(f"Removed path group with {group.path_count} path(s), saved to {output_path}.")


if __name__ == "__main__":
    run_example()
