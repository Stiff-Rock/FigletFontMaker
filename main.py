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


run_js_script("figletAsciiArt.js")
run_bash_script("inkscapeConvert.sh")
run_python_script("fontforgeScript.py")

commands = [
    "sudo -S cp /home/yago/Shared/CodeProjects/TextAsciiArtToSvg/ASCIIART.ttf /usr/share/fonts",
    "sudo -S fc-cache -fv",
]

for cmd in commands:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

print("All scripts executed.")
