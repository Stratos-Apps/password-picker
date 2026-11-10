import secrets
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid length", "Enter a whole number of at least 4.")
        return

    # Include at least one character from each group.
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars.extend(
        secrets.choice(all_chars) for _ in range(length - len(password_chars))
    )

    # Shuffle so the required character types aren't always at the start.
    secrets.SystemRandom().shuffle(password_chars)
    password = "".join(password_chars)

    password_var.set(password)
    copy_button.config(state=tk.NORMAL)
    status_var.set("")


def copy_password():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        status_var.set("Password copied to clipboard.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("420x270")
root.resizable(False, False)
root.configure(bg="#f3f5f9")

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 20, "bold"),
    bg="#f3f5f9",
    fg="#202a44",
)
title.pack(pady=(22, 5))

tk.Label(
    root,
    text="Choose a password length (minimum 4):",
    font=("Arial", 11),
    bg="#f3f5f9",
    fg="#39445c",
).pack(pady=(8, 5))

length_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
length_entry.insert(0, "16")
length_entry.pack()

generate_button = tk.Button(
    root,
    text="Generate password",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg="#4263eb",
    fg="white",
    activebackground="#364fc7",
    activeforeground="white",
    relief="flat",
    padx=14,
    pady=8,
)
generate_button.pack(pady=14)

password_var = tk.StringVar()
password_display = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    justify="center",
    width=32,
    state="readonly",
    readonlybackground="white",
)
password_display.pack(pady=3)

copy_button = tk.Button(
    root,
    text="Copy",
    command=copy_password,
    font=("Arial", 10),
    state=tk.DISABLED,
)
copy_button.pack(pady=8)

status_var = tk.StringVar()
tk.Label(
    root,
    textvariable=status_var,
    font=("Arial", 9),
    bg="#f3f5f9",
    fg="#287a3d",
).pack()

root.mainloop()
