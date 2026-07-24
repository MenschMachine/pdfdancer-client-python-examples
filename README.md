# PDFDancer client Python examples

![PDFDancer logo](media/logo-silver-60h.webp)

## PDF used to be read-only. We fixed that.

Edit text in any real-world PDF. Even ones you didn't create. These examples use
the [`pdfdancer-client-python`](https://pypi.org/project/pdfdancer-client-python/)
package to show how to build reliable, real-world PDF workflows without broken
layouts or corrupted documents. Each script focuses on a single task, so you
can copy, tweak, and drop the patterns into your own projects.

## Prerequisites

- A shell with `python` and `pip`; Python 3.10 or newer is recommended
- A PDFDancer API token (`PDFDANCER_TOKEN`)
- (Optional) A custom API endpoint (`PDFDANCER_BASE_URL`)

The repository includes the PDFs and image fixtures used by the examples. You do
not need to provide another PDF unless you change an example's input path.

## Getting started

On macOS or Linux, from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export PDFDANCER_TOKEN=your-token-here
# optionally set a custom API endpoint
# export PDFDANCER_BASE_URL=https://api.pdfdancer.com
```

On Windows PowerShell, from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

$env:PDFDANCER_TOKEN = "your-token-here"
# optionally set a custom API endpoint
# $env:PDFDANCER_BASE_URL = "https://api.pdfdancer.com"
```

Alternatively, install the client directly if you only need snippets:

```bash
pip install pdfdancer-client-python
```

## Repository layout

Each runnable example is a Python file that can be executed from the repository
root. Most examples keep their input, output, and operation settings near the
top of the file. The category READMEs contain the complete file inventories:

- `examples/working-with-pages/`
  Page reordering, extraction, deletion, and blank-page creation. See
  [`examples/working-with-pages/README.md`](examples/working-with-pages/README.md).
- `examples/working-with-text/`
  Text replacement, deletion, insertion, and styling. See
  [`examples/working-with-text/README.md`](examples/working-with-text/README.md).
- `examples/forms/`
  AcroForm field inspection, filling, checkbox updates, and clearing. See
  [`examples/forms/README.md`](examples/forms/README.md).
- `examples/working-with-images/`
  Image inspection and transformations. See
  [`examples/working-with-images/README.md`](examples/working-with-images/README.md).
- `examples/working-with-paths/`
  Path inspection, grouping, movement, scaling, rotation, removal, and color
  changes. See [`examples/working-with-paths/README.md`](examples/working-with-paths/README.md).
- `examples/clipping/`
  Removal of clipping paths that hide image and vector content. See
  [`examples/clipping/README.md`](examples/clipping/README.md).
- `examples/capabilities/`
  Advanced selectors, snapshots, object creation, image-region filling, path
  grouping, font lookup, and font registration. See
  [`examples/capabilities/README.md`](examples/capabilities/README.md).
- `examples/templates/`
  Reference PDF template assets; this directory has no runnable examples. See
  [`examples/templates/README.md`](examples/templates/README.md).

Most scripts use `examples/Showcase.pdf` and write generated PDFs below
`output/<category>/`. Path examples use `examples/basic-paths.pdf`, the clipping
example uses `examples/clipping/invisible-content-clipping-test.pdf`, and image
creation uses `examples/experiment.png`. The font-registration example also
accepts an optional `PDFDANCER_FONT_PATH`.

## Running examples

1. Export `PDFDANCER_TOKEN` (and optionally `PDFDANCER_BASE_URL`).
2. Open a script and adjust its inputs or operation settings if needed.
3. Run the script from the repository root with plain Python:

```bash
python examples/working-with-pages/02_extract_pages.py
python examples/forms/01_list_fields.py
python examples/clipping/01_clear_clipping.py
python examples/working-with-images/02_move_image.py
```

To install dependencies and run every runnable example in deterministic order,
use the repository runner from macOS or Linux:

```bash
./run.sh
```

The runner uses `.venv`, installs the pinned dependency from `requirements.txt`,
and requires `PDFDANCER_TOKEN` before it starts. It skips package marker files
such as `__init__.py`.

## Creating your own examples

- Duplicate an existing script and focus it on a single workflow.
- Keep input/output paths and operation settings near the top so others can
  tweak and run it quickly.
- Explore `pdf.select_*()` APIs (paragraphs, images, form fields, paths, etc.) to
  discover other objects you can inspect or manipulate.

## Helpful links

- [API documentation](https://docs.pdfdancer.com?utm_source=github&utm_medium=readme&utm_campaign=pdfdancer-python-examples)
- [Product overview](https://www.pdfdancer.com?utm_source=github&utm_medium=readme&utm_campaign=pdfdancer-python-examples)
- [PyPI](https://pypi.org/project/pdfdancer-client-python/)
- [Changelog](https://www.pdfdancer.com/changelog/?utm_source=github&utm_medium=readme&utm_campaign=pdfdancer-python-examples)
- [Status](https://status.pdfdancer.com?utm_source=github&utm_medium=readme&utm_campaign=pdfdancer-python-examples)
- [Issue tracker](https://github.com/MenschMachine/pdfdancer)
