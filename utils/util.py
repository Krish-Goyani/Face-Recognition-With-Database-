import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def get_button(window, text, color, command, fg='white'):
    button = button = tk.Button(
        window,
        text=text,
        activebackground="#333333",
        activeforeground="#FFFFFF",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica', 20, 'bold'),
        relief=tk.RAISED,
        borderwidth=3,
        padx=10,
        pady=5
    )

    return button


def get_img_label(window):
    label = tk.Label(window, bg="#F0F0F0")
    label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text, bg="#F0F0F0")
    label.config(font=("Roboto", 21), justify="left", padx=10, pady=5)
    return label


def get_entry_text(window):
    inputtxt = tk.Text(
        window,
        height=2,
        width=15,
        font=("Arial", 32),
        bg="#FFFFFF",
        fg="#333333",
        insertbackground="#333333",
        relief=tk.SUNKEN,
        borderwidth=2,
        padx=5,
        pady=5
    )
    return inputtxt


def msg_box(title, description):
    root = tk.Tk()
    root.withdraw()
    custom_font = tkfont.Font(family="Helvetica", size=12)
    root.option_add("*Font", custom_font)
    root.option_add("*Background", "#F0F0F0")
    root.option_add("*Foreground", "#333333")
    messagebox.showinfo(title, description)


