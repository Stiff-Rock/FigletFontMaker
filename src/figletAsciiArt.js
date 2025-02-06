import figlet from 'figlet';
import { exec } from 'child_process';
import fs from 'fs';
import path from 'path';
import os from 'os';

let textMap;
try {
  const rawData = fs.readFileSync('charMap.json', 'utf8');
  textMap = JSON.parse(rawData);
} catch (error) {
  console.error('Error reading or parsing file:', error);
}

async function generateSvgFiles(selectedFont) {
  console.log("SELECTED FONT: " + selectedFont)
  for (let key in textMap) {
    const value = textMap[key];

    try {
      const data = await new Promise((resolve, reject) => {
        figlet(key, { font: selectedFont }, (err, data) => {
          if (err) {
            reject(`Error generating ASCII for ${value}: ${err}`);
          } else {
            resolve(data);
          }
        });
      });

      const tempFilePath = path.join(os.tmpdir(), `${value}.txt`);
      fs.writeFileSync(tempFilePath, data);

      exec(`python src/asciiToSvg.py "${tempFilePath}" "${value}"`, (err, _, stderr) => {
        if (err) {
          console.error(`Error executing Python script: ${err}`);
          return;
        }
        if (stderr) {
          console.error(`stderr: ${stderr}`);
          return;
        }
      });
    } catch (err) {
      console.error(`Error occurred with the character '${value}': ${err}`);
    }
  }
  console.log("SVG files created!");
}

const args = process.argv.slice(2);
const font = args[0] || "Standard";

if (font)
  generateSvgFiles(font);
