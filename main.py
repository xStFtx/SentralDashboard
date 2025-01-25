# main.py
import tkinter as tk
from dashboard_app import DashboardApp

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
