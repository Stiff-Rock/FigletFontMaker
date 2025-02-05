import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("FigletFontMaker")

combobox = ttk.Combobox(root, state="readonly")
combobox.grid(row=0, column=0, padx=10, pady=10)


def on_create():
    selected_value = combobox.get()
    print(f"Selected: {selected_value}")


create_button = tk.Button(root, text="Create", command=on_create)
create_button.grid(row=0, column=1, padx=10, pady=10)

entries = ["Option 1", "Option 2", "Option 3"]
combobox["values"] = entries

root.mainloop()
