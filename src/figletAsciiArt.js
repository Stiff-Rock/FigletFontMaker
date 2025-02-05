import figlet from 'figlet';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';
import os from 'os';

const textMap = {
  // Letras mayúsculas
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
  // Letras minúsculas
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
  // Números
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
  // Caracteres especiales y símbolos de puntuación
  "!": "exclamation",
  "@": "at",
  "//": "hashtag",
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
  // Letras con tildes(convertidas a su versión sin tilde para compatibilidad con pyfiglet)
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
  // Caracteres específicos del español
  "ñ": "ntilde",
  "Ñ": "Ntilde",
  "¿": "questiondown",
  "¡": "exclamationdown",
}

for (let key in textMap) {
  const value = textMap[key]

  figlet(key, function(err, data) {
    if (err) {
      console.log("Something went wrong with the character '" + value + "'");
      console.dir(err);
      return;
    }

    const tempFilePath = path.join(os.tmpdir(), `${value}.txt`);
    fs.writeFileSync(tempFilePath, data);

    exec(`python asciiToSvg.py "${tempFilePath}" "${value}"`, (err, _, stderr) => {
      if (err) {
        console.error(`Error executing Python script: ${err}`);
        return;
      }
      if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
      }
    });
  });
}
