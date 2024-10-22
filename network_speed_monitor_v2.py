import psutil
import tkinter as tk
from tkinter import StringVar
import time

# Initialize the Tkinter app
app = tk.Tk()
app.title("Network Speed Monitor")
app.geometry("960x540")

# StringVars to hold speeds
download_var = StringVar()
upload_var = StringVar()

# Labels for displaying network speeds
tk.Label(app, text="Download Speed:").pack()
tk.Label(app, textvariable=download_var).pack()

tk.Label(app, text="Upload Speed:").pack()
tk.Label(app, textvariable=upload_var).pack()

# Variables to store previous counters
prev_sent = psutil.net_io_counters().bytes_sent
prev_recv = psutil.net_io_counters().bytes_recv

# Function to update speeds


def update_speed():
    global prev_sent, prev_recv

    # Get current network counters
    current_sent = psutil.net_io_counters().bytes_sent
    current_recv = psutil.net_io_counters().bytes_recv

    # Calculate speeds in MB/s
    upload_speed = (current_sent - prev_sent) / 1024 / 1024
    download_speed = (current_recv - prev_recv) / 1024 / 1024

    # Update previous counters
    prev_sent, prev_recv = current_sent, current_recv

    # Update StringVars
    download_var.set(f"{download_speed:.2f} MB/s")
    upload_var.set(f"{upload_speed:.2f} MB/s")

    # Schedule the function to run every second
    app.after(1000, update_speed)


# Start the update loop
update_speed()

# Run the Tkinter event loop
app.mainloop()
