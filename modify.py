import os
import glob
import json
import shutil
from lxml import etree as ET
import tkinter as tk
from tkinter import filedialog, messagebox
import platform
from pathlib import Path

APP_NAME = "XMLModify"

if platform.system() == "Darwin":
    settings_dir = Path.home() / "Library" / "Application Support" / APP_NAME
elif platform.system() == "Windows":
    settings_dir = Path(os.getenv("APPDATA")) / APP_NAME
else:  
    settings_dir = Path.home() / f".{APP_NAME.lower()}"

settings_dir.mkdir(parents=True, exist_ok=True)
SETTINGS_FILE = settings_dir / "settings.json"

default_settings = {
    "folder": ""
}

if os.path.exists(SETTINGS_FILE):
    try:
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
    except:
        settings = default_settings
else:
    settings = default_settings


def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)


def process_files():
    tag = "EndToEndId"
    old_p = "1D097"
    new_p = "1D101"
    folder = settings["folder"]

    if not all([tag, old_p, new_p, folder]):
        messagebox.showwarning("Missing Fields", "Please complete all fields and choose a folder.")
        return

    xml_files = glob.glob(os.path.join(folder, "*.xml"))
    if not xml_files:
        messagebox.showinfo("No Files", "No XML files found in the selected folder.")
        return

    backup_folder = os.path.join(folder, "backup")
    os.makedirs(backup_folder, exist_ok=True)

    modified_count = 0
    unmatched_count = 0

    for file in xml_files:
        filename = os.path.basename(file)
        backup_path = os.path.join(backup_folder, filename + ".bak")

        if not os.path.exists(backup_path):
            shutil.copy(file, backup_path)

        parser = ET.XMLParser(remove_blank_text=False)
        tree = ET.parse(file, parser)
        root = tree.getroot()
        modified = False

        for elem in root.iter():
            if elem.tag.endswith(tag):
                if elem.text:
                    text = elem.text.strip()
                    if text.startswith(old_p):
                        elem.text = new_p + text[len(old_p):]
                        modified_count += 1
                        modified = True
                    else:
                        unmatched_count += 1

        if modified:
            tree.write(file, encoding="utf-8", xml_declaration=True, pretty_print=True)

    messagebox.showinfo(
        "Processing Complete",
        f"Files scanned: {len(xml_files)}\n"
        f"Modified tags: {modified_count}\n"
        f"Unmatched existing tags: {unmatched_count}\n"
        f"Backups stored in /backup folder"
    )


def restore_backups():
    folder = folder_entry.get().strip()
    if not folder:
        messagebox.showwarning("No folder", "Select a folder first.")
        return

    backup_folder = os.path.join(folder, "backup")
    if not os.path.exists(backup_folder):
        messagebox.showinfo("No backups", "No backup folder found.")
        return

    bak_files = glob.glob(os.path.join(backup_folder, "*.bak"))
    if not bak_files:
        messagebox.showinfo("No backups", "No .bak files to restore.")
        return

    restored = 0
    for bak in bak_files:
        original = os.path.join(folder, os.path.basename(bak).replace(".bak", ""))
        shutil.copy(bak, original)
        restored += 1

    messagebox.showinfo("Restore Complete", f"Restored {restored} files.")


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)
        settings["folder"] = folder


def run():
    try:
        settings["folder"] = folder_entry.get().strip()

        save_settings()
        process_files()
    except Exception as e:
        import traceback
        print("Error:", e)
        traceback.print_exc()
        messagebox.showerror("Error", f"An error occurred:\n{e}")






app = tk.Tk()
app.title("XML Modifier")

pad = {'padx': 10, 'pady': 5}

tk.Label(app, text="Folder Containing XML Files").pack(**pad)
folder_entry = tk.Entry(app, width=40)
folder_entry.pack()
folder_entry.insert(0, settings["folder"])

tk.Button(app, text="Browse Folder", command=browse_folder, width=30).pack(pady=8)
tk.Button(app, text="Run", command=run, width=30).pack(pady=5)
tk.Button(app, text="Restore from Backup", command=restore_backups, width=30).pack(pady=10)

app.mainloop()
