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
top—edit the paths/text and run it directly:

- `examples/basics/inspect_document.py` – print a quick document summary.
- `examples/text/find_and_replace.py` – replace paragraphs that start with a phrase.
- `examples/text/redact_phrases.py` – bulk-delete paragraphs matching forbidden phrases.
- `examples/pages/reorder_pages.py` – move a page to a new index.
- `examples/forms/fill_form_fields.py` – list and update AcroForm fields.
- `examples/images/place_logo.py` – drop an image onto a page at fixed coordinates.
- `examples/creation/create_blank_pdf.py` – generate a PDF from scratch with branded text and shapes.

Logs produced by the SDK are written to `logs/` – useful for inspecting raw
requests while you experiment.

## Running Examples

1. Export `PDFDANCER_TOKEN` (and optionally `PDFDANCER_BASE_URL`).
2. Open a script and adjust the constants near the top (paths, text, coordinates, etc.).
3. Run the script with plain Python:

```bash
python examples/basics/inspect_document.py
python examples/text/find_and_replace.py
python examples/creation/create_blank_pdf.py
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
