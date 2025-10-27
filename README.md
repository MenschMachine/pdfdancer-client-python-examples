# PDFDancer Client Python Examples

This repository collects bite-sized examples that show what you can do with the
[pdfdancer-client-python](https://pypi.org/project/pdfdancer-client-python/)
package. Each script focuses on a single task—organised by use case—so you can
copy, modify, and integrate the patterns into your own projects.

## Prerequisites

- Python 3.10+
- A PDFDancer API token (`PDFDANCER_TOKEN`)
- (Optional) Custom API endpoint (`PDFDANCER_BASE_URL`, defaults to `https://api.pdfdancer.com`)
- A local PDF file you can experiment with (for the examples that open documents)
- (Optional) A virtual environment to isolate dependencies

## Getting Started

```bash
# clone this repository, then inside the project directory
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export PDFDANCER_TOKEN=your-token-here
# optionally customise the API endpoint
export PDFDANCER_BASE_URL=https://api.pdfdancer.com
```

Alternatively, install the client directly if you only need snippets:

```bash
pip install pdfdancer-client-python
```

## Repository Layout

Each example is a self-contained Python file with configuration constants at the
top—edit the paths/text and run it directly. The core walkthroughs map to the
API docs structure:

- `examples/quickstart/`
  - `01_inspect_document.py` – print the project Showcase summary.
  - `02_extract_text.py` – export all paragraphs into `output/quickstart/`.
  - `03_duplicate_page.py` – clone the first page and save the result.
- `examples/working-with-text/`
  - `01_find_and_replace.py` – swap text that starts with a specific prefix.
  - `02_redact_phrases.py` – delete any paragraph containing disallowed words.
  - `03_highlight_matches.py` – recolor matching paragraphs.
  - `04_move_text.py` – reposition a paragraph on the page.
  - `05_change_font.py` – restyle the Showcase title.
  - `06_add_watermark.py` – stamp DRAFT on every page.

All scripts use `examples/Showcase.pdf` as the input document and write their
outputs inside `output/<category>/`. Logs produced by the SDK are written to
`logs/` – useful for inspecting raw requests while you experiment.

## Running Examples

1. Export `PDFDANCER_TOKEN` (and optionally `PDFDANCER_BASE_URL`).
2. Open a script and adjust the constants near the top (paths, text, coordinates, etc.).
3. Run the script with plain Python:

```bash
python examples/quickstart/01_inspect_document.py
python examples/working-with-text/01_find_and_replace.py
python examples/working-with-text/06_add_watermark.py
```

## Creating Your Own Examples

- Duplicate an existing script and focus it on a single workflow.
- Keep the configuration at the top so others can tweak and run it quickly.
- Explore `pdf.select_*()` APIs (paragraphs, images, form fields, paths, etc.) to
  discover other objects you can inspect or manipulate.

## Helpful Links

- PyPI: https://pypi.org/project/pdfdancer-client-python/
- Issue tracker and feature requests: https://github.com/theflyingcodr/pdfdancer
- PDFDancer product overview: https://pdfdancer.com
