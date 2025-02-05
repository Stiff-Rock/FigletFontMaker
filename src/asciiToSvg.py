import svgwrite
import os
import sys

output_dir = "./ascii"
os.makedirs(output_dir, exist_ok=True)

file_path = sys.argv[1]
value = sys.argv[2]

with open(file_path, "r") as file:
    ascii_art = file.read()

dwg = svgwrite.Drawing(f"{output_dir}/{value}.svg", profile="tiny")
dwg.attribs["xml:space"] = "preserve"

y_position = 10
y_pos_increment = 20
font_size = "12"

for line in ascii_art.splitlines():
    dwg.add(
        dwg.text(
            line, insert=(10, y_position), font_size=font_size, font_family="monospace"
        )
    )
    y_position += y_pos_increment

dwg.save()
