from pathlib import Path
from pdfdancer import Color, PDFDancer

INPUT = Path("examples/Showcase.pdf")
OUTPUT = Path("output/capabilities/created_pages_and_drawing_objects.pdf")

with PDFDancer.open(INPUT) as pdf:
    pdf.new_page(size={"width": 300, "height": 300}).landscape().add()
    page = 8
    pdf.new_line(page).from_point(30, 30).to_point(180, 80).stroke_color(Color.RED).stroke_width(2).add()
    pdf.new_bezier(page).from_point(40, 120).control_point_1(80, 180).control_point_2(150, 60).to_point(220, 120).stroke_color(Color.BLACK).add()
    pdf.new_rectangle(page).at_coordinates(40, 180).with_size(100, 60).stroke_color(Color.RED).add()
    pdf.new_path(page).add_rectangle(180, 170, 80, 60).stroke_color(Color.BLACK).fill_color(Color(220, 220, 80)).add()
    pdf.new_image().from_file(Path("examples/experiment.png")).at(page, 120, 30).add()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(OUTPUT)
