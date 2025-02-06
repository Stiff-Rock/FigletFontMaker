import os
import fontforge
import json

with open("charMap.json", "r") as file:
    text_map = json.load(file)

selectedFont = "ASCIIART"

svg_folder = "ascii_converted"
output_font = f"fonts/{selectedFont}.ttf"
font_name = "ASCIIART"
font_family = "ASCIIART"
font_weight = "Regular"

font = fontforge.font()
font.fontname = font_name
font.familyname = font_family
font.fullname = f"{font_family} {font_weight}"
font.weight = font_weight

fixed_scale = 10.0

for char, name in text_map.items():
    svg_file = os.path.join(svg_folder, f"{name}.svg")
    print(f"---{svg_file}---")

    if os.path.exists(svg_file):
        char_code = ord(char)
        glyph = font.createChar(char_code)

        if char == " ":
            glyph.width = 300
        else:
            glyph.importOutlines(svg_file)
            bbox = glyph.boundingBox()
            glyph.transform([1, 0, 0, 1, -bbox[0], -710])
            glyph.transform([fixed_scale, 0, 0, fixed_scale, 0, 0])

            bbox = glyph.boundingBox()
            glyph.width = round(bbox[2])

    else:
        print(f"Warning: SVG file not found for character '{char}': {svg_file}")

font.generate(output_font)
print(f"Font generated successfully: {output_font}")
