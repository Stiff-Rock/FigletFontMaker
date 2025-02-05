import sys
import subprocess


def run_js_script(script_path):
    try:
        print(f"--Running JavaScript script: {script_path}--")
        subprocess.run(["node", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"--Error occurred while running {script_path}: {e}--")


def run_python_script(script_path):
    try:
        print(f"--Running Python script: {script_path}--")
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"--Error occurred while running {script_path}: {e}--")


def run_bash_script(script_path):
    try:
        print(f"--Running Bash script: {script_path}--")
        subprocess.run(["bash", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"--Error occurred while running {script_path}: {e}--")


if len(sys.argv) > 1:
    font = sys.argv[1]
    run_js_script("src/figletAsciiArt.js")
    run_bash_script("src/inkscapeConvert.sh")
    run_python_script("src/fontforgeScript.py")
    print("All scripts executed.")
