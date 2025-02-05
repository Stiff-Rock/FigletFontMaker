import os
import fontforge

text_map = {
    # Letras mayúsculas
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "N",
    "O": "O",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
    # Letras minúsculas
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
    "h": "h",
    "i": "i",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "t",
    "u": "u",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "y",
    "z": "z",
    # Números
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    # Caracteres especiales y símbolos de puntuación
    "!": "exclamation",
    "@": "at",
    "#": "hashtag",
    "$": "dollar",
    "%": "percent",
    "^": "caret",
    "&": "ampersand",
    "*": "asterisk",
    "(": "left_parenthesis",
    ")": "right_parenthesis",
    "-": "hyphen",
    "_": "underscore",
    "=": "equal",
    "+": "plus",
    "[": "left_bracket",
    "]": "right_bracket",
    "{": "left_brace",
    "}": "right_brace",
    ";": "semicolon",
    ":": "colon",
    "'": "single_quote",
    '"': "double_quote",
    ",": "comma",
    ".": "period",
    "<": "less_than",
    ">": "greater_than",
    "/": "slash",
    "?": "question",
    "\\": "backslash",
    "|": "pipe",
    "`": "backtick",
    "´": "accent",
    "~": "tilde",
    "'": "apostrophe",
    " ": "space",
    # Letras con tildes (convertidas a su versión sin tilde para compatibilidad con pyfiglet)
    "á": "aacute",
    "é": "eacute",
    "í": "iacute",
    "ó": "oacute",
    "ú": "uacute",
    "Á": "Aacute",
    "É": "Eacute",
    "Í": "Iacute",
    "Ó": "Oacute",
    "Ú": "Uacute",
    # Caracteres específicos del español
    "ñ": "ntilde",
    "Ñ": "Ntilde",
    "¿": "questiondown",
    "¡": "exclamationdown",
}

svg_folder = "ascii_converted"
output_font = "ASCIIART.ttf"
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
