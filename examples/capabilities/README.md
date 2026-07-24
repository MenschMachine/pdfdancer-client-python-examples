Additional capability examples using the PDFDancer Python client. Most scripts
use `examples/Showcase.pdf`; path grouping uses `examples/basic-paths.pdf` and
created-object examples also use `examples/experiment.png`. Generated PDFs are
written to `output/capabilities/`.

- `create_pages_and_drawing_objects.py` – create a page and drawing objects.
- `fill_region_of_image.py` – fill a selected region of an image.
- `find_and_register_fonts.py` – find fonts and optionally register a font from
  the `PDFDANCER_FONT_PATH` environment variable.
- `group_paths_in_region_and_resize.py` – group paths in a region and resize
  them.
- `read_snapshots_and_use_coordinate_selectors.py` – read snapshots and use
  coordinate-based selectors.
- `regex_replace_and_style_text.py` – replace text with a regular expression
  and style matching text.
