import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import psutil
import pyperclip

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Productivity Dashboard")
        self.root.geometry("900x700")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Add tabs
        self.add_clipboard_manager_tab()
        self.add_app_launcher_tab()
        self.add_window_manager_tab()
        self.add_resource_tracker_tab()
        self.add_settings_tab()

    def add_clipboard_manager_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Clipboard Manager")

        label = ttk.Label(frame, text="Manage clipboard history and pin items.", wraplength=700, justify="center")
        label.pack(pady=10)

        self.clipboard_history = tk.Listbox(frame, height=15, selectmode=tk.SINGLE)
        self.clipboard_history.pack(pady=10, fill='x', padx=20)

        refresh_button = ttk.Button(frame, text="Refresh Clipboard", command=self.refresh_clipboard)
        refresh_button.pack(pady=5)

        pin_button = ttk.Button(frame, text="Pin Selected", command=self.pin_clipboard_item)
        pin_button.pack(pady=5)

        clear_button = ttk.Button(frame, text="Clear Clipboard", command=self.clear_clipboard)
        clear_button.pack(pady=5)

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

    def add_app_launcher_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="App Launcher")

        label = ttk.Label(frame, text="Launch frequently used applications.", wraplength=700, justify="center")
        label.pack(pady=10)

        self.app_entry = ttk.Entry(frame, width=50)
        self.app_entry.pack(pady=5)
        self.app_entry.insert(0, "Enter app name or path")

        launch_button = ttk.Button(frame, text="Launch App", command=self.launch_app)
        launch_button.pack(pady=5)

    def launch_app(self):
        app_path = self.app_entry.get()
        if app_path:
            try:
                os.startfile(app_path)
                showinfo("Success", f"Launched {app_path}")
            except Exception as e:
                showinfo("Error", f"Failed to launch app: {e}")
        else:
            showinfo("Error", "App path cannot be empty.")

    def add_window_manager_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Window Manager")

        label = ttk.Label(frame, text="Save and restore custom window layouts.", wraplength=700, justify="center")
        label.pack(pady=10)

        save_button = ttk.Button(frame, text="Save Layout", command=self.save_window_layout)
        save_button.pack(pady=5)

        restore_button = ttk.Button(frame, text="Restore Layout", command=self.restore_window_layout)
        restore_button.pack(pady=5)

    def save_window_layout(self):
        showinfo("Save Layout", "Window layout saved. [Feature under development]")

    def restore_window_layout(self):
        showinfo("Restore Layout", "Window layout restored. [Feature under development]")

    def add_resource_tracker_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Resource Tracker")

        label = ttk.Label(frame, text="Monitor CPU, Memory, and Disk Usage.", wraplength=700, justify="center")
        label.pack(pady=10)

        self.cpu_label = ttk.Label(frame, text="CPU Usage: 0%")
        self.cpu_label.pack(pady=5)

        self.memory_label = ttk.Label(frame, text="Memory Usage: 0%")
        self.memory_label.pack(pady=5)

        self.disk_label = ttk.Label(frame, text="Disk Usage: 0%")
        self.disk_label.pack(pady=5)

        refresh_button = ttk.Button(frame, text="Refresh Stats", command=self.refresh_stats)
        refresh_button.pack(pady=10)

        auto_refresh_button = ttk.Button(frame, text="Toggle Auto Refresh", command=self.toggle_auto_refresh)
        auto_refresh_button.pack(pady=5)

        self.auto_refresh = False

    def refresh_stats(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent

            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
            self.disk_label.config(text=f"Disk Usage: {disk_usage}%")
        except Exception as e:
            showinfo("Error", f"Failed to refresh stats: {e}")

    def toggle_auto_refresh(self):
        self.auto_refresh = not self.auto_refresh
        if self.auto_refresh:
            self.auto_refresh_stats()

    def auto_refresh_stats(self):
        if self.auto_refresh:
            self.refresh_stats()
            self.root.after(2000, self.auto_refresh_stats)  # Refresh every 2 seconds

    def add_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Settings")

        label = ttk.Label(frame, text="Configure your dashboard preferences.", wraplength=700, justify="center")
        label.pack(pady=10)

        theme_label = ttk.Label(frame, text="Theme:")
        theme_label.pack(pady=5)

        self.theme_combobox = ttk.Combobox(frame, values=["Light", "Dark", "System Default"], state="readonly")
        self.theme_combobox.current(0)
        self.theme_combobox.pack(pady=5)

        apply_button = ttk.Button(frame, text="Apply Settings", command=self.apply_settings)
        apply_button.pack(pady=10)

        reset_button = ttk.Button(frame, text="Reset to Default", command=self.reset_settings)
        reset_button.pack(pady=5)

    def apply_settings(self):
        selected_theme = self.theme_combobox.get()
        showinfo("Settings", f"Applied theme: {selected_theme}")

    def reset_settings(self):
        self.theme_combobox.current(0)
        showinfo("Settings", "Settings reset to default.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
