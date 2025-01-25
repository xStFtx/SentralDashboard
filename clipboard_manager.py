# clipboard_manager.py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pyperclip

class ClipboardManager:
    def __init__(self, parent):
        self.frame = parent
        label = ttk.Label(self.frame, text="Manage clipboard history, pin items, and clear clipboard.", wraplength=800, justify="center")
        label.pack(pady=10)

        self.clipboard_history = tk.Listbox(self.frame, height=15, selectmode=tk.SINGLE)
        self.clipboard_history.pack(pady=10, fill='x', padx=20)

        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(pady=10)

        refresh_button = ttk.Button(buttons_frame, text="Refresh Clipboard", command=self.refresh_clipboard)
        refresh_button.grid(row=0, column=0, padx=5)

        pin_button = ttk.Button(buttons_frame, text="Pin Selected", command=self.pin_clipboard_item)
        pin_button.grid(row=0, column=1, padx=5)

        clear_button = ttk.Button(buttons_frame, text="Clear Clipboard", command=self.clear_clipboard)
        clear_button.grid(row=0, column=2, padx=5)

    def refresh_clipboard(self):
        self.clipboard_history.delete(0, tk.END)
        try:
            clipboard_content = pyperclip.paste()
            if clipboard_content:
                self.clipboard_history.insert(tk.END, clipboard_content)
            else:
                self.clipboard_history.insert(tk.END, "Clipboard is empty.")
        except Exception as e:
            showinfo("Error", f"Failed to access clipboard: {e}")

    def pin_clipboard_item(self):
        selected = self.clipboard_history.get(tk.ACTIVE)
        if selected:
            showinfo("Pinned", f"Pinned clipboard item: {selected}")
        else:
            showinfo("Error", "No item selected.")

    def clear_clipboard(self):
        try:
            pyperclip.copy("")
            self.clipboard_history.delete(0, tk.END)
            showinfo("Success", "Clipboard cleared.")
        except Exception as e:
            showinfo("Error", f"Failed to clear clipboard: {e}")
