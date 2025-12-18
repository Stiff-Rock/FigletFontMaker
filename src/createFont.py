import os
import sys
import subprocess

FIGLET_SCRIPT = "src/figletAsciiArt.js"
BASH_INK_SCRIPT = "src/inkscapeConvert.sh"

script_dir = os.path.dirname(os.path.abspath(__file__))
FONT_FORGE_SCRIPT = os.path.join(script_dir, "fontforgeScript.py")
FF_PYTHON = "C:\\Program Files\\FontForgeBuilds\\bin\\ffpython.exe"

GIT_BASH_PATH = "C:\\Program Files\\Git\\git-bash.exe"

font = sys.argv[1]

if len(sys.argv) > 1:
    try:
        print(f"--Running JavaScript script: {FIGLET_SCRIPT}--")
        subprocess.run(["node", FIGLET_SCRIPT, font], check=True)

        print(f"--Running Python script: {BASH_INK_SCRIPT}--")
        subprocess.run([GIT_BASH_PATH, BASH_INK_SCRIPT], check=True)

        print(f"--Running Bash script: {FONT_FORGE_SCRIPT}--")
        subprocess.run([FF_PYTHON, FONT_FORGE_SCRIPT], check=True)
    except subprocess.CalledProcessError as e:
        print(f"--Error while running: {e}--")

    print("All scripts executed.")
