# resource_tracker.py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import psutil

class ResourceTracker:
    def __init__(self, parent):
        self.frame = parent
        label = ttk.Label(self.frame, text="Monitor CPU, Memory, and Disk Usage with real-time updates.", wraplength=800, justify="center")
        label.pack(pady=10)

        self.cpu_label = ttk.Label(self.frame, text="CPU Usage: 0%", font=("Arial", 12))
        self.cpu_label.pack(pady=5)

        self.memory_label = ttk.Label(self.frame, text="Memory Usage: 0%", font=("Arial", 12))
        self.memory_label.pack(pady=5)

        self.disk_label = ttk.Label(self.frame, text="Disk Usage: 0%", font=("Arial", 12))
        self.disk_label.pack(pady=5)

        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(pady=10)

        refresh_button = ttk.Button(buttons_frame, text="Refresh Stats", command=self.refresh_stats)
        refresh_button.grid(row=0, column=0, padx=5)

        auto_refresh_button = ttk.Button(buttons_frame, text="Toggle Auto Refresh", command=self.toggle_auto_refresh)
        auto_refresh_button.grid(row=0, column=1, padx=5)

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
            self.frame.after(2000, self.auto_refresh_stats)  # Refresh every 2 seconds
