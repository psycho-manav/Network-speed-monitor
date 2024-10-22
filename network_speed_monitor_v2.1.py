import psutil
import tkinter as tk
from tkinter import ttk
import time

class NetworkSpeedMonitor:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Speed Monitor")
        self.master.geometry("960x540")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()
        
        self.prev_sent = psutil.net_io_counters().bytes_sent
        self.prev_recv = psutil.net_io_counters().bytes_recv
        
        self.update_speed()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20")
        main_frame.pack(expand=True)

        ttk.Label(main_frame, text="Download Speed:", font=('Arial', 14)).grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.download_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.download_var, font=('Arial', 14, 'bold')).grid(row=0, column=1, sticky='w', padx=5, pady=5)

        ttk.Label(main_frame, text="Upload Speed:", font=('Arial', 14)).grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.upload_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.upload_var, font=('Arial', 14, 'bold')).grid(row=1, column=1, sticky='w', padx=5, pady=5)

    def update_speed(self):
        current_sent = psutil.net_io_counters().bytes_sent
        current_recv = psutil.net_io_counters().bytes_recv

        upload_speed = (current_sent - self.prev_sent) / 1024 / 1024
        download_speed = (current_recv - self.prev_recv) / 1024 / 1024

        self.prev_sent, self.prev_recv = current_sent, current_recv

        self.download_var.set(f"{download_speed:.2f} MB/s")
        self.upload_var.set(f"{upload_speed:.2f} MB/s")

        self.master.after(1000, self.update_speed)

def main():
    root = tk.Tk()
    app = NetworkSpeedMonitor(root)
    root.mainloop()

if __name__ == "__main__":
    main()