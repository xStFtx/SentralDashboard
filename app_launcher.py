# app_launcher.py
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

class AppLauncher:
    def __init__(self, parent):
        self.frame = parent
        label = ttk.Label(self.frame, text="Launch frequently used applications or custom scripts.", wraplength=800, justify="center")
        label.pack(pady=10)

        self.app_entry = ttk.Entry(self.frame, width=50)
        self.app_entry.pack(pady=5)
        self.app_entry.insert(0, "Enter app name or path")

        launch_button = ttk.Button(self.frame, text="Launch App", command=self.launch_app)
        launch_button.pack(pady=5)

        self.shortcuts_frame = ttk.Frame(self.frame)
        self.shortcuts_frame.pack(pady=10)

        ttk.Label(self.shortcuts_frame, text="Quick Launch:").pack(pady=5)

        self.quick_apps = ["notepad", "calc", "cmd"]
        for app in self.quick_apps:
            ttk.Button(self.shortcuts_frame, text=app.capitalize(), command=lambda a=app: self.launch_app_directly(a)).pack(pady=2)

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

    def launch_app_directly(self, app_name):
        try:
            os.startfile(app_name)
            showinfo("Success", f"Launched {app_name}")
        except Exception as e:
            showinfo("Error", f"Failed to launch app: {e}")
