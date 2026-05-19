import tkinter as tk
from tkinter import scrolledtext
import subprocess
from datetime import datetime
import os

def run_command():

    command = command_entry.get().strip()

    if command == "":
        return

    output_area.insert(
        tk.END,
        f"\n❯ {command}\n"
    )

    if command == "pwd":
        command = "cd"

    elif command == "ls":
        command = "dir"

    elif command == "clear":
        clear_output()
        command_entry.delete(0, tk.END)
        return

    if command == "date":

        current_date = datetime.now().strftime("%Y-%m-%d")

        output_area.insert(
            tk.END,
            f" Current Date: {current_date}\n"
        )

        command_entry.delete(0, tk.END)

        return

    if command == "time":

        current_time = datetime.now().strftime("%H:%M:%S")

        output_area.insert(
            tk.END,
            f" Current Time: {current_time}\n"
        )

        command_entry.delete(0, tk.END)

        return

    if command.startswith("cd "):

        path = command[3:].strip()

        try:
            os.chdir(path)

            output_area.insert(
                tk.END,
                f"Changed directory to:\n{os.getcwd()}\n"
            )

        except FileNotFoundError:

            output_area.insert(
                tk.END,
                "Directory not found.\n"
            )

        command_entry.delete(0, tk.END)

        return

    try:

        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )

        output_area.insert(tk.END, result)

    except subprocess.CalledProcessError as e:

        output_area.insert(
            tk.END,
            f"\nError:\n{e.output}"
        )

    output_area.see(tk.END)

    command_entry.delete(0, tk.END)

def clear_output():
    output_area.delete(1.0, tk.END)

window = tk.Tk()

window.title("MiniShell")
window.geometry("1000x650")
window.configure(bg="#0f172a")

header_frame = tk.Frame(
    window,
    bg="#172554",
    height=80
)

header_frame.pack(fill=tk.X)

title_label = tk.Label(
    header_frame,
    text="MiniShell",
    font=("Segoe UI", 28, "bold"),
    bg="#172554",
    fg="#ff66c4"
)

title_label.pack(pady=18)

subtitle_label = tk.Label(
    window,
    text="Modern Command Line Interface",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#93c5fd"
)

subtitle_label.pack(pady=(10, 5))

command_frame = tk.Frame(
    window,
    bg="#0f172a"
)

command_frame.pack(pady=15)

command_entry = tk.Entry(
    command_frame,
    width=55,
    font=("Consolas", 15),
    bg="#1e293b",
    fg="#f8fafc",
    insertbackground="#ff66c4",
    relief="flat",
    bd=10
)

command_entry.pack(side=tk.LEFT, padx=10)

run_button = tk.Button(
    command_frame,
    text="Run",
    command=run_command,
    font=("Segoe UI", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#3b82f6",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=8,
    cursor="hand2"
)

run_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(
    command_frame,
    text="Clear",
    command=clear_output,
    font=("Segoe UI", 12, "bold"),
    bg="#ff66c4",
    fg="white",
    activebackground="#ff85d1",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)

clear_button.pack(side=tk.LEFT, padx=5)

output_frame = tk.Frame(
    window,
    bg="#0f172a"
)

output_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

output_area = scrolledtext.ScrolledText(
    output_frame,
    wrap=tk.WORD,
    font=("Consolas", 12),
    bg="#111827",
    fg="#93c5fd",
    insertbackground="white",
    relief="flat",
    bd=15
)

output_area.pack(fill=tk.BOTH, expand=True)

output_area.insert(
    tk.END,
    "Welcome to MiniShell\n\n"
)

output_area.insert(
    tk.END,
    "Type a command and press ENTER or click Run.\n"
)

output_area.insert(
    tk.END,
    "Supported Commands:\n"
)

output_area.insert(
    tk.END,
    "• pwd\n• ls\n• cd\n• mkdir\n• echo\n• date\n• time\n• clear\n\n"
)

command_entry.bind(
    "<Return>",
    lambda event: run_command()
)

command_entry.focus()

window.mainloop()