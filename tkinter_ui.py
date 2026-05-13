from pathlib import Path
import os
import tkinter as tk
from tkinter import messagebox, simpledialog


# ---------------- FUNCTIONS ---------------- #

def create_file():
    file_name = simpledialog.askstring("Create File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File already exists!")
    else:
        content = simpledialog.askstring("Content", "Enter file content:")

        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "File created successfully!")


def read_file():
    file_name = simpledialog.askstring("Read File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            content = file.read()

        messagebox.showinfo("File Content", content)

    else:
        messagebox.showerror("Error", "File not found!")


def update_file():
    file_name = simpledialog.askstring("Update File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        choice = simpledialog.askinteger(
            "Update",
            "Press 1 to overwrite\nPress 2 to append"
        )

        content = simpledialog.askstring(
            "Content",
            "Enter new content:"
        )

        if choice == 1:

            with open(file_name, 'w') as file:
                file.write(content)

            messagebox.showinfo("Success", "File overwritten!")

        elif choice == 2:

            with open(file_name, 'a') as file:
                file.write(content)

            messagebox.showinfo("Success", "Content appended!")

        else:
            messagebox.showerror("Error", "Invalid choice!")

    else:
        messagebox.showerror("Error", "File not found!")


def delete_file():
    file_name = simpledialog.askstring("Delete File", "Enter file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():
        os.remove(p)

        messagebox.showinfo("Success", "File deleted!")

    else:
        messagebox.showerror("Error", "File not found!")


def rename_file():
    file_name = simpledialog.askstring("Rename File", "Enter old file name:")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        new_name = simpledialog.askstring(
            "Rename",
            "Enter new file name:"
        )

        p.rename(new_name)

        messagebox.showinfo("Success", "File renamed!")

    else:
        messagebox.showerror("Error", "File not found!")


def create_folder():
    folder_name = simpledialog.askstring(
        "Create Folder",
        "Enter folder name:"
    )

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists():
        messagebox.showerror("Error", "Folder already exists!")

    else:
        p.mkdir()

        messagebox.showinfo("Success", "Folder created!")


def delete_folder():
    folder_name = simpledialog.askstring(
        "Delete Folder",
        "Enter folder name:"
    )

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists() and p.is_dir():

        p.rmdir()

        messagebox.showinfo("Success", "Folder deleted!")

    else:
        messagebox.showerror("Error", "Folder not found!")


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("CRUD File Management System")
root.geometry("400x500")
root.config(bg="lightblue")


title = tk.Label(
    root,
    text="FILE MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)

title.pack(pady=20)


buttons = [
    ("Create File", create_file),
    ("Read File", read_file),
    ("Update File", update_file),
    ("Delete File", delete_file),
    ("Rename File", rename_file),
    ("Create Folder", create_folder),
    ("Delete Folder", delete_folder),
]

for text, command in buttons:

    btn = tk.Button(
        root,
        text=text,
        command=command,
        width=25,
        height=2,
        bg="darkblue",
        fg="white",
        font=("Arial", 11, "bold")
    )

    btn.pack(pady=8)


root.mainloop()