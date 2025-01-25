# settings.py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Settings:
    def __init__(self, parent):
        self.frame = parent
        label = ttk.Label(self.frame, text="Configure your dashboard preferences.", wraplength=800, justify="center")
        label.pack(pady=10)

        theme_label = ttk.Label(self.frame, text="Theme:")
        theme_label.pack(pady=5)

        self.theme_combobox = ttk.Combobox(self.frame, values=["Light", "Dark", "System Default"], state="readonly")
        self.theme_combobox.current(0)
        self.theme_combobox.pack(pady=5)

        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(pady=10)

        apply_button = ttk.Button(buttons_frame, text="Apply Settings", command=self.apply_settings)
        apply_button.grid(row=0, column=0, padx=5)

        reset_button = ttk.Button(buttons_frame, text="Reset to Default", command=self.reset_settings)
        reset_button.grid(row=0, column=1, padx=5)

    def apply_settings(self):
        selected_theme = self.theme_combobox.get()
        showinfo("Settings", f"Applied theme: {selected_theme}")

    def reset_settings(self):
        self.theme_combobox.current(0)
        showinfo("Settings", "Settings reset to default.")
