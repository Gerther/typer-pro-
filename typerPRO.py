import tkinter as tk
from tkinter import filedialog
import keyboard
import threading
import time
import json
import os

keys_sequence = []
press_durations = {}
running = False
entries = []
save_directory = ""

def press_keys_in_loop():
    global keys_sequence, press_durations, running
    while running:
        for key in keys_sequence:
            if not running:
                return
            keyboard.press(key)
            time.sleep(press_durations[key])
            keyboard.release(key)

def toggle_pressing():
    global running
    if not running:
        running = True
        threading.Thread(target=press_keys_in_loop).start()
    else:
        running = False

def select_keys():
    global keys_sequence, press_durations, running
    keys_sequence = [entry[0].get() for entry in entries]
    press_durations = {entry[0].get(): float(entry[1].get()) for entry in entries}
    toggle_pressing()

def add_key_entry():
    row = len(entries) + 1
    label_key = tk.Label(root, text=f"key {row}:")
    label_key.grid(row=row, column=0, padx=10, pady=5)
    entry_key = tk.Entry(root)
    entry_key.grid(row=row, column=1, padx=10, pady=5)
    label_duration = tk.Label(root, text=f"Duration for key {row}:")
    label_duration.grid(row=row, column=2, padx=10, pady=5)
    entry_duration = tk.Entry(root)
    entry_duration.grid(row=row, column=3, padx=10, pady=5)
    entries.append((entry_key, entry_duration, label_key, label_duration))

def remove_key_entry():
    if entries:
        entry_key, entry_duration, label_key, label_duration = entries.pop()
        entry_key.destroy()
        entry_duration.destroy()
        label_key.destroy()
        label_duration.destroy()

def save_keys():
    global save_directory
    file_name = file_name_entry.get() or "key_settings"
    if not file_name.endswith('.json'):
        file_name += '.json'
    if not save_directory:
        save_directory = os.getcwd()
    file_path = os.path.join(save_directory, file_name)
    key_data = {
        "keys": [entry[0].get() for entry in entries],
        "durations": [entry[1].get() for entry in entries]
    }
    with open(file_path, "w") as f:
        json.dump(key_data, f)
    print(f"Settings saved to {file_path}")

def load_keys():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            key_data = json.load(f)
        for entry in entries:
            entry[0].destroy()
            entry[1].destroy()
            entry[2].destroy()
            entry[3].destroy()
        entries.clear()
        for key, duration in zip(key_data["keys"], key_data["durations"]):
            add_key_entry()
            entries[-1][0].insert(0, key)
            entries[-1][1].insert(0, duration)
        print(f"Settings loaded from {file_path}")

def select_save_directory():
    global save_directory
    save_directory = filedialog.askdirectory()
    print(f"Selected save directory: {save_directory}")

root = tk.Tk()
root.title("Teest")

add_key_entry()
add_key_entry()
add_key_entry()
add_key_entry()

start_button = tk.Button(root, text="Start", command=toggle_pressing)
start_button.grid(row=0, column=4, padx=10, pady=5)

select_button = tk.Button(root, text="Select Keys", command=select_keys)
select_button.grid(row=1, column=4, padx=10, pady=5)

add_button = tk.Button(root, text="+", command=add_key_entry)
add_button.grid(row=2, column=4, padx=10, pady=5)

remove_button = tk.Button(root, text="-", command=remove_key_entry)
remove_button.grid(row=3, column=4, padx=10, pady=5)

file_name_label = tk.Label(root, text="Save file name:")
file_name_label.grid(row=4, column=4, padx=10, pady=5)
file_name_entry = tk.Entry(root)
file_name_entry.grid(row=4, column=5, padx=10, pady=5)

save_dir_button = tk.Button(root, text="Select Save Directory", command=select_save_directory)
save_dir_button.grid(row=5, column=4, padx=10, pady=5)

save_button = tk.Button(root, text="Save", command=save_keys)
save_button.grid(row=6, column=4, padx=10, pady=5)

load_button = tk.Button(root, text="Load", command=load_keys)
load_button.grid(row=6, column=5, padx=10, pady=5)

root.mainloop()
