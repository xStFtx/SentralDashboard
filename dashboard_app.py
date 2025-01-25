# dashboard_app.py
import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import psutil
import pyperclip
from clipboard_manager import ClipboardManager
from app_launcher import AppLauncher
from window_manager import WindowManager
from resource_tracker import ResourceTracker
from settings import Settings

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Productivity Dashboard")
        self.root.geometry("1000x750")

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
        ClipboardManager(frame)

    def add_app_launcher_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="App Launcher")
        AppLauncher(frame)

    def add_window_manager_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Window Manager")
        WindowManager(frame)

    def add_resource_tracker_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Resource Tracker")
        ResourceTracker(frame)

    def add_settings_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Settings")
        Settings(frame)
