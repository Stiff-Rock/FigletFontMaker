import tkinter as tk
from tkinter import ttk
import subprocess
import json

root = tk.Tk()
root.title("FigletFontMaker")

entries = ["NaN"]

result = subprocess.run(
    ["node", "src/getFigletFontList.js"], capture_output=True, text=True
)

if result.returncode == 0:
    js_output = result.stdout.strip()
    try:
        entries = json.loads(js_output)
        print("JS Output (as list):", entries)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Error:", result.stderr)

combobox = ttk.Combobox(root, values=entries)
combobox.grid(row=0, column=0, padx=10, pady=10)
combobox.set("Standard")


def on_create():
    selected_value = combobox.get()
    subprocess.run(["python", "src/createFont.py", selected_value], check=True)


create_button = tk.Button(root, text="Create", command=on_create)
create_button.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
