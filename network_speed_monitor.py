import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import time

# Initialize deque to store network speeds (up to 60 samples for a 1-minute window)
download_speeds = deque([0]*60, maxlen=60)
upload_speeds = deque([0]*60, maxlen=60)

# Variables to store previous counters
prev_sent = psutil.net_io_counters().bytes_sent
prev_recv = psutil.net_io_counters().bytes_recv

# Figure and axis for plotting
fig, ax = plt.subplots()
# Adjust Y-axis to 10 MB/s; modify if higher speeds are expected
ax.set_ylim(0, 10)
ax.set_xlim(0, 59)  # 60 seconds window
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (MB/s)")
ax.set_title("Real-Time Network Speed")

# Lines for upload and download speeds
line_download, = ax.plot(
    download_speeds, label="Download (MB/s)", color='blue')
line_upload, = ax.plot(upload_speeds, label="Upload (MB/s)", color='red')
ax.legend(loc="upper right")

# Function to update the plot in real-time


def update(frame):
    global prev_sent, prev_recv

    # Get the current network I/O counters
    current_sent = psutil.net_io_counters().bytes_sent
    current_recv = psutil.net_io_counters().bytes_recv

    # Calculate the upload and download speeds (in MB/s)
    upload_speed = (current_sent - prev_sent) / \
        1024 / 1024  # Convert bytes to MB
    download_speed = (current_recv - prev_recv) / \
        1024 / 1024  # Convert bytes to MB

    # Update the previous counters
    prev_sent = current_sent
    prev_recv = current_recv

    # Append the new speeds to the deques
    upload_speeds.append(upload_speed)
    download_speeds.append(download_speed)

    # Update the line data for plotting
    line_upload.set_ydata(upload_speeds)
    line_download.set_ydata(download_speeds)

    # Redraw the plot with the new data
    ax.relim()
    ax.autoscale_view()

    return line_upload, line_download


# Animation to continuously update the plot every 1000ms (1 second)
ani = animation.FuncAnimation(fig, update, interval=1000)

# Show the plot
plt.show()
