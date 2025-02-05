import sys
import subprocess

figlet = "src/figletAsciiArt.js"
bashInk = "src/inkscapeConvert.sh"
fontForce = "src/fontforgeScript.py"

font = sys.argv[1]

if len(sys.argv) > 1:
    try:
        print(f"--Running JavaScript script: {figlet}--")
        subprocess.run(["node", figlet, font], check=True)

        print(f"--Running Python script: {bashInk}--")
        subprocess.run(["bash", bashInk], check=True)

        print(f"--Running Bash script: {fontForce}--")
        subprocess.run(["python", fontForce], check=True)
    except subprocess.CalledProcessError as e:
        print(f"--Error while running: {e}--")

    print("All scripts executed.")
